import unittest
import utils

from commands.gender_detection import GenderDetection

class CommandkeyDict(unittest.TestCase):
	def runTest(self):
		commands = utils.get_commands_dict()
		self.assertIsInstance(commands['gender-detection'], GenderDetection)

class CommandkeyList(unittest.TestCase):
	def runTest(self):
		commands = utils.get_commands_names_list()
		self.assertTrue('gender-detection' in commands)