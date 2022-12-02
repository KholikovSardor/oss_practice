Sardor Kholikov, [12/2/2022 8:06 PM]
import math
import sys
from PyQt5.QtWidgets import *

class Main(QDialog):

    def init(self):
        super().init()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        layout_button = QGridLayout()
        layout_equation_solution = QFormLayout()
        self.equation_solution = QLineEdit('')
        self.equation_solution.setPlaceholderText('0')
        layout_equation_solution.addRow(self.equation_solution)

        button_add = QPushButton("+")
        button_sub = QPushButton("-")
        button_mult = QPushButton("x")
        button_div = QPushButton("/")
        button_equal = QPushButton("=")
        button_backspace = QPushButton("del")
        button_modulo = QPushButton("%")
        button_clear_entry = QPushButton("CE")
        button_clear = QPushButton("C")
        button_reciprocal = QPushButton("1/x")
        button_square = QPushButton("x²")
        button_root_square = QPushButton("√x")
        button_dot = QPushButton(".")
        button_inverse = QPushButton("+/-")

        button_add.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_sub.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_mult.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_div.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        button_modulo.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        button_inverse.clicked.connect(lambda state, num = "+/-": self.number_button_clicked(num))
        button_equal.clicked.connect(self.button_equal_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)        
        button_clear_entry.clicked.connect(self.button_clear_entry_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_reciprocal.clicked.connect(self.button_reciprocal_clicked)
        button_square.clicked.connect(self.button_square_clicked)
        button_root_square.clicked.connect(self.button_root_square_clicked)
        

        layout_button.addWidget(button_add, 4, 3)
        layout_button.addWidget(button_sub,3, 3)
        layout_button.addWidget(button_mult, 2, 3)
        layout_button.addWidget(button_div, 1, 3)
        layout_button.addWidget(button_backspace, 0, 3)
        layout_button.addWidget(button_equal, 5, 3)
        layout_button.addWidget(button_modulo, 0, 0)
        layout_button.addWidget(button_clear_entry, 0, 1)
        layout_button.addWidget(button_clear, 0, 2)
        layout_button.addWidget(button_reciprocal, 1, 0)
        layout_button.addWidget(button_square, 1, 1)
        layout_button.addWidget(button_root_square, 1, 2)
        layout_button.addWidget(button_dot, 5, 2)
        layout_button.addWidget(button_inverse, 5, 0)
        
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number > 0:
                x,y = divmod(number-1, 3)
                layout_button.addWidget(number_button_dict[number], x+2 , y)
            elif number==0:
                layout_button.addWidget(number_button_dict[number], 5, 1)
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_button)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    
    def number_button_clicked(self, num):
        equation = self.equation_solution.text()
        equation += str(num)
        self.equation_solution.setText(equation)

Sardor Kholikov, [12/2/2022 8:06 PM]
def button_operation_clicked(self, operation):
        equation = self.equation_solution.text()
        equation += operation
        self.equation_solution.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation_solution.text()
        solution = eval(equation)
        self.equation_solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation_solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation_solution.text()
        equation = equation[:-1]
        self.equation_solution.setText(equation)
    
    def button_clear_entry_clicked(self):
        self.equation_solution.setText("")

    def button_reciprocal_clicked(self,num):
        equation=self.equation_solution.text()
        equation = str(float(equation)*-1)
        self.equation_solution.setText(equation)
    
    def button_square_clicked(self):
        equation = self.equation_solution.text()
        equation = float(equation)
        equation = equation ** 2
        equation = str(equation)
        self.equation_solution.setText(equation)

    def button_root_square_clicked(self):
        equation = self.equation_solution.text()
        equation = float(equation)
        equation = equation**0.5
        equation = str(equation)
        self.equation_solution.setText(equation)
        
if name == 'main':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())