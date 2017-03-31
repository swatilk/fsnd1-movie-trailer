import fresh_tomatoes
import media

# Sets data for movies (TV shows) list
toy_story = media.Movie(
    "Toy Story",
    "A story of  boy and his toys come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",    # noqa
    "https://www.youtube.com/watch?v=ZZv1vki4ou4")

avatar = media.Movie(
    "Avatar",
    "A marine in an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",    # noqa
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

hahk = media.Movie(
    "Hum Aapke Hain Koun",
    "A love story",
    "https://upload.wikimedia.org/wikipedia/fi/thumb/b/bf/HumAapkeHainKoun.jpg/250px-HumAapkeHainKoun.jpg",    # noqa
    "https://www.youtube.com/watch?v=45JY12a6zJA")

atla = media.Movie(
    "Avatar: The last airbender",
    "The story of the last airbender",    # noqa
    "https://upload.wikimedia.org/wikipedia/en/9/9b/Avatar-_The_Last_Airbender_Book_1_DVD.jpg",    # noqa
    "https://www.youtube.com/watch?v=nm-wiB60nHs")

godfather = media.Movie(
    "The Godfather",
    "Story of the man taking over his father's mafia empire",    # noqa
    "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/The_Godfather%2C_The_Game.jpg/250px-The_Godfather%2C_The_Game.jpg",    # noqa
    "https://www.youtube.com/watch?v=dNE2PvbesQU")

kirik = media.Movie(
    "Kirik Party",
    "Story about young college kids",
    "https://upload.wikimedia.org/wikipedia/en/1/1f/Kirik_Part_Poster.jpg",    # noqa
    "https://www.youtube.com/watch?v=IfvnbER_6sQ")

# Assigns all the movies (TV shows) to an array
movies = [toy_story, avatar, hahk, atla, godfather, kirik]

# Invokes method on fresh_tomatoes.py by passing in the 'movies' array
fresh_tomatoes.open_movies_page(movies)
