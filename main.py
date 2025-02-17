from collatz_calculator import selection
from tkinter import ttk
import tkinter as tk

def main() -> None:
    window = tk.Tk()
    window.title("Fire Application")
    window.geometry("400x300+960+540")
    window.resizable(False, False)
   
    window.iconbitmap("definitivo.ico")

    button = ttk.Button(window, text="IDK")
    button.pack()
    window.mainloop()


    selection()

if __name__ == '__main__':
    main()
