import streamlit as st
from recommender import recommend_movies

st.title("🎬 IMDb Movie Recommendation System (2024)")
st.write("Enter a movie storyline and get top 5 similar movies:")

user_input = st.text_area("✍️ Enter a storyline here:")

if st.button("Recommend"):
    if user_input.strip() != "":
        results = recommend_movies(user_input, top_n=5)

        if not results.empty:
            st.subheader("Top 5 Recommended Movies:")
            for i, row in results.iterrows():
                st.markdown(f"**{row['Movie Name']}**")
                st.write(row['Storyline'])
                #st.write(f"**{row['Storyline'].upper()}**")
                st.markdown("---")
        else:
            st.warning("No similar movies found.")
    else:
        st.warning("Please enter a storyline first.")