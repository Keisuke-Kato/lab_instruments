import pyvisa as visa
import numpy as np

rm = visa.ResourceManager()

class E5071C:
	def __init__(self, rm, resource_name):
		self.instr = rm.open_resource(resource_name)
		print(self.instr.query('*IDN?'))

	def set_freq_center(self,fc):
		self.instr.write(':SENS:FREQ:CENT '+str(int(fc)))

	def set_freq_span(self,span):
		self.instr.write(':SENS:FREQ:SPAN '+str(int(span)))

	def set_freq_i(self,fi):
		self.instr.write(':SENS:FREQ:STAR '+str(int(fi)))

	def set_freq_f(self,ff):
		self.instr.write(':SENS:FREQ:STOP '+str(int(ff)))

	def set_frange_c(self,fc,span):
		self.set_freq_center(fc)
		self.set_freq_span(span)

	def set_frange_if(self,fi,ff):
		self.set_freq_i(fi)
		self.set_freq_f(ff)

	def get_freq_array(self):
		data = self.instr.query_ascii_values(':SENS:FREQ:DATA?',container=np.array)
		return data

	def set_point_num(self,num):
		self.instr.write(':SENS:SWE:POIN %s' % num)

	def set_dataformat(self,datatype):
		self.instr.write(':CALC:FORM %s' % datatype)

	def set_dataformat_mlog(self):
		self.instr.write(':CALC:FORM MLOG')

	def set_dataformat_slin(self):
		self.instr.write(':CALC:FORM SLIN')

	def get_data(self):
		self.set_dataformat('SLIN')
		data = self.instr.query_ascii_values(':CALC:DATA:FDAT?',container=np.array)
		mag = data[0::2]
		phase = data[1::2]
		return mag, phase

	def set_IFBW(self,ifbw):
		self.instr.write(':SENS:BAND %s' % ifbw)

	def set_average(self, count):
		self.instr.write(':SENS:AVER:COUN %s' % count)

	def average_on(self):
		self.instr.write(':SENS:AVER ON')

	def average_off(self):
		self.instr.write(':SENS:AVER OFF')

	def clear_average_count(self):
		self.instr.write(':SENS:AVER:CLE')