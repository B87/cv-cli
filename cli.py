import argparse
import sys
import utils

implemented_commands = ['gender-detection']
implemented_commands_str = "Implemented commands are : "+",".join(implemented_commands)

class CapitalisedHelpFormatter(argparse.HelpFormatter):
	def add_usage(self, usage, actions, groups, prefix=None):
		if prefix is None:
			prefix = 'Usage: '
			return super(CapitalisedHelpFormatter, self).add_usage(usage, actions, groups, prefix)

parser = argparse.ArgumentParser(description = 'Shell util to manipulate and extract information from images') 
parser.add_argument("-in", "--input", help='Path of the folder containing the input images in jpg format', required = False, default = None)
parser.add_argument("-o", "--output", help='Destination path for the output of the process, if not provided the results will be pinted on the console',
 required = False, default = None )
parser.add_argument("-c", "--command", help='Name of the command to run.' + implemented_commands_str, required = True)
parser.add_argument("-p", "--print", help='Print results and images during processing', required = False, action = 'store_true', default = False)
args = parser.parse_args()

input = utils.resolve_input(args.input)
command = utils.resolve_command(args.command, implemented_commands_str)
output = utils.resolve_output(args.output)

for image in input.getImages():
	result = command.processImage(image)
	output.outputResult(result)