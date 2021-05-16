from tkinter import ttk, constants
import tkinter.messagebox


class UI:
    """Class for user interface
    """

    def __init__(self, root, calculator, result_var, note_service):
        """Constructor for the class, creates the UI that is displayed for the user

        Args:
            root : Window for user interface where all widgets go to
            calculator : Calculator object the user interface uses
            result_var : Result of calculations displayed
            note_service : Functionality for adding and displaying notes
        """
        self._root = root
        self._entry = None
        self._note_entry = None
        self._calculator = calculator
        self._result_var = result_var
        self._note_service = note_service

    def start(self):
        """Creates the widgets; buttons, labels, entries for the application
        """

        self._result_var.set(self._calculator.result)
        header_label = ttk.Label(master=self._root, text="Laskin")
        input_label = ttk.Label(master=self._root, text="Syöte:")
        input_note_label = ttk.Label(
            master=self._root, text="Uusi muistiinpano:")
        self._entry = ttk.Entry(master=self._root)
        self._note_entry = ttk.Entry(master=self._root, width=40)

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

        counternumber_button = ttk.Button(
            master=self._root,
            text="+/-",
            command=self._handle_counter_click
        )

        topercentage_button = ttk.Button(
            master=self._root,
            text="%",
            command=self._handle_to_percentage_click
        )

        save_note_button = ttk.Button(
            master=self._root,
            text="Tallenna",
            command=self._handle_save_click
        )

        delete_notes_button = ttk.Button(
            master=self._root,
            text="Tyhjennä muistiinpanot",
            command=self._handle_delete_notes_click
        )

        output_label = ttk.Label(
            master=self._root, text="Tulos:", background='yellow')
        output_itself = ttk.Label(
            master=self._root, textvariable=self._result_var, background='yellow')
        self._notebox = tkinter.Listbox(
            master=self._root, width=40)
        self._get_notes_at_start()

        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        input_label.grid(row=1, column=0, columnspan=2, padx=5)
        input_note_label.grid(row=1, column=4, columnspan=3, padx=5)
        self._entry.grid(row=2, column=0, columnspan=2)
        self._note_entry.grid(row=2, column=4, columnspan=3, padx=5)
        save_note_button.grid(row=3, column=4, columnspan=3)
        self._notebox.grid(row=6, column=4, columnspan=2)
        plus_button.grid(row=3, column=0)
        minus_button.grid(row=3, column=1)
        multiply_button.grid(row=4, column=0, sticky=constants.N)
        divide_button.grid(row=4, column=1, sticky=constants.N)
        all_clear_button.grid(row=5, columnspan=2,
                              sticky=(constants.W, constants.N))
        counternumber_button.grid(row=6, column=0, sticky=constants.N)
        topercentage_button.grid(row=6, column=1, sticky=constants.N)
        output_label.grid(row=7, column=0, sticky=constants.N)
        output_itself.grid(row=7, column=1, sticky=constants.N)
        delete_notes_button.grid(row=7, column=4)

    def _handle_plus_click(self):
        """Handles the functionality of user pressing the +-button
        """
        entry_value = self._entry.get()
        try:
            self._calculator.add(float(entry_value))
            self._result_var.set(self._calculator.result)
        except:
            if len(entry_value) < 1:
                self._error_message("Tyhjällä syötteellä ei voida laskea")
            else:
                self._error_message(
                    "Syötäthän laskimeen pelkkiä numeroita. Huomioithan, että desimaalina käytetään pistettä.")

    def _handle_minus_click(self):
        """Handles the functionality of user pressing the - -button
        """
        entry_value = self._entry.get()
        try:
            self._calculator.subtract(float(entry_value))
            self._result_var.set(self._calculator.result)
        except:
            if len(entry_value) < 1:
                self._error_message("Tyhjällä syötteellä ei voida laskea")
            else:
                self._error_message(
                    "Syötäthän laskimeen pelkkiä numeroita. Huomioithan, että desimaalina käytetään pistettä.")

    def _handle_multiply_click(self):
        """Handles the functionality of user pressing the *-button
        """
        entry_value = self._entry.get()
        try:
            self._calculator.multiply(float(entry_value))
            self._result_var.set(self._calculator.result)
        except:
            if len(entry_value) < 1:
                self._error_message("Tyhjällä syötteellä ei voida laskea")
            else:
                self._error_message(
                    "Syötäthän laskimeen pelkkiä numeroita. Huomioithan, että desimaalina käytetään pistettä.")

    def _handle_divide_click(self):
        """Handles the functionality of user pressing the /-button
        """
        entry_value = self._entry.get()
        try:
            self._calculator.divide(float(entry_value))
            self._result_var.set(self._calculator.result)
        except:
            if len(entry_value) < 1:
                self._error_message("Tyhjällä syötteellä ei voida laskea")
            else:
                self._error_message(
                    "Syötäthän laskimeen pelkkiä numeroita. Huomioithan, että desimaalina käytetään pistettä.")

    def _handle_all_clear_click(self):
        """Handles the functionality of user pressing the AC-button
        """
        self._calculator.clear()
        self._result_var.set(self._calculator.result)

    def _handle_counter_click(self):
        """Handles the functionality of user pressing the +/- -button
        """
        self._calculator.counternumber()
        self._result_var.set(self._calculator.result)

    def _handle_to_percentage_click(self):
        """Handles the functionality of user pressing the %-button
        """
        self._calculator.to_percentage()
        self._result_var.set(self._calculator.result)

    def _handle_save_click(self):
        """Handles the functionality of user pressing Tallenna-button
        """
        content = self._note_entry.get()
        if len(content) < 2:
            self._error_message("Muistiinpanon minimipituus on 2 merkkiä")
        else:
            self._note_service.create_note(content)
            self._notebox.delete(0, tkinter.END)
            results = self._note_service.show_notes()
            for result in results:
                self._notebox.insert(tkinter.END, result + '\n')

    def _handle_delete_notes_click(self):
        self._note_service.delete_notes()
        self._notebox.delete(0, tkinter.END)

    def _get_notes_at_start(self):
        """Function that fetches the notes from database. Used when starting the app.
        """
        results = self._note_service.show_notes()
        for result in results:
            self._notebox.insert(tkinter.END, result + '\n')

    def _error_message(self, message):
        """Handles functionality of sending a messagebox to the user when invalid input is given

        Args:
        message : Message to be displayed to the user
        """
        tkinter.messagebox.showinfo(
            "Virheellinen syöte", message)
