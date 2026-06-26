# 🍃 Fruit Leaf Disease Detection using CNN

> Automatically detect and classify diseases in fruit leaves using deep learning — helping farmers identify crop problems early.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=flat&logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-latest-red?style=flat&logo=keras)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=flat&logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

---

## 🔍 What It Does

This project uses a Convolutional Neural Network (CNN) to classify fruit leaf images into disease categories. Given an image of a fruit leaf, the model predicts whether the leaf is healthy or infected — and if infected, identifies the specific disease.

**Example:**
> Upload a photo of a mango leaf → Model detects *"Anthracnose disease"* with 92% confidence → Farmer takes early action before crop damage spreads.

---

## ✨ Features

- 🖼️ **Image Classification** — Multi-class disease detection from leaf images
- 🔧 **Image Preprocessing Pipeline** — Automated resizing, normalization, and augmentation using OpenCV
- 📊 **Model Evaluation** — Accuracy, loss curves, and confusion matrix for performance analysis
- 🔄 **Data Augmentation** — Rotation, flipping, zoom to improve model generalization
- 🧠 **CNN Architecture** — Custom deep learning model built with TensorFlow and Keras
- ⚡ **Prediction Pipeline** — Feed any leaf image and get instant disease classification

---

## 🏗️ Model Architecture

```
Input Image (224x224x3)
        │
        ▼
Conv2D + ReLU + MaxPooling
        │
        ▼
Conv2D + ReLU + MaxPooling
        │
        ▼
Conv2D + ReLU + MaxPooling
        │
        ▼
Flatten
        │
        ▼
Dense (512) + Dropout
        │
        ▼
Dense (Num Classes) + Softmax
        │
        ▼
Predicted Disease Class
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| Deep Learning | TensorFlow 2.x, Keras |
| Image Processing | OpenCV, NumPy |
| Data Handling | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Environment | Jupyter Notebook |

---

## 📁 Project Structure

```
fruit-leaf-disease-detection/
├── dataset/
│   ├── train/           # Training images (organized by class)
│   └── test/            # Testing images
├── notebooks/
│   └── model_training.ipynb   # Full training walkthrough
├── src/
│   ├── preprocess.py    # Image preprocessing & augmentation
│   ├── model.py         # CNN model definition
│   ├── train.py         # Training script
│   └── predict.py       # Single image prediction
├── models/
│   └── fruit_disease_model.h5  # Saved trained model
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- GPU recommended (but CPU works too)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Jayanthgowda33/fruit-leaf-disease-detection.git
cd fruit-leaf-disease-detection

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Training the Model

```bash
python src/train.py
```

### Predict on a New Image

```bash
python src/predict.py --image path/to/leaf_image.jpg
```

### Or Run the Notebook

```bash
jupyter notebook notebooks/model_training.ipynb
```

---

## 📊 Results

| Metric | Score |
|--------|-------|
| Training Accuracy | ~95% |
| Validation Accuracy | ~90% |
| Model Size | ~25 MB |

> _Update these numbers with your actual results from training_

---

## 📸 Demo

> _Add sample images here — a healthy leaf vs a diseased leaf, and the model's prediction_
>
> **Tip:** Add 2-3 example images directly in your repo under an `examples/` folder and display them here. Visual results are very impressive to recruiters!

---

## 🌱 Real-World Impact

Early detection of leaf disease can:
- Prevent up to **30-40% crop loss** in affected regions
- Reduce unnecessary pesticide usage
- Help farmers make faster, data-driven decisions

This project demonstrates how AI can be applied to solve real agricultural challenges.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repo
2. Create your branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👤 Author

**Jayanth Gowda S K**
- 📧 gowdajayanth837@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/jayanth-gowda-b62344351)
- 🐙 [GitHub](https://github.com/Jayanthgowda33)

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ **If you found this useful, please give it a star!**
