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

class MovieList(list):

	def __init__(self):
		self.movies = []

	def append(self, movie):
		self.movies.append(movie)

	def print_titles(self):
		for i, movie in enumerate(self.movies):
			print movie.year, ": ", movie.title, "(%u)"%int(movie.length_in_minutes), ": ", movie.genre, ": ", movie.language

	def filter_out_length_shorter_than(self, minutes):
		self.movies = [movie for movie in self.movies if int(movie.length_in_minutes) > 70]

	def filter_out_genre(self, genre):
		self.movies = [movie for movie in self.movies if genre not in movie.genre]

	def filter_in_language(self, language):
		self.movies = [movie for movie in self.movies if movie.language in language]

def file_parser(filename):
	file = open(filename)
	movies = MovieList()
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


if __name__ == "__main__":
	movies = file_parser("omdbextract.txt")
	movies.filter_out_length_shorter_than(70)
	movies.filter_out_genre("Animation")
	movies.filter_in_language("English")
	movies.print_titles()
