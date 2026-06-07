import streamlit as st
import pandas as pd
import joblib

# setting up the page
st.set_page_config(page_title = "Salary Predictor", layout="centered")
st.title("Machine Learning Salary Predictor")
st.write("Enter your details below to estimate your annual salary: ")

# @st.cache_data ensures the CSV is only loaded once, keeping the app super fast
@st.cache_data

# load the dataset
def load_data():
    return pd.read_csv("cleaned_data.csv")

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data file not found!")
    st.stop()
 
 # load the model
try:
    model = joblib.load('salary_predictor_gradient_model.pkl')
except FileNotFoundError:
    st.error("Model File not found!")
    st.stop()

# building the user interface
st.subheader("Your Information")

job_title_options = sorted(df['Job Title'].dropna().unique())
education_options = sorted(df['Education Level'].dropna().unique())
gender_options = sorted(df['Gender'].dropna().unique())

# create input widgets
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", min_value = 18, max_value = 80, value = 35)
    years_experience = st.slider("Years of Experience", min_value = 0.0, max_value= 40.0, value = 5.0, step = 0.5)
    
with col2:
    gender = st.selectbox("Gender", gender_options)
    education = st.selectbox("Education Level", education_options)
    job_title = st.selectbox("Job Title", job_title_options)

# make the prediction
if st.button("Predict My Salary", type="secondary"):

    input_data = pd.DataFrame(
        {
        'Age': [age],
        'Gender': [gender],
        'Education Level': [education],
        'Job Title': [job_title],
        'Years of Experience': [years_experience]
        }
    )

    # generate the prediction
    try:
        prediction = model.predict(input_data)
        predicted_salary = prediction[0]

        # Show the main success message
        st.success(f"### Estimated Annual Salary: ${predicted_salary:,.2f}")
        
        # Calculate the historical average
        avg_job_salary = df[df['Job Title'] == job_title]['Salary'].mean()

        if pd.notna(avg_job_salary):
            st.markdown("---") 
            st.subheader("Comparison 📊")
            
            # Add a dynamic metric widget with an up/down arrow
            difference = predicted_salary - avg_job_salary
            st.metric(
                label=f"Average vs. Your Prediction as {job_title}", 
                value=f"${predicted_salary:,.0f}", 
                delta=f"${difference:,.0f}"
            )
            
            # Draw a comparative bar chart
            chart_data = pd.DataFrame(
                {"Salary ($)": [avg_job_salary, predicted_salary]}, 
                index=["Historical Average", "Your ML Prediction"]
            )
            st.bar_chart(chart_data, y_label="Annual Salary ($)", x_label="Average vs.Your Prediction")
            st.success("!Disclamer: The historical average and M-L prediction may vary vastly, as the historical average does not " \
            "depend on any external parameters(it takes the average of salaries based on the Job Title), but the Machine Learning Model predicts on the basis of many factors such as Age, Gender, Years of Experience," \
            " Job Title and Education Level. ")
        
    except Exception as e:
        st.error(f"Error making prediction: {e}")




    