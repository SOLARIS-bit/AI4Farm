import streamlit as st

# Page config
st.set_page_config(
    page_title="AI4Farm - Soil Health Estimator",
    page_icon="🌱",
    layout="centered",
)

# HEADER
st.markdown("""
<div style='text-align: center;'>
    <h1>🌱 AI4Farm</h1>
    <h3>Soil Health Estimator for Small Farmers</h3>
    <p style='color: gray;'>Smart, simple and accessible crop decision support</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.subheader("🧪 Soil Information")
st.write("Fill out the details below to generate a soil health assessment.")

# INPUTS IN TWO COLUMNS
col1, col2 = st.columns(2)

with col1:
    soil_color = st.selectbox("Soil Color", ["Dark", "Brown", "Reddish", "Pale"])
    soil_texture = st.selectbox("Soil Texture", ["Sandy", "Loamy", "Clay", "Silty"])
    crop = st.selectbox("Crop Type", ["Maize", "Cassava", "Beans", "Rice", "Other"])

with col2:
    moisture = st.slider("Soil Moisture (%)", 0, 100, 40)
    organic = st.slider("Organic Matter Level (%)", 0, 10, 3)
    rainfall = st.slider("Rainfall (last 7 days, mm)", 0, 200, 50)

st.markdown("---")

# PROCESS BUTTON
if st.button("🌾 Analyze Soil"):

    score = 50

    # Soil color influence
    color_factor = {"Dark": 15, "Brown": 5, "Reddish": -5, "Pale": -10}
    score += color_factor[soil_color]

    # Moisture impact
    if moisture < 30:
        score -= 15
        moisture_status = "Too dry"
    elif moisture > 70:
        score -= 5
        moisture_status = "Too wet"
    else:
        score += 5
        moisture_status = "Optimal moisture"

    # Organic matter
    if organic >= 5:
        score += 10
        organic_status = "High organic content"
    elif organic >= 3:
        score += 5
        organic_status = "Average organic matter"
    else:
        score -= 10
        organic_status = "Low organic matter"

    # Soil texture impact
    texture_factor = {"Loamy": 10, "Sandy": -5, "Clay": -5, "Silty": 0}
    score += texture_factor[soil_texture]

    # Rainfall
    if rainfall < 20:
        score -= 10
        rain_status = "Insufficient rainfall"
    elif rainfall > 150:
        score -= 5
        rain_status = "Excessive rainfall"
    else:
        score += 5
        rain_status = "Healthy rainfall"

    # Clamp score between 0–100
    score = max(0, min(score, 100))

    # Risk category
    if score < 40:
        risk = "❌ High Risk — Unhealthy Soil"
        color = "red"
    elif score < 70:
        risk = "⚠️ Medium Risk — Average Soil"
        color = "orange"
    else:
        risk = "✅ Low Risk — Healthy Soil"
        color = "green"

    # RESULTS SECTION
    st.markdown("---")
    st.subheader("📊 Soil Health Report")

    st.markdown(
        f"""
        <div style='padding: 15px; border-radius: 10px; background-color: #f0f2f6;'>
            <h3 style='color:{color};'>Soil Health Score: {score}/100</h3>
            <p><b>Risk Level:</b> {risk}</p>
            <ul>
                <li><b>Moisture:</b> {moisture_status}</li>
                <li><b>Organic Matter:</b> {organic_status}</li>
                <li><b>Rainfall:</b> {rain_status}</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # RECOMMENDATIONS
    st.subheader("🌿 Recommendations")

    if score < 40:
        st.error("""
        - Add compost or manure  
        - Increase organic matter  
        - Improve irrigation or water retention  
        - Avoid planting sensitive crops  
        """)
    elif score < 70:
        st.warning("""
        - Monitor watering carefully  
        - Add moderate organic amendments  
        - Choose crops adapted to medium fertility  
        """)
    else:
        st.success("""
        - Soil is healthy  
        - Maintain current practices  
        - Avoid overwatering and excessive fertilizer  
        """)

st.markdown("---")

# ABOUT
st.markdown("""
### ℹ️ About AI4Farm
AI4Farm is a conceptual AI-powered tool designed to help smallholder farmers evaluate soil health using simple inputs and lightweight algorithms.  
Developed for the **MIT Solve Challenge** and educational purposes at Aivancity.
""")

st.markdown("<p style='text-align: center; color: gray;'>© 2025 AI4Farm</p>", unsafe_allow_html=True)
