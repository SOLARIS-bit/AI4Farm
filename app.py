import streamlit as st
from fpdf import FPDF

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="AI4Farm – Soil Health Estimator",
    layout="centered"
)

# ------------------------------------------------------
# TRANSLATION FUNCTION
# ------------------------------------------------------
def T(en, fr):
    return en if st.session_state.get("lang", "en") == "en" else fr

# ------------------------------------------------------
# PREMIUM LOGO HEADER
# ------------------------------------------------------
LOGO_URL = "https://raw.githubusercontent.com/SOLARIS-bit/ai4farm/main/static/ChatGPT Image 29 nov 2025, 11_27_54 a.m..png"

st.markdown(f"""
    <div style='text-align:center; margin-top: -10px; margin-bottom: 10px;'>
        <img src="{LOGO_URL}" style="width:150px; border-radius:8px;"/>
        <h1 style="font-size:40px; font-weight:800; margin-bottom:0; margin-top:10px;">
            AI4Farm
        </h1>
        <p style="font-size:18px; color:#8f9094; margin-top:0;">
            Smart Soil Intelligence for Small Farmers
        </p>
    </div>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# PREMIUM CSS
# ------------------------------------------------------
st.markdown("""
<style>
.report-box {
    padding: 18px;
    background-color: #f9fafb;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    margin-bottom: 15px;
}
.section-title {
    font-size: 26px;
    font-weight: 700;
    margin-top: 20px;
}
.recommend-box {
    padding: 14px;
    border-radius: 10px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# LANGUAGE SELECTOR
# ------------------------------------------------------
lang = st.radio(
    "Language / Langue",
    ["en", "fr"],
    format_func=lambda x: "English" if x == "en" else "Français",
    horizontal=True
)
st.session_state["lang"] = lang

st.markdown("---")

# ------------------------------------------------------
# USER INPUTS
# ------------------------------------------------------
st.subheader(T("🌱 Soil Data Input", "🌱 Données du sol à analyser"))

soil_color = st.selectbox(
    T("Soil Color", "Couleur du sol"),
    ["Dark Brown", "Brown", "Reddish", "Yellowish", "Pale/Gray"]
)

soil_texture = st.selectbox(
    T("Soil Texture", "Texture du sol"),
    ["Clay", "Sandy", "Loamy", "Silty", "Gravelly"]
)

moisture = st.slider(
    T("Moisture Level (%)", "Humidité (%)"),
    0, 100, 50
)

organic = st.slider(
    T("Organic Matter (%)", "Matière organique (%)"),
    0, 15, 4
)

rainfall = st.slider(
    T("Recent Rainfall (mm)", "Pluviométrie récente (mm)"),
    0, 300, 50
)

crop = st.selectbox(
    T("Crop Type", "Type de culture"),
    ["Maize", "Cassava", "Beans", "Rice", "Tomato", "Groundnut"]
)

# ------------------------------------------------------
# AI MODEL EXPLANATION
# ------------------------------------------------------
with st.expander(T("🤖 How the AI-inspired model works", "🤖 Comment fonctionne le modèle inspiré de l’IA")):
    st.write(T(
        """
AI4Farm uses a light scoring model inspired by agricultural AI systems.
It evaluates soil using 6 key factors and produces a Soil Health Score.

### The model does 3 things:
1. **Extracts features** (color, texture, moisture, organic matter, rainfall, crop)
2. **Applies weights** (loamy soil ↑, pale color ↓, low organic ↓)
3. **Classifies risk**:
- Healthy (70–100)
- Medium (40–69)
- Degraded (0–39)
""",
"""
AI4Farm utilise un modèle léger inspiré des systèmes d’IA agricoles.
Il analyse 6 facteurs et calcule un score de santé du sol.

### Le modèle fait 3 choses :
1. **Analyse des caractéristiques**  
2. **Applique des pondérations**  
3. **Classe le risque** :
- Sol sain (70–100)
- Sol moyen (40–69)
- Sol dégradé (0–39)
"""
    ))

# ------------------------------------------------------
# SCORING SYSTEM (AI-INSPIRED)
# ------------------------------------------------------
score = 50

# Soil color effect
if soil_color == "Dark Brown":
    score += 20
elif soil_color == "Brown":
    score += 10
elif soil_color == "Pale/Gray":
    score -= 10

# Soil texture effect
if soil_texture == "Loamy":
    score += 20
elif soil_texture == "Sandy":
    score -= 10
elif soil_texture == "Gravelly":
    score -= 15

# Moisture
if 40 <= moisture <= 70:
    score += 15
else:
    score -= 10

# Organic matter
if organic < 2:
    score -= 20
elif organic >= 6:
    score += 15

# Rainfall
if rainfall < 30:
    score -= 5
elif rainfall > 180:
    score -= 10
else:
    score += 5

# Clamp score
score = max(0, min(100, score))

# Risk level
if score >= 70:
    risk = T("Healthy Soil", "Sol sain")
    color = "green"
elif score >= 40:
    risk = T("Moderate Soil", "Sol moyen")
    color = "orange"
else:
    risk = T("Degraded Soil", "Sol dégradé")
    color = "red"

# ------------------------------------------------------
# DISPLAY RESULTS
# ------------------------------------------------------
st.subheader(T("📊 Soil Health Results", "📊 Résultats de santé du sol"))

st.markdown(f"""
<div class="report-box">
    <h3 style="color:{color};">{risk}</h3>
    <p><b>{T("Soil Health Score", "Score de santé du sol")}:</b> {score}/100</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# AI EXPLANATION BUTTON (FIXED)
# ------------------------------------------------------
if st.button(T("💡 Explain this result (AI style)", "💡 Expliquer ce résultat (style IA)")):
    st.info(T(
        f"""
### 🔍 AI-style Interpretation

**Soil Health Score:** {score}/100  
**Category:** {risk}

**Key factors considered:**  
- Soil color: **{soil_color}**  
- Soil texture: **{soil_texture}**  
- Moisture: **{moisture}%**  
- Organic matter: **{organic}%**  
- Rainfall: **{rainfall} mm**  
- Crop: **{crop}**

This reasoning imitates how small agricultural AI models classify soil quality.
""",
        f"""
### 🔍 Interprétation style IA

**Score de santé du sol :** {score}/100  
**Catégorie :** {risk}

**Facteurs clés pris en compte :**  
- Couleur : **{soil_color}**  
- Texture : **{soil_texture}**  
- Humidité : **{moisture}%**  
- Matière organique : **{organic}%**  
- Pluie : **{rainfall} mm**  
- Culture : **{crop}**

Ce raisonnement imite la logique des petits modèles IA agricoles.
"""
    ))

# ------------------------------------------------------
# PDF REPORT GENERATOR
# ------------------------------------------------------
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()

    # UTF-8 font
    pdf.add_font("DejaVu", "", fname="DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", "", 14)

    pdf.cell(0, 10, txt="AI4Farm – Soil Health Report", ln=True, align='C')

    pdf.set_font("DejaVu", "", 12)
    pdf.ln(5)
    pdf.cell(0, 10, f"Soil Health Score: {score}/100", ln=True)
    pdf.cell(0, 10, f"Risk Category: {risk}", ln=True)
    pdf.ln(5)

    pdf.multi_cell(0, 8, f"""
Soil Color: {soil_color}
Soil Texture: {soil_texture}
Moisture: {moisture}%
Organic Matter: {organic}%
Rainfall: {rainfall} mm
Crop: {crop}
""")

    return pdf.output(dest="S").encode("utf-8")
