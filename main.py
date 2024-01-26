import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QLabel, QLineEdit


class Main:

    def __init__(self):
        self.initUI()
    def initUI(self):
        terminal = QLabel("Terminal")
        term_input = QLineEdit()
        apply_button = QPushButton("Apply")

        apply_button.clicked.connect(self.applyChanges)

        layout = QGridLayout()
        layout.addWidget(terminal,0 ,0)
        layout.addWidget(term_input,1 ,0)
        layout.addWidget(apply_button,2 ,0)

        MainWidget.setLayout(layout)
        
    def applyChanges(self):
        print('Apply Button CLicked')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWidget = QWidget()
    main_app = Main()
    main_app.initUI()
    MainWidget.show()
    sys.exit (app.exec())
