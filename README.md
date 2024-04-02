# Sentiment Analysis App

This is a simple web application built using Streamlit for sentiment analysis. The app utilizes the Cardiff University Twitter RoBERTa model for sentiment analysis. It allows users to input text and provides sentiment analysis results categorized into negative, neutral, and positive sentiments.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Credits](#credits)

## Introduction

Sentiment analysis is a natural language processing (NLP) technique used to determine the sentiment expressed in a piece of text. It is widely applied in various fields such as social media monitoring, customer feedback analysis, and market research. This application provides a user-friendly interface for conducting sentiment analysis using state-of-the-art NLP models.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/kevin-291/sentiment-analysis.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sentiment-analysis
    ```

3. Install the required dependencies listed in `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5. Access the app in your web browser by following the URL provided in the terminal.

6. Enter the text you want to analyze in the provided text area.

7. Click on the "Analyse" button to get sentiment analysis results.

## Installation

If you prefer to install the application without cloning the repository, you can create a new Python virtual environment and install the required dependencies manually.

1. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3. Install the required dependencies:

    ```bash
    pip install streamlit transformers scipy
    ```

4. Download the source code from the repository or create your own Python script containing the sentiment analysis logic.

5. Run the Streamlit app using the command:

    ```bash
    streamlit run app.py
    ```

## Dependencies

The application relies on the following Python libraries:

- `streamlit`: A Python framework for building interactive web applications.
- `transformers`: A library provided by Hugging Face for working with pre-trained NLP models.
- `scipy`: A library for scientific computing in Python.

For detailed information about the versions, refer to the `requirements.txt` file.

## Cardiff University Twitter RoBERTa Model

The Cardiff University Twitter RoBERTa model is a pre-trained NLP model fine-tuned specifically for sentiment analysis tasks on Twitter data. It is based on the RoBERTa architecture, which is a variant of the BERT model developed by Facebook AI and the University of Washington.

## Credits

- The sentiment analysis model is based on the Cardiff University Twitter RoBERTa model.
- The sentiment analysis model is loaded using the Hugging Face `transformers` library.
- The application interface is built using Streamlit.

