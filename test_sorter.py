import unittest
import sorter

class TestSorter(unittest.TestCase):

	def test_should_parse_movie_titles(self):
		movies = sorter.file_parser("omdbextract.txt")
		self.assertEqual(movies[0].title, "Nobody Notices")
		self.assertEqual(movies[1].title, "Tinder and Grinder")
		self.assertEqual(movies[-1].title, "Autopsie d'un mariage blanc")
		self.assertEqual(movies[-2].title, "En la caja")

	def test_should_only_show_movies_less_than_70_mins(self):
		movies = sorter.file_parser("omdbextract.txt")
		short_movies = sorter.length_over(movies, 70)
		for movie in short_movies:
			self.assertTrue(int(movie.length_in_minutes) > 70)

if __name__ == "__main__":
	unittest.main()
