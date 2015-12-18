#Help from Programming Foundations with Python
import media
import fresh_tomatoes
#Creates instance objects of Movie
batman = media.Movie("The Dark Knight Rises",
"Batman must stop the joker from terrorizing Gotham",
"https://upload.wikimedia.org/wikipedia/en/thumb/8/83/Dark_knight_rises_poster.jpg/220px-Dark_knight_rises_poster.jpg",
"https://youtu.be/g8evyE9TuYk")

lion = media.Movie("The Lion King",
"Semba grows up to stop Car",
"https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/The_Lion_King_poster.jpg/220px-The_Lion_King_poster.jpg",
"https://youtu.be/jOIu472cCq0")

prison = media.Movie("The Shawshank Redemption",
"Man who was falsely accused escapes from prison",
"https://upload.wikimedia.org/wikipedia/en/thumb/8/81/ShawshankRedemptionMoviePoster.jpg/220px-ShawshankRedemptionMoviePoster.jpg",
"https://youtu.be/6hB3S9bIaco")
#Stores Movie Objects in a list
mov = [batman,lion,prison]
#Passes Movie list to method
fresh_tomatoes.open_movies_page(mov)
