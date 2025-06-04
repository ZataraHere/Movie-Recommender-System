# 🎬 Movie Recommender System

This is a content-based movie recommendation web application built using **Streamlit**. Given a selected movie, it suggests 5 similar movies along with their posters using cosine similarity of movie features.

---

## 🚀 Features

- Suggests 5 similar movies based on your selection
- Displays movie posters using TMDb API
- Lightweight and deployable on platforms like Render
- Loads model files (`.pkl`) dynamically from Google Drive

---

## 🧠 How it Works

1. Movie metadata and similarity matrix are precomputed and stored in `.pkl` files.
2. The user selects a movie from the dropdown.
3. Cosine similarity is used to find the top 5 similar movies.
4. Movie posters are fetched via the **TMDb API** using the movie ID.

---

## 🧰 Tech Stack

- Python 3.11
- Streamlit
- Pandas, Pickle, Requests
- TMDb API
- Google Drive (`gdown`)

---

## 🛠 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/ZataraHere/Movie-Recommender-System.git
cd Movie-Recommender-System

### 2. Install Dependencies
'''bash


