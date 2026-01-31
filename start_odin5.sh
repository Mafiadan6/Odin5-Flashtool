#!/bin/bash

# Odin5 GUI Launcher
echo "🔥 Starting Odin5 Flash Tool GUI..."
echo "🌐 By 爪卂丂ㄒ乇尺爪工刀ᗪ"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if PyQt5 is installed
if ! python3 -c "import PyQt5" &> /dev/null; then
    echo "📦 Installing PyQt5..."
    pip3 install PyQt5
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install PyQt5. Please install it manually: pip3 install PyQt5"
        exit 1
    fi
fi

# Check if odin5 binary exists
if [ ! -f "./odin5" ]; then
    echo "⚠️  Warning: odin5 binary not found in current directory"
    echo "   The GUI will run but flashing functionality may be limited"
fi

# Start the GUI with sudo and stderr redirected to suppress dbus/dconf warnings
sudo python3 odin5_gui.py 2>/dev/null