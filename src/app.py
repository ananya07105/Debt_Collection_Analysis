import streamlit as st
import json
from profanity_detection import detect_profanity
from compliance_check import check_compliance
from call_quality import analyze_call_quality

st.title("Call Analysis Tool")

uploaded_file = st.file_uploader("Upload a JSON file", type=["json"])
analysis_type = st.selectbox("Select Analysis", ["Profanity Detection", "Privacy Compliance", "Call Quality"])

if uploaded_file:
    data = json.load(uploaded_file)

    if analysis_type == "Profanity Detection":
        result = detect_profanity([data])
        st.write(f"Profanity Found: {len(result)} instances")
    elif analysis_type == "Privacy Compliance":
        result = check_compliance(data)
        st.write("Privacy Violation Found" if not result else "No Violations")
    elif analysis_type == "Call Quality":
        result = analyze_call_quality(data)
        st.write(result)
