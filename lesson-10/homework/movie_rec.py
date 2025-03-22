import requests
import random
import textwrap

# TMDb API Key (Replace with your actual API key)
API_KEY = "cf34ad56adcbf38b790a47907c2f9ba7"

# TMDb Genre Mapping
GENRE_MAP = {
    "action": 28, "adventure": 12, "animation": 16, "comedy": 35,
    "crime": 80, "drama": 18, "fantasy": 14, "horror": 27,
    "mystery": 9648, "romance": 10749, "sci-fi": 878, "thriller": 53
}
# Reverse mapping for displaying genre names
REVERSE_MAP = {v: k.capitalize() for k, v in GENRE_MAP.items()}


def get_random_movie(genre_name=None):
    """
    Fetches a random movie from TMDb, optionally filtered by genre.

    Parameters:
        genre_name (str): The name of the genre to filter by (e.g., "comedy", "sci-fi").
                          If None or invalid, returns movies from all genres.

    Returns:
        None (prints movie details)
    """
    BASE_URL = "https://api.themoviedb.org/3/discover/movie"  # Correct endpoint

    # Convert genre name to ID if provided
    genre_id = GENRE_MAP.get(genre_name.lower()) if genre_name else None

    # Define parameters
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "page": random.randint(1, 10),  # Get movies from a random page
        "with_genres": genre_id if genre_id else "",  # Apply genre filter if valid
    }

    # Send request to TMDb API
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        movies = data["results"]

        if movies:
            movie = random.choice(movies)  # Pick a random movie
            title = movie["title"]
            overview = textwrap.fill(movie["overview"], 100)  # Wrap text to 100 chars
            release_date = movie["release_date"]
            movie_genres = [REVERSE_MAP[g] for g in movie["genre_ids"] if g in REVERSE_MAP]

            # Display movie details
            print(f"\n🎬 **{title}** ({release_date})")
            print(f"📖 {overview}")
            print(f"🎭 Genres: {', '.join(movie_genres) if movie_genres else 'Unknown'}\n")
        else:
            print(f"No movies found for genre '{genre_name}'!")
    else:
        print("API error or invalid API key!")


# Run the script
if __name__ == "__main__":
    user_input = input("Enter a genre (leave blank to skip): ").strip()
    get_random_movie(user_input if user_input else None)
