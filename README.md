# 🎬 Movie Recommender System

This is a content-based movie recommendation web application built using **Streamlit**. Given a selected movie, it suggests 5 similar movies along with their posters using cosine similarity of movie features.

![Preview](https://github.com/ZataraHere/Movie-Recommender-System/blob/accab9cc78649261b7188055d052a8c6b417dbf9/Screenshot-.PNG)
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
```
git clone https://github.com/ZataraHere/Movie-Recommender-System.git
cd Movie-Recommender-System
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Set TMDb API Key
Create an environment variable or store it securely in your deployment environment:

**For local dev:**
```
export TMDB_API_KEY=your_tmdb_api_key
```
**For Render or other platforms:**
```
Add TMDB_API_KEY as a secret environment variable.
```
✅ You can obtain a free TMDb API key by signing up at https://www.themoviedb.org.

### 4. Run the App
```
streamlit run app.py
```

## 📦 Model Files
The following .pkl files are large and excluded from GitHub:

`movie_dict.pkl`

`similarity.pkl`

These are automatically downloaded from Google Drive on first run using the `gdown` library.

## 🔐 Environment Variables
 | Variable	     | Description        |
 |---------------|--------------------|
| `TMDB_API_KEY`	 |  `Your TMDb API Key` |

## 🧪 Example
Select: `Inception`

**Recommendations:**

The Prestige

Interstellar

The Matrix

Shutter Island

Memento




