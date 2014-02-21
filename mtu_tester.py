import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonMtuSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_search_on_homepage(self):
		driver = self.driver
		driver.get("http://mtu.edu")
		self.assertIn("hockey", driver.title)
		elem = driver.find_element_by_name("q")
		elem.send_keys("hockey")
		elem.send_keys(Keys.RETURN)
		self.assertIn("Google". driver.title)

	def closeUp(self):
		driver.close()

if __name__ == "__main__":
	unittest.main()