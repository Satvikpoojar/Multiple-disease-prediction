import os
import pickle
import streamlit as st

# Load models from saved directory
heart_model_path = r"E:\sathvik projects\ml projects\Multiple disease\heart_disease_model.sav"
parkinsons_model_path = r"E:\sathvik projects\ml projects\Multiple disease\parkinsons_model.sav"

heart_disease_model = pickle.load(open(heart_model_path, 'rb'))
parkinsons_model = pickle.load(open(parkinsons_model_path, 'rb'))

st.title("🧠💓 Multiple Disease Predictor")

tabs = st.tabs(["❤️ Heart Disease", "🧠 Parkinson's Disease"])

# -------- Heart Disease Tab --------
with tabs[0]:
    st.header("Heart Disease Prediction")
    
    age = st.number_input("Age", min_value=1)
    sex = st.radio("Sex", options=["Female", "Male"])
    cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)
    trestbps = st.number_input("Resting Blood Pressure")
    chol = st.number_input("Serum Cholesterol (mg/dl)")
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", options=[0, 1])
    restecg = st.number_input("Resting ECG Results (0-2)", min_value=0, max_value=2)
    thalach = st.number_input("Max Heart Rate Achieved")
    exang = st.radio("Exercise Induced Angina", options=[0, 1])
    oldpeak = st.number_input("ST Depression Induced by Exercise")
    slope = st.number_input("Slope of the Peak Exercise ST Segment (0-2)", min_value=0, max_value=2)
    ca = st.number_input("Number of Major Vessels (0-4)", min_value=0, max_value=4)
    thal = st.number_input("Thal (0=Normal, 1=Fixed, 2=Reversible)", min_value=0, max_value=2)

    if st.button("🔍 Predict Heart Disease"):
        sex_numeric = 0 if sex.lower() == 'female' else 1
        input_data = [age, sex_numeric, cp, trestbps, chol, fbs, restecg, thalach,
                      exang, oldpeak, slope, ca, thal]
        try:
            prediction = heart_disease_model.predict([input_data])[0]
            if prediction == 1:
                st.error("⚠️ The person has heart disease.")
            else:
                st.success("✅ The person does not have heart disease.")
        except Exception as e:
            st.error(f"Error in prediction: {e}")

# -------- Parkinson's Disease Tab --------
with tabs[1]:
    st.header("Parkinson's Disease Prediction")

    fo = st.number_input("MDVP:Fo(Hz)")
    fhi = st.number_input("MDVP:Fhi(Hz)")
    flo = st.number_input("MDVP:Flo(Hz)")
    jitter_percent = st.number_input("MDVP:Jitter(%)")
    jitter_abs = st.number_input("MDVP:Jitter(Abs)")
    rap = st.number_input("MDVP:RAP")
    ppq = st.number_input("MDVP:PPQ")
    ddp = st.number_input("Jitter:DDP")
    shimmer = st.number_input("MDVP:Shimmer")
    shimmer_db = st.number_input("MDVP:Shimmer(dB)")
    apq3 = st.number_input("Shimmer:APQ3")
    apq5 = st.number_input("Shimmer:APQ5")
    apq = st.number_input("MDVP:APQ")
    dda = st.number_input("Shimmer:DDA")
    nhr = st.number_input("NHR")
    hnr = st.number_input("HNR")
    rpde = st.number_input("RPDE")
    dfa = st.number_input("DFA")
    spread1 = st.number_input("Spread1")
    spread2 = st.number_input("Spread2")
    d2 = st.number_input("D2")
    ppe = st.number_input("PPE")

    if st.button("🔍 Predict Parkinson's Disease"):
        try:
            input_data = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer,
                          shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa,
                          spread1, spread2, d2, ppe]
            prediction = parkinsons_model.predict([input_data])[0]
            if prediction == 1:
                st.error("⚠️ The person has Parkinson's disease.")
            else:
                st.success("✅ The person does not have Parkinson's disease.")
        except Exception as e:
            st.error(f"Error in prediction: {e}")
