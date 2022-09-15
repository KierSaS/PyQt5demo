import sys#必须导入的
from PyQt5.QtWidgets import QApplication, QMainWindow#必须
import VHlayout

if __name__ == '__main__':
    app =QApplication(sys.argv)
    mainwindow = QMainWindow() #创建这个主窗口,每次的第一步
    ui = VHlayout.Ui_MainWindow() #创建主窗口之后，就创建由设计器生成的类，
    ui.setupUi(mainwindow) #调用类里面的方法.setupUi,而这个方法需要额外传入一个量，这个量是主窗口，指的是需要向哪一个主窗口上添加控件
    mainwindow.show()
    sys.exit(app.exec_())