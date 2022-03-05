from tkinter import messagebox

import ttkbootstrap as ttk

from application import Application


def on_closing():
    if messagebox.askyesno("Sair", "Você deseja sair?"):
        raise SystemExit


if __name__ == "__main__":
    app = ttk.Window(
        title="ERP tunado",
        themename="litera",
        resizable=(False, False)
    )
    Application(app)
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
