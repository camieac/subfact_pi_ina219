#!/usr/bin/python

from raspi_ina219.ina219 import INA219

ina = INA219()
result = ina.getBusVoltage_V()

print "Shunt   : %.3f mV" % ina.getShuntVoltage_mV()
print "Bus     : %.3f V" % ina.getBusVoltage_V()
print "Current : %.3f mA" % ina.getCurrent_mA()
