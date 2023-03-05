# This Python file uses the following encoding: utf-8
import sys
from YouTubeVideoDownloader import YouTubeVideoDownloader
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from PySide6.QtCore import Qt

class Widget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(300, 220)
        self.setWindowTitle('Video Downloader')

        self.url_lineEdit = QLineEdit(self)
        self.url_lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.url_lineEdit.setAlignment(Qt.AlignCenter)
        self.url_lineEdit.setPlaceholderText("Paste a link")

        self.button = QPushButton("Download")
        self.button.clicked.connect(self.on_button_click)

        vertical_layout = QVBoxLayout(self)
        vertical_layout.addWidget(self.url_lineEdit)
        vertical_layout.addWidget(self.button)

    def on_button_click(self):
        self.button.setEnabled(False)
        self.url_lineEdit.setEnabled(False)

        path = QFileDialog.getExistingDirectory(self)
        if  path != "":
            yt = YouTubeVideoDownloader()
            yt.download(self.url_lineEdit.text(), path)

        self.button.setEnabled(True)
        self.url_lineEdit.setEnabled(True)

        QMessageBox.about(self, "Download info", "Download finished succesfully")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
