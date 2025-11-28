import streamlit as st

# Page configuration
st.set_page_config(page_title="AI4Farm", layout="centered")

# Title
st.title("🌱 AI4Farm - Soil Health Estimator")
st.write("A simple AI-assisted tool to estimate soil health for small farmers.")

# User inputs
soil_color = st.selectbox("Select soil color:", ["Dark", "Brown", "Reddish", "Pale"])
moisture = st.slider("Estimated soil moisture (%)", 0, 100, 40)
crop = st.selectbox("Select crop type:", ["Maize", "Cassava", "Beans", "Rice", "Other"])

# Process button
if st.button("Analyze Soil"):

    # Basic scoring (simple logic for demo purposes)
    score = 50

    # Soil color impact
    if soil_color == "Dark":
        score += 20
    elif soil_color == "Brown":
        score += 10
    elif soil_color == "Pale":
        score -= 10

    # Moisture impact
    if moisture < 30:
        score -= 15
    elif moisture > 70:
        score -= 10
    else:
        score += 5

    # Display results
    st.subheader(f"🌾 Soil Health Score: {score}/100")

    if score < 50:
        st.error("⚠️ Your soil may be unhealthy. Consider adding compost or organic fertilizer.")
    elif score < 70:
        st.warning("⚠️ Your soil is average. Improving moisture control may help yield.")
    else:
        st.success("✅ Your soil looks healthy! Keep maintaining good practices.")
