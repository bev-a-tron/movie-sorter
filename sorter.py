class Movie:
	id = ""
	title = ""
	year = ""
	length = ""

	def __init__(self, id, title, year, length):
		self.id = id
		self.title = title
		self.year = year
		self.length = length

def file_parser(filename):
	file = open(filename)
	movies = []
	for line in file:
		movie_info = line.split("\t");
		id = movie_info[0]
		title = movie_info[2]
		year = movie_info[3][:4]
		length = movie_info[5]

		this_movie = Movie(id, title, year, length)
		movies.append(this_movie)
	return movies

def print_all_movie_titles(movies):
	for i, movie in enumerate(movies):
		print movie.year, ": ", movie.title

if __name__ == "__main__":
	movies = file_parser("omdbextract.txt")
	print_all_movie_titles(movies)