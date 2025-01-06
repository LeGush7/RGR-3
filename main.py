import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


def ford_bellman():
    try:
        vertexes = int(vertexes_entry.get())
        edges_input = edges_text.get('1.0', tk.END).strip()
        origin = origin_entry.get().strip()

        if not edges_input:
            messagebox.showerror('Ошибка', 'Введите информацию о рёбрах графа')
            return

        edges = []
        vertexes_set = set()

        for line in edges_input.splitlines():
            u, v, w = line.split()
            w = int(w)
            edges.append((u, v, w))
            vertexes_set.add(u)
            vertexes_set.add(v)

        if len(vertexes_set) < vertexes:
            messagebox.showerror('Ошибка', 'Кажется, Вы не указали несколько вершин')
            return
        elif len(vertexes_set) > vertexes:
            messagebox.showerror('Ошибка', 'Кажется, Вы указали лишние вершины')
            return

        if origin not in vertexes_set:
            messagebox.showerror('Ошибка', 'Такая вершина отсутствует')
            return

        length = {vertex: float('inf') for vertex in vertexes_set}
        length[origin] = 0

        for i in range(vertexes - 1):
            for u, v, w in edges:
                if length[u] != float('inf') and length[u] + w < length[v]:
                    length[v] = length[u] + w

        for u, v, w in edges:
            if length[u] != float('inf') and length[u] + w < length[v]:
                messagebox.showerror('Внимание', 'В графе присутствует отрицательный цикл')
                return

        result = "\n".join(sorted([f'Вершина {vertex}: 'f'{dist if dist != float("inf") else "∞"}'
                            for vertex, dist in length.items()]))
        result_text.config(state='normal')
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f'Минимальные расстояния:\n{result}')
        result_text.config(state='disabled')
    except ValueError:
        messagebox.showerror('Ошибка', 'Некорректный ввод данных')


root = tk.Tk()
root.title('Алгоритм Форда-Беллмана')
root.geometry('800x800')


tk.Label(root, text='Введите количество вершин:', font=('Arial', 14)).pack(pady=5)
vertexes_entry = tk.Entry(root, font=('Arial', 14), width=10)
vertexes_entry.pack(pady=5)


tk.Label(root, text='Введите рёбра графа (u v w):', font=('Arial', 14)).pack(pady=5)
edges_text = ScrolledText(root, height=10, width=70, font=('Arial', 12))
edges_text.pack(pady=5)
edges_text.bind('<Control-v>', lambda e: edges_text.event_generate('<<Paste>>'))


tk.Label(root, text='Введите исходную вершину:', font=('Arial', 14)).pack(pady=5)
origin_entry = tk.Entry(root, font=('Arial', 14), width=10)
origin_entry.pack(pady=5)
origin_entry.bind('<Control-v>', lambda e: origin_entry.event_generate('<<Paste>>'))


tk.Button(root, text='Запустить', command=ford_bellman, font=('Arial', 14), bg='#44824c').pack(pady=20)


result_text = ScrolledText(root, height=15, width=70, font=('Arial', 12))
result_text.pack(pady=10)
result_text.config(state='disabled')


root.mainloop()
