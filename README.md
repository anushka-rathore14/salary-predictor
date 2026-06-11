<div align="center">

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=35&pause=1000&color=00D9FF&center=true&vCenter=true&multiline=true&width=900&height=100&lines=%F0%9F%92%B0+Tech+Salary+Prediction;End-to-End+Machine+Learning+Dashboard" alt="Typing SVG" /></a>

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:00d9ff&height=200&section=header&text=Salary%20Predictor&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Interactive%20Data%20Science%20Dashboard%20%7C%20Live%20on%20Streamlit&descSize=18&descAlignY=55&descColor=58a6ff" width="100%"/>

<br/>


![GitHub last commit](https://img.shields.io/github/last-commit/anushka-rathore14/salary-predictor?style=for-the-badge&color=00d9ff&labelColor=0d1117)
![GitHub repo size](https://img.shields.io/github/repo-size/anushka-rathore14/salary-predictor?style=for-the-badge&color=7c3aed&labelColor=0d1117)
[![GitHub stars](https://img.shields.io/github/stars/anushka-rathore14/salary-predictor?style=for-the-badge&color=36BCF7)](https://github.com/anushka-rathore14/salary-predictor/stargazers)
[![Open in Streamlit](https://img.shields.io/badge/Open%20in-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://salary-predictor-eq9ftpswnpwyarfnn2xeex.streamlit.app/)
</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🧠 About This Project

> *A complete, end-to-end Machine Learning pipeline predicting tech compensation — deployed as an interactive web dashboard using Streamlit.*

This project demonstrates a full-stack data science lifecycle. It takes raw, messy compensation data, processes it through a robust engineering pipeline, trains a predictive regression model, and serves the results dynamically through a live Streamlit UI.

<div align="center">

| 🎯 Goal | 📊 Dataset | 🏆 Model | 📈 Accuracy (R²) |
|:--------|:-----------|:------------------|:-----------------|
| Predict Salary | 6704 listings × 6 features | Gradient Boosting Regressor | **89.56%** |

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

### 🔎 Why This Project Matters (Recruiter View)

This project demonstrates my ability to:

-Clean, preprocess, and manipulate raw datasets using Python and Pandas, including complex string replacements and data type conversions.

-Design and implement machine learning models for predictive analysis and numerical forecasting.

-Perform targeted feature engineering to extract meaningful variables and optimize model accuracy.

-Develop robust, modular backend code to support data ingestion pipelines and mathematical computations.

-Analyze and transform complex structured data into actionable quantitative insights.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🗺️ System Architecture

The application follows a structured, production-aligned approach. The model training pipeline is decoupled from the user interface, communicating via a serialized `.pkl` file.



    Raw CSV Data --> Data Cleaning via Pandas --> Scikit-Learn Model Training --> Streamlit Dashboard Integration --> End User Interface

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 📈 Results and Evaluation

The model was evaluated using standard regression metrics to ensure reliable and consistent salary estimates. Performance on the testing holdout set yielded the following results:

* **R² Score:** [0.89] — Indicates the model explains a high variance in salary data.
* **Mean Absolute Error (MAE):** [$11,550] — The average absolute difference between the predicted and actual salaries.
* **Root Mean Squared Error (RMSE):** [$15,602] — Penalizes larger prediction errors to ensure outlier robustness.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 💻 Tech Stack and Tools

<div align="center">

<p>
  <img src="https://skillicons.dev/icons?i=python,vscode,git,github&theme=dark" height="50"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white" />
</p>

<p>
  <img src="https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=google-colab&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />

</p>

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🚀 Getting Started

### 🌐 The Cloud Way (Recommended)
You do not need to install anything to interact with the model.
👉 <a href="https://salary-predictor-eq9ftpswnpwyarfnn2xeex.streamlit.app/" target="_blank" rel="noopener noreferrer">Salary Predictor</a>

```
### ▶️ Run Locally

```bash
# 1. Clone the repository
git clone [https://github.com/anushka-rathore14/salary-predictor.git](https://github.com/anushka-rathore14/salary-predictor.git)
   cd salary-predictor

# 2. Install the required dependencies:
pip install -r requirements.txt

# 3. Run the dashboard locally:
streamlit run app.py
```

### ☁️ Run on Google Colab
1. Upload `Salary_Prediction_Projecr.ipynb` and `Salary_Data.csv` to Google Colab.
2. Run all cells — no additional setup is required.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 📊 Dataset Overview

The dataset consists of **6,704** used salary listings from Salary_Data dataset.  The dataset used in this project was provided as part of the Complete Data Science and Machine Learning 
course on GeeksForGeeks, taught by <a href="https://github.com/JayanGupta" target="_blank" rel="noopener noreferrer">Mr. Jayan Gupta</a>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

**Key Features Include:**
- **Categorical**: `Gender`, `Education Level`, `Job Title`
- **Numerical**: `Age`, `Years of Experience`

*(Note: High cardinality features like `Salary` were dropped during the feature selection phase to mitigate the curse of dimensionality and prevent overfitting.)*

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🤝 Contributing & Support

Contributions, issues, and feature requests are welcome! 

1. 🍴 Fork the Project
2. 🌿 Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your Changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to the Branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

**If you found this project helpful for learning Machine Learning, please give it a ⭐!**

<div align="center">

<!-- Animated Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:00d9ff&height=120&section=footer" width="100%"/>

<br/>

<b>Made with ❤️ by <a href="https://github.com/anushka-rathore14">Anushka Rathore</a></b>

<br/><br/>

<img src="https://forthebadge.com/images/badges/built-with-love.svg" />
<img src="https://forthebadge.com/images/badges/made-with-python.svg" />
<img src="https://forthebadge.com/images/badges/open-source.svg" />

</div>


