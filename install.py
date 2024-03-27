# installer for rs485-solar driver
# Copyright 2024 Jon Fear
# Distributed under terms of the GPLv3

from weecfg.extension import ExtensionInstaller

def loader():
    return rs485-solarInstaller()

class rs485-solarInstaller(ExtensionInstaller):
    def __init__(self):
        super(rs485-solarInstaller, self).__init__(
            version="0.1",
            name='rs485-solar',
            description='Collect data from PYR20 Solar hardware',
            author="Jon Fear",
            author_email="",
            files=[('bin/user', ['bin/user/weewx-rs485-solar.py'])]
        )