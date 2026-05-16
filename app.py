import streamlit as st
import pandas as pd
import joblib
import numpy as np
import plotly.graph_objects as go

# Set page configuration for a professional clinical look
st.set_page_config(
    page_title="Med-AI | Professional Diabetes Diagnostic System",
    page_icon="🧬",
    layout="wide"
)

# Advanced CSS for a Premium Glassmorphism Interface
st.markdown("""
    <style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%);
    }
    
    /* Custom Sidebar */
    [data-testid="stSidebar"] {
        background-color: #004d40;
        color: white;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Glassmorphism Cards */
    .clinical-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        margin-bottom: 20px;
    }
    
    .header-style {
        font-family: 'Inter', sans-serif;
        color: #004d40;
        font-weight: 800;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.5);
        border-radius: 10px 10px 0 0;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: bold;
    }

    .stTabs [aria-selected="true"] {
        background-color: #00796b !important;
        color: white !important;
    }
    
    /* Custom Button */
    div.stButton > button:first-child {
        background: linear-gradient(to right, #00796b, #004d40);
        color: white;
        border: none;
        padding: 15px 30px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        color: #e0f2f1;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_resources():
    try:
        model = joblib.load('models/diabetes_model.joblib')
        preprocessor = joblib.load('models/preprocessor.joblib')
        return model, preprocessor
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None

model, preprocessor = load_resources()

# Sidebar Clinical Context
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🏥 CLINICAL CONTEXT</h2>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/200/medical-doctor.png")
    st.markdown("---")
    st.markdown("""
    **Analytical Engine:** Random Forest v1.2  
    **Dataset:** Longitudinal Research Data  
    **Clinician:** Engineer Talha  
    """)
    st.success("✅ System Status: Active")
    st.markdown("---")
    st.info("The prediction score is calculated using clinical parameters including HbA1c, HOMA-IR, and BMI markers.")

# Main Application Header
st.markdown("<h1 class='header-style'>🧬 Advanced Diabetes Diagnostic Dashboard</h1>", unsafe_allow_html=True)

if model is None or preprocessor is None:
    st.error("⚠️ Model artifacts missing. Please ensure models are trained and stored in the 'models/' directory.")
else:
    # Layout with Glassmorphism
    with st.container():
        st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
        tab1, tab2, tab3 = st.tabs(["📊 BIOMETRIC DATA", "🧪 BLOOD ANALYSIS", "📝 CLINICAL HISTORY"])

        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                age = st.slider("Patient Age", 1, 100, 45)
                gender = st.selectbox("Gender", ["Male", "Female"])
                bmi = st.number_input("Body Mass Index (BMI)", 10.0, 50.0, 24.5, step=0.1)
            with col2:
                bp = st.number_input("Blood Pressure (Systolic)", 80, 200, 120)
                calories = st.number_input("Daily Calorie Intake", 1000, 5000, 2200)
                sedentary = st.slider("Sedentary Hours/Day", 0, 24, 6)

        with tab2:
            col1, col2 = st.columns(2)
            with col1:
                glucose = st.number_input("Fasting Glucose (mg/dL)", 50, 300, 95)
                hb_a1c = st.number_input("HbA1c Level (%)", 3.0, 15.0, 5.4, step=0.1)
                insulin = st.number_input("Insulin (µU/mL)", 0.0, 100.0, 12.0)
            with col2:
                homa_ir = st.number_input("HOMA-IR Score", 0.0, 15.0, 1.2)
                trig = st.number_input("Triglycerides (mg/dL)", 50, 400, 150)
                ldl = st.number_input("LDL Cholesterol (mg/dL)", 50, 300, 100)

        with tab3:
            col1, col2 = st.columns(2)
            with col1:
                family_history = st.checkbox("Family History of Diabetes")
                on_medication = st.checkbox("Currently on Medication")
                smoking = st.checkbox("Smoking History")
            with col2:
                alcohol = st.checkbox("Regular Alcohol Consumption")
                activity = st.selectbox("Physical Activity", ["low", "medium", "high"])
                sleep = st.slider("Sleep Duration (Hours)", 4, 12, 7)
        
        st.markdown("</div>", unsafe_allow_html=True)

    # Prediction Action
    if st.button("🚀 EXECUTE DIAGNOSTIC ANALYSIS"):
        # Prepare Data
        input_dict = {
            'year': [2026], 'country': ["Pakistan"], 'age': [age], 'gender': [gender],
            'BMI': [bmi], 'family_history': [1 if family_history else 0],
            'fasting_glucose': [glucose], 'HbA1c': [hb_a1c], 'insulin': [insulin],
            'HOMA_IR': [homa_ir], 'triglycerides': [trig], 'HDL': [45.0],
            'LDL': [ldl], 'blood_pressure': [bp], 'daily_calories': [calories],
            'sugar_intake': [25.0], 'physical_activity': [activity],
            'sleep_hours': [sleep], 'stress_level': [5], 'sedentary_hours': [sedentary],
            'stage': [0], 'geo_risk_factor': [0.1],
            'on_medication': [1 if on_medication else 0], 'alive': [1],
            'smoking': [1 if smoking else 0], 'alcohol': [1 if alcohol else 0],
            'BMI_category': ["Normal" if bmi < 25 else "Overweight"],
            'glucose_prev': [glucose], 'bmi_prev': [bmi]
        }
        
        df_input = pd.DataFrame(input_dict)
        processed = preprocessor.transform(df_input)
        
        # ML Inference
        prediction = model.predict(processed)[0]
        probability = model.predict_proba(processed)[0][1]
        
        st.markdown("---")
        
        # Result Layout
        res_col1, res_col2 = st.columns([1, 1])
        
        with res_col1:
            st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
            if prediction == 1:
                st.error("### 🚨 CLINICAL ALERT: HIGH RISK")
                color = "#d32f2f"
            else:
                st.success("### ✅ DIAGNOSIS: LOW RISK")
                color = "#2e7d32"
            
            st.metric(label="Risk Probability", value=f"{probability*100:.1f}%", delta=f"{'Danger' if prediction==1 else 'Safe'}")
            
            # Gauge Chart
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = probability * 100,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Probability Score", 'font': {'size': 24}},
                gauge = {
                    'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                    'bar': {'color': color},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "gray",
                    'steps': [
                        {'range': [0, 40], 'color': '#c8e6c9'},
                        {'range': [40, 70], 'color': '#fff9c4'},
                        {'range': [70, 100], 'color': '#ffcdd2'}],
                }))
            fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with res_col2:
            st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)
            st.subheader("📋 Clinical Insights")
            st.write(f"**Patient Age:** {age} Years")
            st.write(f"**HbA1c Status:** {'Elevated' if hb_a1c > 6.0 else 'Normal Range'}")
            st.write(f"**Metabolic Index:** BMI is {bmi:.1f}, which is categorized as {'Obese' if bmi > 30 else 'Overweight' if bmi > 25 else 'Healthy'}.")
            st.divider()
            st.markdown("""
                **Recommendations:**
                - Monitor postprandial glucose levels.
                - Routine check of lipid profile markers.
                - Implement lifestyle modifications if risk > 50%.
            """)
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #004d40; font-weight: bold;'>Med-AI v2.0 | Clinical Intelligence Framework | Semester Project</p>", unsafe_allow_html=True)
