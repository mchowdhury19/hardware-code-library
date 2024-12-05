import sys
import json
from PyQt5.QtWidgets import QApplication as qa, QDialog as qd, QVBoxLayout as qvb, QLabel as ql, QLineEdit as qline, QPushButton as qpb, QMessageBox as qmsg

class SettingsDialog(qd):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings/Path Director")
        self.setGeometry(100, 100, 400, 200)

        self.layout = qvb(self)

        self.config_path_label = ql("Config Path:", self)
        self.config_path_input = qline(self)

        self.logs_path_label = ql("Logs Path:", self)
        self.logs_path_input = qline(self)

        self.layout.addWidget(self.config_path_label)
        self.layout.addWidget(self.config_path_input)
        self.layout.addWidget(self.logs_path_label)
        self.layout.addWidget(self.logs_path_input)
        self.font_size_label = ql("Test Table Font Size:", self)
        self.font_size_input = qline(self)
        
        self.layout.addWidget(self.config_path_label)
        self.layout.addWidget(self.config_path_input)
        
        self.layout.addWidget(self.logs_path_label)
        self.layout.addWidget(self.logs_path_input)
        
        self.layout.addWidget(self.font_size_label)
        self.layout.addWidget(self.font_size_input)
        
        self.save_button = qpb("Save", self)
        self.save_button.clicked.connect(self.save_to_file)
        self.layout.addWidget(self.save_button)
    
    def save_to_file(self):
        config_path = self.config_path_input.text()
        logs_path = self.logs_path_input.text()
        try:
            font_size = int(self.font_size_input.text())
        except ValueError:
            qmsg.critical(self, "Error", "Font size must be an integer.")
            return

        data = {
            "configs path": config_path,
            "logs path": logs_path,
            "test table font size": font_size
        }
        """
        with open("settings.json", "w") as f:
          # steve = 
           f = open("settings.json","w")
           f.write(json.dumps(data,indent=4))"""
        
        with open("settings.json","w") as f:
            json.dump(data,f,indent=4)
        
        qmsg.information(self, "Success", "Settings saved to settings.json.")

# Main app
if __name__ == "__main__":
    app = qa(sys.argv)
    dialog = SettingsDialog()
    dialog.exec_()
