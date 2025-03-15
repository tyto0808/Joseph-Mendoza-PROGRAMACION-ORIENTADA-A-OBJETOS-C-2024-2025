import tkinter as tk
from tkinter import messagebox


class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación GUI Básica")

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=5)

        # Campo de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Botón para agregar información
        self.add_button = tk.Button(root, text="Agregar", command=self.add_item)
        self.add_button.pack(pady=5)

        # Lista para mostrar datos
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=5)

        # Botón para limpiar información
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_list)
        self.clear_button.pack(pady=5)

    def add_item(self):
        item = self.entry.get()
        if item:
            self.listbox.insert(tk.END, item)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El campo de texto está vacío")

    def clear_list(self):
        self.listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
