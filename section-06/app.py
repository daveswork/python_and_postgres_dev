from movie import Movie
from user import User


user = User.load_from_file('Dave.txt')

print(user.movies)

