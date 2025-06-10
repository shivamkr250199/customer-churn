# 🔮 Telco Customer Churn Prediction

A machine learning web application to predict whether a telecom customer is likely to churn, built using Flask, trained on SMOTE-balanced data using a fine-tuned Random Forest Classifier.

---

## 🚀 Live Demo

🌐 [Deployed on Render](#) *(replace with your actual Render URL)*

---

## 📌 Project Features

- 📊 Exploratory Data Analysis (EDA) & Visualizations
- 🧪 SMOTE for handling class imbalance
- ⚙️ Hyperparameter tuning using GridSearchCV
- ✅ Model evaluation with Accuracy, Confusion Matrix, Classification Report
- 🌐 Flask-based web application with clean, colorful UI
- 🧠 Supports LightGBM and XGBoost as alternative models
- 💾 Model and encoders saved using Pickle for reuse
- 📦 Deployable on Render with `requirements.txt`

---

## 🧠 ML Workflow Summary

- **Model:** RandomForestClassifier (Tuned with GridSearchCV)
- **Vectorization:** LabelEncoding for categorical features
- **Imbalance Handling:** SMOTE
- **Best Accuracy:** Achieved using cross-validation on balanced data

---

## 📁 Folder Structure

TelcoChurnPredictor/
├── app.py
├── best_random_forest_model.pkl
├── encoders.pkl
├── requirements.txt
├── templates/
│ ├── index.html
│ └── result.html
├── static/
│ └── style.css
└── README.md




## 🛠️ Installation & Running Locally

### 1. Clone the repository


git clone https://github.com/shivamk250199/customer-churn-.git
cd customer-churn

2. Create and activate virtual environment
Windows:
bash

python -m venv venv
venv\Scripts\activate
macOS/Linux:
bash

python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash


pip install -r requirements.txt

4. Run the Flask app
bash

python app.py
Visit http://127.0.0.1:5000 in your browser.

🌐 Deployment on Render
🔧 Steps:
Push your code to a GitHub repository.

Go to https://render.com.

Click "New Web Service" → Connect your GitHub repo.

Set the Build Command:



pip install -r requirements.txt
Set the Start Command:


python app.py
Set Python version (if needed) in render.yaml or use .python-version.

📷 UI Preview

🧾 License
This project is licensed under the MIT License. Feel free to use and modify.

🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

✨ Author
Shivam Kumar

📧 emsail: shivamshandaliya1998@gmail.com

📍 India
