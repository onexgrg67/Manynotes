import tkinter as tk
from tkinter import filedialog, messagebox
print("""
░▒█▀▄▀█░█▀▀▄░█▀▀▄░█░░█░█▀▀▄░▄▀▀▄░▀█▀░█▀▀░█▀▀
░▒█▒█▒█░█▄▄█░█░▒█░█▄▄█░█░▒█░█░░█░░█░░█▀▀░▀▀▄
░▒█░░▒█░▀░░▀░▀░░▀░▄▄▄▀░▀░░▀░░▀▀░░░▀░░▀▀▀░▀▀▀

""")
print("\nYou want white or black mode? ")
class Manynotes:
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.menu = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu, tearoff=0)

    def run(self):
        self.root.title("Manynotes")
        self.root.geometry("800x600")
        self.text_area.pack(fill='both', expand=1)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.root.config(menu=self.menu)
        self.root.mainloop()

    def new_file(self):
        self.text_area.delete(1.0, 'end')

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, 'end')
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, 'end'))

if __name__ == "__main__":
    root = tk.Tk()
    manynotes = Manynotes(root)
    manynotes.run()