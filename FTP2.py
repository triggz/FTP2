import logging
import os
import sys
from ftplib import FTP
from ftputil import FTPHost
from pathlib import Path
from threading import Thread
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog
from main_form import Ui_MainWindow

class MainForm(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':

    # Logging

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s','%c')
    console_handler.setFormatter(log_formatter)
    log.addHandler(console_handler)

    # Start the Aplication
    app = QApplication(sys.argv)
    # Create the main form
    form = MainForm()
    # Show the main form
    form.show()

    app.exec_()
