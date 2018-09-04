from functools import wraps
import time

token = "2fdcbe37fb989f07645b38c3abebab7dae597a5b316a9978f7d57eddb5c67fc76708f3d765bc2ae12de8f"

def pause(view_func):
	def decorator(*args, **kwargs):
		time.sleep(0.34)
		return view_func(*args, **kwargs)
	return wraps(view_func)(decorator)