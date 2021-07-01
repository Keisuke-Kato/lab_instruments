import pyvisa as visa
import numpy as np

rm = visa.ResourceManager()

class N5222A:
	def __init__(self, rm, resource_name):
		self.instr = rm.open_resource(resource_name)
		self.instr.write_termination = '\n'
		self.instr.read_termination = '\n'
		print(self.instr.query('*IDN?'))

	def setStartFreq(self,freq,ch=1):
		self.instr.write('SENS%d:FREQ:STAR %f' % (ch,freq))

	def setStopFreq(self,freq,ch=1):
		self.instr.write('SENS%d:FREQ:STOP %f' % (ch,freq))

	def setCenterFreq(self,freq,ch=1):
		self.instr.write('SENS%d:FREQ:CENT %f' % (ch,freq))

	def setFreqSpan(self,freq,ch=1):
		self.instr.write('SENS%d:FREQ:SPAN %f' % (ch,freq))

	def getStartFreq(self,ch=1):
		f = self.instr.query_ascii_values('SENS%d:FREQ:STAR?' % ch)[0]
		return f

	def getStopFreq(self,ch=1):
		f = self.instr.query_ascii_values('SENS%d:FREQ:STOP?' % ch)[0]
		return f

	def getCenterFreq(self,ch=1):
		f = self.instr.query_ascii_values('SENS%d:FREQ:CENT?' % ch)[0]
		return f

	def getFreqSpan(self,ch=1):
		f = self.instr.query_ascii_values('SENS%d:FREQ:SPAN?' % ch)[0]
		return f

	def setNumberOfPoints(self,num,ch=1):
		self.instr.write('SENS%d:SWE:POIN %d' % (ch,num))

	def getNumberOfPoints(self,ch=1):
		n = self.instr.query_ascii_values('SENS%d:SWE:POIN?' % ch)[0]
		return n

	def setIFBW(self,ifbw,ch=1):
		self.instr.write('SENS%d:BWID %f' % (ch,ifbw))

	def getIFBW(self,ch=1):
		ifbw = self.instr.query_ascii_values('SENS%d:BWID?' % ch)[0]
		return ifbw

	def setOutputState(self,state): # (ON, OFF)
		self.instr.write('OUTP %s' % state)

	def getOutputState(self):
		state = self.instr.query_ascii_values('OUTP?'[0])
		return state

	def setOutputPower(self,pow,ch=1): # unit:dBm
		self.instr.write('SOUR%d:POW %f' % (ch,pow))

	def getOutputPower(self,ch=1):
		pow = self.instr.query_ascii_values('SOUR%d:POW?' % ch)[0]
		return pow

	def setSweepType(self,type,ch=1): # (LIN, PWR, CW, SEG, PHASE)
		self.instr.write('SENS%d:SWE:TYPE %s' % (ch,type))

	def getSweepType(self,ch=1):
		type = self.instr.query('SENS%d:SWE:TYPE?' % ch)
		return type

	def setSegmentSweepState(self,state): # (ON, OFF)
		self.instr.write('SENS:SEGM %s' % state)

	def getSegmentSweepState(self):
		state = self.instr.query_ascii_values('SENS:SEGM?')
		return state

	def addSegment(self,num):
		self.instr.write('SENS:SEGM%d:ADD' % num)

	def deleteSegment(self,num):
		self.instr.write('SENS:SEGM%d:DEL' % num)

	def deleteAllSegment(self):
		self.instr.write('SENS:SEGM:DEL:ALL')

	def getSegmentCount(self):
		n = self.query_ascii_values('SENS:SEGM:COUN?'[0])
		return n

	def setSegmentStartFreq(self,snum,freq): # unit:GHz
		self.instr.write('SENS:SEGM%d:FREQ:STAR %f' % (snum,freq*1e+9))

	def setSegmentStopFreq(self,snum,freq):
		self.instr.write('SENS:SEGM%d:FREQ:STOP %f' % (snum,freq*1e+9))

	def setSegmentCenterFreq(self,snum,freq):
		self.instr.write('SENS:SEGM%d:FREQ:CENT %f' % (snum,freq*1e+9))

	def setSegmentFreqSpan(self,snum,freq):
		self.instr.write('SENS:SEGM%d:FREQ:SPAN %f' % (snum,freq*1e+9))

	def getSegmentStartFreq(self,snum):
		f = self.instr.query_ascii_values('SENS:SEGM%d:FREQ:STAR?' % snum)[0]
		return f

	def getSegmentStopFreq(self,snum):
		f = self.instr.query_ascii_values('SENS:SEGM%d:FREQ:STOP?' % snum)[0]
		return f

	def getSegmentCenterFreq(self,snum):
		f = self.instr.query_ascii_values('SENS:SEGM%d:FREQ:CENT?' % snum)[0]
		return f

	def getSegmentFreqSpan(self,snum):
		f = self.instr.query_ascii_values('SENS:SEGM%d:FREQ:SPAN?' % snum)[0]
		return f

	def setSegmentNumberOfPoints(self,snum,num):
		self.instr.write('SENS:SEGM%d:SWE:POIN %d' % (snum,num))

	def getSegmentNumberOfPoints(self,snum):
		n = self.instr.query_ascii_values('SENS:SEGM%d:SWE:POIN?' % snum)[0]
		return n

	def setSegmentIFBW(self,snum,ifbw): #unit:kHz
		self.instr.write('SENS:SEGM%d:BWID %f' % (snum,ifbw*1e+3))

	def getSegmentIFBW(self,snum):
		ifbw = self.instr.query_ascii_values('SENS:SEGM%d:BWID?' % snum)[0]
		return ifbw

	def setSegmentIFBWControl(self,state): # (ON, OFF)
		self.instr.write('SENS:SEGM:BWID:CONT %s' % state)

	def getSegmentIFBWControl(self):
		state = self.instr.query_ascii_values('SENS:SEGM:BWID:CONT?')[0]
		return state

	def setDataFormat(self,form): # (MLIN, MLOG, PHAS, UPH, IMAG, REAL, POL, SMIT, SADM, SWR, GDEL, KELV, FAHR, CELS)
		self.instr.write('CALC:FORM %s' % form)

	def getDataFormat(self):
		form = self.instr.query('CALC:FORM?')
		return form

	def setElectricalDelay(self,edel):
		self.instr.write('CALC:CORR:EDEL %f' % edel)

	def getElectricalDelay(self):
		edel = self.instr.query_ascii_values('CALC:CORR:EDEL?')[0]
		return edel

	def setElectricalDelayDistance(self,d): #unit: meter
		self.instr.write('CALC:CORR:EDEL:DIST %f' % d)

	def getElectricalDelayDistance(self):
		d = self.instr.query_ascii_values('CALC:CORR:EDEL:DIST?')[0]
		return d

	def setVelocityFactor(self,v):
		self.instr.write('CALC:CORR:RVEL:COAX %f' % v)

	def getVelocityFactor(self):
		v = self.instr.query_ascii_values('CALC:CORR:RVEL:COAX?')[0]
		return v

	def setAveragingState(self,state): # (ON,OFF)
		self.instr.write('SENS:AVER %s' % state)

	def getAveragingState(self):
		state = self.query_ascii_values('SENS:AVER?')[0]
		return state

	def setAveragingFactor(self,i):
		self.instr.write('SENS:AVER:COUN %d' % i)

	def getAveragingFactor(self):
		i = self.instr.query_ascii_values('SENS:AVER:COUN?')[0]
		return i

	def restartAveraging(self):
		self.instr.write('SENS:AVER:CLE')

	def getData(self,datapoint='FDATA'):
		data = self.instr.query_ascii_values('CALC:DATA? %s' % datapoint, container=np.array)
		return data

	def setTriggerModeContinuous(self,ch=1):
		self.instr.write('SENS%d:SWE:MODE CONT' % ch)

	def setTriggerModeHold(self,ch=1):
		self.instr.write('SENS%d:SWE:MODE HOLD' % ch)

	def setTriggerModeSingle(self,ch=1):
		self.instr.write('SENS%d:SWE:MODE SING' % ch)