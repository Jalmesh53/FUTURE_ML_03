# 🤖 Customer Support Chatbot (Task 3)

## 📌 Project Overview

This project is the final task for the **Future Interns Machine Learning Internship**. The goal was to build a smart virtual assistant capable of handling customer queries automatically.

To demonstrate versatility, I implemented this solution using **two different approaches**:

1.  **The "Code-First" Approach:** A custom NLP model using Python & Scikit-learn.
2.  **The "No-Code" Approach:** A cloud-based agent using Google Dialogflow.

---

## 🔹 Approach 1: Python & Streamlit (Custom NLP)

This version uses **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Logistic Regression** to classify user intents and map them to responses.

### 🛠️ Tech Stack

- **Python**: Core logic.
- **NLTK**: Text preprocessing and tokenization.
- **Scikit-learn**: Vectorization and Intent Classification model.
- **Streamlit**: Interactive web-based chat interface.

### 🚀 Key Features

- **Intent Recognition:** Detects if a user is asking about "Orders", "Returns", or "Contact".
- **Instant Responses:** Delivers predefined answers instantly based on the trained model.
- **Chat UI:** A clean, user-friendly interface running on Localhost.

### 📂 How to Run

1.  Navigate to the Python folder:
    ```bash
    cd Python_Version
    ```
2.  Install dependencies:
    ```bash
    pip install streamlit nltk scikit-learn
    ```
3.  Run the application:
    ```bash
    streamlit run chatbot.py --browser.gatherUsageStats false
    ```

---

## 🔹 Approach 2: Google Dialogflow (Cloud Agent)

This version leverages **Google's NLU (Natural Language Understanding)** engine to handle conversations via a cloud interface.

### 🛠️ Setup Details

- **Platform:** Google Cloud Dialogflow ES.
- **Intents Created:** Order Status, Return Policy, Greetings.
- **Integration:** Web Demo.

### 📸 Preview

_(Screenshots of the Dialogflow test console are included in the `Dialogflow_Version` folder)._

---

## 📂 Project Structure

```text
FUTURE_ML_03/
├── Python_Version/
│   ├── chatbot.py        # The main Python application
│   ├── intents.json      # The dataset (Patterns & Responses)
├── Dialogflow_Version/
│   ├── dialogflow_screenshot.png  # Proof of cloud implementation
├── README.md             # Project documentation
```
