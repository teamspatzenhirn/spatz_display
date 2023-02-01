import docker

from PySide6 import QtCore
from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QWidget,
    QGridLayout,
    QPushButton,
    QPlainTextEdit
)

from setup_logger import logging
import time

class DockerTab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        #super(ViewController, self).__init__()

        self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')

        app = self.parent().app
        self.disp_width = app.primaryScreen().size().width()
        self.disp_height = app.primaryScreen().size().height()
        btn_size = self.disp_width / 5

        Gridlayout = QGridLayout()

        button_start_ade = QPushButton("Start ADE")
        button_start_ade.clicked.connect(self.start_ade)
        button_start_ade.setFixedSize(btn_size, btn_size)

        button_start_ros = QPushButton("Start ROS")
        button_start_ros.clicked.connect(self.start_ros)
        button_start_ros.setFixedSize(btn_size, btn_size)

        #layout = QVBoxLayout()
        #layout.setAlignment(QtCore.Qt.AlignCenter)
        #version = QLabel(f"Docker Version: {self.getDockerVersion()}")
        #version.setAlignment(QtCore.Qt.AlignCenter)
        #layout.addWidget(version)

        self.terminal = QPlainTextEdit()
        self.terminal.setReadOnly(True)

        self.inputpipe = QtCore.QProcess()
        self.outputpipe = QtCore.QProcess()
        self.outputpipe.readyReadStandardOutput.connect(self.handle_stdout)
        self.outputpipe.readyReadStandardError.connect(self.handle_stderr)
        self.outputpipe.start("tail", ["-f", "/mnt/outputpipe"])


        self.dockerRunning = QWidget()
        self.dockerRunning.setUpdatesEnabled(True)

        Gridlayout.addWidget(button_start_ade, 0, 0)
        Gridlayout.addWidget(button_start_ros, 1, 0)
        #Gridlayout.addLayout(layout, 0, 1)
        Gridlayout.addWidget(self.dockerRunning, 0, 1)
        Gridlayout.addWidget(self.terminal, 1, 1)

        self.setLayout(Gridlayout)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timer_test)
        self.timer.start()


    def timer_test(self):
        logging.info("Timer!")
        self.getDockerRunning()
        self.DockerLayout.update()
        self.test2.setText(str(time.time()))


    def getDockerRunning(self):
        self.DockerLayout = QGridLayout()

        self.test2 = QLabel("Test")
        self.DockerLayout.addWidget(self.test2, 0, 3)

        for index, entry in enumerate(["ID", "name", "status"]):
            label = QLabel(entry)
            #label.setAlignment(QtCore.Qt.AlignRight)
            self.DockerLayout.addWidget(label, 0, index)

        for index, container in enumerate(self.client.containers.list()):
            container_id = self.client.containers.get(container.id)
            label_name = QLabel()
            label_name.setText(f"{container_id.name}")
            logging.info(container_id.name)
            #label_name.setAlignment(QtCore.Qt.AlignLeft)
            label_id = QLabel()
            label_id.setText(f"{container_id.short_id}")
            #label_id.setAlignment(QtCore.Qt.AlignRight)
            label_status = QLabel()
            label_status.setText(f"{container_id.status}")
            self.DockerLayout.addWidget(label_id, index + 1, 0)
            self.DockerLayout.addWidget(label_name, index + 1, 1)
            self.DockerLayout.addWidget(label_status, index + 1, 2)

        self.dockerRunning.setLayout(self.DockerLayout)

        logging.info("docker running")

    def getDockerVersion(self):
        version = self.client.version()['Components'][0]['Version']
        logging.info(f"Docker Server version: {version}")
        return version

    def start_ade(self):
        logging.info("Starting ADE (maybe)...")
        self.terminal.clear()
        self.inputpipe.startDetached("/bin/bash", ["-c", "echo 'cd ~/ade-home/2021 && ade start' > /mnt/inputpipe"])
        #self.update()


    def start_ros(self):
        logging.info("Starting ROS (maybe)...")
        for container in self.client.containers.list():
            ade_container = self.client.containers.get(container.id)
            if(ade_container.name == "ade"):
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