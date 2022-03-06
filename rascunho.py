import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import ttkbootstrap as ttkb

def calendar_view():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def dateentry_view():
    def print_sel():
        print(cal.get_date())
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
    ttk.Button(top, text="ok", command=print_sel).pack()

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Calendar', command=calendar_view).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=dateentry_view).pack(padx=10, pady=10)

root.mainloop()