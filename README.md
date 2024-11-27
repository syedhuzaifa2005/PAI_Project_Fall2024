# Project Report on Breast Cancer Wisconsin Dataset

**Group Members:**  
- Syed Huzaifa Ali [23K-0004]  
- Amna Asim Khan [23K-0859]  
- Haris Ahmed [23K-6005]  

## 1. Dataset Overview

The dataset we are working on is the Breast Cancer Wisconsin (Diagnostic) Dataset, which is commonly used in machine learning and data analysis for classification tasks. This dataset contains information regarding various characteristics of cell nuclei present in breast cancer biopsies.

- **Number of Rows:** 569 rows  
- **Number of Columns:** 32 columns  

The columns include both features (e.g., radius, texture, perimeter, area) and the target variable (diagnosis), which is a binary classification:
- **Malignant (M):** Malignant tumor  
- **Benign (B):** Benign tumor  

**Key columns in the dataset:**
- **ID:** Unique identifier for each tumor sample  
- **Diagnosis:** A binary classification indicating whether the tumor is benign (B) or malignant (M)  
- **Features:** Various measurements (radius, texture, smoothness, compactness, concavity, etc.) calculated from images of the tumor.

## 2. Information to be Extracted from the Dataset

Using Python libraries such as Pandas, Matplotlib, and Seaborn, the following information can be extracted and analyzed:

### Data Cleaning:
- Check for missing values, duplicates, and outliers in the dataset. 
- Analyze data types of columns and handle any incorrect or inconsistent data types.

### Summary Statistics:
- Use descriptive statistics (mean, median, standard deviation, etc.) to understand the distribution of the features.

### Data Visualization:
- **Distribution of Target Variable:** Plot the number of benign and malignant cases.
- **Correlations:** Analyze how features are correlated with each other (e.g., which features have high correlation with diagnosis).
- **Feature Distributions:** Visualize the distribution of various features to understand their range and variability across different classes.
- **Class Distribution:** Check the balance between malignant and benign cases to assess whether the dataset is imbalanced.
- **Relationship Between Features and Diagnosis:** Investigate how the features (such as radius, texture, etc.) vary between malignant and benign tumors.

## 3. Explanation of Graphs and Insights

Data visualizations play a crucial role in extracting meaningful insights from the dataset. Below are common types of graphs that can be created, along with their purposes:

### 3.1. Histograms of Selected Features
- **Purpose:** The histograms display the distribution of selected features for both malignant and benign samples.
- **Key Insights:**
  - **Malignant vs. Benign:** Features such as `radius_mean`, `perimeter_mean`, and `area_mean` show clear differences between malignant and benign samples, with malignant tumors generally having higher values.
  - **Feature Variability:** Some features, like `smoothness_mean`, show overlapping distributions for both classes, indicating that they might be less discriminative for classification.
  - **Stacked Bars:** The use of stacked bars with distinct colors (blue for malignant and orange for benign) makes it easy to compare the distributions of each feature between the two classes.

### 3.2. Correlation Heatmap
- **Purpose:** The heatmap visualizes the correlation between pairs of features in the dataset.
- **Key Insights:**
  - **Strong Correlations:** Features like `radius_mean` and `perimeter_mean` have a high positive correlation, suggesting they provide similar information and could be redundant.
  - **Feature Relationships:** The heatmap helps identify which features are highly correlated, which can inform feature selection strategies to reduce multicollinearity in modeling.

### 3.3. Summary Statistics Bar Plot
- **Purpose:** The bar plot presents summary statistics (mean, median, standard deviation, and variance) for the top 10 selected features.
- **Key Insights:**
  - **Variation in Features:** Features like `perimeter_mean` and `area_mean` show significant variation (high standard deviation), which indicates their importance in distinguishing between benign and malignant samples.
  - **Central Tendency:** The mean and median values for features such as `radius_mean` and `texture_mean` are close, suggesting a normal distribution for these features in the dataset.

### 3.4. Top 10 Weights from Logistic Regression Model
- **Purpose:** This bar plot displays the top 10 most influential features based on their absolute weights in a logistic regression model.
- **Key Insights:**
  - **Important Features:** Features like `radius_mean`, `perimeter_mean`, `perimeter_worst`, `radius_worst`, `concavity_worst`, `area_mean`, `concave_points_worst`, `concave_points_mean`, `texture_mean`, `texture_worst`, have the highest absolute weights, indicating their strong influence on the model's classification of malignant vs. benign tumors.
  - **Interpretation:** These features are critical for the model's predictions, and understanding their impact can help in explaining the model’s decision-making process.

## 4. Conclusion

Through this project, we can not only gain insights into the characteristics of breast cancer tumors but also develop a more intuitive understanding of how different features contribute to distinguishing between benign and malignant cases. Data visualization is key in making this process more transparent and accessible.
