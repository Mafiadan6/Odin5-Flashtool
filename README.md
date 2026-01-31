# 🔥 Odin5 Flash Tool - Advanced Samsung Firmware Flasher 🔥

<div align="center">

[![License](https://img.shields.io/github/license/mafiadan6/Odin5-Flash-Tool)](LICENSE)
[![Stars](https://img.shields.io/github/stars/mafiadan6/Odin5-Flash-Tool)](https://github.com/mafiadan6/Odin5-Flash-Tool/stargazers)
[![Forks](https://img.shields.io/github/forks/mafiadan6/Odin5-Flash-Tool)](https://github.com/mafiadan6/Odin5-Flash-Tool/network/members)
[![Issues](https://img.shields.io/github/issues/mafiadan6/Odin5-Flash-Tool)](https://github.com/mafiadan6/Odin5-Flash-Tool/issues)

**By 爪卂丂ㄒ乇尺爪工刀ᗪ**

*The most advanced Samsung firmware flashing tool with intuitive GUI interface*

</div>

---

## 📸 Screenshot

![Odin5 Flash Tool Screenshot](Screenshot%20from%202026-01-30%2021-54-15.png)

---

## 🤝 Connect with Me

<div align="center">

[Telegram Group](https://t.me/mastermindszs) | [Telegram](https://t.me/bitcockiii)

</div>

---

## 🚀 Features

- ✨ **Intuitive GUI Interface** - Easy-to-use graphical interface built with PyQt5
- 📱 **Multi-Partition Support** - Flash BL, AP, CP, CSC, and USERDATA partitions
- 🔌 **Auto-Device Detection** - Automatically detects connected Samsung devices in download mode
- ⚡ **T-Flash Mode** - Enhanced flashing speed with T-Flash support
- 🔄 **Auto-Reboot Option** - Automatic reboot after successful flashing
- 🗑️ **Data Erase Option** - Secure data wiping capabilities
- 📊 **Real-Time Logging** - Comprehensive output logs for debugging
- 🎨 **Dark Theme UI** - Eye-friendly dark mode interface

---

## 🛠️ Prerequisites

- Linux Operating System (Ubuntu/Debian/Fedora recommended)
- Python 3.6 or higher
- PyQt5 library
- Root privileges (sudo access)
- Samsung device in Download Mode

## ✅ Tested On

- Ubuntu Desktop (Fully tested and compatible)

---

## 📦 Installation

### Clone the Repository
```bash
git clone https://github.com/mafiadan6/Odin5-Flash-Tool.git
cd Odin5-Flash-Tool
```

### Install Dependencies
```bash
# For Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3 python3-pip

# For Fedora/RHEL
sudo dnf install python3 python3-pip

# Install Python dependencies from requirements.txt
pip3 install -r requirements.txt
```

---

## 🚀 Quick Start

### Method 1: Using the Start Script
```bash
chmod +x start_odin5.sh
./start_odin5.sh
```

### Method 2: Direct Execution
```bash
chmod +x odin5
chmod +x odin5_gui.py
sudo python3 odin5_gui.py
```

### Method 3: Using the Run Script
```bash
chmod +x run_odin5.sh
./run_odin5.sh
```

---

## 📋 Usage Guide

### 1. Prepare Your Device
- Power off your Samsung device
- Enter Download Mode: Press **Volume Down + Home + Power** simultaneously
- Connect the device to your computer via USB

### 2. Launch the Tool
- Run the GUI using one of the methods above
- The tool will automatically detect your connected device

### 3. Select Firmware Files
- **BL**: Bootloader file (.tar format)
- **AP**: Application/PDA file (.tar format)
- **CP**: Modem/Communication Processor file (.tar format)
- **CSC**: Consumer Software Customization file (.tar format)
- **USERDATA**: User data partition (optional)

### 4. Configure Options
- **Auto Reboot**: Enable automatic reboot after flashing
- **Erase Data**: Wipe all data during flashing (⚠️ Irreversible!)
- **T-Flash Mode**: Enable faster flashing speeds

### 5. Start Flashing
- Click the **🔥 START FLASH** button
- Monitor the progress in the output log
- Wait for the completion message

---

## ⚙️ Supported Partitions

| Partition | Flag | Description |
|-----------|------|-------------|
| **Bootloader (BL)** | `-b` | Device bootloader firmware |
| **Application (AP)** | `-a` | Android OS and system files |
| **Communication (CP)** | `-c` | Modem and radio firmware |
| **CSC (Customization)** | `-s` | Regional carrier settings |
| **User Data** | `-u` | Factory reset and data partition |

---

## 🛡️ Safety Features

- 🔒 **Permission Checks** - Ensures proper root access
- ⚠️ **File Validation** - Verifies firmware file integrity
- 🛑 **Safety Warnings** - Alerts for potentially dangerous operations
- 📉 **Progress Monitoring** - Real-time flash progress tracking
- 🚨 **Error Handling** - Graceful error recovery and reporting

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🐛 Bug Reports & Feature Requests

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/mafiadan6/Odin5-Flash-Tool/issues) with detailed information about:

- Your Linux distribution and version
- Python version
- Device model and firmware
- Steps to reproduce the issue
- Expected vs actual behavior

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Special thanks to the open-source community for PyQt5
- Inspired by the original Odin tool for Samsung devices
- Created with ❤️ by **爪卂丂ㄒ乇尺爪工刀ᗪ**

---

## ⚠️ Disclaimer

> **⚠️ WARNING**: This tool is designed for advanced users. Improper use may brick your device or void warranty. Always backup your data before flashing. The author is not responsible for any damage caused by misuse of this tool.

---

<div align="center">

**Made with 💻 by [mafiadan6](https://github.com/mafiadan6)**
  
⭐ Star this repo if it helped you!

</div>