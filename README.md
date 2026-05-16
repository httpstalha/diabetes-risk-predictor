# Advanced Clinical Diabetes Prediction System

## 🚀 Overview
This is a professional-grade AI system designed for the prediction of Type 2 Diabetes using high-fidelity clinical markers. The system integrates a robust Machine Learning backend with a modern Web Interface for real-time risk assessment.

---

## 📂 Project Structure
- **`Diabetes_Prediction.ipynb`**: Comprehensive data analysis and model training pipeline.
- **`app.py`**: Professional Streamlit-based Web Application.
- **`models/`**: Contains pre-trained `diabetes_model.joblib` and `preprocessor.joblib`.
- **`data/`**: Research-grade clinical dataset.
- **`README.md`**: Project documentation and setup guide.

---

## 🧬 Scientific Methodology
The prediction engine is powered by a **Random Forest Ensemble** algorithm. Unlike basic models, this system analyzes complex interactions between 30 features, including:
- **HbA1c & Fasting Glucose**: Core biological indicators.
- **Lipid Profile (HDL, LDL, Triglycerides)**: Metabolic markers.
- **Lifestyle Factors**: BMI, Stress Level, and Physical Activity.

---

## 🏥 Clinical Dashboard (GUI)
The **Streamlit** GUI provides a user-friendly way to input patient data. It outputs:
1. **Risk Category**: (High/Low Risk)
2. **Probability Score**: Quantified risk percentage.
3. **Medical Insights**: Brief analysis based on input values.

---

## ⚙️ Setup & Execution
1. **Install Requirements**:
   ```bash
   pip install streamlit joblib scikit-learn pandas matplotlib seaborn
   ```
2. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## 👨‍💻 Developed By
**Engineer Talha**  
*Semester Project - Clinical Intelligence Systems*
