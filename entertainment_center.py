import fresh_tomatoes
import media

#create the movies
toy_story = media.Movie("Toy Story",
                        "http://dvdmedia.ign.com/dvd/image/object/143/14332015/toy-story_dvd-box-art.jpg",
                        "A story of a boy and his toys that come to life",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc", "John Lasseter", 1995)

scott_pilgrim = media.Movie("Scott Pilgrim vs. The World",
                            "http://i.jeded.com/i/scott-pilgrim-vs-the-world.32473.jpg",
                            "Scott Pilgrim must defeat his new girlfriend's seven evil exes"
                            " in order to win her heart.",
                            "https://www.youtube.com/watch?v=8NUBVcit5VM", "Edgar Wright", 2010)

ferris_bueller = media.Movie("Ferris Bueller's Day Off",
                             "http://ecx.images-amazon.com/images/I/51C3C9AW28L._SY300_.jpg",
                             "A high school wise guy is determined to have a day off from school, "
                             "despite what the principal thinks of that.",
                             "https://www.youtube.com/watch?v=R-P6p86px6U", "John Hughes", 1986)

shaun_dead = media.Movie("Shaun of the Dead",
                         "https://upload.wikimedia.org/wikipedia/en/e/ec/Shaun-of-the-dead.jpg",
                         "A man decides to turn his moribund life around by winning back his ex-girlfriend"
                         ", reconciling his relationship with his mother, "
                         "and dealing with an entire community that has returned "
                         "from the dead to eat the living.",
                         "https://www.youtube.com/watch?v=yfDUv3ZjH2k", "Edgar Wright", 2004)

ironman = media.Movie("Iron Man",
                       "http://ecx.images-amazon.com/images/I/518LjxcQxtL._SX200_QL80_.jpg",
                       "After being held captive in an Afghan cave, "
                       "an engineer creates a unique weaponized suit of armor to fight evil.",
                       "https://www.youtube.com/watch?v=8hYlB38asDY","Jon Favreau",2008)
aladdin = media.Movie("Aladdin",
                      "http://ecx.images-amazon.com/images/I/519HEW58T8L.jpg",
                      "When a street urchin vies for the love of a beautiful princess, "
                      "he uses a genie's magic power to make himself "
                      "off as a prince in order to marry her.",
                      "https://www.youtube.com/watch?v=cmUZuZniouU",
                      "Ron Clements",
                      1992)
#store the movies in an array
movies = [toy_story, scott_pilgrim, ferris_bueller, shaun_dead, ironman, aladdin]

fresh_tomatoes.open_movies_page(movies)