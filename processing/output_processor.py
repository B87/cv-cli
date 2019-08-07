from abc import ABC, abstractmethod 

import cv2

class Output(ABC):

	"""
		Save result to the desired system
	"""
	@abstractmethod
	def outputResult(self, result):
		pass

	@abstractmethod
	def printResult(self, result):
		pass

class ImageResult():
	def __init__(self, boxes):
		self.boxes = boxes

class ImageOutput(Output):
	def outputResult(self, result):
		pass
		
	def printResult(self, result):
		pass