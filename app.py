import streamlit as st
import pandas as pd
from fpdf import FPDF
import io
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI4Farm - Soil Health Estimator",
    page_icon="🌱",
    layout="centered",
)

# Branding / logo header
st.markdown("""
<div style='text-align:center;'>
    <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Icon_soil.svg/512px-Icon_soil.svg.png' 
         width='90' style='margin-bottom:10px;'/>
</div>
""", unsafe_allow_html=True)

# Language selector (English / Français)
lang = st.radio("Language / Langue", ["English", "Français"], index=0, horizontal=True)

def T(en, fr):
    return fr if lang == "Français" else en

# Title and subtitle
st.markdown(f"""
<div style='text-align: center;'>
    <h1>🌱 AI4Farm</h1>
    <h3>{T("Soil Health Estimator for Small Farmers", "Estimateur de la santé des sols pour petits agriculteurs")}</h3>
    <p style='color: gray;'>{T("Smart, simple and accessible crop decision support", "Support décisionnel simple, accessible et intelligent pour les cultures")}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Optional: farm location picker (latitude / longitude)
st.subheader(T("📍 Farm Location (optional)", "📍 Emplacement de la ferme (optionnel)"))
with st.expander(T("Use coordinates to personalize recommendations (optional). Leave empty to skip.", "Utilisez des coordonnées pour personnaliser les recommandations (optionnel). Laisser vide pour ignorer.")):
    lat = st.text_input(T("Latitude (e.g. -1.2921)", "Latitude (ex : -1.2921)"), value="")
    lon = st.text_input(T("Longitude (e.g. 36.8219)", "Longitude (ex : 36.8219)"), value="")
    if lat and lon:
        try:
            lat_f = float(lat)
            lon_f = float(lon)
            df_map = pd.DataFrame({"lat": [lat_f], "lon": [lon_f]})
            st.map(df_map)
        except Exception:
            st.warning(T("Invalid coordinates. Please enter numeric latitude and longitude.", "Coordonnées invalides. Veuillez entrer des valeurs numériques."))
    else:
        st.info(T("You can optionally add latitude & longitude for a map preview.", "Vous pouvez éventuellement ajouter latitude & longitude pour un aperçu de la carte."))

st.markdown("---")

# Input area
st.subheader(T("🧪 Soil Information", "🧪 Informations sur le sol"))
st.write(T("Fill out the details below to generate a soil health assessment.", "Remplissez les informations ci-dessous pour générer une évaluation de la santé du sol."))

col1, col2 = st.columns(2)
with col1:
    soil_color = st.selectbox(T("Soil Color", "Couleur du sol"), [T("Dark", "Sombre"), T("Brown", "Marron"), T("Reddish", "Roussâtre"), T("Pale", "Pâle")])
    # store internal keys
    soil_color_key = {"Dark": "Dark", "Sombre": "Dark",
                      "Brown": "Brown", "Marron": "Brown",
                      "Reddish": "Reddish", "Roussâtre": "Reddish",
                      "Pale": "Pale", "Pâle": "Pale"}[soil_color]

    soil_texture = st.selectbox(T("Soil Texture", "Texture du sol"), [T("Sandy", "Sableux"), T("Loamy", "Limoneux"), T("Clay", "Argileux"), T("Silty", "Luté")] )
    soil_texture_key = {T("Sandy", "Sableux"): "Sandy",
                        T("Loamy", "Limoneux"): "Loamy",
                        T("Clay", "Argileux"): "Clay",
                        T("Silty", "Luté"): "Silty"}[soil_texture]

    crop = st.selectbox(T("Crop Type", "Type de culture"), [T("Maize","Maïs"), T("Cassava","Manioc"), T("Beans","Haricots"), T("Rice","Riz"), T("Other","Autre")])
    crop_key = {T("Maize","Maïs"): "Maize", T("Cassava","Manioc"): "Cassava", T("Beans","Haricots"): "Beans", T("Rice","Riz"): "Rice", T("Other","Autre"): "Other"}[crop]

with col2:
    moisture = st.slider(T("Soil Moisture (%)", "Humidité du sol (%)"), 0, 100, 40)
    organic = st.slider(T("Organic Matter Level (%)", "Taux de matière organique (%)"), 0, 10, 3)
    rainfall = st.slider(T("Rainfall (last 7 days, mm)", "Pluviométrie (7 derniers jours, mm)"), 0, 200, 50)

st.markdown("---")

# Help text and how it works
with st.expander(T("How AI4Farm estimates soil health (short)", "Comment AI4Farm estime la santé du sol (bref)")):
    st.write(T(
        "AI4Farm combines simple user inputs with public data and a lightweight scoring model to provide a Soil Health Score and actionable recommendations. This is a conceptual tool and not a laboratory test.",
        "AI4Farm combine des entrées simples, des données publiques et un modèle de scoring léger pour fournir un score de santé du sol et des recommandations actionnables. C'est un outil conceptuel, pas un test de laboratoire."
    ))

# Scoring factors
color_factor = {"Dark": 15, "Brown": 5, "Reddish": -5, "Pale": -10}
texture_factor = {"Loamy": 10, "Sandy": -5, "Clay": -5, "Silty": 0}

# Analyze button and logic
if st.button(T("🌾 Analyze Soil", "🌾 Analyser le sol")):
    # Use the internal keys for calculation
    score = 0.0

    # Weighted scoring model (AI-inspired heuristic)
    # Color & texture
    score += color_factor.get(soil_color_key, 0) * 1.2
    score += texture_factor.get(soil_texture_key, 0) * 1.5

    # Organic matter importance
    score += (organic * 2.0)

    # Moisture contribution (scale)
    score += (moisture / 10.0)

    # Rainfall contribution (scale)
    score += (rainfall / 20.0)

    # Extra adjustments (penalties)
    if moisture < 20:
        score -= 8
        moisture_status = T("Too dry", "Trop sec")
    elif moisture > 80:
        score -= 5
        moisture_status = T("Too wet", "Trop humide")
    else:
        moisture_status = T("Optimal moisture", "Humidité optimale")
        score += 2

    if organic < 2:
        score -= 12
        organic_status = T("Low organic matter", "Faible matière organique")
    elif organic < 5:
        organic_status = T("Average organic matter", "Matière organique moyenne")
    else:
        organic_status = T("High organic matter", "Matière organique élevée")

    if rainfall < 10:
        score -= 10
        rain_status = T("Insufficient rainfall", "Pluviométrie insuffisante")
    elif rainfall > 150:
        score -= 5
        rain_status = T("Excessive rainfall", "Pluviométrie excessive")
    else:
        rain_status = T("Healthy rainfall", "Pluviométrie saine")
        score += 1

    # Minor crop-specific tweak (conceptual)
    if crop_key == "Maize" and organic < 3:
        score -= 2

    # Final clamp and integer conversion
    score = int(max(0, min(round(score), 100)))

    # Risk category and color
    if score < 40:
        risk = T("❌ High Risk — Unhealthy Soil", "❌ Risque élevé — Sol non sain")
        risk_color = "red"
    elif score < 70:
        risk = T("⚠️ Medium Risk — Average Soil", "⚠️ Risque moyen — Sol moyen")
        risk_color = "orange"
    else:
        risk = T("✅ Low Risk — Healthy Soil", "✅ Risque faible — Sol sain")
        risk_color = "green"

    # Display results (report card)
    st.markdown("---")
    st.subheader(T("📊 Soil Health Report", "📊 Rapport de santé du sol"))

    st.markdown(
        f"""
        <div style='padding: 15px; border-radius: 10px; background-color: #f7fafc;'>
            <h3 style='color:{risk_color};'>{T('Soil Health Score', 'Score de santé du sol')}: {score}/100</h3>
            <p><b>{T('Risk Level', 'Niveau de risque')}:</b> {risk}</p>
            <ul>
                <li><b>{T('Moisture', 'Humidité')}:</b> {moisture_status}</li>
                <li><b>{T('Organic Matter', 'Matière organique')}:</b> {organic_status}</li>
                <li><b>{T('Rainfall (7 days)', 'Pluie (7 jours)')}:</b> {rain_status}</li>
                <li><b>{T('Soil Texture', 'Texture du sol')}:</b> {soil_texture}</li>
                <li><b>{T('Soil Color', 'Couleur du sol')}:</b> {soil_color}</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Recommendations block
    st.subheader(T("🌿 Recommendations", "🌿 Recommandations"))
    if score < 40:
        st.error(T(
            "- Add compost or manure\n- Increase organic matter\n- Improve irrigation or water retention\n- Avoid planting sensitive crops",
            "- Ajouter du compost ou du fumier\n- Augmenter la matière organique\n- Améliorer l'irrigation ou la rétention d'eau\n- Éviter de planter des cultures sensibles"
        ))
    elif score < 70:
        st.warning(T(
            "- Monitor watering carefully\n- Add moderate organic amendments\n- Choose crops adapted to medium fertility",
            "- Surveillez l'arrosage\n- Ajouter des amendements organiques modérés\n- Choisir des cultures adaptées à une fertilité moyenne"
        ))
    else:
        st.success(T(
            "- Soil is healthy\n- Maintain current practices\n- Avoid overwatering and excessive fertilizer",
            "- Le sol est sain\n- Maintenez les pratiques actuelles\n- Évitez le sur-arrosage et l'excès d'engrais"
        ))

    # PDF generation function (returns bytes)
    def generate_pdf_bytes(score, risk, moisture_status, organic_status, rain_status,
                           soil_texture, soil_color, crop, lat, lon):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 8, "AI4Farm Soil Health Report", ln=True, align="C")
        pdf.ln(6)
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 6, f"Date: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}", ln=True)
        if lat and lon:
            pdf.cell(0, 6, f"Location: {lat}, {lon}", ln=True)
        pdf.ln(4)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 7, f"Score: {score}/100", ln=True)
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 6, f"Risk Level: {risk}", ln=True)
        pdf.ln(3)
        pdf.cell(0, 6, f"Moisture: {moisture_status}", ln=True)
        pdf.cell(0, 6, f"Organic Matter: {organic_status}", ln=True)
        pdf.cell(0, 6, f"Rainfall (7d): {rain_status}", ln=True)
        pdf.cell(0, 6, f"Soil Texture: {soil_texture}", ln=True)
        pdf.cell(0, 6, f"Soil Color: {soil_color}", ln=True)
        pdf.cell(0, 6, f"Crop: {crop}", ln=True)
        pdf.ln(6)
        pdf.multi_cell(0, 6, T(
            "Notes: This is a conceptual soil health estimation tool for educational purposes. It does not replace laboratory analysis.",
            "Remarques : Ceci est une estimation conceptuelle de la santé du sol à des fins éducatives. Elle ne remplace pas les analyses de laboratoire."
        ))
        # Output to bytes
        s = pdf.output(dest='S').encode('latin-1')
        return s

    # Download button for PDF
    pdf_bytes = generate_pdf_bytes(score, risk, moisture_status, organic_status, rain_status,
                                   soil_texture, soil_color, crop, lat, lon)
    st.download_button(
        label=T("📄 Download Soil Report (PDF)", "📄 Télécharger le rapport (PDF)"),
        data=pdf_bytes,
        file_name="AI4Farm_Soil_Report.pdf",
        mime="application/pdf"
    )

    # Small note about the model
    st.info(T(
        "This tool uses a heuristic, AI-inspired scoring model for demonstration. For production, training with local soil samples is required.",
        "Cet outil utilise un modèle heuristique inspiré de l'IA à des fins de démonstration. Pour la production, une formation avec des échantillons locaux est nécessaire."
    ))

    st.markdown("---")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"""
<p style='text-align:center; color:gray; font-size: 13px;'>
AI4Farm © 2025 — {T('Designed with ❤️ for sustainable agriculture', 'Conçu avec ❤️ pour une agriculture durable')}<br>
{T('Version 2.0 — Premium Demo', 'Version 2.0 — Démo Premium')}
</p>
""", unsafe_allow_html=True)
