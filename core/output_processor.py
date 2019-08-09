
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

class ImageOutput(Output):
	def outputResult(self, result):
		boxes = result.boxes
		img = result.source_image.copy()
		for box in boxes:
			frameHeight = img.shape[0]
			cv2.rectangle(img, (box.x1, box.y1), (box.x2, box.y2), (0, 255, 0), int(round(frameHeight/150)), 8)
			cv2.putText(img, box.label, (box.x1, box.y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
		
		cv2.imshow('Press any key to exit', img)
		cv2.waitKey()

class ConsoleOutput(Output):
	def outputResult(self, result: ImageResult):
		print(result)