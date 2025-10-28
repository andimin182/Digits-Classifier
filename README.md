# 🧠 Digit Classification using CNN

A simple **Convolutional Neural Network (CNN)** built with **Keras** to classify handwritten digits from the **MNIST dataset**.  
This project demonstrates a basic deep learning pipeline — from data preprocessing to model training, evaluation, and saving.

---

## 🚀 Overview

This project trains a CNN model to recognize digits (0–9) using the **MNIST dataset**, which contains 70,000 grayscale images of handwritten digits (28x28 pixels).

The model achieves over **98% accuracy** after just a few epochs of training.

---

## 🧩 Model Architecture

| Layer Type | Parameters | Activation |
|-------------|-------------|-------------|
| Conv2D | 64 filters, 3x3 kernel | ReLU |
| Conv2D | 32 filters, 3x3 kernel | ReLU |
| Flatten | — | — |
| Dense | 10 units | Softmax |

---

## ⚙️ How It Works

1. **Load the MNIST dataset**  
   The dataset is split into training and testing sets.  
2. **Reshape and normalize the data**  
   Input images are reshaped to `(28, 28, 1)` and scaled between `0–1`.  
3. **One-hot encode labels**  
   Converts numeric labels (0–9) into categorical vectors.  
4. **Build and compile the CNN**  
   Using `adam` optimizer and `categorical_crossentropy` loss.  
5. **Train the model**  
   For 3 epochs using both training and validation data.  
6. **Evaluate and save the model**  
   The final model is saved as `trained_model.h5`.

---

