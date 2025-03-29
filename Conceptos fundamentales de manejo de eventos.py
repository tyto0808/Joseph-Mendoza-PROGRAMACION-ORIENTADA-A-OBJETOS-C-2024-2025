import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        self.tasks = []  # Lista para almacenar las tareas

        # Campo de entrada para nuevas tareas
        self.entry_task = tk.Entry(root, width=40)
        self.entry_task.grid(row=0, column=0, padx=10, pady=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox para mostrar las tareas
        self.listbox_tasks = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
        self.listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botón para marcar como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_completed)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        # Vincular la tecla Enter para añadir tareas
        self.entry_task.bind("<Return>", self.add_task_enter)

    def add_task(self, event=None):
        task = self.entry_task.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def add_task_enter(self, event):
        self.add_task()

    def mark_completed(self):
        try:
            selected_index = self.listbox_tasks.curselection()[0]
            task = self.tasks[selected_index]
            # Marcar la tarea como completada (agregar un prefijo "Completada: ")
            self.tasks[selected_index] = "Completada: " + task
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.listbox_tasks.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")

    def update_task_listbox(self):
        # Limpiar la lista y agregar las tareas actualizadas
        self.listbox_tasks.delete(0, tk.END)
        for task in self.tasks:
            self.listbox_tasks.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
