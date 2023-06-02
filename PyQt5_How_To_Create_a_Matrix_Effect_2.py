import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QGridLayout, QLabel
from PyQt5.QtCore import QTimer, Qt
from random import randint, choice
from string import ascii_letters, digits


class MatrixRain(QWidget):
    def __init__(self):
        super().__init__()

        self.chars = ascii_letters + digits
        self.column_count = 30  # number of character columns
        self.row_count = 20  # number of characters in a row
        self.grid_layout = None
        self.columns = []
        self.timers = []

        self.initUI()

    def initUI(self):
        # Set up the window.
        self.setGeometry(300, 300, 650, 450)
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle("Matrix Effect")

        # Create layout to hold character columns.
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        # Create character grid.
        for col in range(self.column_count):
            column = []
            for row in range(self.row_count):
                label = QLabel(self)
                # Each character in a column has a darker color than its predecessor
                label.setStyleSheet(f"color: rgba(0, 255, 0, "
                                    f"{1 - row/self.row_count}); font-size: 20px;")
                label.setAlignment(Qt.AlignCenter)
                self.grid_layout.addWidget(label, row, col)
                column.append(label)
            self.columns.append(column)

        # Set up timers to update columns.
        self.timers = [QTimer() for _ in range(self.column_count)]
        for i, timer in enumerate(self.timers):
            timer.timeout.connect(self.create_updater(i))
            timer.start(randint(100, 200))  # random start times

    def create_updater(self, index):
        def update_column():
            column = self.columns[index]
            # Move all characters down the column.
            for i in reversed(range(1, self.row_count)):
                column[i].setText(column[i - 1].text())
            # Insert new random character at the top.
            column[0].setText(choice(self.chars))
        return update_column


if __name__ == '__main__':
    app = QApplication(sys.argv)
    matrix = MatrixRain()
    matrix.show()
    sys.exit(app.exec_())
