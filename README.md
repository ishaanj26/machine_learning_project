# Machine Learning Projects Repository

Welcome to my Machine Learning Projects repository! 🚀 This is a dedicated space where I will explore and implement various machine learning projects, starting from beginner-level concepts to more advanced applications. Each project will include code, explanations, and relevant datasets to help you follow along or use it for your learning journey.

---

## Repository Structure

```
├── MovieRecommendation/           # Movie Recommendation Project
```

## Current Projects

### 1. **Movie Recommendation System** 🎬
   **Objective:** Build a system that recommends movies to users based on their preferences.
   
   **Tech Stack:**
   - Language: Jupyter Notebook,Python
   - Libraries: Pandas, NumPy, sklearn, ast, nltk, pickle, streamlit

   **Approach:**
   - **Dataset:** The dataset was sourced from [TMDb](https://www.themoviedb.org/) for movie details and metadata.
   - **Data Cleaning:** Removed duplicates and missing values, extracted genres, keywords, cast, and crew using custom parsing functions.
   - **Feature Engineering:** Created a unified "tags" column by combining movie metadata and applied stemming to standardize terms.
   - **Model:** Used cosine similarity on vectorized movie features to recommend similar movies.
   - **Posters:** Integrated OMDb API for fetching movie posters and details.
   - **UI:** Developed an interactive interface with Streamlit for user-friendly recommendations.

---

## Future Projects
- Customer Churn Prediction
- Time Series Sales Forecasting
- Credit Card Fraud Detection
- Fake News Detection
- Sentiment Analysis
- Disease Detection
- Face Recognition using FaceNet

---

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/ishaanj26/machine_learning_project.git
   ```
2. Navigate to the project folder:
   ```bash
   cd machine-learning-projects
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Open the Jupyter notebook to explore the project:
   ```bash
   jupyter notebook notebooks/movie_recommender.ipynb
   ```

---

## Contributions
Feel free to fork this repository, suggest improvements, or add new features! 😊

---

## License
This project is licensed under the [MIT License](LICENSE).
