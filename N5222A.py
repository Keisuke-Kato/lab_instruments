import pyvisa as visa
import numpy as np

rm = visa.ResourceManager()

class N5222A:
	def __init__(self, rm, resource_name):
		self.instr = rm.open_resource(resource_name)
		print(self.instr.query('*IDN?'))