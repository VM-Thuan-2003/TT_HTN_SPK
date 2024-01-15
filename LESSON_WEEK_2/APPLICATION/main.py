import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class MyApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create widgets
        label = QLabel('Hello, PyQt!')
        button = QPushButton('Click me!')

        # Connect button click event to a function
        button.clicked.connect(self.onButtonClick)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('My PyQt Application')

    def onButtonClick(self):
        # Function to handle button click
        print('Button clicked!')

if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MyApplication()
    window.show()

    # Run the application event loop
    sys.exit(app.exec_())
