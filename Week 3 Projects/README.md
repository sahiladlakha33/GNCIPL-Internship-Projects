# Week 3 Projects

This directory contains Jupyter notebooks for the GNCIPL Internship Week 3 data analysis projects by Sahil Adlakha.

---

## GNCIPL Week 3 Project: Mall Customer Segmentation (Clustering)

**Submitted By:** Sahil Adlakha  
**Project Type:** Customer Segmentation  
**Techniques Used:** K-Means Clustering, Elbow Method  
**Dataset:** Mall_Customers.csv (from Kaggle)  

### Project Overview

This notebook performs customer segmentation for a retail store using clustering techniques. The workflow includes:

- **Loading and exploring the dataset**
  - Features include CustomerID, Gender, Age, Annual Income, and Spending Score.
  - Basic statistics, null value checks, and data visualizations (scatter plots, box plots).

- **Data Visualization**
  - Visualizes relationships between Age, Annual Income, and Spending Score.
  - Box plots for numerical features.

- **Clustering**
  - Uses the Elbow Method to determine the optimal number of customer segments (clusters).
  - Applies K-Means clustering (typically 5 clusters found optimal).
  - Assigns cluster labels to each customer.

- **Cluster Visualization**
  - Plots clusters and centroids to show customer groups in terms of annual income and spending score.

**Libraries Used:** pandas, matplotlib, seaborn, scikit-learn

---

## Getting Started

1. Clone this repository.
2. Download the dataset (`Mall_Customers.csv`) from Kaggle and place it in the Week 3 Projects directory.
3. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```
4. Open and run the notebook in Jupyter to reproduce the analysis.

---

## License

This project is for educational and internship purposes.