from abc import ABC, abstractmethod, abstractproperty
from nptyping import Array
from core.results import ImageResult 

"""
	Command base class
"""
class BaseCommand(ABC):

	@abstractproperty
	def cli_str_key(self) -> str: 
		pass
		
	#@timeit
	@abstractmethod
	def processImage(self, image: Array[int]) -> ImageResult:
		pass