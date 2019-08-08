from abc import ABC, abstractmethod 

import numpy as np

from typing import List
from nptyping import Array

"""
	ImageBox and ImageResult are the data structures resulting of command processing
"""
class ImageBox:
	def __init__(self, x1: int, y1 : int, x2 : int, y2 : int, labels : List[str]):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.labels = labels

class ImageResult:
	
	def __init__(self, source_image: Array[int], boxes : List[ImageBox]):
		self.source_image = source_image
		self.boxes = boxes

	def __str__(self):
		return { 'source_image' : self.source_image, 'boxes' : self.boxes }

"""
	Input proceessor base class
"""
class Input(ABC):
	
	#@timeit
	@abstractmethod
	def getImages(self):
		pass

"""
	Command base class
"""
class BaseCommand(ABC):

	#@timeit
	@abstractmethod
	def processImage(self, image: Array[int]) -> ImageResult:
		pass

"""
	Output processor base class
"""
class Output(ABC):

	@abstractmethod
	def outputResult(self, result: ImageResult):
		pass

	# Print result to console
	@abstractmethod
	def printResult(self, result: ImageResult):
		pass