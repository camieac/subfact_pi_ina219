#!/usr/bin/python

from raspi_ina219.ina219 import INA219

ina = INA219()
result = ina.getBusVoltage_V()

print "shunt:%.3f bus:%.3f current:%d power:%d" % ( ina.getShuntVoltage_mV(), ina.getBusVoltage_V(), ina.getCurrent_mA(), ina.getPower_mW() )
