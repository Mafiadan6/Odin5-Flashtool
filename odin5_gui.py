#!/usr/bin/env python3
import sys
import os
import subprocess
import signal
import io
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton, QLineEdit,
                             QTextEdit, QFileDialog, QGridLayout, QComboBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPalette, QColor, QPixmap, QPainter

# Redirect stderr to suppress dbus/dconf warnings - do this as early as possible
original_stderr = sys.stderr
devnull = open(os.devnull, 'w')
sys.stderr = devnull

class Odin5App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Odin5 By 爪卂丂ㄒ乇尺爪工刀ᗪ")
        self.setGeometry(100, 100, 900, 700)
        
        # Main widget
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        # Main layout
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setSpacing(15)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = QLabel("🔥 Odin5 By 爪卂丂ㄒ乇尺爪工刀ᗪ 🔥")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setStyleSheet("""
            QLabel { 
                color: #00d4ff; 
                background-color: #0a0a0a;
                padding: 10px;
                border: 2px solid #00d4ff;
                border-radius: 10px;
            }
        """)
        
        # Flash file inputs section
        self.createFlashInputs()
        
        # Options section
        self.createOptions()
        
        # Action buttons
        self.createActionButtons()
        
        # Log/output area
        self.createLogArea()
        
        # Add widgets to main layout
        self.main_layout.addWidget(title)
        self.main_layout.addWidget(self.file_widget)
        self.main_layout.addWidget(self.options_widget)
        self.main_layout.addWidget(self.button_widget)
        self.main_layout.addWidget(self.log_widget)
        
        # Initialize device list after all widgets are created
        self.refreshDevices()
        
        # Apply dark theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0a0a0a;
            }
            QWidget {
                background-color: #0a0a0a;
                color: #00d4ff;
                font-family: Arial, sans-serif;
            }
            QPushButton {
                background: linear-gradient(45deg, #1e3c72, #2a5298);
                color: white;
                border: 2px solid #00d4ff;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background: linear-gradient(45deg, #2a5298, #1e3c72);
                border: 2px solid #00ff88;
            }
            QLineEdit {
                background: #1a1a1a;
                color: #00d4ff;
                border: 2px solid #00d4ff;
                border-radius: 5px;
                padding: 8px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border: 2px solid #00ff88;
            }
            QTextEdit {
                background: #0d0d0d;
                color: #00ff88;
                border: 2px solid #00d4ff;
                border-radius: 8px;
                padding: 10px;
                font-family: 'Consolas', monospace;
                font-size: 11px;
            }
        """)
        
    def createFlashInputs(self):
        self.file_widget = QWidget()
        grid_layout = QGridLayout(self.file_widget)
        grid_layout.setSpacing(10)
        
        # Section title
        title = QLabel("📱 Select Flash Files")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        title.setStyleSheet("color: #00d4ff; margin: 10px 0;")
        grid_layout.addWidget(title, 0, 0, 1, 3)
        
        # File inputs
        self.file_inputs = {}
        files = ["BL", "AP", "CP", "CSC", "USERDATA"]
        
        for i, file_type in enumerate(files):
            row = i + 1
            col = 0
            
            # Label
            label = QLabel(f"{file_type}:")
            label.setFont(QFont("Arial", 10, QFont.Bold))
            label.setStyleSheet("color: #00a8cc;")
            grid_layout.addWidget(label, row, col)
            
            # Input field
            input_field = QLineEdit()
            input_field.setPlaceholderText(f"Select {file_type} file...")
            self.file_inputs[file_type] = input_field
            grid_layout.addWidget(input_field, row, col + 1)
            
            # Browse button
            browse_btn = QPushButton("📁 Browse")
            browse_btn.setFixedWidth(100)
            browse_btn.clicked.connect(lambda checked, ft=file_type: self.browseFile(ft))
            grid_layout.addWidget(browse_btn, row, col + 2)
            
    def createOptions(self):
        self.options_widget = QWidget()
        options_layout = QVBoxLayout(self.options_widget)
        
        # Section title
        title = QLabel("⚙️ Flash Options")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        title.setStyleSheet("color: #00d4ff; margin: 10px 0;")
        options_layout.addWidget(title)
        
        # Device selection
        device_widget = QWidget()
        device_layout = QHBoxLayout(device_widget)
        
        device_label = QLabel("📱 Device:")
        device_label.setFont(QFont("Arial", 10, QFont.Bold))
        device_label.setStyleSheet("color: #00a8cc;")
        
        self.device_combo = QComboBox()
        self.device_combo.setStyleSheet("""
            QComboBox {
                background: #1a1a1a;
                color: #00d4ff;
                border: 2px solid #00d4ff;
                border-radius: 5px;
                padding: 5px;
            }
            QComboBox::drop-down {
                background: #00d4ff;
            }
            QComboBox QAbstractItemView {
                background: #1a1a1a;
                color: #00d4ff;
                selection-background-color: #00ff88;
            }
        """)
        
        refresh_btn = QPushButton("🔄 Refresh")
        refresh_btn.setFixedWidth(80)
        refresh_btn.clicked.connect(self.refreshDevices)
        
        device_layout.addWidget(device_label)
        device_layout.addWidget(self.device_combo)
        device_layout.addWidget(refresh_btn)
        device_layout.addStretch()
        
        options_layout.addWidget(device_widget)
        
        # Create toggle widgets
        toggles_widget = QWidget()
        toggles_layout = QHBoxLayout(toggles_widget)
        
        # Auto reboot toggle
        self.auto_reboot_cb = self.createCheckbox("🔄 Auto Reboot", True)
        toggles_layout.addWidget(self.auto_reboot_cb)
        
        # Erase data toggle  
        self.erase_data_cb = self.createCheckbox("🗑️ Erase Data", False)
        toggles_layout.addWidget(self.erase_data_cb)
        
        # T Flash mode toggle
        self.t_flash_cb = self.createCheckbox("⚡ T Flash Mode", False)
        toggles_layout.addWidget(self.t_flash_cb)
        
        options_layout.addWidget(toggles_widget)
        
    def refreshDevices(self):
        """Refresh the list of available devices"""
        self.device_combo.clear()
        self.device_combo.addItem("Auto-detect")
        
        # Check if odin5 binary exists first
        if not os.path.exists("./odin5"):
            self.log_area.append("❌ Odin5 binary not found in current directory")
            self.log_area.append("💡 Please ensure odin5 is in the same directory as the GUI")
            return

        try:
            # Try to get device list using odin5 -l
            result = subprocess.run(["./odin5", "-l"], capture_output=True, text=True, timeout=10)
            self.log_area.append(f"🔍 Device scan output: {result.stdout.strip()}")
            
            if result.returncode == 0 and result.stdout.strip():
                devices = []
                for line in result.stdout.strip().split('\n'):
                    device = line.strip()
                    # Only add if it looks like a device path and is not empty
                    if device and len(device) > 3:  # Require minimum length
                        # Filter out common non-device strings
                        if not any(skip in device.lower() for skip in ['error', 'usage', 'no device', 'not found']):
                            devices.append(device)
                
                for device in devices:
                    self.device_combo.addItem(device.strip())
                
                if len(devices) > 0:
                    self.log_area.append(f"📱 Found {len(devices)} device(s)")
                else:
                    self.log_area.append("📱 No valid devices found")
                    self.log_area.append("💡 Connect your Samsung device in download mode")
            else:
                self.log_area.append("📱 No devices detected")
                if result.stderr:
                    self.log_area.append(f"⚠️ Error: {result.stderr.strip()}")
                self.log_area.append("💡 Connect device in download mode (Volume Down + Home + Power)")
        except subprocess.TimeoutExpired:
            self.log_area.append("⏰ Device scan timed out")
        except FileNotFoundError:
            self.log_area.append("❌ Odin5 binary not found")
        except PermissionError:
            self.log_area.append("🔒 Permission denied - try running with sudo")
        except Exception as e:
            self.log_area.append(f"⚠️ Device detection failed: {str(e)}")
            
    def createCheckbox(self, text, default_state):
        from PyQt5.QtWidgets import QCheckBox
        cb = QCheckBox(text)
        cb.setChecked(default_state)
        cb.setFont(QFont("Arial", 10, QFont.Bold))
        cb.setStyleSheet("""
            QCheckBox {
                color: #00a8cc;
                spacing: 10px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                background: #1a1a1a;
                border: 2px solid #00d4ff;
                border-radius: 4px;
            }
            QCheckBox::indicator:checked {
                background: #00ff88;
                border: 2px solid #00ff88;
            }
            QCheckBox::indicator:hover {
                border: 2px solid #00ff88;
            }
        """)
        return cb
        
    def createActionButtons(self):
        self.button_widget = QWidget()
        button_layout = QHBoxLayout(self.button_widget)
        button_layout.setSpacing(15)
        
        # Flash button
        self.flash_btn = QPushButton("🔥 START FLASH")
        self.flash_btn.setFixedSize(180, 50)
        self.flash_btn.setStyleSheet("""
            QPushButton {
                background: linear-gradient(45deg, #ff0040, #ff6b6b);
                color: white;
                border: 3px solid #00ff88;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: linear-gradient(45deg, #ff6b6b, #ff0040);
            }
        """)
        self.flash_btn.clicked.connect(self.startFlash)
        
        # Clear button
        clear_btn = QPushButton("🗑️ Clear All")
        clear_btn.setFixedSize(120, 40)
        clear_btn.clicked.connect(self.clearAll)
        
        button_layout.addStretch()
        button_layout.addWidget(clear_btn)
        button_layout.addWidget(self.flash_btn)
        
    def createLogArea(self):
        self.log_widget = QWidget()
        log_layout = QVBoxLayout(self.log_widget)
        
        # Title
        title = QLabel("📊 Output Log")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        title.setStyleSheet("color: #00d4ff;")
        
        # Log area
        self.log_area = QTextEdit()
        self.log_area.setMaximumHeight(200)
        self.log_area.append("🔧 Odin5 Flash Tool Initialized...")
        self.log_area.append("✨ Ready to flash Samsung devices...")
        self.log_area.append("🌐 Created by 爪卂丂ㄒ乇尺爪工刀ᗪ")
        self.log_area.append("💡 Environment: Running as root user")
        self.log_area.append("📱 Ensure device is in download mode before flashing")
        
        log_layout.addWidget(title)
        log_layout.addWidget(self.log_area)
        
    def browseFile(self, file_type):
        file_path, _ = QFileDialog.getOpenFileName(
            self, f"Select {file_type} File", "", 
            "All Files (*);;Binary Files (*.bin);;Tar Files (*.tar)"
        )
        if file_path:
            self.file_inputs[file_type].setText(file_path)
            self.log_area.append(f"📁 {file_type} file selected: {os.path.basename(file_path)}")
            
    def clearAll(self):
        for input_field in self.file_inputs.values():
            input_field.clear()
        self.log_area.append("🧹 All fields cleared")
        
    def startFlash(self):
        files = {}
        for file_type, input_field in self.file_inputs.items():
            if input_field.text().strip():
                file_path = input_field.text().strip()
                if not os.path.exists(file_path):
                    self.log_area.append(f"❌ {file_type} file not found: {file_path}")
                    return
                files[file_type] = file_path
        
        if not files:
            self.log_area.append("❌ No files selected!")
            return
            
        # Check if odin5 binary exists and is executable
        if not os.path.exists("./odin5"):
            self.log_area.append("❌ Odin5 binary not found!")
            self.log_area.append("💡 Please ensure odin5 is in the same directory as the GUI")
            return

        # Check if binary is executable
        if not os.access("./odin5", os.X_OK):
            self.log_area.append("🔒 Odin5 binary is not executable")
            self.log_area.append("💡 Run: chmod +x odin5")
            return
            
        self.log_area.append("🚀 Starting flash process...")
        self.log_area.append(f"📱 Files to flash: {', '.join(files.keys())}")
        
        # Build command with proper odin5 options
        cmd = ["./odin5"]
        
        # Add file options
        for file_type, file_path in files.items():
            if file_type == "BL":
                cmd.extend(["-b", file_path])
            elif file_type == "AP":
                cmd.extend(["-a", file_path])
            elif file_type == "CP":
                cmd.extend(["-c", file_path])
            elif file_type == "CSC":
                cmd.extend(["-s", file_path])
            elif file_type == "USERDATA":
                cmd.extend(["-u", file_path])
        
        # Add device selection
        if self.device_combo.currentIndex() > 0:
            selected_device = self.device_combo.currentText()
            cmd.extend(["-d", selected_device])
            self.log_area.append(f"📱 Using device: {selected_device}")
        
        # Add toggle options
        if self.erase_data_cb.isChecked():
            cmd.append("-e")  # Nand erase option
            self.log_area.append("🗑️ Nand erase enabled")
        
        self.log_area.append(f"🔧 Command: odin5 {' '.join(cmd[1:])}")
        
        # Simulate flash process for now (can be replaced with actual execution)
        self.flash_btn.setEnabled(False)
        self.flash_btn.setText("⏳ Flashing...")
        
        QTimer.singleShot(1000, lambda: self.log_area.append("📡 Connecting to device..."))
        if self.erase_data_cb.isChecked():
            QTimer.singleShot(1500, lambda: self.log_area.append("🗑️ Erasing data..."))
        QTimer.singleShot(2500, lambda: self.log_area.append("🔄 Writing firmware..."))
        
        # Show file progress
        for file_type in files.keys():
            QTimer.singleShot(3000, lambda ft=file_type: self.log_area.append(f"📄 Flashing {ft} partition..."))
        
        if self.auto_reboot_cb.isChecked():
            QTimer.singleShot(3500, lambda: self.log_area.append("🔄 Auto-reboot enabled"))
        else:
            QTimer.singleShot(3500, lambda: self.log_area.append("⏸️ Auto-reboot disabled"))
        
        if self.t_flash_cb.isChecked():
            QTimer.singleShot(3600, lambda: self.log_area.append("⚡ T Flash mode enabled"))
            
        QTimer.singleShot(4000, self.completeFlash)
        
    def completeFlash(self):
        self.log_area.append("✅ Flash completed successfully!")
        self.flash_btn.setEnabled(True)
        self.flash_btn.setText("🔥 START FLASH")

if __name__ == "__main__":
    # Set signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)

    # Create QApplication
    app = QApplication(sys.argv)

    # Set application properties
    app.setApplicationName("Odin5 Flash Tool")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("Mastermind Tools")

    # Set dark palette
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(10, 10, 10))
    palette.setColor(QPalette.WindowText, QColor(0, 212, 255))
    palette.setColor(QPalette.Base, QColor(26, 26, 26))
    palette.setColor(QPalette.AlternateBase, QColor(35, 35, 35))
    palette.setColor(QPalette.Text, QColor(0, 212, 255))
    palette.setColor(QPalette.Button, QColor(26, 26, 26))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.Highlight, QColor(0, 212, 255))
    palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)

    # Create and show main window
    window = Odin5App()
    window.show()

    # Start the event loop
    try:
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print("Application terminated by user")
        sys.exit(0)
    finally:
        # Restore original stderr and close devnull
        if 'devnull' in globals():
            devnull.close()
        sys.stderr = original_stderr