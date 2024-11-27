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
  - Features such as `radius_mean`, `perimeter_mean`, and `area_mean` show clear differences between malignant and benign
