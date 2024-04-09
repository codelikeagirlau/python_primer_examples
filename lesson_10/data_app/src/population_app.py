import tkinter as tk
from tkinter import messagebox, simpledialog
from data_loader import load_data
from analysis import filter_age_data, process_age_data, process_age_data_over_time, filter_data_by_year

class PopulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Population Data Analysis")
        self.root.geometry("600x400")

        # Load the data
        self.data = load_data('lesson_10\data_app\data\data_nairne.csv')
        self.age_data = filter_age_data(self.data) if self.data is not None else None

        # Create buttons and help buttons
        self.add_button("View Age Distribution", self.show_age_distribution, process_age_data)
        self.add_button("View Age Distribution Over Time", self.show_age_distribution_over_time, process_age_data_over_time)
        self.add_button("Query Yearly Data", self.query_yearly_data, self.query_yearly_data) 

    def add_button(self, text, command, func):
        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        tk.Button(frame, text=text, command=command).pack(side=tk.LEFT)
        tk.Button(frame, text="?", command=lambda: self.show_help(func)).pack(side=tk.LEFT)

    def show_help(self, func):
        """
        Shows the docstring of the given function.
        
        Parameters:
            func (function): The function whose docstring is to be displayed.
        """
        docstring = func.__doc__ or "No documentation available"
        messagebox.showinfo("Help", docstring)
        
    def show_age_distribution(self):
        """
        Display the age distribution summary.
        This method processes the filtered age data and shows the summary in a message box.
        """
        if self.age_data is not None:
             age_summary = process_age_data(self.age_data)
             age_summary_str = age_summary.to_string(index=False)
             messagebox.showinfo("Age Distribution Summary", age_summary_str)
        else:
             messagebox.showerror("Error", "Data is not loaded properly.")

    def show_age_distribution_over_time(self):
        """
        Display the age distribution over time summary.
        This method processes the filtered age data to show how the age distribution changes over time.
        """
        if self.age_data is not None:
             age_summary_over_time = process_age_data_over_time(self.age_data)
             age_summary_over_time_str = age_summary_over_time.to_string(index=False)
             messagebox.showinfo("Age Distribution Over Time Summary", age_summary_over_time_str)
        else:
              messagebox.showerror("Error", "Data is not loaded properly.")

    def query_yearly_data(self):
         """
         Asks the user for a year and shows age data for that year.
         Displays an error message if the year is not in the data.
         """
         year = simpledialog.askinteger("Input", "Enter a year to check age data for", parent=self.root)
         if year and self.age_data is not None:
               year_data = filter_data_by_year(self.age_data, year)
               if not year_data.empty:
                     year_data_str = year_data.to_string(index=False)
                     messagebox.showinfo(f"Age Data for {year}", year_data_str)
               else:
                     messagebox.showerror("Error", f"No data available for the year {year}.")
         elif not year:
               messagebox.showerror("Error", "No year entered.")

        
if __name__ == "__main__":
    root = tk.Tk()
    app = PopulationApp(root)
    root.mainloop()
