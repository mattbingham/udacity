import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "img/movie_toy-story.jpg",
                        "https://www.youtube.com/watch?v=NTdKQzVFeis")
avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "img/movie_avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
bourne_identity = media.Movie("Bourne Identity",
                     "A man is picked up by a fishing boat, bullet-riddled and suffering from amnesia, before racing to elude assassins and regain his memory.",
                     "img/movie_bourne-identity.jpg",
                     "https://www.youtube.com/watch?v=SZh7ZaiYXjI")
hunger_games = media.Movie("The Hunger Games",
                     "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games: a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
                     "img/movie_hunger-games.jpg",
                     "https://www.youtube.com/watch?v=mfmrPu43DF8")
irobot = media.Movie("I, Robot",
                     "In 2035, a technophobic cop investigates a crime that may have been perpetrated by a robot, which leads to a larger threat to humanity.",
                     "img/movie_i-robot.jpg",
                     "https://www.youtube.com/watch?v=rL6RRIOZyCM")
xmen_apocalypse = media.Movie("X-Men Apocolypse",
                     "After the re-emergence of the world's first mutant, world-destroyer Apocalypse, the X-Men must unite to defeat his extinction level plan.",
                     "img/movie_xmen-apocalypse.jpg",
                     "https://www.youtube.com/watch?v=COvnHv42T-A")

movies = [toy_story, avatar, bourne_identity, hunger_games, irobot, xmen_apocalypse]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)