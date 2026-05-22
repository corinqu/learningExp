import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def new_file(window, text_edit):
    #create a new file, clear the text editor and reset the title
    text_edit.delete(1.0, tk.END)
    window.title("Easy Text Editor - New File")

   
def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        text = f.read()
        text_edit.insert(tk.END, text)
    window.title(f"Easy Text Editor - {filepath}")


def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as f:
        text = text_edit.get(1.0, tk.END)
        f.write(text)
    window.title(f"Easy Text Editor - {filepath}")


def main():
  window = tk.Tk()
  window.title("Easy Text Editor")
  window.geometry("400x300")


  text_edit = tk.Text(window, font=("Arial", 12))
  text_edit.grid(row=0, column=1)


  frame = tk.Frame(window)
  frame.grid(row=0, column=0)
  

  new_button = tk.Button(frame, text="New", command=lambda: new_file(window, text_edit))
  new_button.grid(row=0, column=0, sticky="ns")
  open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))
  open_button.grid(row=1, column=0, sticky="ns")
  save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
  save_button.grid(row=2, column=0, sticky="ns")


  window.bind("<Command-n>", lambda event: new_file(window, text_edit))
  window.bind("<Command-o>", lambda event: open_file(window, text_edit))
  window.bind("<Command-s>", lambda event: save_file(window, text_edit))


  window.mainloop()

if __name__ == "__main__":
    main()