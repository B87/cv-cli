import time
from commands.base import BaseCommand
from typing import Dict, List

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

def get_all_subclasses(cls):
    all_subclasses = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses

def get_commands_dict() -> Dict[str, BaseCommand]:
	dict = {}
	all_subclasses = get_all_subclasses(BaseCommand)
	for clazz in all_subclasses:
		instance = clazz()
		dict[instance.cli_str_key()] = instance
	return dict

def get_commands_names_list() -> List[str]:
	result = []
	for k in get_commands_dict():
		result.append(k)
	return result