from json import JSONEncoder


from typing import List
from nptyping import Array

"""
	ImageBox and ImageResult are the data structures resulting of command processing
"""
class MyEncoder(JSONEncoder):
	def default(self, o):
		return o.__dict__
		
class ImageBox:
	def __init__(self, x1: int, y1 : int, x2 : int, y2 : int, label : str):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.label = label

	def __str__(self):
		return MyEncoder().encode(self)

	__repr__ = __str__

class ImageResult:
	
	def __init__(self, source_image: Array[int], boxes : List[ImageBox]):
		self.source_image = source_image
		self.boxes = boxes

	def __str__(self):
		return "{ \"source_image\" :"+str(self.source_image)+", \"boxes\" : "+str(self.boxes)+" }"

	__repr__ = __str__
