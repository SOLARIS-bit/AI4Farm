# 🌱 AI4Farm – Soil Health Estimator

```markdown
![Live Streamlit App](https://img.shields.io/badge/Live_App-Online-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
``` 

AI4Farm is a lightweight, AI-inspired soil health assessment tool designed for smallholder farmers. It computes a Soil Health Score (0–100) and provides actionable recommendations based on inputs such as moisture, organic matter, texture, rainfall, and soil color.

This project was created for the **MIT Solve Challenge** and for academic work at **Aivancity School of Technology, Business & Society**.

---

## 🚀 Live Demo

Open the live app here:
https://ai4farm-lfxvkgtcyh9ppk4yvz3fvm.streamlit.app/

---

## Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Deployment (Streamlit Cloud)](#-deployment-streamlit-cloud)
- [Tech Stack](#-tech-stack)
- [Contributing](#-contributing)
- [License & Credits](#-license--credits)
- [Author](#-author)

---

## ✨ Features

- 🌍 Multilingual support (English & French)
- 🧠 Soil Health scoring algorithm (0–100) based on agronomic rules
- 📍 Geolocation mapping via latitude/longitude inputs
- 🌾 Personalized, timestamped PDF recommendations for offline records
- 🎨 Dark/green themed UI optimized for ease of use in field settings

---

## 📂 Project Structure

````markdown
ai4farm/
├── app.py
├── requirements.txt
├── README.md
````

---

## ▶️ Installation

Recommended: create a virtual environment and install dependencies.

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

If you prefer to install only the core packages used by the app:

```bash
pip install streamlit fpdf pandas
```

---

## ⚙️ Usage

Run the Streamlit app locally:

```bash
streamlit run app.py
```

Enter farm data (moisture, organic matter, texture, rainfall, soil color, latitude/longitude) into the UI and press Run to see the Soil Health Score and recommendations. Use the PDF export button to download a timestamped report.

---

## ☁️ Deployment (Streamlit Cloud)

1. Push this repository to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub account, choose the SOLARIS-bit/AI4Farm repository and select `app.py`
4. Deploy 🚀

---

## 🛠️ Tech Stack

- Frontend: Streamlit (Python)
- Data processing: pandas
- PDF generation: FPDF
- Logic: Custom Python rules/algorithms

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome! Please open an issue or submit a pull request with a clear description of the change and why it's needed.

Suggested steps for contributors:
1. Fork the repository
2. Create a branch: git checkout -b feature/your-feature
3. Make your changes and add tests if appropriate
4. Push to your fork and open a PR

---

## 📄 License & Credits

This project was developed for academic purposes and the MIT Solve Challenge. Add your preferred license file (e.g., MIT) to the repository if you want to allow reuse. Please credit the original author if you reuse the project.

---

## 👤 Author

Developed by **Kennedy MBA**
Aivancity School of Technology, Business & Society
2025

---

## ✉️ Contact

For questions or collaboration, open an issue or contact the author via their GitHub profile: https://github.com/SOLARIS-bit
