import pyvisa as visa

rm = visa.ResourceManager()

class PWR1201MH:
	def __init__(self, resource_name, rm=rm):
		self.instr = rm.open_resource(resource_name)
		print(self.instr.query('*IDN?'))
		self.instr.read_termination = '\n'
		self.instr.write_termination = '\n'

# voltage
	def setVoltage(self, voltage):
		self.instr.write('VOLT %s' % voltage)

	def getVoltage(self):
		voltage = self.instr.query_ascii_values('VOLT?')[0]
		return voltage

	def setVoltageRange(self, state): # LH = 'LOW' or 'HIGH'
		self.instr.write('CURR:EXT:RANG %s' % state)

	def getVoltageRange(self):
		state = self.instr.query('CURR:EXT:RANG?')
		return state # 'LOW' or 'HIGH'

# current
	def setCurrent(self, current):
		self.instr.write('CURR %s' % current)

	def getCurrent(self):
		current = self.instr.query_ascii_values('CURR?')[0]
		return current

	def setCurrentLimit(self, limit):
		self.instr.write('CURR:PROT %s' % limit)

	def getCurrentLimit(self):
		limit = self.instr.query_ascii_values('CURR:PROT?')[0]
		return limit

# measured output
	def getMeasuredCV(self):
		current, voltage = self.instr.query_ascii_values('MEAS:ALL?')
		return current, voltage

	def getMeasuredCurrent(self):
		current = self.instr.query_ascii_values('MEAS:CURR?')[0]
		return current

	def getMeasuredVoltage(self):
		voltage = self.instr.query_ascii_values('MEAS:VOLT?')[0]
		return voltage

# output switch
	def setOutputState(self, state):
		self.instr.write('OUTP %s' % state)

	def getOutputState(self):
		state = self.instr.query_ascii_values('OUTP?')[0]
		return state