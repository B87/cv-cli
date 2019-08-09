
import cv2

from abc import ABC, abstractmethod
from core.results import ImageResult

"""
	Output processor base class
"""
class Output(ABC):

	@abstractmethod
	def outputResult(self, result: ImageResult):
		pass

	# Print result to console
	def printResult(self, result: ImageResult):
		print(result)

class ImageOutput(Output):
	def outputResult(self, result):
		cv2.imshow('', result.source_image)
		cv2.waitKey()
		#boxes = result[boxes]
		#img = result[source_image]
		pass
		
	def printResult(self, result):
		pass