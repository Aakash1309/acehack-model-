### 📊 Data Sources
The prediction model is trained using a hybrid dataset:
* **Public Health Data:** Scraped/sourced from official health department records.
* **Kaggle:** [Link to your specific Kaggle dataset]
* *Note: The raw .csv file was removed to stay within GitHub size limits.*

---

## 🚀 Deploying the Streamlit App
This project uses Streamlit for the web UI. Below are quick start instructions for running locally and deploying.

### ✅ Run locally
1. Create a Python environment (recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

### ☁️ Deploy to Streamlit Community Cloud
1. Push this repo to GitHub.
2. In Streamlit Community Cloud, click **New app** and connect your GitHub repo.
3. Set **Main file** to `app.py`.

### 📦 Deploy to Heroku (optional)
Heroku can run Streamlit apps using the included `Procfile`:
1. Create a Heroku app.
2. Push this repo to Heroku.
3. The app will start automatically.

---
