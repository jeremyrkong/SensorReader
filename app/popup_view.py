import tkinter as tk
from tkinter import messagebox as tkMessageBox


class PopupView(tk.Frame):
    """ Popup Window """

    LABEL_NAME = ["ID", "Date", "Sensor Name", "Min Reading", "Avg Reading", "Max Reading", "Status"]

    def __init__(self, parent, update_popup_callback, close_popup_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=2, columnspan=2)

        self._list_data = []

        self._update_popup_callback = update_popup_callback
        self._close_popup_callback = close_popup_callback
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the popup """
        for number in range(len(PopupView.LABEL_NAME)):
            self._label = tk.Label(self, text=PopupView.LABEL_NAME[number] + ":", anchor="e", width=12)
            self._label.grid(row=number, column=1, padx=(20))

        self._id_entry = tk.Entry(self, width=25)
        self._id_entry.grid(row=0, column=2, padx=10)
        self._timestamp_entry = tk.Entry(self, width=25)
        self._timestamp_entry.grid(row=1, column=2, padx=10)
        self._model_entry = tk.Entry(self, width=25)
        self._model_entry.grid(row=2, column=2, padx=10)
        self._min_entry = tk.Entry(self, width=25)
        self._min_entry.grid(row=3, column=2, padx=10)
        self._avg_entry = tk.Entry(self, width=25)
        self._avg_entry.grid(row=4, column=2, padx=10)
        self._high_entry = tk.Entry(self, width=25)
        self._high_entry.grid(row=5, column=2, padx=10)
        self._status_entry = tk.Entry(self, width=25)
        self._status_entry.grid(row=6, column=2, padx=10)

        self._update = tk.Button(self,
                                 text="Update",
                                 command=self._update_popup_callback)
        self._update.grid(row=8, column=2, pady=(2,0))
        self._close = tk.Button(self,
                                text="Close",
                                command=self._close_popup_callback)
        self._close.grid(row=9, column=2, pady=(20,4))

    def insert_values(self, id, timestamp, model, min, avg, high, status):
        """" Insert values into parent entries """
        self._id_entry.insert(0, id)
        self._id_entry.configure(state="disabled")
        self._timestamp_entry.insert(0, timestamp)
        self._timestamp_entry.configure(state="disabled")
        self._model_entry.insert(0, model)
        self._min_entry.insert(0, min)
        self._avg_entry.insert(0, avg)
        self._high_entry.insert(0, high)
        self._status_entry.insert(0, status)

    def get_form_data(self):
        """" Return values from parent entries """
        return {
                "id": self._id_entry.get(),
                "model": self._model_entry.get(),
                "min_reading": self._min_entry.get(),
                "avg_reading": self._avg_entry.get(),
                "max_reading": self._high_entry.get(),
                "status": self._status_entry.get()
                }

    def get_timestamp(self):
        """" Return timestamp from parent entry """
        return {
            "timestamp": self._timestamp_entry.get()
        }

