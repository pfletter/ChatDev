'''
This is the main file of the AI in Healthcare report software. It contains the GUI implementation and handles user interactions.
'''
import tkinter as tk
from tkinter import Tk, Label, Button
from report_generator import ReportGenerator
class AIHealthcareReportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI in Healthcare Report")
        self.report_generator = ReportGenerator()
        self.create_widgets()
    def create_widgets(self):
        self.label = Label(self.root, text="AI in Healthcare Report")
        self.label.pack()
        self.generate_button = Button(self.root, text="Generate Report", command=self.generate_report)
        self.generate_button.pack()
    def generate_report(self):
        report = self.report_generator.generate_report()
        # Additional code to save or display the generated report
        print(report)
if __name__ == "__main__":
    root = Tk()
    app = AIHealthcareReportApp(root)
    root.mainloop()