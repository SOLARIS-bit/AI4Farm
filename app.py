import streamlit as st
import pandas as pd
from fpdf import FPDF
import re
from datetime import datetime

# ----------------------------------
# 🌱 PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="AI4Farm – Soil Intelligence",
    page_icon="🌱",
    layout="centered",
)

# ----------------------------------
# 🍃 NATURAL TITLE HEADER
# ----------------------------------
st.markdown("""
<div style='text-align:center; padding:25px 10px 10px 10px;'>
    <h1 style='font-size:48px; margin-bottom:0;'>
        🌱 AI4Farm
    </h1>
    <p style='color:#4a4a4a; font-size:20px; margin-top:6px;'>
        Smart Soil Intelligence for Small Farmers
    </p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------
# 🌿 ECO BACKGROUND STYLE
# ----------------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #e9fce9 0%, #f7fff7 60%, #ffffff 100%);
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0) !important;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------
# 🌳 GREEN CARD CSS
# ----------------------------------
st.markdown("""
<style>
.green-card {
    background-color: #e7f5e9;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0px 4px 18px rgba(0, 128, 0, 0.10);
    margin-bottom: 22px;
    transition: 0.3s ease;
}
.green-card:hover {
    background-color: #ddf0e3;
    box-shadow: 0px 5px 22px rgba(0, 128, 0, 0.20);
}
.section-title {
    font-size: 30px;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)


# ----------------------------------
# 🌍 LANGUAGE SELECTOR
# ----------------------------------
lang = st.radio("Language / Langue", ["English", "Français"], horizontal=True)

def T(en, fr):
    return fr if lang == "Français" else en


# ----------------------------------
# 📍 OPTIONAL LOCATION INPUT
# ----------------------------------
st.markdown("<div class='green-card'>", unsafe_allow_html=True)
st.subheader("📍 " + T("Farm Location (optional)", "Emplacement de la ferme (optionnel)"))

with st.expander(T("Add latitude & longitude to display your farm on a map.",
                   "Ajoutez latitude & longitude pour afficher votre ferme sur une carte.")):
    lat = st.text_input("Latitude", "")
    lon = st.text_input("Longitude", "")
    if lat and lon:
        try:
            lat_f = float(lat)
            lon_f = float(lon)
            st.map(pd.DataFrame({"lat": [lat_f], "lon": [lon_f]}))
        except:
            st.warning(T("Invalid coordinates.", "Coordonnées invalides."))

st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------------
# 🧪 SOIL INFORMATION INPUT
# ----------------------------------
st.markdown("<div class='green-card'>", unsafe_allow_html=True)
st.subheader("🌱 " + T("Soil Information", "Informations sur le sol"))

col1, col2 = st.columns(2)

with col1:
    soil_color = st.selectbox(
        T("Soil Color", "Couleur du sol"),
        [T("Dark", "Sombre"), T("Brown", "Marron"), T("Reddish", "Roussâtre"), T("Pale", "Pâle")]
    )
    soil_color_key = {"Dark":"Dark","Sombre":"Dark",
                      "Brown":"Brown","Marron":"Brown",
                      "Reddish":"Reddish","Roussâtre":"Reddish",
                      "Pale":"Pale","Pâle":"Pale"}[soil_color]

    soil_texture = st.selectbox(
        T("Soil Texture", "Texture du sol"),
        [T("Sandy","Sableux"), T("Loamy","Limoneux"),
         T("Clay","Argileux"), T("Silty","Luté")]
    )
    soil_texture_key = {
        T("Sandy","Sableux"):"Sandy",
        T("Loamy","Limoneux"):"Loamy",
        T("Clay","Argileux"):"Clay",
        T("Silty","Luté"):"Silty"
    }[soil_texture]

    crop = st.selectbox(
        T("Crop Type","Type de culture"),
        [T("Maize","Maïs"), T("Cassava","Manioc"),
         T("Beans","Haricots"), T("Rice","Riz"), T("Other","Autre")]
    )
    crop_key = {
        T("Maize","Maïs"):"Maize",
        T("Cassava","Manioc"):"Cassava",
        T("Beans","Haricots"):"Beans",
        T("Rice","Riz"):"Rice",
        T("Other","Autre"):"Other"
    }[crop]

with col2:
    moisture = st.slider(T("Soil Moisture (%)","Humidité du sol (%)"), 0, 100, 40)
    organic = st.slider(T("Organic Matter (%)","Matière organique (%)"), 0, 10, 3)
    rainfall = st.slider(T("Rainfall 7 days (mm)","Pluie 7 jours (mm)"), 0, 200, 50)

st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------------
# 🧠 MODE: STANDARD or AI EXPLANATION
# ----------------------------------
st.markdown("<div class='green-card'>", unsafe_allow_html=True)
mode = st.radio("Mode:", ["Standard Recommendations", "AI Explanation Mode"], horizontal=True)
st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------------
# 🔢 SCORING FACTORS
# ----------------------------------
color_factor = {"Dark":15, "Brown":5, "Reddish":-5, "Pale":-10}
texture_factor = {"Loamy":10, "Sandy":-5, "Clay":-5, "Silty":0}


# ----------------------------------
# 🌾 ANALYZE BUTTON
# ----------------------------------
if st.button("🌾 " + T("Analyze Soil","Analyser le sol")):

    # ----------------------
    # 🧮 SCORE CALCULATION
    # ----------------------
    score = 0.0
    score += color_factor[soil_color_key] * 1.2
    score += texture_factor[soil_texture_key] * 1.5
    score += organic * 2
    score += moisture / 10
    score += rainfall / 20

    if moisture < 20:
        score -= 8
        moisture_status = T("Too dry","Trop sec")
    elif moisture > 80:
        score -= 5
        moisture_status = T("Too wet","Trop humide")
    else:
        score += 2
        moisture_status = T("Optimal moisture","Humidité optimale")

    if organic < 2:
        score -= 12
        organic_status = T("Low organic matter","Faible matière organique")
    elif organic < 5:
        organic_status = T("Medium organic matter","Matière organique moyenne")
    else:
        organic_status = T("High organic matter","Matière organique élevée")

    if rainfall < 10:
        score -= 10
        rain_status = T("Very low rainfall","Pluie insuffisante")
    elif rainfall > 150:
        score -= 5
        rain_status = T("Excessive rainfall","Pluie excessive")
    else:
        rain_status = T("Healthy rainfall","Bonne pluviométrie")
        score += 1

    score = int(max(0, min(round(score), 100)))

    # RISK CATEGORY
    if score < 40:
        risk = T("❌ High Risk — Unhealthy Soil","❌ Risque élevé — Sol non sain")
        risk_color = "red"
    elif score < 70:
        risk = T("⚠️ Medium Risk — Average Soil","⚠️ Risque moyen — Sol moyen")
        risk_color = "orange"
    else:
        risk = T("✅ Low Risk — Healthy Soil","✅ Risque faible — Sol sain")
        risk_color = "green"


    # ----------------------------------
    # 🍃 SOIL HEALTH REPORT
    # ----------------------------------
    st.markdown("<div class='green-card'>", unsafe_allow_html=True)
    st.markdown(f"""
        <h3 class='section-title'>🍃 {T("Soil Health Report","Rapport de santé du sol")}</h3>

        <b>{T("Score","Score")}:</b>
        <span style='color:{risk_color}; font-size:26px;'> {score}/100 </span><br><br>

        <b>{T("Risk Level","Niveau de risque")}:</b> {risk}<br><br>

        <b>{T("Moisture","Humidité")}:</b> {moisture_status}<br>
        <b>{T("Organic Matter","Matière organique")}:</b> {organic_status}<br>
        <b>{T("Rainfall (7 days)","Pluie (7 jours)")}:</b> {rain_status}<br>
        <b>{T("Soil Texture","Texture du sol")}:</b> {soil_texture}<br>
        <b>{T("Soil Color","Couleur du sol")}:</b> {soil_color}<br>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


    # ----------------------------------
    # 🌾 RECOMMENDATIONS / AI MODE
    # ----------------------------------
    st.markdown("<div class='green-card'>", unsafe_allow_html=True)
    st.subheader("🌾 " + T("Recommendations","Recommandations"))

    if mode == "Standard Recommendations":
        if score < 40:
            st.error(T(
                "- Add compost or manure\n- Improve irrigation\n- Increase organic matter\n- Avoid sensitive crops",
                "- Ajouter du compost ou du fumier\n- Améliorer l'irrigation\n- Augmenter la matière organique\n- Éviter les cultures sensibles"
            ))
        elif score < 70:
            st.warning(T(
                "- Monitor watering\n- Add organic inputs\n- Choose medium-fertility crops",
                "- Surveiller l'arrosage\n- Ajouter des amendements organiques\n- Choisir des cultures adaptées"
            ))
        else:
            st.success(T(
                "- Soil is healthy\n- Maintain practices\n- Avoid overwatering",
                "- Le sol est sain\n- Maintenir les bonnes pratiques\n- Éviter le sur-arrosage"
            ))

    else:
        st.info(f"""
### 🤖 {T("AI Explanation","Explication IA")}

{T("Your score is calculated using:", "Votre score est calculé avec :")}

- {T("Color factor","Facteur couleur")}: {color_factor[soil_color_key]} × 1.2  
- {T("Texture factor","Facteur texture")}: {texture_factor[soil_texture_key]} × 1.5  
- {T("Organic matter contribution","Contribution de la matière organique")}: {organic * 2}  
- {T("Moisture contribution","Contribution de l'humidité")}: {moisture / 10}  
- {T("Rainfall contribution","Contribution de la pluie")}: {rainfall / 20}  

{T("Penalties applied for imbalance in moisture, organic matter or rainfall.",
   "Pénalités appliquées pour déséquilibre de l'humidité, de la matière organique ou de la pluie.")}

### {T("AI-Generated Interpretation","Interprétation générée par l'IA")}  
**{risk}**
""")

    st.markdown("</div>", unsafe_allow_html=True)


    # ----------------------------------
    # 📄 PDF EXPORT (FIXED FOR UNICODE)
    # ----------------------------------
    def remove_non_ascii(txt):
        return re.sub(r"[^\x00-\x7F]+", "", txt)

    def generate_pdf_bytes():
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial","B",14)
        pdf.cell(0,8,"AI4Farm Soil Health Report", ln=True, align="C")
        pdf.ln(4)

        pdf.set_font("Arial", size=11)
        pdf.cell(0,6,f"Date: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}", ln=True)
        if lat and lon:
            pdf.cell(0,6,f"Location: {lat}, {lon}", ln=True)

        pdf.ln(4)
        pdf.cell(0,6,remove_non_ascii(f"Score: {score}/100"), ln=True)
        pdf.cell(0,6,remove_non_ascii(f"Risk: {risk}"), ln=True)
        pdf.cell(0,6,remove_non_ascii(f"Moisture: {moisture_status}"), ln=True)
        pdf.cell(0,6,remove_non_ascii(f"Organic Matter: {organic_status}"), ln=True)
        pdf.cell(0,6,remove_non_ascii(f"Rainfall: {rain_status}"), ln=True)

        pdf.ln(6)
        pdf.multi_cell(0,6,
            remove_non_ascii(
                "This is a conceptual soil health estimation tool. Not a laboratory analysis."
            )
        )

        return pdf.output(dest="S").encode("latin-1","ignore")

    pdf_bytes = generate_pdf_bytes()

    st.download_button(
        label="📄 " + T("Download PDF Report","Télécharger le rapport PDF"),
        data=pdf_bytes,
        file_name="AI4Farm_Soil_Report.pdf",
        mime="application/pdf"
    )


# ----------------------------------
# 🌻 FOOTER
# ----------------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:#4a4a4a; font-size:14px; padding-top:10px;'>
🍃 AI4Farm © 2025 — Designed for Sustainable Agriculture<br>
<em>Nature. Data. Intelligence.</em>
</p>
""", unsafe_allow_html=True)
