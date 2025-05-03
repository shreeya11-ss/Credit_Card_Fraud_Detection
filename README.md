# 💳 Credit Card Fraud Detection

This project is focused on detecting fraudulent credit card transactions using machine learning algorithms. It uses a real-world anonymized dataset and provides insights into how classification techniques can help reduce financial fraud.

## 📂 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Results](#results)
- [License](#license)

## 📌 Overview

Credit card fraud is a growing problem in the digital economy. This project implements supervised learning models to identify fraudulent transactions from the dataset. The models are evaluated using various metrics due to the class imbalance in the data.

## 📊 Dataset

The dataset used in this project is provided by [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud). It contains transactions made by European cardholders in September 2013.

- Number of transactions: 284,807
- Fraudulent transactions: 492
- Features: 30 (including 'Time', 'Amount', and 28 anonymized features: V1–V28)

## ⚙️ Technologies Used

- Python 3.x
- Jupyter Notebook / VS Code
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Imbalanced-learn (for SMOTE, etc.)

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
