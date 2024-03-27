weewx-rs485-solar
Copyright 2024 Jon Fear
Distributed under terms of the GPLv3

This is a driver for weewx that collects data from The PYR20 Solar Radiation Sensor via RS485.

===============================================================================
Installation

1) install the the driver

  weectl extension install https://github.com/jonfear/weewx-rs485-solar/archive/master.zip

2) configure weeWX to use the driver

  weectl station reconfigure

3) restart weeWX

  sudo systemctl restart weewx