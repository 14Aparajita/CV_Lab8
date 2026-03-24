# Depthwise Separable CNN for CIFAR-10 Classification

## Overview

This project implements a Convolutional Neural Network using **Depthwise Separable Convolutions (DSC)** for efficient image classification on the CIFAR-10 dataset.

The goal is to reduce computational complexity while maintaining high classification accuracy.

---

## Key Concepts

### Depthwise Convolution

Applies one filter per input channel.

### Pointwise Convolution

Uses 1×1 convolution to combine channel outputs.

### Depthwise Separable Convolution

Combination of depthwise and pointwise convolution for efficiency.

---

## Dataset

* CIFAR-10 dataset
* 60,000 images
* 10 classes
* Image size: 32×32

---

## Model Architecture

* Conv2D (32 filters)
* BatchNorm + ReLU

### Depthwise Separable Blocks:

* SeparableConv2D (64)
* SeparableConv2D (128)
* SeparableConv2D (256)

Each block includes:

* Batch Normalization
* ReLU Activation
* MaxPooling

### Final Layers:

* Global Average Pooling
* Dense (128)
* Dropout (0.3)
* Softmax Output

---

## Training Configuration

* Optimizer: Adam
* Loss: Categorical Crossentropy
* Epochs: 10
* Batch Size: 64

---

## Results

| Metric            | Value   |
| ----------------- | ------- |
| Training Accuracy | ~85–90% |
| Test Accuracy     | ~80–85% |

---

## How to Run

```bash
git clone https://github.com/yourusername/Depthwise-Separable-CNN-CIFAR10.git
cd Depthwise-Separable-CNN-CIFAR10
pip install -r requirements.txt
```

Run notebook:

```
DSC_CIFAR10.ipynb
```

---

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib

---

## Applications

* Mobile vision systems
* Real-time image processing
* Embedded AI

---

## Author

Student Project
Computer Vision Lab
B.Tech – AI & DS

---

## License

For academic use only.
