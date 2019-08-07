from processing.input_processor import WebCamInput, LocalFSInput
from processing.commands.gender_detection import GenderIdentification
from processing.output_processor import ImageOutput
"""
Parse string key to input implementation
"""
def resolve_input(input):
	if input:
		return LocalFSInput(input)
	else:
		return WebCamInput()

"""
Parse string key to command implementation
"""
def resolve_command(command, implemented_commands_str):
	if command == "gender-detection":
		return GenderIdentification()
	else:
		sys.exit('The command provided is not implemented. ' + implemented_commands_str)
		
"""
Parse string key to output processor implementation
"""
def resolve_output(save):
	return ImageOutput()