<div align="center">

<img src="https://img.icons8.com/clouds/150/medical-doctor.png" alt="Med-AI Logo"/>

# 🧬 Med-AI: Type 2 Diabetes Risk Prediction System

### Clinical-Grade Machine Learning · Streamlit Web App · Random Forest Ensemble

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.57-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/httpstalha/diabetes-risk-predictor?style=for-the-badge&color=yellow)](https://github.com/httpstalha/diabetes-risk-predictor/stargazers)

**An advanced, end-to-end clinical AI system that predicts Type 2 Diabetes risk in real-time using 30 biomarkers — powered by Random Forest and deployed via a glassmorphism Streamlit dashboard.**

</div>

---

## 📌 Table of Contents

- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Model Performance](#-model-performance)
- [Setup & Installation](#-setup--installation)
- [How It Works](#-how-it-works)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🔬 About The Project

> **"Early detection saves lives."**

Diabetes affects **537 million adults globally** (IDF, 2025), yet a large percentage go undiagnosed until complications arise. This project bridges the gap between raw clinical data and actionable medical insight.

**Med-AI** is an applied ML project that trains a **Random Forest Ensemble** on a research-grade longitudinal dataset and deploys it as an interactive web application. Clinicians or researchers can input 30 clinical biomarkers and receive an **instant probability score** along with personalized medical insights.

This project is designed for:
- 🎓 **Students** learning applied machine learning in healthcare
- 🏥 **Researchers** prototyping clinical decision-support tools
- 💼 **Developers** exploring Streamlit deployment with ML pipelines

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧠 **ML Pipeline** | End-to-end `scikit-learn` pipeline with preprocessing + Random Forest model |
| 📊 **30 Clinical Features** | Biometric, biochemical, lifestyle, and historical data inputs |
| 🌡️ **Risk Gauge Chart** | Animated Plotly gauge showing real-time diabetes probability score |
| 💊 **Medical Insights** | Auto-generated patient-specific clinical recommendations |
| 🎨 **Glassmorphism UI** | Premium teal-themed Streamlit interface with custom CSS |
| 🚀 **One-Command Launch** | Instantly runnable with `streamlit run app.py` |
| 📁 **Pre-trained Models** | `.joblib` models included — no retraining required |

---

## 🛠️ Tech Stack

**Machine Learning:**
- `scikit-learn` — Random Forest Classifier, preprocessing pipeline
- `pandas` & `numpy` — Data manipulation
- `joblib` — Model serialization

**Web App:**
- `Streamlit` — Frontend framework
- `Plotly` — Interactive gauge charts
- Custom CSS (Glassmorphism design)

**Data:**
- Research-grade longitudinal Type 2 Diabetes dataset (v3)
- 30 clinical features: HbA1c, HOMA-IR, Triglycerides, BMI, Glucose, and more

---

## 📂 Project Structure
