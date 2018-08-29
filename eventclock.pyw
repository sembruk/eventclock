#!/usr/bin/env python3

import sys
from PyQt5.QtCore import Qt, QTimer, QTime
#from PyQt5.QtGui import QApplication
from PyQt5.QtWidgets import QApplication, QLabel

class MainWindow(QLabel):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setStyleSheet("MainWindow { background: white; };")
        self.setWindowTitle("EventClock")
        self.setAlignment(Qt.AlignCenter)

        font = self.font()
        font.setBold(True)
        self.setFont(font)
 
        self.timer = QTimer();

        self.timer.timeout.connect(self.updateTime);

        self.timer.start(500)
        self.updateTime()

    def updateTime(self):
        str = QTime.currentTime().toString();
        self.setText(str)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            if (self.windowState() == Qt.WindowFullScreen):
                self.showNormal();
            else:
                self.showFullScreen();

    def resizeEvent(self, event):
        text = self.text()
        h = 0
        w = 0
        while w < self.width() - 20: 
            h += 5
            font = self.font()
            font.setPixelSize(h)
            self.setFont(font)
            fm = self.fontMetrics()
            w = fm.width(text)

def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())

