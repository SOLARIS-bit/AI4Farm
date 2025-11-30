# 🌱 AI4Farm – Soil Health Estimator

```markdown
![Streamlit App](https://img.shields.io/badge/Live_App-Online-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge)
```


AI4Farm is a lightweight, AI-inspired soil health assessment tool designed for smallholder farmers.  
It provides a Soil Health Score out of 100 along with actionable recommendations based on moisture, organic matter, texture, rainfall, and soil color.

This project was created for the **MIT Solve Challenge** and for academic work at **Aivancity School of Technology, Business & Society**.

---

## 🚀 Live Demo
👉 https://ai4farm-lfxvkgtcyh9ppk4yvz3fvm.streamlit.app/

---

## ✨ Features

* **🌍 Multilingual Support:** seamless toggling between English and French for broader accessibility in West/Central Africa and global contexts.
* **🧠 Intelligent Scoring Algorithm:** Calculates a 0-100 health score based on weighted agronomic principles.
* **📍 Geolocation Mapping:** Visualizes farm location using Latitude/Longitude inputs.
* **🌾 Personalized Recommendations:** Provides specific advice based on risk levels (e.g., "Add compost," "Improve drainage").
* **📄 PDF Export:** Generates a downloadable, timestamped report for offline record-keeping.
* **🎨 Eco-Friendly UI:** A custom-styled dark/green theme designed to be easy on the eyes.
---

## 📂 Project Structure

```

ai4farm/
│── app.py
│── requirements.txt
│── README.md

````

---

## ▶️ Run Locally

```bash
pip install streamlit fpdf
streamlit run app.py
````

---

## ☁️ Deployment (Streamlit Cloud)

1. Push this repository to GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Choose your repo → select `app.py`
4. Deploy 🚀

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Python framework for data apps)
* **Data Processing:** [Pandas](https://pandas.pydata.org/)
* **Report Generation:** [FPDF](https://pyfpdf.readthedocs.io/)
* **Logic:** Custom Python algorithms

---

## 👤 Author

Developed by **Kennedy MBA**
Aivancity School of Technology, Business & Society
2025
