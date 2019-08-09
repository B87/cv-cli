import unittest
import numpy as np
import os
import sys

from core.input_processor import LocalFSInput

from cv_cli import ROOT_DIR 

class LocalFSInputTest(unittest.TestCase):
	def runTest(self):
		input = LocalFSInput(os.path.join(ROOT_DIR, 'data/images/people/woman_frontal.jpg'))
		result = input.getImages()

		self.assertTrue(len(result) == 1)
		self.assertIsInstance(result[0], np.ndarray) 