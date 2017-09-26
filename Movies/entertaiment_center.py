import Media
import fresh_tomatoes

toy_story = Media.Movie("Toy story","A story of a boy and his toys that come to life","https://i.ytimg.com/vi/0i5d2oBCYE4/maxresdefault.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")

#print toy_story.storyline

Avatar = Media.Movie("Avatar","A marine on an alien planet","http//www.upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Post","http://www.youtube.com/watch?v=-9ceBgWV8io")
#print Avatar.storyline
#Avatar.Show_trailer()

Movies = [toy_story,Avatar]
#fresh_tomatoes.open_movies_page(Movies)
print Media.Movie.__doc__