import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 320, 300)
        self.setWindowTitle('Крестики-нолики')

        self.result = QLabel(self)
        self.result.resize(100, 100)
        self.result.move(130, 210)

        self.new_game_button = QPushButton('Новая Игра', self)
        self.new_game_button.resize(80, 20)
        self.new_game_button.move(110, 270)
        self.new_game_button.clicked.connect(self.new)

        self.x_radio = QRadioButton('X', self)
        self.x_radio.setChecked(True)
        self.x_radio.move(120, 20)
        self.x_radio.clicked.connect(self.radio)

        self.o_radio = QRadioButton('O', self)
        self.o_radio.move(160, 20)
        self.o_radio.clicked.connect(self.radio)

        self.button_grid = self.buttons()

        self.count = 0

    def pole(self):
        sender = self.sender()
        if self.result.text() != '':
            self.new()
        self.radio
        if sender.text() == '' and not self.win()[0]:
            if self.count % 2 == 0:
                sender.setText('X')
            else:
                sender.setText('O')
            self.count += 1
        a = self.win()
        if a[0]:
            self.result.setText(f'Выиграл {a[1]}!')
        if not a[0] and self.end():
            self.result.setText('Ничья!')

    def new(self):
        '''self.x.setChecked(True)
        self.o.setChecked(False)'''
        for elem in self.button_grid:
            for e in elem:
                e.setText('')
        self.result.clear()
        if self.x_radio.isChecked():
            self.count = 0
        else:
            self.count = 1

    def radio(self):
        sender = self.sender()
        if sender == self.o_radio and self.start():
            self.count = 1
        else:
            self.count = 0
        self.new()

    def start(self):
        for elem in self.button_grid:
            for i in range(3):
                if elem[i].text() != '':
                    return False
        return True

    def end(self):
        for elem in self.button_grid:
            for i in range(3):
                if elem[i].text() == '':
                    return False
        return True

    def win(self):
        for s in range(3):
            a = self.button_grid[0][s].text()
            b = self.button_grid[1][s].text()
            if a == b and b == self.button_grid[2][s].text() and self.button_grid[2][s].text() != '':
                return [True, self.button_grid[0][s].text()]
            c = self.button_grid[s][0].text()
            d = self.button_grid[s][1].text()
            if c == d and d == self.button_grid[s][2].text() and self.button_grid[s][2].text() != '':
                return [True, self.button_grid[s][0].text()]
        e = self.button_grid[0][2].text()
        f = self.button_grid[1][1].text()
        g = self.button_grid[2][0].text()
        if (e == f == g or self.button_grid[0][0].text() == f == self.button_grid[2][2].text()) and f != '':
            return [True, self.button_grid[1][1].text()]
        return [False, '-']

    def buttons(self):
        al = []
        x = 50
        y = 50
        for i in range(3):
            s = []
            for j in range(3):
                cell = 'cell_' + str(i) + str(j)
                self.p(cell)
                self.cell = QPushButton(self)
                self.cell.resize(60, 60)
                self.cell.move(x, y)
                self.cell.clicked.connect(self.pole)
                s.append(self.cell)
                x += 70
            y += 70
            x = 50
            al.append(s)
        return al

    def p(self, s):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToe()
    ex.show()
    sys.exit(app.exec())