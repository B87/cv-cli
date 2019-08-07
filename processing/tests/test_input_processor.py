import unittest
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

from processing.input_processor import LocalFSInput

from definitions import ROOT_DIR 

class LocalFSInputTest(unittest.TestCase):
	def runTest(self):
		input = LocalFSInput(os.path.join(ROOT_DIR, 'data/images/people/woman_frontal.jpg'))
		result = input.getImages()

		self.assertTrue(len(result) == 1)
		self.assertIsInstance(result[0], np.ndarray) 


suite = unittest.TestSuite()
suite.addTests([LocalFSInputTest()])
unittest.TextTestRunner().run(suite)