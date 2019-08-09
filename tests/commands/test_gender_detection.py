import unittest
import cv2
from commands.gender_detection import GenderDetection

class GenderDetectionTest(unittest.TestCase):
	def runTest(self):
		command = GenderDetection()
		result = command.processImage(cv2.imread('data/images/people/woman_frontal.jpg'))
		print(result)
		
		self.assertTrue(len(result.boxes) > 0)