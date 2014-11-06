class Movie:
	id = ""
	title = ""
	year = ""
	length = ""
	genre = ""
	language = ""

	def __init__(self, id = "", title = "", year = "", length_in_minutes = "", genre = "", language = ""):
		self.id = id
		self.title = title
		self.year = year
		self.length_in_minutes = length_in_minutes
		self.genre = genre
		self.language = language

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
		language = movie_info[17]

		this_movie = Movie(id = id, title = title, year = year, length_in_minutes = length, genre = genre, language = language)
		movies.append(this_movie)
	return movies

def print_movie_titles(movies):
	for i, movie in enumerate(movies):
		print movie.year, ": ", movie.title, "(%u)"%int(movie.length_in_minutes), ": ", movie.genre, ": ", movie.language

def filter_out_length_shorter_than(movies, minutes):
	return [movie for movie in movies if int(movie.length_in_minutes) > 70]

def filter_out_genre(movies, genre):
	return [movie for movie in movies if genre not in movie.genre]

def filter_in_language(movies, language):
	return [movie for movie in movies if movie.language in language]

if __name__ == "__main__":
	movies = file_parser("omdbextract.txt")
	print_movie_titles(movies)
	
	long_movies = filter_out_length_shorter_than(movies, 70)
	print_movie_titles(long_movies)

	no_animation_movies = filter_out_genre(movies, "Animation")
	print_movie_titles(no_animation_movies)
	
	english_only_movies = filter_in_language(movies, "English")
	print_movie_titles(english_only_movies)