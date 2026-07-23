# 🎬 Intelligent Media Recommendation Engine (Hybrid Architecture)

An interactive, full-stack data application designed to help users discover cinematic content (movies and anime) through both traditional algorithmic filtering and generative AI capabilities.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

---

## 📌 Features

### 📊 1. Algorithmic Database Recommender (Tab 1)
* **Structured Content Filtering:** Evaluates dataset attributes (Genre, Ratings, Type) to surface mathematically relevant matches.
* **Interactive UI Cards:** Displays selected items and recommended matches using custom UI cards featuring star ratings, badges, and descriptions.
* **Index-Optimized View:** Custom data indexing designed for seamless data exploration and tabular previews.

### 🤖 2. Generative AI Assistant (Tab 2)
* **Natural Language Queries:** Allows users to ask open-ended subjective requests (e.g., *"Recommend 3 psychological thrillers with mind-bending twists like Perfect Blue"*).
* **Live LLM Integration:** Powered by Google's `gemini-3.6-flash` model using the official `google-genai` SDK.
* **Secure API Interface:** Implements client-side API key handling for secure, quota-safe usage.

---

## 🛠️ Tech Stack & Tools

* **Frontend / Dashboard Framework:** Streamlit
* **Data Processing & Analytics:** Pandas
* **AI Model & API:** Google Gemini API (`gemini-3.6-flash`)
* **Environment / Language:** Python 3.x

---

## 🚀 Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Mohammadvakil-Shaikh/media-recommendation-engine.git](https://github.com/Mohammadvakil-Shaikh/media-recommendation-engine.git)
   cd media-recommendation-engine
