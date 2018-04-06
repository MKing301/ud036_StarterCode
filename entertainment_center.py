import fresh_tomatoes
import media
'''
fresh_tomatoes.py is a Udacity provided Python module
that contains a function called open_movies_page
that takes in one argument, which is a list of movies
and creates an HTML file which visualize the list
of movies

media is a python module that contains the movie class, which the constructor
for the movie class is written

'''

# courageous is an instance of the Movie class in the Media module for the
# movie Courageous
courageous = media.Movie("Courageous",
                         '''When a tragedy strikes close to home, four police
                         officers struggle with their faith and their roles as
                         husbands and fathers; together they make a decision
                         that will change all of their lives.''',
                         "https://upload.wikimedia.org/wikipedia/en/thumb/3/"
                         "3b/Courageous_Cover.JPG/220px-Courageous_Cover.JPG",
                         "https://www.youtube.com/watch?v=rLYmku9OJ6A",
                         "Released - Aug 26, 2011")

# do_you_believe is an instance of the Movie class in the Media module for the
# movie Do You Believe
do_you_believe = media.Movie("Do You Believe?",
                             '''When a pastor is shaken by the visible faith of
                             a street corner preacher, he is reminded that true
                             belief always requires action. His response
                             ignites a journey that impacts everyone it touches
                             in ways that only God could orchestrate.''',
                             "https://images-na.ssl-images-amazon.com/images/"
                             "M/MV5BMjE5MzAxMjUyMl5BMl5BanBnXkFtZTgwNDk1OTMwN"
                             "DE@._V1_SY1000_CR0,0,772,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=9kBcmuGuS7M",
                             "Released - Mar 20, 2015")

# fireproof is an instance of the Movie class in the Media module for the
# movie Firerproof
fireproof = media.Movie("Fireproof",
                        ''' In an attempt to save his marriage, a firefighter
                        uses a 40-day experiment known as "The Love Dare".''',
                        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b7/"
                        "Fireproof_poster.jpg/220px-Fireproof_poster.jpg",
                        "https://www.youtube.com/watch?v=YK5-5qf9IQs",
                        "Released - Sep 26, 2008")

# gods_not_dead is an instance of the Movie class in the Media module for the
# movie God's Not Dead
gods_not_dead = media.Movie("God's Not Dead",
                            '''College philosophy professor Mr. Radisson's
                            curriculum is challenged by his new student, Josh,
                            who believes God exists.''',
                            "http://www.impawards.com/2014/posters/"
                            "gods_not_dead.jpg",
                            "https://www.youtube.com/watch?v=bMjo5f9eiX8",
                            "Released - Apr 11, 2014")

# risen is an instance of the Movie class in the Media module for the
# movie Risen
risen = media.Movie("Risen",
                    '''Witness one of the most important events in human
                    history through the eyes of a nonbeliever.
                    Risen is a depiction of events surrounding Christ's
                    missing body after his crucifixion.''',
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcTlr6azlxH"
                    "_XC22SFc-9rt16xOcBtzt17WiiHZOJQAZLg_2ZIxE",
                    "https://www.youtube.com/watch?v=OcTVLfn5i8g",
                    "Released - Feb 19, 2016")

# war_room is an instance of the Movie class in the Media module for the
# movie War Room
war_room = media.Movie("War Room",
                       '''A seemingly perfect family looks to fix their
                       problems with the help of Miss Clara, an older,
                       wiser woman.''',
                       "https://images-na.ssl-images-amazon.com/images/"
                       "M/MV5BMTYyNTUxMjQwNF5BMl5BanBnXkFtZTgwNDY5MDIwNTE"
                       "@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=2DbRwcrhiLA",
                       "Released - Nov 27, 2015")

# movies is a list of my favorite movies; each an instance of the Movie class
movies = [courageous, do_you_believe, fireproof, gods_not_dead, risen,
          war_room]


fresh_tomatoes.open_movies_page(movies)
'''
open_movies_page function contained in the fresh_tomatoes module takes in one
argument, which is a list of movies and creates an HTML file which visualize
the list of movies

Input(s):
movies - list of movies created for the library

'''
