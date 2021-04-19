from tkinter import Tk, ttk, constants, DoubleVar
from calculator import Calculator


class UI:
    def __init__(self, root):
        self._root = root
        self._entry = None
        self._calculator = Calculator()
        self._result_var = DoubleVar()

    def start(self):
        self._result_var.set(self._calculator.result)

        header_label = ttk.Label(master=self._root, text="Laskin")
        input_label = ttk.Label(master=self._root, text="Syöte:")
        self._entry = ttk.Entry(master=self._root)

        plus_button = ttk.Button(
            master=self._root,
            text="+",
            command=self._handle_plus_click
        )

        minus_button = ttk.Button(
            master=self._root,
            text="-",
            command=self._handle_minus_click
        )

        multiply_button = ttk.Button(
            master=self._root,
            text="*",
            command=self._handle_multiply_click
        )

        divide_button = ttk.Button(
            master=self._root,
            text="/",
            command=self._handle_divide_click
        )

        all_clear_button = ttk.Button(
            master=self._root,
            text="AC",
            command=self._handle_all_clear_click
        )

        output_label = ttk.Label(master=self._root, text="Tulos:")
        output_itself = ttk.Label(
            master=self._root, textvariable=self._result_var)

        header_label.grid(row=0, column=0, columnspan=2)
        input_label.grid(row=1, column=0, columnspan=2)
        self._entry.grid(row=2, column=0, columnspan=2)
        plus_button.grid(row=3, column=0)
        minus_button.grid(row=3, column=1)
        multiply_button.grid(row=4, column=0)
        divide_button.grid(row=4, column=1)
        output_label.grid(row=6, column=0)
        output_itself.grid(row=6, column=1)
        all_clear_button.grid(row=5, columnspan=2, sticky=constants.W)

    def _handle_plus_click(self):
        entry_value = self._entry.get()
        self._calculator.add(float(entry_value))
        self._result_var.set(self._calculator.result)

    def _handle_minus_click(self):
        entry_value = self._entry.get()
        self._calculator.subtract(float(entry_value))
        self._result_var.set(self._calculator.result)

    def _handle_multiply_click(self):
        entry_value = self._entry.get()
        self._calculator.multiply(float(entry_value))
        self._result_var.set(self._calculator.result)

    def _handle_divide_click(self):
        entry_value = self._entry.get()
        self._calculator.divide(float(entry_value))
        self._result_var.set(self._calculator.result)

    def _handle_all_clear_click(self):
        self._calculator.clear()
        self._result_var.set(self._calculator.result)


window = Tk()
window.title("Laskin")

ui = UI(window)
ui.start()
window.mainloop()
