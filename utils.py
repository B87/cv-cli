import time
from processing.input_processor import WebCamInput, LocalFSInput
from processing.commands.gender_detection import GenderIdentification
from processing.output_processor import ImageOutput

"""
Parse string key to input implementation
"""
def resolve_input(input):
	if input:
		print('... using localFs input')
		return LocalFSInput(input)
	else:
		print('... using webcam input')
		return WebCamInput()

"""
Parse string key to command implementation
"""
def resolve_command(command, implemented_commands_str):
	if command == "gender-detection":
		print('... executing gender-detection command')
		return GenderIdentification()
	else:
		sys.exit('The command provided is not implemented. ' + implemented_commands_str)
		
"""
Parse string key to output processor implementation
"""
def resolve_output(save):
	return ImageOutput()

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