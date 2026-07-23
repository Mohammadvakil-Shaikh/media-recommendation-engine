import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(page_title="Hybrid Media Recommender", page_icon="🎬", layout="wide")

st.title("🎬 Intelligent Hybrid Media Recommendation Engine")
st.caption("Powered by Content-Based Filtering & Generative AI")

# ---------------------------------------------------------
# Load Expanded Dataset
# ---------------------------------------------------------
@st.cache_data
def load_data():
    media_data = [
        {"Title": "Perfect Blue", "Type": "Anime Movie", "Genre": "Psychological Thriller", "Rating": 8.0, "Description": "A pop singer turns actress and begins to lose her grip on reality as she is stalked by an obsessed fan."},
        {"Title": "The Dark Knight", "Type": "Movie", "Genre": "Action/Thriller", "Rating": 9.0, "Description": "Batman faces the Joker, a criminal mastermind who plunges Gotham City into anarchy."},
        {"Title": "Jujutsu Kaisen 0", "Type": "Anime Movie", "Genre": "Anime/Action", "Rating": 7.8, "Description": "Yuta Okkotsu gains control of a powerful cursed spirit and enrolls at Tokyo Jujutsu High."},
        {"Title": "Shutter Island", "Type": "Movie", "Genre": "Psychological Thriller", "Rating": 8.2, "Description": "A U.S. Marshal investigates the disappearance of a murderer who escaped from a hospital for the criminally insane."},
        {"Title": "Demon Slayer: Mugen Train", "Type": "Anime Movie", "Genre": "Anime/Action", "Rating": 8.2, "Description": "Tanjiro and the Demon Slayer Corps aboard the Mugen Train on a deadly mission."},
        {"Title": "Fight Club", "Type": "Movie", "Genre": "Psychological Thriller", "Rating": 8.8, "Description": "An insomniac office worker and a devil-may-care soap maker form an underground fight club."},
        {"Title": "Monster", "Type": "Anime Series", "Genre": "Psychological Thriller", "Rating": 8.7, "Description": "A brilliant brain surgeon gets involved with a former patient who is now a dangerous psychopath."},
        {"Title": "Inception", "Type": "Movie", "Genre": "Action/Sci-Fi", "Rating": 8.8, "Description": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea."}
    ]
    df = pd.DataFrame(media_data)
    df.index = range(1, len(df) + 1)
    return df

df = load_data()

# ---------------------------------------------------------
# Recommendation Logic (Content-Based)
# ---------------------------------------------------------
def get_recommendations(selected_title, data):
    target_row = data[data['Title'] == selected_title].iloc[0]
    target_genre = target_row['Genre']
    
    # Filter by same genre, excluding the selected title
    matches = data[(data['Genre'] == target_genre) & (data['Title'] != selected_title)]
    
    # Sort by rating descending
    matches = matches.sort_values(by='Rating', ascending=False)
    return target_row, matches

# ---------------------------------------------------------
# UI Layout (Tabs)
# ---------------------------------------------------------
tab1, tab2 = st.tabs(["📊 Database & Filter Engine", "🤖 AI Media Assistant"])

# ---------------------------------------------------------
# TAB 1: Database Recommender
# ---------------------------------------------------------
with tab1:
    st.subheader("Select a Movie or Anime to Find Similar Titles")
    
    selected_movie = st.selectbox("Choose a title from our database:", df['Title'].values)
    
    if st.button("Get Recommendations", type="primary"):
        selected_info, recs = get_recommendations(selected_movie, df)
        
        # Display Selected Item Details
        st.markdown(f"### Selected: **{selected_info['Title']}** ({selected_info['Type']})")
        st.info(f"**Genre:** {selected_info['Genre']} | **Rating:** ⭐ {selected_info['Rating']}\n\n_{selected_info['Description']}_")
        
        st.divider()
        st.subheader("Top Recommended Matches")
        
        if recs.empty:
            st.warning("No direct genre matches found in current local database.")
        else:
            cols = st.columns(len(recs))
            for idx, (_, row) in enumerate(recs.iterrows()):
                with cols[idx]:
                    st.success(f"**{row['Title']}**")
                    st.caption(f"{row['Type']} • ⭐ {row['Rating']}")
                    st.write(f"**Genre:** {row['Genre']}")
                    st.write(row['Description'])

    with st.expander("View Full Database Table"):
        st.dataframe(df, use_container_width=True)

# ---------------------------------------------------------
# TAB 2: AI Assistant Mode
# ---------------------------------------------------------
with tab2:
    st.subheader("Ask the AI Recommender Anything")
    st.write("Type complex, custom requests (e.g., *'Suggest psychological thrillers with mind-bending twists'*).")
    
    user_prompt = st.text_area("Your Request:", placeholder="E.g., I loved Shutter Island and Perfect Blue. Recommend 3 anime or movies with dark mystery atmosphere.")
    api_key_input = st.text_input("Gemini API Key (Optional for live AI calls):", type="password", help="Get a free key at aistudio.google.com")
    
    if st.button("Generate AI Recommendations"):
        if not user_prompt:
            st.warning("Please enter a prompt first.")
        elif not api_key_input:
            st.warning("Enter a free Gemini API key to enable live AI responses, or use Tab 1 for the database engine.")
        else:
            try:
                from google import genai
                client = genai.Client(api_key=api_key_input)
                
                with st.spinner("AI is analyzing cinematic patterns..."):
                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=f"You are an expert movie and anime recommendation assistant. Respond concisely to this user query with top recommendations, ratings, and brief reasons why: {user_prompt}"
                    )
                    st.markdown("### 🤖 AI Recommendations")
                    st.write(response.text)
            except Exception as e:
                st.error(f"Error connecting to AI service: {e}")