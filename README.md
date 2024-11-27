# Project Report: Breast Cancer Wisconsin Dataset

## Group Members:
- **Syed Huzaifa Ali** [23K-0004]  
- **Amna Asim Khan** [23K-0859]  
- **Haris Ahmed** [23K-6005]  

---

## 1. Dataset Overview
The dataset we are working on is the **Breast Cancer Wisconsin (Diagnostic) Dataset**, commonly used in machine learning and data analysis for classification tasks. This dataset contains information regarding various characteristics of cell nuclei present in breast cancer biopsies.

### Key Details:
- **Number of Rows**: 569  
- **Number of Columns**: 32  
- **Target Variable**: `diagnosis` (Binary Classification)  
  - **Malignant (M)**: Malignant tumor  
  - **Benign (B)**: Benign tumor  

### Key Columns:
- **ID**: Unique identifier for each tumor sample.  
- **Diagnosis**: Target variable indicating whether the tumor is benign or malignant.  
- **Features**: 30 numerical measurements calculated from images of the tumor. Examples include:
  - Radius
  - Texture
  - Perimeter
  - Area
  - Smoothness
  - Compactness
  - Concavity
  - Symmetry

---

## 2. Information to be Extracted from the Dataset
Using Python libraries such as Pandas, Matplotlib, and Seaborn, the following information can be extracted and analyzed:

### Data Cleaning:
- Check for **missing values**, **duplicates**, and **outliers** in the dataset.  
- Analyze data types of columns and handle any incorrect or inconsistent data types.

### Summary Statistics:
- Use descriptive statistics such as **mean**, **median**, **standard deviation**, and others to understand the distribution of features.

### Data Visualization:
1. **Distribution of Target Variable**:  
   - Plot the number of benign and malignant cases.  

2. **Correlations**:  
   - Analyze how features are correlated with each other, especially with the target variable (`diagnosis`).  

3. **Feature Distributions**:  
   - Visualize the range and variability of features across different classes (malignant vs. benign).  

4. **Class Distribution**:  
   - Check the balance between malignant and benign cases to assess whether the dataset is imbalanced.

5. **Relationships Between Features and Diagnosis**:  
   - Investigate how the features (e.g., `radius`, `texture`) vary between malignant and benign tumors.

---

## 3. Explanation of Graphs and Insights

### 3.1. Histograms of Selected Features
#### Purpose:
The histograms display the distribution of selected features for both malignant and benign samples.

#### Key Insights:
- **Malignant vs. Benign**:  
  - Features such as `radius_mean`, `perimeter_mean`, and `area_mean` show clear differences between malignant and benign samples, with malignant tumors generally having higher values.  
- **Feature Variability**:  
  - Some features, like `smoothness_mean`, show overlapping distributions for both classes, indicating that they might be less discriminative for classification.  
- **Stacked Bars**:  
  - The use of stacked bars with distinct colors (blue for malignant and orange for benign) makes it easy to compare the distributions of each feature between the two classes.

---

### 3.2. Correlation Heatmap
#### Purpose:
The heatmap visualizes the correlation between pairs of features in the dataset.

#### Key Insights:
- **Strong Correlations**:  
  - Features like `radius_mean` and `perimeter_mean` have a high positive correlation, suggesting they provide similar information and could be redundant.  
- **Feature Relationships**:  
  - The heatmap helps identify which features are highly correlated, which can inform feature selection strategies to reduce multicollinearity in modeling.

---

### 3.3. Summary Statistics Bar Plot
#### Purpose:
The bar plot presents summary statistics (mean, median, standard deviation, and variance) for the top 10 selected features.

#### Key Insights:
- **Variation in Features**:  
  - Features like `perimeter_mean` and `area_mean` show significant variation (high standard deviation), which indicates their importance in distinguishing between benign and malignant samples.  
- **Central Tendency**:  
  - The mean and median values for features such as `radius_mean` and `texture_mean` are close, suggesting a normal distribution for these features in the dataset.

---

### 3.4. Top 10 Weights from Logistic Regression Model
#### Purpose:
This bar plot displays the top 10 most influential features based on their absolute weights in a logistic regression model.

#### Key Insights:
- **Important Features**:  
  - Features like `radius_mean`, `perimeter_mean`, `perimeter_worst`, `radius_worst`, `concavity_worst`, `area_mean`, `concave_points_worst`, `concave_points_mean`, `texture_mean`, and `texture_worst` have the highest absolute weights, indicating their strong influence on the model's classification of malignant vs. benign tumors.  
- **Interpretation**:  
  - These features are critical for the model's predictions, and understanding their impact can help in explaining the model’s decision-making process.

---

## 4. Conclusion
Through this project, we have gained insights into the characteristics of breast cancer tumors and developed a more intuitive understanding of how different features contribute to distinguishing between benign and malignant cases. Data visualization was instrumental in making this process transparent and accessible. By identifying the most important features, we can focus on enhancing the predictive power of machine learning models for breast cancer diagnosis.
