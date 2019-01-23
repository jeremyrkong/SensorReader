import tkinter as tk
from tkinter import ttk


class RightNavbarView(tk.Frame):
    """ Navigation Bar """

    def __init__(self, parent, getall_callback, delete_callback, page_popup_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._getall_callback = getall_callback
        self._delete_callback = delete_callback
        self._page_popup_callback = page_popup_callback

        self._create_widgets()

    def _create_widgets(self):
        """" Creates the widgets for the right navigation view """
        self._get_all_button = tk.Button(self, text="Get All Readings", command=self._getall_callback, width=13)
        self._get_all_button.grid(row=1, column=0, padx=(0,540), pady=(0,8))

        self._update_button = tk.Button(self, text="Update Reading", command=self._page_popup_callback, width=12)
        self._update_button.grid(row=4, column=2, padx=10, pady=(0,155))
        self._delete_button = tk.Button(self, text="Delete Reading", command=self._delete_callback, width=12)
        self._delete_button.grid(row=4, column=2, padx=10, pady=(0,100))
        
        self.selected_item = ''

        # Data table view
        self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)

        self.table = ttk.Treeview(self, show="headings", yscrollcommand=self._scrollbar.set)
        self._scrollbar.config(command=self.table.yview)
        self.table.bind('<ButtonRelease-1>', self.get_selected_item)
        self.table.grid(row=4, column=0)
        self._scrollbar.grid(row=4, column=1, sticky=tk.N+tk.S+tk.W+tk.E)
        self.table['columns'] = ('id',
                                 'timestamp',
                                 'model',
                                 'min_reading',
                                 'avg_reading',
                                 'max_reading',
                                 'status')
        self.table.heading('id', text="ID")
        self.table.heading('timestamp', text="Date")
        self.table.heading('model', text="Sensor Name")
        self.table.heading('min_reading', text="Min Reading")
        self.table.heading('avg_reading', text="Avg Reading")
        self.table.heading('max_reading', text="Max Reading")
        self.table.heading('status', text="Status")

        self.table.column('id', width=45)
        self.table.column('timestamp', width=170)
        self.table.column('model', width=170)
        self.table.column('min_reading', width=80)
        self.table.column('avg_reading', width=80)
        self.table.column('max_reading', width=80)
        self.table.column('status', width=70)

    def insert_data(self, data):
        """" Insert data into treeview table """
        data_list = []

        for key,value in data.items():
            data_list.append(value)
        self.table.insert('', 'end', values=(data_list))
        
    def get_selected_item(self, a):
        """" Assigns selected reading properties on mouseclick from treeview table """
        current_item = self.table.focus()
        current_item_dict = self.table.item(current_item)
        self.selected_item = current_item_dict

    def get_selected_row(self):
        """" Get selected reading properties on mouseclick from treeview table"""
        current_row = self.table.focus()
        return self.table.item(current_row)

    def delete_log(self, selected_id):
        """" Remove row by ID from treeview table """
        for row in self.table.get_children():
            if self.table.item(row)["values"][0] == selected_id:
                self.table.delete(row)

