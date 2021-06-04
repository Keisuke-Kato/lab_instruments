from numpy.core.arrayprint import BoolFormat
import pyvisa as visa

rm = visa.ResourceManager()

class PWR1201MH:
	def __init__(self, resource_name, rm=rm):
		self.instr = rm.open_resource(resource_name)
		print(self.instr.query('*IDN?'))
		self.instr.read_termination = '\n'
		self.instr.write_termination = '\n'

# voltage
	def set_voltage(self, voltage):
		self.instr.write('VOLT %s' % voltage)

	def get_voltage(self):
		voltage = self.instr.query_ascii_values('VOLT?')[0]
		return voltage

	def set_vrange(self, LH): # LH = 'LOW' or 'HIGH'
		self.instr.write('CURR:EXT:RANG %s' % LH)

	def get_vrange(self):
		LH = self.instr.query('CURR:EXT:RANG?')
		return LH # 'LOW' or 'HIGH'

# current
	def set_current(self, current):
		self.instr.write('CURR %s' % current)

	def get_current(self):
		current = self.instr.query_ascii_values('CURR?')[0]
		return current

	def set_current_limit(self, limit):
		self.instr.write('CURR:PROT %s' % limit)

	def get_current_limit(self):
		limit = self.instr.query_ascii_values('CURR:PROT?')[0]
		return limit

# measured output
	def get_apply_meas(self):
		current, voltage = self.instr.query_ascii_values('MEAS:ALL?')
		return current, voltage

	def get_current_meas(self):
		current = self.instr.query_ascii_values('MEAS:CURR?')[0]
		return current

	def get_voltage_meas(self):
		voltage = self.instr.query_ascii_values('MEAS:VOLT?')[0]
		return voltage

# output switch
	def set_output(self, output):
		self.instr.write('OUTP %s' % output)

	def get_output(self):
		state = self.instr.query_ascii_values('OUTP?')[0]
		return state