weewx-rs485-solar
Copyright 2024 AI and others
## Distributed under terms of the GPLv3  ##  I think. This needs to be clarified.

This is a driver for weewx that collects data from The PYR20 Solar Radiation Sensor via RS485.

PLEASE NOTE, This driver is very experimental and as of today 28 March 2024 does not work. It is not ready for production use and may/will crash a working system. Use at your own peril. 

This driver was written usig AI and also copying lumps of other peoples code, gjr80 and mwall thank you both for the guide.

===============================================================================
Installation

1) install the the driver

  weectl extension install https://github.com/jonfear/weewx-rs485-solar/archive/master.zip

2) configure weeWX to use the driver

  weectl station reconfigure

3) restart weeWX

  sudo systemctl restart weewx

4) Pray!
