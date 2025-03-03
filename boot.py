# This file is executed on every boot (including wake-boot from deepsleep)
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'your_ssid'
password = 'your_password'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)
station.config(dhcp_hostname="espotify")

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())