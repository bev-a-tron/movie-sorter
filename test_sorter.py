import unittest
import sorter

class TestSorter(unittest.TestCase):

	def setUp(self):
		self.movies = sorter.file_parser("omdbextract.txt")

	def test_should_parse_movie_titles(self):
		self.assertEqual(self.movies.movies[0].title, "Nobody Notices")
		self.assertEqual(self.movies.movies[1].title, "Tinder and Grinder")
		self.assertEqual(self.movies.movies[-1].title, "Autopsie d'un mariage blanc")
		self.assertEqual(self.movies.movies[-2].title, "En la caja")

	def test_should_only_show_movies_greater_than_70_mins(self):
		self.movies.filter_out_length_shorter_than(70)
		for movie in self.movies:
			self.assertTrue(int(movie.length_in_minutes) > 70)

	def test_should_not_show_animation(self):
		animation = "Animation"
		self.movies.filter_out_genre(animation)
		for movie in self.movies:
			self.assertTrue(animation not in movie.genre)

	def test_should_not_show_non_english(self):
		english = "English"
		self.movies.filter_in_language(english)
		for movie in self.movies:
			self.assertTrue(english in movie.language)

if __name__ == "__main__":
	unittest.main()
