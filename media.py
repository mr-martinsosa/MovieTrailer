import webbrowser

class Movie():
#store movie titles, box art, storyline, movie trailer URLs, director and year

    def __init__(self, title, poster_image, storyline,
                 trailer_youtube_url, movie_director, year): #initialize the object with the info
        self.title = title
        self.poster_image_url = poster_image
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.movie_director = movie_director
        self.year = year

    def show_trailer(self): #pop out a trailer for the movie
        webbrowser.open(self.trailer_youtube_url)