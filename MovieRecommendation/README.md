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
   git clone https://github.com/yourusername/reCommando.git
2. Navigate to the project folder:
   ```bash
   cd reCommando
3. Install the necessary dependencies:
```bash
   pip install -r requirements.txt
4. Run the program:
```bash
streamlit run reCommander.py

Usage
Start the program by executing the script.
Input your preferences, such as preferred genres, actors, or ratings.
Get a list of movie recommendations tailored to your tastes.
Example
bash
Copy code
Enter your preferred genre: Action
Enter your preferred rating (1-10): 8
reCommando suggests the following movies:
1. Movie Title 1
2. Movie Title 2
3. Movie Title 3
   
## Contributions
Feel free to fork this repository, suggest improvements, or add new features! 😊

---

## License
This project is licensed under the [MIT License](LICENSE).
