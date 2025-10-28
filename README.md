# 🎨 Digit Classification & Paint Application (Keras + Tkinter)

A complete project that combines **deep learning** and **GUI development** — featuring a **Convolutional Neural Network (CNN)** trained on **MNIST** for handwritten digit recognition, and a **Tkinter-based Paint App** that allows users to draw digits and get live predictions.

---

## 🧠 Overview

This project demonstrates a full end-to-end digit recognition pipeline:

1. **Train a CNN model** on the MNIST dataset using Keras/TensorFlow.  
2. **Save and reuse the model** for predictions.  
3. **Create a Paint GUI** where users can draw digits and get them classified by the trained model in real-time.  

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png" width="400"/>
</p>

---

## 🧩 Project Structure
```yaml
├── trained_model.h5 # Saved CNN model
├── digit_CNNClassification.py # CNN training script
├── paint.py # Paint and prediction GUI app
├── Data/
│ ├── paint.ico # App icon
│ ├── image0.png # Saved drawings
│ └── ...
└── README.md
```
---

## ⚙️ CNN Model Summary

| Layer Type | Parameters | Activation |
|-------------|-------------|-------------|
| Conv2D | 64 filters, 3x3 kernel | ReLU |
| Conv2D | 32 filters, 3x3 kernel | ReLU |
| Flatten | — | — |
| Dense | 10 units | Softmax |

The model achieves an accuracy of **~98%** on the MNIST test set.

---

## 🚀 Training the CNN Model

Run the training script to build and save the model:

```bash
python train_model.py
```
The script performs:

- Dataset loading and preprocessing

- Model definition and compilation

- Training for 3 epochs

- Evaluation and saving (trained_model.h5)

You’ll see outputs like:

```yaml
Test loss: 0.06
Test accuracy: 0.98
Model saved successfully..
```

## 🖌️ Paint Application (Digit Classifier GUI)
Once your model is trained and saved as trained_model.h5, you can launch the Paint app:

```bash
python paint.py
```
This opens a Tkinter-based GUI where you can:

- Draw digits with your mouse

- Adjust brush size

- Change pen and background colors

- Clear the canvas

- Save your drawings

- Get instant predictions for drawn digits

## 🧠 Prediction Pipeline
The Paint app performs the following steps:

- Save your drawing as an image (e.g. image0.png)

- Preprocess it

- Run inference using the CNN model (trained_model.h5)

- Display the predicted digit in the GUI
