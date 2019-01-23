import tkinter as tk


class Page1View(tk.Frame):
    """ Page 1 """

    LABEL_NAME = ["Sensor", "Low Temp", "Avg Temp", "Max Temp", "Status"]

    def __init__(self, parent, submit_callback):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._submit_callback = submit_callback

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 1 """

        for number in range(len(Page1View.LABEL_NAME)):
            self._label = tk.Label(self, text=Page1View.LABEL_NAME[number] + ":", anchor="e", width=10)
            self._label.grid(row=number + 1, column=1, padx=(20))

        self._sensor_entry = tk.Entry(self)
        self._sensor_entry.grid(row=1, column=2, padx=10)
        self._low_entry = tk.Entry(self)
        self._low_entry.grid(row=2, column=2, padx=10)
        self._avg_entry = tk.Entry(self)
        self._avg_entry.grid(row=3, column=2, padx=10)
        self._high_entry = tk.Entry(self)
        self._high_entry.grid(row=4, column=2, padx=10)
        self._status_entry = tk.Entry(self)
        self._status_entry.grid(row=5, column=2, padx=10)

        self._button = tk.Button(self,
                                 text="Add Reading",
                                 command=self._submit_callback)
        self._button.grid(row=7, column=2, padx=20, pady=5)


    def get_form_data(self):
        return {
                "model": self._sensor_entry.get(),
                "min_reading": self._low_entry.get(),
                "avg_reading": self._avg_entry.get(),
                "max_reading": self._high_entry.get(),
                "status": self._status_entry.get()
                }
