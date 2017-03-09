import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys',
                        'https://upload.wikimedia.org/wikipedia/zh/d/dc/Movie_poster_toy_story.jpg',
                        'https://youtu.be/zQPWkjdORjo?list=RDQMSOzCDTUqy4k')

#print(toy_story.storyline)

avatar = media.Movie('Avatar',
                     'A marine on alien planet',
                     'https://upload.wikimedia.org/wikipedia/zh/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://youtu.be/sbuGO9Pvufs?list=RDQMWsc-sqsg0zs')

#print(avatar.storyline)

#avatar.show_trailer()

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)

