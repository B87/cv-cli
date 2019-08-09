from abc import ABC, abstractmethod, abstractproperty 

import numpy as np

from nptyping import Array
from typing import Dict

from core.results import ImageResult
from core.input_processor import WebCamInput, LocalFSInput
from core.output_processor import ImageOutput, ConsoleOutput
import utils
import sys

class CommandExecution():

	def __init__(self, input_key: str, command_key: str, output_key: str = 'test'):
		self.input_key = input_key
		self.command_key = command_key
		self.output_key = output_key

	def execute(self):
		input = self.resolve_input()
		try:
			command = utils.get_commands_dict()[self.command_key]
		except KeyError:
			print("Provided command "+self.command_key+" is not implemented. Implemented commands ->  "+str(utils.get_commands_names_list()))
			sys.exit(1)

		output = self.resolve_output()

		for image in input.getImages():
			result = command.processImage(image)
			output.outputResult(result)

	def resolve_input(self):
		if self.input_key:
			print('... using local file system input')
			return LocalFSInput(self.input_key)
		else:
			print('... using webcam input')
			return WebCamInput()
		
	def resolve_output(self):
		if self.output_key == 'console':
			print('... printing results to console')
			return ConsoleOutput()
		elif self.output_key == 'image':
			print('... printing as image')
			return ImageOutput()
		else:
			print("The provided output "+self.output_key+ " not exists. Use either console or image.")
			sys.exit(1)

	def __str__(self):
		return "{input_key : "+self.input_key+", command_key : "+self.command_key+", output_key : "+self.output_key+"}"