#!/usr/bin/env python3

# Copyright (C) 2018 Herman Õunapuu
#
# This file is part of Linux GPU Manager.
#
# Linux GPU Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Linux GPU Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Linux GPU Manager.  If not, see <http://www.gnu.org/licenses/>.


import sys

import dbus.exceptions
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

from controller import GPUManager

# Initialize a main loop
DBusGMainLoop(set_as_default=True)
loop = GLib.MainLoop()

# Declare a name where our service can be reached
try:
    bus_name = dbus.service.BusName("ee.ounapuu.GPUManager",
                                    bus=dbus.SystemBus(),
                                    do_not_queue=True)
except dbus.exceptions.NameExistsException:
    print("service is already running")
    sys.exit(1)

# Run the loop
try:
    GPUManager(bus_name)
    loop.run()
except KeyboardInterrupt:
    print("keyboard interrupt received")
except Exception as e:
    print("Unexpected exception occurred: '{}'".format(str(e)))
finally:
    loop.quit()
