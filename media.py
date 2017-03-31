import webbrowser


# Creates a class to store all info of a movie (TV show)
class Movie:
    # Sets the data for each instance of the class by invoking 'init' method
    def __init__(
            self, movie_title, movie_storyline,
            poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Opens the trailer of the movie \
    # when its poster is clicked

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
