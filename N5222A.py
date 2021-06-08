import pyvisa as visa
import numpy as np

rm = visa.ResourceManager()

class N5222A:
	def __init__(self, rm, resource_name):
		self.instr = rm.open_resource(resource_name)
		print(self.instr.query('*IDN?'))

	def set_freq_center(self,fc):
		self.instr.write(':SENSE:FREQ:CENT '+str(int(fc)))

	def set_freq_span(self,span):
		self.instr.write(':SENSE:FREQ:SPAN '+str(int(span)))

	def set_freq_i(self,fi):
		self.instr.write(':SENSE:FREQ:STAR '+str(int(fi)))

	def set_freq_f(self,ff):
		self.instr.write(':SENSE:FREQ:STOP '+str(int(ff)))