import cv2
import os
import sys

from abc import ABC, abstractmethod

"""
	Input proceessor base class
"""
class Input(ABC):
	
	#@timeit
	@abstractmethod
	def getImages(self):
		pass

def wait_for_frame(capture):
	# TODO : Put a timeout
	while cv2.waitKey(1) < 0:
		# Read frame
		hasFrame, frame = capture.read()
		print(type(frame))
		if not hasFrame:
			cv2.waitKey()
			break
	return frame

class WebCamInput(Input):

	def getImages(self):
		cap = cv2.VideoCapture(0)
		frame = wait_for_frame(cap)
		return [frame]

class LocalFSInput(Input):
	def __init__(self, path):
		self.path = path 

	def getImages(self):
		if(os.path.exists(self.path)):
			if os.path.isdir(self.path):
				print("... folder detected, reading all images in it")
				images = []
				for r, d, f in os.walk(self.path):
					for filename in f:
						if filename.endswith('.' + 'jpg'):
							images.append(cv2.imread((self.path)))
				return images
			else:
				print("... reading image from " + self.path)
				return [cv2.imread((self.path))]
		else:
			print("Privided input path "+self.path+" does not exist")
			sys.exit(1)
