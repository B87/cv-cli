from abc import ABC, abstractmethod

import time

"""
	Decorator to print the duration time of a function execution
"""
def timeit(method):
	def timed(*args, **kw):
		ts = time.time()
		result = method(*args, **kw)
		te = time.time()        
		if 'log_time' in kw:
			name = kw.get('log_name', method.__name__.upper())
			kw['log_time'][name] = int((te - ts) * 1000)
		else:
			print ('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
		return result    
	return timed

class BaseCommand(ABC):
	
	def __init__(self): 
		pass

	@abstractmethod
	@timeit
	def processImage(self, image):
		pass

