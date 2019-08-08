import unittest
import numpy as np
import os
import sys

from processing.input_processor import LocalFSInput

from cv-cli import ROOT_DIR 

class BaseTest(unittest.TestCase):
	def __ini__():
		pass

class LocalFSInputTest(BaseTest):
	def runTest(self):
		input = LocalFSInput(os.path.join(ROOT_DIR, 'data/images/people/woman_frontal.jpg'))
		result = input.getImages()

		self.assertTrue(len(result) == 1)
		self.assertIsInstance(result[0], np.ndarray) 

suite = unittest.TestSuite()
suite.addTests([LocalFSInputTest()])
unittest.TextTestRunner().run(suite)