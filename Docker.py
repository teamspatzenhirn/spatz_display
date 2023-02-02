import docker

from PySide6 import QtCore
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QGridLayout,
    QPushButton,
    QPlainTextEdit
)

from setup_logger import logging

class DockerTab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')

        app = self.parent().app
        self.disp_width = app.primaryScreen().size().width()
        self.disp_height = app.primaryScreen().size().height()
        btn_size = self.disp_width / 5

        gridlayout = QGridLayout()

        self.button_start_ade = QPushButton("Start ADE")
        self.button_start_ade.clicked.connect(self.start_ade)
        self.button_start_ade.setFixedSize(btn_size, btn_size)

        button_start_ros = QPushButton("Start ROS")
        button_start_ros.clicked.connect(self.start_ros)
        button_start_ros.setFixedSize(btn_size, btn_size)

        adeRunningStatus = QWidget()
        adeRunningStatusLayout = QGridLayout()
        for index, entry in enumerate(["ID", "name", "status"]):
            label = QLabel(entry)
            adeRunningStatusLayout.addWidget(label, 0, index)


        self.adeRunningStatusLabel_id = QLabel()
        self.adeRunningStatusLabel_name = QLabel()
        self.adeRunningStatusLabel_status = QLabel()
        adeRunningStatusLayout.addWidget(self.adeRunningStatusLabel_id, 1, 0)
        adeRunningStatusLayout.addWidget(self.adeRunningStatusLabel_name, 1, 1)
        adeRunningStatusLayout.addWidget(self.adeRunningStatusLabel_status, 1, 2)

        adeRunningStatus.setLayout(adeRunningStatusLayout)

        self.terminal = QPlainTextEdit()
        self.terminal.setReadOnly(True)

        self.inputpipe = QtCore.QProcess()
        self.outputpipe = QtCore.QProcess()
        self.outputpipe.readyReadStandardOutput.connect(self.handle_stdout)
        self.outputpipe.readyReadStandardError.connect(self.handle_stderr)
        self.outputpipe.start("tail", ["-f", "/mnt/outputpipe"])


        gridlayout.addWidget(self.button_start_ade, 0, 0)
        gridlayout.addWidget(button_start_ros, 1, 0)
        gridlayout.addWidget(adeRunningStatus, 0, 1)
        gridlayout.addWidget(self.terminal, 1, 1)

        self.setLayout(gridlayout)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start()


    def update_timer(self):
        self.updateStatus()


    def updateStatus(self):
        for container in self.client.containers.list():
            try:
                ade_container = self.client.containers.get(container.id)
                if ade_container.name == "ade":
                    self.adeRunningStatusLabel_id.setText(f"{container.short_id}")
                    self.adeRunningStatusLabel_name.setText(f"{container.name}")
                    self.adeRunningStatusLabel_status.setText(f"{container.status}")
                    self.button_start_ade.setDisabled(True)
                else:
                    self.adeRunningStatusLabel_status.setText(f"not running")
                    self.button_start_ade.setDisabled(False)
            except:
                self.adeRunningStatusLabel_status.setText(f"not running")
                self.button_start_ade.setDisabled(False)


    def getDockerVersion(self):
        version = self.client.version()['Components'][0]['Version']
        logging.info(f"Docker Server version: {version}")
        return version

    def start_ade(self):
        logging.info("Starting ADE (maybe)...")
        self.terminal.clear()
        self.inputpipe.startDetached("/bin/bash", ["-c", "echo 'cd ~/ade-home/2021 && ade start' > /mnt/inputpipe"])


    def start_ros(self):
        logging.info("Starting ROS (maybe)...")
        for container in self.client.containers.list():
            ade_container = self.client.containers.get(container.id)
            if ade_container.name == "ade":
                logging.info(f"Found Container {ade_container.name} with id {container.id}")
                launch_file = "freedrive_11_combined_perception.launch.py"
                _, stream = ade_container.exec_run(cmd=f"/opt/ros/humble/bin/ros2 launch teamspatzenhirn_launch {launch_file}", stream=True, workdir="/home/spatz/2021")
                for data in stream:
                    logging.info(data.decode())
                    self.terminal.appendPlainText(data.decode())

    def handle_stdout(self):
        data = self.outputpipe.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.terminal.appendPlainText(stdout)

    def handle_stderr(self):
        data = self.outputpipe.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.terminal.appendPlainText(stderr)