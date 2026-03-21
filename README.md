# Potato Disease Detection Application

## Project Overview
This project is designed to detect diseases in potato crops using advanced machine learning techniques and technologies, including TensorFlow and FastAPI. The application aims to help farmers identify diseases early to prevent crop loss and improve yield.

## Features
- User-friendly web interface using Streamlit.
- Disease detection using a trained model based on TensorFlow.
- RESTful API built with FastAPI for seamless integration with other applications.
- Interactive data visualizations using Jupyter notebooks.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Rubal-code/potato-disease.git
   cd potato-disease
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Guide
1. To run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. To access the FastAPI endpoints, run:
   ```bash
   uvicorn main:app --reload
   ```
3. For Jupyter notebooks, run:
   ```bash
   jupyter notebook
   ```

## Project Structure
```
potato-disease/
├── app.py             # Streamlit application
├── main.py            # FastAPI application
├── models/            # Contains trained machine learning models
│   └── model.h5      # Example model file
├── notebooks/         # Jupyter notebooks for exploration and visualization
└── requirements.txt   # Dependencies
```

## Model Details
The primary model used for disease detection is built using TensorFlow. It is trained on a dataset of potato images labeled with various diseases. The architecture and hyperparameters of the model are defined in `model.py`.

## API Documentation
- **GET /predict**: To obtain disease prediction for an input image.
- **POST /upload**: To upload an image for prediction.

## Contributing Guidelines
Contributions are welcome! Please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix:
  ```bash
  git checkout -b feature/new-feature
  ```
- Commit your changes:
  ```bash
  git commit -m 'Add new feature'
  ```
- Push to the branch:
  ```bash
  git push origin feature/new-feature
  ```
- Open a Pull Request.

Thank you for your interest in contributing to the Potato Disease Detection project!