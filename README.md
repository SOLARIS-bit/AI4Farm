# 📁 **AI4Farm — GitHub Repository Structure**

```
ai4farm/
│── app.py
│── requirements.txt
│── README.md
```

---

# 🧠 **1. app.py (complete Streamlit app)**

Copy/paste this into a file called **app.py**:

```python
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
```

---

# 📦 **2. requirements.txt**

Create a file named **requirements.txt**:

```
streamlit
```

That’s all Streamlit Cloud needs to install.

---

# 📝 **3. README.md (professional GitHub version)**

Create a file called **README.md** and paste this:

````markdown
# 🌱 AI4Farm – Soil Health Estimator

AI4Farm is a simple prototype designed to help small farmers estimate the health of their soil using basic inputs and AI-inspired logic.

This project was created as part of the **MIT Solve Challenge** and the **C1 English Project** at aivancity.

---

## 🚀 Demo

A live demo will be available once deployed to **Streamlit Cloud**.

---

## 🎯 Purpose

Smallholder farmers often lack access to expensive soil testing services.  
AI4Farm uses **simple rules**, **open data**, and **user input** to provide a quick estimation of soil health.

This prototype:
- Takes 3 simple inputs (soil color, moisture, crop type)
- Computes a Soil Health Score out of 100
- Gives practical advice to the user

It is not a scientific soil test — but a **conceptual demo** showing how AI could support sustainable agriculture.

---

## 🧠 How It Works

- Built with **Python + Streamlit**
- Uses simple scoring logic emulating a basic AI model
- Runs in the browser with no installation needed

---

## ▶️ Run Locally

Make sure you have Python installed, then run:

```bash
pip install streamlit
streamlit run app.py
````

The app will open automatically in your browser.

---

## 🌐 Deployment

This app is ready for free deployment on **Streamlit Cloud**:

1. Upload files to GitHub
2. Go to: [https://share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Select `app.py`
5. Deploy 🚀

---

## 📂 Project Structure

```
ai4farm/
│── app.py
│── requirements.txt
│── README.md
```

---

## ✨ Author

Developed by **SOLARIS-bit**
For **MIT Solve 2025 Challenge**
Aivancity School of Technology, Business & Society

```

---
