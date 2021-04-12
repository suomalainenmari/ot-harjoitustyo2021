from tkinter import Tk, ttk, constants, IntVar
class UI:
  def __init__(self,root):
    self._root = root
    self._entry = None
  
  def start(self):
    self._result_var = IntVar()
    self._result_var.set("0")
    header_label = ttk.Label(master=self._root, text="Laskin")
    input_label = ttk.Label(master=self._root, text="Syöte:")
    self._entry = ttk.Entry(master=self._root)
    plus_button = ttk.Button(
      master=self._root,
       text="+",
       command= self._handle_plus_click
       )

    minus_button = ttk.Button(
      master=self._root,
      text="-",
      command= self._handle_minus_click
      )
    
    output_label = ttk.Label(master=self._root, text="Tulos:")
    output_itself = ttk.Label(master=self._root, textvariable=self._result_var)


    header_label.grid(row=0, column=0, columnspan=2)
    input_label.grid(row=1, column=0,columnspan=2)
    self._entry.grid(row=2,column=0,columnspan=2)
    plus_button.grid(row=3,column=0)
    minus_button.grid(row=3,column=1)
    output_label.grid(row=4,column=0)
    output_itself.grid(row=4, column=1)

  def _handle_plus_click(self):
    entry_value = self._entry.get()
    print(f"Value of entry is {entry_value}")
    increased_value = self._result_var.get()+int(entry_value)
    self._result_var.set(increased_value)


  def _handle_minus_click(self):
    entry_value = self._entry.get()
    print(f"Value of entry is {entry_value}")
    decreased_value = self._result_var.get()-int(entry_value)
    self._result_var.set(decreased_value)

window = Tk()  
window.title("Laskin")

ui= UI(window)
ui.start()
window.mainloop()