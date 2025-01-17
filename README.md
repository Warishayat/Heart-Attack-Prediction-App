
# Heart Attack Prediction App

This is a machine learning-powered web application for predicting the likelihood of heart disease based on user-provided medical data. The app uses a pre-trained **Decision Tree Classifier** model to predict whether a user is likely to have heart disease based on features like age, gender, blood pressure, glucose levels, and more.

## Demo

You can interact with the app directly on Hugging Face Spaces:  
[Heart Attack Prediction App](https://huggingface.co/spaces/Waris01/Heart-Attack-Prediction-App)

## Features

- **Age**: User can input their age (1–100).
- **Gender**: Select gender (Male/Female).
- **Medical Data**: Input values for blood pressure, glucose levels, heart rate, troponin, and more.
- **Prediction**: Predicts whether the user is likely to have a heart disease based on the entered data.

## How to Use

1. **Open the app**: Click on the demo link above to open the Heart Disease Prediction app.
2. **Enter the details**:
    - Provide values for parameters like age, gender, impulse, blood pressure, glucose, etc.
3. **Click "Submit"**: Once all data is entered, click the "Submit" button to receive the prediction result.
4. **View the result**: The app will show whether the user is likely to have heart disease or not based on the input data.

## Model Details

This application uses a **Decision Tree Classifier** model trained to predict the likelihood of heart disease based on a dataset containing features like:
- **Age**
- **Gender**
- **Blood Pressure**
- **Glucose Levels**
- **Heart Rate**
- **Troponin Levels**

The model has been serialized using **pickle** and is loaded in the app to make predictions.

## Installation (if you want to run the app locally)

### Prerequisites

- **Python 3.x**
- **Streamlit**
- **scikit-learn**
- **pandas**
- **pickle**

### Clone the repository

```bash
(https://github.com/Warishayat/Heart-Attack-Prediction-App)
cd heart-disease-predict
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app locally

```bash
streamlit run app.py
```

## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push your changes (`git push origin feature-branch`).
6. Create a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to Hugging Face for providing a platform to deploy the app.
- Libraries used: Streamlit, scikit-learn, pandas, and pickle.
- Data used for training the model is publicly available.

---

### Customization:
1. **Space URL**: Replace the demo URL with the actual URL for your Hugging Face Space.
2. **GitHub Repository**: If you have the source code hosted on GitHub, link to it in the appropriate sections (e.g., `(https://github.com/Warishayat/Heart-Attack-Prediction-App)`).
3. **Model Description**: Feel free to provide more details about the dataset or how the model was trained.

With this, users visiting your Hugging Face Space will have a clear understanding of your app, its features, and how to use it!
