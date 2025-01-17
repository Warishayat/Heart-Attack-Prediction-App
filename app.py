import streamlit as st
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

import warnings 
warnings.filterwarnings("ignore")

with open('TreeModel.pkl', 'rb') as f:
    model = pickle.load(f)

def get_user_input():
    age = st.number_input('Age', min_value=1, max_value=100, value=50)
    gender = st.radio('Gender', options=['Male', 'Female'])
    gender = 1 if gender == 'Male' else 0
    impluse = st.number_input('Impluse', min_value=0, max_value=1000, value=50)
    pressurehight = st.number_input('Pressure High', min_value=0, max_value=250, value=120)
    pressurelow = st.number_input('Pressure Low', min_value=0, max_value=150, value=80)
    glucose = st.number_input('Glucose', min_value=0.0, max_value=500.0, value=100.0)
    kcm = st.number_input('KCM', min_value=0.0, max_value=300.0, value=10.0)
    troponin = st.number_input('Troponin', min_value=0.0, max_value=10.0, value=0.1)

    # Return the user input as a DataFrame
    user_input = pd.DataFrame([[age, gender, impluse, pressurehight, pressurelow, glucose, kcm, troponin]], 
                              columns=['age', 'gender', 'impluse', 'pressurehight', 'pressurelow', 'glucose', 'kcm', 'troponin'])
    return user_input

# Main function
def main():
    st.title("Heart Disease Predict App❤️🩺")
    st.markdown("""
    This is a simple web app to predict the likelihood of heart disease (positive or negative) based on inputs.
    """)
    
    # Input form section
    with st.expander('Enter your data'):
        user_input = get_user_input()

    # Submit button for making prediction
    if st.button('Submit'):
        # Display the user's input for confirmation
        st.subheader('User Input:')
        st.write(user_input)
        
        # Make predictions using the loaded model
        prediction = model.predict(user_input)
        
        # Display prediction result
        if prediction[0] == 1:
            st.success("Prediction: Positive (Heart Disease Likely)")
        else:
            st.markdown("<h3 style='color:red;'>Prediction: Negative (Heart Disease Unlikely)</h3>", unsafe_allow_html=True)
if __name__ == '__main__':
    main()
