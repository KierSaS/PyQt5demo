import sys
from PyQt5.QtWidgets import QApplication,QWidget
if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    #尺寸
    w.resize(300,150)
    w.move(300,300)
    w.setWindowTitle('一个基于普通的Pyqt5界面应用')
    w.show()

    #通过exit安全结束
    sys.exit(app.exec_())

    #嵌入UI文件，
    #python -m PyQt5.uic.pyuic XXX.ui -o demo.py