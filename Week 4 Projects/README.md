# GNCIPL Internship Week 4 Project: Real Estate Segmentation

**Submitted By:** Sahil Adlakha  
**Domain:** Real Estate  
**Dataset:** California Housing Dataset (Built-in, scikit-learn)

## Project Overview

This notebook performs segmentation on California real estate data to analyze and cluster housing prices based on location and value. The main steps include:

- **Data Loading & Exploration:**  
  Uses the built-in California Housing dataset. Explores structure, checks for nulls, and inspects features such as latitude, longitude, and median house value.

- **Preprocessing:**  
  - Selects only location and price columns.
  - Applies normalization using StandardScaler.
  - Bins house prices for categorical analysis.

- **Dimensionality Reduction:**  
  Utilizes PCA to reduce the feature space to two principal components for easier clustering and visualization.

- **Clustering:**  
  - Uses the Elbow Method to determine the optimal number of clusters.
  - Applies K-Means clustering (e.g., 4 clusters).
  - Assigns each data point to a cluster.

- **Visualization:**  
  - Plots clusters and price bins.
  - Displays results on a map using Folium for geographic visualization.

## How to Run

1. **Clone this repository.**
2. **Install required libraries:**
   ```bash
   pip install pandas numpy scikit-learn matplotlib folium
3. **Open GNCIPL ```Week 4 Project.ipynb``` in Jupyter Notebook or JupyterLab.**
4. **Run the notebook cells sequentially to reproduce the analysis and visualizations.**

## Notes

- The notebook uses the California Housing dataset via ```sklearn.datasets.fetch_california_housing```, so no data download is required.
- Make sure to trust the notebook in Jupyter to view interactive maps.

## License

This project is for educational and internship purposes only.
