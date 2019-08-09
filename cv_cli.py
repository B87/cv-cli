import argparse
import utils
import os
import cv2

from core.execution import CommandExecution

"""
	
"""

implemented_commands = ['gender-detection']
implemented_commands_str = "Implemented commands are : "+",".join(implemented_commands)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

MODELS_DIR = os.path.join(ROOT_DIR, 'data/models')


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = 'Shell util to manipulate and extract information from images') 
	parser.add_argument("-in", "--input", help='Path of the folder containing the input images in jpg format', required = False, default = None)
	parser.add_argument("-o", "--output", help='Destination path for the output of the process, if not provided the results will be pinted on the console',
	 required = False, default = None )
	parser.add_argument("-c", "--command", help='Name of the command to run.' + implemented_commands_str, required = True)
	parser.add_argument("-p", "--print", help='Print results and images during processing', required = False, action = 'store_true', default = False)

	args = parser.parse_args()
	
	execution = CommandExecution(args.input, args.command, args.output)
	execution.execute()