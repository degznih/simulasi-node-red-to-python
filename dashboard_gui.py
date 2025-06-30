from PyQt5 import QtWidgets, QtCore
import sys
import random

class SensorDashboard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulasi Dashboard Sensor - Dega")
        self.resize(600, 400)

        layout = QtWidgets.QGridLayout()
        self.labels = {}
        sensors = [
            "Irradiance (W/m2)",
            "Voltage (V)",
            "Current (A)",
            "Active Power (W)",
            "Frequency (Hz)",
            "Power Factor",
            "Total Energy (kWh)"
        ]

        for i, sensor in enumerate(sensors):
            name_label = QtWidgets.QLabel(sensor)
            value_label = QtWidgets.QLabel("0")
            value_label.setStyleSheet("font-size: 20px; color: green;")
            self.labels[sensor] = value_label
            layout.addWidget(name_label, i // 2, (i % 2) * 2)
            layout.addWidget(value_label, i // 2, (i % 2) * 2 + 1)

        self.setLayout(layout)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_values)
        self.timer.start(5000)

    def update_values(self):
        data = {
            "Irradiance (W/m2)": round(random.uniform(600, 800), 2),
            "Voltage (V)": round(random.uniform(220, 230), 2),
            "Current (A)": round(random.uniform(1, 2), 3),
            "Active Power (W)": round(random.uniform(300, 400), 1),
            "Frequency (Hz)": round(random.uniform(49.9, 50.1), 2),
            "Power Factor": round(random.uniform(0.85, 0.95), 2),
            "Total Energy (kWh)": round(random.uniform(5000, 6000), 1)
        }

        for key in data:
            self.labels[key].setText(str(data[key]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dashboard = SensorDashboard()
    dashboard.show()
    sys.exit(app.exec_())
