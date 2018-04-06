import webbrowser
''' webbrowser module used for displaying web-based content to users'''


class Movie():
    '''This class provides a way to store movie related information.

       It contains a list of movie ratings stored in a class variable called
       VALID_RATINGS.

       It contains 2 methods:

       __init__ - the constructor for the move class
       show_trailer - which is used to play a movie trailer

    '''

    # Movie class list variable listing the movie ratings
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, release_date):
        '''This is the constructor for the Movie class which will allow
           instances of movies to be created.

           Input(s):
           self - represents the instance of the class
           movie_title - the title of the movie
           movie_storline - the plot of the story
           poster_image - image of the poster for the movie
           trailer_youtube - the YouTube link for the movie trailer
           release_date - the release date of the movie

        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date

    def show_trailer(self):
        '''This function utilizes the webbrowswer.open function

           Inputs(s):
           self - represents the instance of the class

        '''
        webbrowser.open(self.trailer_youtube_url)
        '''webbrowser.open function displays url using the default browser

           Input(s):
           self.trailer_youtube_url - the movie instance YouTube link for the
           movie trailer

        '''
