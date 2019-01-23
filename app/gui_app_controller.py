import tkinter as tk
from tkinter import messagebox as tkMessageBox
from app.top_navbar_view import TopNavbarView
from app.page1_view import Page1View
from app.page2_view import Page2View
from app.bottom_navbar_view import BottomNavbarView
from app.popup_view import PopupView
from app.right_navbar_view import RightNavbarView
import requests
import json

API_ENDPOINT = "http://127.0.0.1:5000/sensor"


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    VALUES = 2
    ID = 0
    TIMESTAMP = 1
    MODEL = 2
    MIN_READING = 3
    AVG_READING = 4
    MAX_READING = 5
    STATUS = 6

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        self._top_navbar = TopNavbarView(self, self._page_callback)
        self._page1 = Page1View(self, self._page1_submit_callback)
        self._page2 = Page2View(self, self._page2_submit_callback)
        self._bottom_navbar = BottomNavbarView(self, self._quit_callback)
        self._right_navbar = RightNavbarView(self, self._right_navbar_getall_callback,
                                             self._right_navbar_delete_callback, self._page_popup_callback)

        self._top_navbar.grid(row=0, columnspan=4, pady=10)
        self._page1.grid(row=1, columnspan=4, pady=10)
        # Hide Page 2 by default
        self._curr_page = TopNavbarView.TEMPERATURE
        self._right_navbar.grid(row=1, column=4, pady=10, padx=(0, 20))
        self._bottom_navbar.grid(row=2, columnspan=6, pady=10, padx=(900, 0))

    def _close_popup_callback(self):
        """" Callback to close popup window """
        self._popup_win.destroy()

    def _page1_submit_callback(self):
        """" Callback to add reading from Temperature page """
        form_json_data = self._page1.get_form_data()
        print("Submit Temperature Log")

        headers = {"content-type": "application/json"}
        response = requests.post(API_ENDPOINT + "/temperature/reading", json=form_json_data, headers=headers)
        print(form_json_data)
        print(response.status_code)

        if form_json_data['model'] == '':
            tkMessageBox.showwarning('Invalid operation', 'All fields must be filled')
        elif form_json_data['min_reading'] == '':
            tkMessageBox.showwarning('Invalid operation', 'All fields must be filled')
        elif form_json_data['avg_reading'] == '':
            tkMessageBox.showwarning('Invalid operation', 'All fields must be filled')
        elif form_json_data['max_reading'] == '':
            tkMessageBox.showwarning('Invalid operation', 'All fields must be filled')
        elif form_json_data['status'] == '':
            tkMessageBox.showwarning('Invalid operation', 'All fields must be filled')
        elif response.status_code == 400:
            tkMessageBox.showwarning('Invalid operation', 'Please verify that fields are inputted correctly')
        elif response.status_code == 200:
            self._right_navbar_getall_callback()

    def _page2_submit_callback(self):
        """" Callback to add reading from Pressure page """
        form_json_data = self._page2.get_form_data()
        print("Submit Pressure Log")

        headers = {"content-type": "application/json"}
        response = requests.post(API_ENDPOINT + "/pressure/reading", json=form_json_data, headers=headers)
        print(form_json_data)
        print(response.status_code)

        if form_json_data['model'] == '':
            tkMessageBox.showwarning('Invalid operation', 'All fields must be filled')
        elif form_json_data['min_reading'] == '':
            tkMessageBox.showwarning('Invalid operation', 'All fields must be filled')
        elif form_json_data['avg_reading'] == '':
            tkMessageBox.showwarning('Invalid operation', 'All fields must be filled')
        elif form_json_data['max_reading'] == '':
            tkMessageBox.showwarning('Invalid operation', 'All fields must be filled')
        elif form_json_data['status'] == '':
            tkMessageBox.showwarning('Invalid operation', 'All fields must be filled')
        elif response.status_code == 200:
            self._right_navbar_getall_callback()

    def _right_navbar_getall_callback(self):
        """" Callback to populate table from database with Get-all API call """
        for row in self._right_navbar.table.get_children():
            self._right_navbar.table.delete(row)

        if (self._curr_page == TopNavbarView.TEMPERATURE):

            response = requests.get(API_ENDPOINT + '/temperature/reading/all')
            temp_obj_list = response.json()

            for temp_dict in temp_obj_list:
                self._right_navbar.insert_data(temp_dict)

        elif (self._curr_page == TopNavbarView.PRESSURE):

            response = requests.get(API_ENDPOINT + '/pressure/reading/all')
            press_obj_list = response.json()

            for press_dict in press_obj_list:
                self._right_navbar.insert_data(press_dict)

    def _right_navbar_delete_callback(self):
        """" Callback to delete log """
        self.get_selected_id = None
        try:
            self.get_selected_id = str(self._right_navbar.selected_item["values"][0])
        except:
            if self.get_selected_id == None:
                tkMessageBox.showwarning('Invalid operation', 'Select a reading from the table')
        if self.get_selected_id is not None:
            if (self._curr_page == TopNavbarView.TEMPERATURE):
                requests.delete(API_ENDPOINT + '/temperature/reading/' + self.get_selected_id)
                self.get_selected_id = None

            elif (self._curr_page == TopNavbarView.PRESSURE):
                requests.delete(API_ENDPOINT + '/pressure/reading/' + self.get_selected_id)
                self.get_selected_id = None

            self._right_navbar_getall_callback()

    def _page_callback(self):
        """ Callback for switching between Temperature and Pressure pages """
        curr_page = self._top_navbar.curr_page.get()
        if (self._curr_page != curr_page and self._curr_page == TopNavbarView.TEMPERATURE):
            self._page1.grid_forget()
            self._page2.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PRESSURE
        elif (self._curr_page != curr_page and self._curr_page == TopNavbarView.PRESSURE):
            self._page2.grid_forget()
            self._page1.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.TEMPERATURE

    def _page_popup_callback(self):
        """" Opens the Update Popup window """
        self._popup_win = tk.Toplevel()
        self._popup = PopupView(self._popup_win, self._update_popup_callback, self._close_popup_callback)
        row_data = self._right_navbar.get_selected_row()
        row_data = self._right_navbar.get_selected_row()
        print(row_data)
        dict_list = []
        for value in row_data.values():
            dict_list.append(value)
        sensor_data = dict_list[MainAppController.VALUES]
        try:
            self._popup.insert_values(sensor_data[MainAppController.ID],
                                      sensor_data[MainAppController.TIMESTAMP],
                                      sensor_data[MainAppController.MODEL],
                                      sensor_data[MainAppController.MIN_READING],
                                      sensor_data[MainAppController.AVG_READING],
                                      sensor_data[MainAppController.MAX_READING],
                                      sensor_data[MainAppController.STATUS],
                                      )
        except IndexError:
            self._close_popup_callback()
            tkMessageBox.showwarning('Invalid operation', 'Select a reading from the table')

    def _update_popup_callback(self):
        """" Callback to update reading through Update Popup then repopulate table """
        popup_data = self._popup.get_form_data()

        if (self._curr_page == TopNavbarView.TEMPERATURE):
            headers = {"content-type": "application/json"}
            requests.put(API_ENDPOINT + '/temperature/reading/' + popup_data['id'], json=popup_data, headers=headers)
            print(popup_data)

        elif (self._curr_page == TopNavbarView.PRESSURE):
            headers = {"content-type": "application/json"}
            requests.put(API_ENDPOINT + '/pressure/reading/' + popup_data['id'], json=popup_data, headers=headers)
            print(popup_data)

        self._right_navbar_getall_callback()

    def _quit_callback(self):
        """" Callback to quit GUI """
        if tkMessageBox.askyesno('Verify', 'Really quit?'):
            self.quit()


if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()
