import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class ModernIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Tkinter IDE")
        self.root.geometry("1000x600")
        style = ttk.Style()
        style.theme_use('clam')
        self.left_frame = ttk.Frame(self.root, width=200, relief="sunken")
        self.left_frame.grid(row=0, column=0, sticky="nswe")
        self.tree = ttk.Treeview(self.left_frame)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.load_files(os.getcwd()) 
        self.right_frame = ttk.Frame(self.root)
        self.right_frame.grid(row=0, column=1, sticky="nswe")
        self.text_area = tk.Text(self.right_frame, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.toolbar = ttk.Frame(self.root, padding="5 0 5 5")
        self.toolbar.grid(row=1, column=0, columnspan=2, sticky="we")
        self.add_toolbar_buttons()

    def add_toolbar_buttons(self):
        """Create and add toolbar buttons."""
        open_btn = ttk.Button(self.toolbar, text="Open", command=self.open_file)
        open_btn.grid(row=0, column=0, padx=5)

        save_btn = ttk.Button(self.toolbar, text="Save", command=self.save_file)
        save_btn.grid(row=0, column=1, padx=5)

    def load_files(self, path):
        """Load and display files in the left file explorer."""
        self.tree.delete(*self.tree.get_children())
        for filename in os.listdir(path):
            self.tree.insert('', 'end', filename, text=filename)
        self.tree.bind("<Double-1>", self.on_file_select)

    def on_file_select(self, event):
        """Open a file from the file explorer in the text editor."""
        selected_file = self.tree.selection()
        if selected_file:
            file_path = os.path.join(os.getcwd(), self.tree.item(selected_file[0])['text'])
            self.open_file(file_path)

    def open_file(self, file_path=None):
        """Open and load the content of a file."""
        if not file_path:
            file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)  # Clear previous content
                self.text_area.insert(tk.END, content)  # Insert file content
                self.root.title(f"Modern Tkinter IDE - {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    def save_file(self):
        """Save the content from the text editor to a file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content.strip())
                messagebox.showinfo("Success", f"File saved as {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")


def main():
    root = tk.Tk()
    app = ModernIDE(root)
    root.mainloop()


if __name__ == "__main__":
    main()
