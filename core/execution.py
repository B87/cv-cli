from abc import ABC, abstractmethod, abstractproperty 

import numpy as np

from nptyping import Array
from typing import Dict

from core.results import ImageResult
from core.input_processor import WebCamInput, LocalFSInput
from core.output_processor import ImageOutput
import utils
import sys

class CommandExecution():

	def __init__(self, input_key: str, command_key: str, output_key: str = 'test'):
		self.input_key = input_key
		self.command_key = command_key
		self.output_key = output_key

	def execute(self):
		print(self)
		input = self.resolve_input()
		try:
			command = utils.get_commands_dict()[self.command_key]
		except KeyError:
			print("Provided command "+self.command_key+" is note implemented. Implemented commands ->  "+str(utils.get_commands_names_list()))
			sys.exit(1)

		output = self.resolve_output(self.output_key)

		for image in input.getImages():
			result = command.processImage(image)
			#cv2.imshow('', image)
			output.outputResult(result)

	def resolve_input(self):
		if self.input_key:
			print('... using local file system input')
			return LocalFSInput(self.input_key)
		else:
			print('... using webcam input')
			return WebCamInput()
		
	def resolve_output(self, out):
		return ImageOutput()

	def __str__(self):
		return "{input_key : "+self.input_key+", command_key : "+self.command_key+", output_key : "+self.output_key+"}"