import io
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from joblib import load

# Load data
def load_data():
    data_path = r'./media/data.csv'
    df = pd.read_csv(data_path)
    df.drop(columns=['Unnamed: 32', 'id'], inplace=True)
    df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})
    return df

# Convert plot to base64
def plot_to_base64(fig):
    img_buf = io.BytesIO()
    fig.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')
    img_buf.close()
    return img_base64

# Generate histograms
def generate_histograms():
    df = load_data()

    selected_features = ['radius_mean', 'texture_mean', 'area_mean', 'smoothness_mean', 'compactness_mean',
                         'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'perimeter_mean']
    
    fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(12, 15))
    axes = axes.ravel()

    dfM = df[df['diagnosis'] == 1]  # Malignant
    dfB = df[df['diagnosis'] == 0]  # Benign

    custom_colors = ['#1f77b4', '#ff7f0e']  # Blue and orange

    for idx, ax in enumerate(axes):
        feature = selected_features[idx]
        binwidth = (df[feature].max() - df[feature].min()) / 50
        ax.hist([dfM[feature], dfB[feature]], 
                bins=np.arange(df[feature].min(), df[feature].max() + binwidth, binwidth),
                alpha=0.6, stacked=True, density=True,
                label=['Malignant', 'Benign'], color=custom_colors)
        ax.legend(loc='upper right', fontsize=8)
        ax.set_title(f'{feature}', fontsize=10, fontweight='bold')
        ax.set_xlabel(feature, fontsize=9)
        ax.set_ylabel('Density', fontsize=9)

    plt.tight_layout()
    return plot_to_base64(fig)

# Generate correlation heatmap
def generate_correlation_heatmap():
    df = load_data()
    correlation_matrix = df.corr()
    plt.figure(figsize=(18, 16))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True, square=True, linewidths=0.5, annot_kws={"size": 10})
    plt.xticks(fontsize=12, rotation=45, ha='right')
    plt.yticks(fontsize=12)

    return plot_to_base64(plt)

# Generate summary statistics
def generate_summary_statistics():
    df = load_data()
    
    # Prepare train_inputs and numeric_cols
    top_10_features = [
        'area_mean', 'concave points_mean', 'concave points_worst', 
        'concavity_worst', 'perimeter_mean', 'perimeter_worst', 
        'radius_mean', 'radius_worst', 'texture_mean', 'texture_worst'
    ]
    
    train_inputs = df[top_10_features].copy()
    numeric_cols = train_inputs.columns.tolist()

    numeric_summary = train_inputs[numeric_cols].agg(['mean', 'median', 'std', 'var'])
    stats_df = numeric_summary.T
    plt.figure(figsize=(15, 7))
    stats_df.plot(kind='bar', figsize=(15, 7), colormap='viridis')
    plt.title("Summary Statistics (Mean, Median, Std, Variance)")
    plt.ylabel("Values")
    plt.xlabel("Features")
    plt.grid(axis='y')
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plot_to_base64(plt)

# Generate top 10 weights plot
def generate_top10_weights():
    # Load logistic regression model
    model = load('ml_model/logistic_regression_model.joblib')

    # Prepare weights_df
    top_10_features = [
        'area_mean', 'concave points_mean', 'concave points_worst', 
        'concavity_worst', 'perimeter_mean', 'perimeter_worst', 
        'radius_mean', 'radius_worst', 'texture_mean', 'texture_worst'
    ]
    
    weights_df = pd.DataFrame({
        'feature': top_10_features,
        'weight': model.coef_.flatten()  # Flatten the array for easier handling
    })

    top10_weights_df = weights_df.reindex(weights_df['weight'].abs().sort_values(ascending=False).index).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top10_weights_df, x='weight', y='feature', palette='viridis')
    plt.title("Top 10 Features by Absolute Weight in Logistic Regression")
    plt.xlabel("Weight")
    plt.ylabel("Feature")
    plt.tight_layout()

    return plot_to_base64(plt)
