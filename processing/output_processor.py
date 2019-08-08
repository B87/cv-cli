
import cv2

from models import Output

class ImageOutput(Output):
	def outputResult(self, result):
		cv2.imshow(result)
		#boxes = result[boxes]
		#img = result[source_image]
		pass
		
	def printResult(self, result):
		pass