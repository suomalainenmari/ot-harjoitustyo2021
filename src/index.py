from tkinter import Tk, DoubleVar
from user_interface.user_interface import UI
from calculator.calculator import Calculator
from services.note_service import note_service


def main():
  """Sets up the UI for the calculator
  """
    window = Tk()
    window.title("Laskin")
    calculator = Calculator()
    result_var = DoubleVar()

    ui = UI(window, calculator, result_var, note_service)
    ui.start()
    window.mainloop()


if __name__ == '__main__':
    main()
