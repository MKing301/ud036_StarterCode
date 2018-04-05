import webbrowser


class Movie():
    '''This class provides a way to store movie related information'''

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # Movie class variable

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, release_date):
        '''This method initialize the Movie class '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date

    def show_trailer(self):
        '''This function opens a web browser and plays the
        selected movie's trailer'''
        webbrowser.open(self.trailer_youtube_url)