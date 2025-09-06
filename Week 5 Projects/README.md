# GNCIPL Internship Week 5 Project: Fashion MNIST Classifier

**Author:** Sahil Adlakha   
**Domain:** Fashion Classification   
**Technology:** Neural Network   
**Dataset:** Fashion MNIST(Built-in)(tensorflow.keras)

## Overview

This project demonstrates image classification using the Fashion MNIST dataset and deep learning with TensorFlow/Keras. The objective is to build a neural network that accurately classifies grayscale images of clothing items into one of 10 categories.

## Project Steps

1. **Data Loading & Exploration**
   - Load training and test sets
   - Visualize sample images
   - Inspect data distribution

2. **Preprocessing**
   - Normalize pixel values to [0,1]
   - (Optional) Data augmentation

3. **Model Building**
   - Define a Sequential neural network using Keras
   - Use layers such as Flatten, Dense, Dropout

4. **Training**
   - Compile the model with appropriate loss and optimizer
   - Train the model and validate on test data

5. **Evaluation**
   - Assess accuracy and loss on test set
   - Display confusion matrix and classification report

6. **Visualization**
   - Plot training/validation accuracy and loss curves
   - Visualize predictions on test images


**Libraries Used:** tensorflow, numpy, matplotlib

## How to Run

1. Clone this repository or open the notebook in Colab/Jupyter.
2. Install required dependencies:
    ```bash
    pip install tensorflow numpy matplotlib scikit-learn
    ```
3. Run the cells in `Fashion_MNIST_Classifier.ipynb` sequentially.

## Results

- Achieves high accuracy (>85%) on test data.
- Demonstrates the effectiveness of neural networks for image classification tasks.

## References

- [Fashion MNIST Dataset](https://github.com/zalandoresearch/fashion-mnist)
- [TensorFlow Documentation](https://www.tensorflow.org/) (Note: Tensorflow show some errors while working with Python 3.13. It works well with 3.12.)

## License

This project is for educational and internship purposes only.
