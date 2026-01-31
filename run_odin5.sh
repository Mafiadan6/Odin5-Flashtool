#!/bin/bash
# Wrapper script to run Odin5 GUI with stderr suppressed

# Run the GUI with sudo and stderr redirected to suppress dbus/dconf warnings
sudo python odin5_gui.py 2>/dev/null