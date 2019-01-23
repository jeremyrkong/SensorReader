import tkinter as tk


class TopNavbarView(tk.Frame):
    """ Navigation Bar """

    TEMPERATURE = 1
    PRESSURE = 2

    def __init__(self, parent, page_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._page_callback = page_callback

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """
        tk.Label(self,
                 text="Select Sensor:").grid(row=0, column=0)

        self.curr_page = tk.IntVar()

        tk.Radiobutton(self,
                       text="Temperature",
                       variable=self.curr_page,
                       command=self._page_callback,
                       value=TopNavbarView.TEMPERATURE).grid(row=0, column=1)

        tk.Radiobutton(self,
                       text="Pressure",
                       variable=self.curr_page,
                       command=self._page_callback,
                       value=TopNavbarView.PRESSURE).grid(row=0, column=2)

        self.curr_page.set(TopNavbarView.TEMPERATURE)

