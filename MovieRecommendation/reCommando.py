import streamlit as st
import pickle
import requests

new_df=pickle.load(open('movies.pkl','rb'))
# new_df=new_df['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_title):
    apiKey='e99f6b48'
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={apiKey}"
    response = requests.get(url)
    data=response.json()
    return data['Poster']
   

def recommend(selected_movie):
        movie_index = new_df[new_df['title'] == selected_movie].index[0]
        distances=similarity[movie_index]
        movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x :x[1])[1:6]
       
        recommended_movies=[]
        recommended_movies_posters=[]
        for i in movies_list:
            recommended_movies.append(new_df.iloc[i[0]].title)
            # fetch poster
            recommended_movies_posters.append(fetch_poster(new_df.iloc[i[0]].title))
        return recommended_movies,recommended_movies_posters

def display_movie_info(movie_data):
    st.title(movie_data['Title'])
    st.image(movie_data['Poster'])
    st.write(f"**Year:** {movie_data['Year']}")
    st.write(f"**Genre:** {movie_data['Genre']}")
    st.write(f"**Director:** {movie_data['Director']}")
    st.write(f"**Plot:** {movie_data['Plot']}")
    st.write(f"**Rating:** {movie_data['imdbRating']}")

# Create a styled title box
st.markdown("""
    <div style='text-align: center; display: flex; align-items: center; justify-content: left; margin-bottom: 0px;'>
        <span style='font-family: Arial, sans-serif; font-size: 36px; color: #003366; font-weight: bold';>re</span>
        <span style='font-family: Arial, sans-serif; font-size: 36px; color: #0099CC; font-weight: bold;'>Commando.</span>
    </div>
""", unsafe_allow_html=True)

# Create a title box
st.title("Movie Recommendation System")

# Create a select box
selected_option = st.selectbox("Choose an option:", new_df['title'])

# Display the selected option
st.write("You selected:", selected_option)

if st.button('Recommend'):
    # Logic to recommend a movie can be added here
    st.write(f"Recommendations based on {selected_option} are as following :")
    with st.spinner('Fetching...'):
        name,posters=recommend(selected_option)
    st.success("Recommendations fetched successfully!")
    cols = st.columns(5)  # Create 5 columns for the grid
    for i in range(5):
        with cols[i]:
            st.markdown(f"""
                <div style='text-align: center;'>
                    <div style='text-overflow: ellipsis; overflow: hidden; white-space: nowrap; width: 100%;'>{name[i]}</div>
                    <img src='{posters[i]}' style='width: 150px;'>
                </div>
            """, unsafe_allow_html=True)

        