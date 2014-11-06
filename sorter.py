class Movie:
	id = ""
	title = ""
	year = ""
	length = ""
	genre = ""

	def __init__(self, id, title, year, length_in_minutes, genre):
		self.id = id
		self.title = title
		self.year = year
		self.length_in_minutes = length_in_minutes
		self.genre = genre

def file_parser(filename):
	file = open(filename)
	movies = []
	for line in file:
		movie_info = line.split("\t");
		id = movie_info[0]
		title = movie_info[2]
		year = movie_info[3][:4]
		length = movie_info[5][0:-4].replace(',', '')
		if length == "": length = 0
		genre = movie_info[6]

		this_movie = Movie(id, title, year, length, genre)
		movies.append(this_movie)
	return movies

def print_movie_titles(movies):
	for i, movie in enumerate(movies):
		print movie.year, ": ", movie.title, "(%u)"%int(movie.length_in_minutes), ": ", movie.genre

def filter_by_length_greater_than(movies, minutes):
	return [movie for movie in movies if int(movie.length_in_minutes) > 70]

def filter_by_genre(movies, genre):
	return [movie for movie in movies if genre not in movie.genre]

if __name__ == "__main__":
	movies = file_parser("omdbextract.txt")
	print_movie_titles(movies)
	long_movies = filter_by_length_greater_than(movies, 70)
	print_movie_titles(long_movies)
	no_animation_movies = filter_by_genre(movies, "Animation")
	print_movie_titles(no_animation_movies)