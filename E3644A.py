import pyvisa as visa

rm = visa.ResourceManager()

class E3644A:
	def __init__(self, rm, resource_name):
		self.instr = rm.open_resource(resource_name)
		print(self.instr.query('*IDN?'))
		self.instr.read_termination = '\n'
		self.instr.write_termination = '\n'

	def set_apply(self, voltage, current):
		self.instr.write('APPL %s %s' % (voltage,current))

	def set_voltage(self, voltage):
		self.instr.write('VOLT %s' % voltage)

	def set_current(self, current):
		self.instr.write('CURR %s' % current)

	def set_vrange(self, LH):
		self.instr.write('VOLT:RANG %s' % LH)

	def get_apply(self):
		print(self.instr.query('APPL?'))

	def set_output(self, output):
		self.instr.write('OUTP %s' % output)

	def get_output(self):
		print(self.instr.query('OUTP?'))

	def set_current_step(self,step):
		self.instr.write('CURR:STEP %s' % step)

	def get_current_step(self):
		print(self.instr.query('CURR:STEP?'))

	def set_voltage_step(self,step):
		self.instr.write('VOLT:STEP %s' % step)

	def get_voltage_step(self):
		print(self.instr.query('VOLT:STEP?'))	