import unittest
import sorter

class TestSorter(unittest.TestCase):

	def setUp(self):
		self.movies = sorter.file_parser("omdbextract.txt")

	def test_should_parse_movie_titles(self):
		self.assertEqual(self.movies[0].title, "Nobody Notices")
		self.assertEqual(self.movies[1].title, "Tinder and Grinder")
		self.assertEqual(self.movies[-1].title, "Autopsie d'un mariage blanc")
		self.assertEqual(self.movies[-2].title, "En la caja")

	def test_should_only_show_movies_greater_than_70_mins(self):
		long_movies = sorter.filter_by_length_greater_than(self.movies, 70)
		for movie in long_movies:
			self.assertTrue(int(movie.length_in_minutes) > 70)

	def test_should_not_show_animation(self):
		genre = "Animation"
		no_animation = sorter.filter_by_genre(self.movies, genre)
		for movie in no_animation:
			self.assertTrue(genre not in movie.genre)

if __name__ == "__main__":
	unittest.main()
