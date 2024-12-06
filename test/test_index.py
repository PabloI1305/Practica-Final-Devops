import unittest
from bs4 import BeautifulSoup

class TestIndexHtml(unittest.TestCase):
    def test_hola_mundo(self):
        with open("index.html", "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
            h1 = soup.find("h1")
            self.assertIsNotNone(h1)
            self.assertEqual(h1.text, "Hola Mundo")

if __name__ == "__main__":
    unittest.main()
