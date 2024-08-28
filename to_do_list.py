import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []
        
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)
        
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)
        
        mark_done_button = tk.Button(root, text="Mark Task as Done", command=self.mark_task_done)
        mark_done_button.pack(pady=5)
        
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.pack(pady=5)
        
    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append({"task": task, "completed": False})
            self.entry.delete(0, tk.END)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def mark_task_done(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
    
    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_str = task["task"] + " (Done)" if task["completed"] else task["task"]
            self.task_listbox.insert(tk.END, task_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
