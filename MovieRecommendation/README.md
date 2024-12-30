# reCommando - Movie Recommendation Program

reCommando is a movie recommendation system designed to help users discover movies based on their preferences. Using various recommendation algorithms, it suggests movies that are most likely to match the user's taste, making the process of finding a great movie easy and efficient.

## Features

- **Personalized Movie Recommendations**: Provides recommendations based on the user's movie preference
- **User-Friendly Interface**: Simple, easy-to-use interface for inputting preferences and receiving suggestions.
- **Content-based Filtering**: Uses content-based filtering for accurate recommendations.

## Tech Stack:
- Language: Jupyter Notebook,Python
- Libraries: Pandas, NumPy, sklearn, ast, nltk, pickle, streamlit

## Approach:
- **Dataset:** The dataset was sourced from [TMDb](https://www.themoviedb.org/) for movie details and metadata.
- **Data Cleaning:** Removed duplicates and missing values, extracted genres, keywords, cast, and crew using custom parsing functions.
- **Feature Engineering:** Created a unified "tags" column by combining movie metadata and applied stemming to standardize terms.
- **Model:** Used cosine similarity on vectorized movie features to recommend similar movies.
- **Posters:** Integrated OMDb API for fetching movie posters and details.
- **UI:** Developed an interactive interface with Streamlit for user-friendly recommendations.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ishaanj26/machine_learning_project.git
2. Navigate to the project folder:
   ```bash
   cd MovieRecommendation
3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the program:
   ```bash
   streamlit run reCommander.py

Usage
Start the program by executing the script.
Input your preferences, such as preferred movie.
Get a list of movie recommendations tailored to your tastes.
Example:
   ```bash
   Enter your preferred movie: Tangled.
reCommando suggests the following movies:
1. Out of Inferno
2. The Princess and the Frog
3. Home on the Range
4. Animals United
5. Toy Story 3
   
## Contributions
Feel free to fork this repository, suggest improvements, or add new features! 😊

---

## License
This project is licensed under the [MIT License](LICENSE).
