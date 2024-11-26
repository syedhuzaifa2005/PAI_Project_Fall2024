import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump


def load_data():
    data_path = r'./media/data.csv'
    df = pd.read_csv(data_path)
    df.drop(columns=['Unnamed: 32', 'id'], inplace=True)
    df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})
    return df

# Top 10 features based on prior analysis or domain knowledge
top_10_features = [
    'area_mean', 'concave points_mean', 'concave points_worst', 
    'concavity_worst', 'perimeter_mean', 'perimeter_worst', 
    'radius_mean', 'radius_worst', 'texture_mean', 'texture_worst'
]

def train_and_save_model():
    df = load_data()

    # Split data into training and test sets
    train_val_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    train_inputs, train_targets = train_val_df[top_10_features], train_val_df['diagnosis']
    test_inputs, test_targets = test_df[top_10_features], test_df['diagnosis']
    
    # Impute missing values (if any)
    imputer = SimpleImputer(strategy='mean')
    train_inputs = imputer.fit_transform(train_inputs)
    test_inputs = imputer.transform(test_inputs)
    
    # Scale features to a range of [0, 1]
    scaler = MinMaxScaler()
    train_inputs = scaler.fit_transform(train_inputs)
    test_inputs = scaler.transform(test_inputs)

    # Train logistic regression model
    model = LogisticRegression(solver='lbfgs', max_iter=500, tol=1e-4)
    model.fit(train_inputs, train_targets)

    # Save model and preprocessing objects
    dump(model, 'ml_model/logistic_regression_model.joblib')
    dump(imputer, 'ml_model/imputer.joblib')
    dump(scaler, 'ml_model/scaler.joblib')

    # Evaluate model accuracy
    y_pred = model.predict(test_inputs)
    accuracy = accuracy_score(test_targets, y_pred)
        
    return accuracy

if __name__ == "__main__":
    model, accuracy, train_inputs, train_targets, test_inputs, test_targets = train_and_save_model()
