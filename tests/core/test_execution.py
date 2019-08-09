import unittest
from core.execution import CommandExecution

class CommandExecutionGenderDetectionTest(unittest.TestCase):
	def runTest(self):
	 	execution = CommandExecution('data/images/people/woman_frontal.jpg', 'gender-detection', 'console')
	 	execution.execute() 


class CommandExecutionInvalidCommand(unittest.TestCase):
	def runTest(self):
	 	execution = CommandExecution('data/images/people/woman_frontal.jpg' 'invalid', 'console')
	 	self.assertRaises(SystemExit, execution.execute) 