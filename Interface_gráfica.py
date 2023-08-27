import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Inserção_de_dados import *



class BellmanFordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Viagem por capitais")
        self.root.geometry("800x600")

        background_image = Image.open("Images\Background_image.png")
        self.background_photo = ImageTk.PhotoImage(background_image)

        self.root.iconbitmap("Images\Icone.ico")
        # Usando um Label para exibir a imagem de fundo
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.label = tk.Label(root, text="Selecione os Países:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.frame = ttk.Frame(root)
        self.frame.pack()

        self.source_label = tk.Label(self.frame, text="País Inicio:", font=("Arial", 12))
        self.source_label.grid(row=0, column=0)

        self.source_var = tk.StringVar()
        self.source_combo = ttk.Combobox(self.frame, textvariable=self.source_var)
        self.source_combo.grid(row=0, column=1)

        self.destination_label = tk.Label(self.frame, text="País Destino:", font=("Arial", 12))
        self.destination_label.grid(row=1, column=0)

        self.destination_var = tk.StringVar()
        self.destination_combo = ttk.Combobox(self.frame, textvariable=self.destination_var)
        self.destination_combo.grid(row=1, column=1)

        self.result_text = tk.Text(root, height=5, width=50, font=("Arial", 12))
        self.result_text.pack()

        self.popular_combos_vertices()

        self.run_button = ttk.Button(root, text="Viajar", command=self.executar_bellman_ford)
        self.run_button.pack(pady=10)

    def popular_combos_vertices(self):
        self.source_combo["values"] = [vertice.nome for vertice in grafo.vertices_dista]
        self.destination_combo["values"] = [vertice.nome for vertice in grafo.vertices_dista]

    def executar_bellman_ford(self):
        vertice_origem_nome = self.source_var.get()
        vertice_destino_nome = self.destination_var.get()

        if vertice_origem_nome == vertice_destino_nome:
            self.result_text.insert(tk.END, "Os vértices de origem e destino são iguais.\n")
            return

        vertice_origem = vertice_origem_nome
        vertice_destino = vertice_destino_nome

        if not vertice_origem or not vertice_destino:
            self.result_text.insert(tk.END, "Selecione os vértices de origem e destino.\n")
            return

        aresta = grafo.encontrar_peso_aresta(vertice_origem, vertice_destino)

        if aresta:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END,
                                    f"Menor caminho de {vertice_origem_nome} para {vertice_destino_nome}: {aresta}\n")
            self.result_text.insert(tk.END, "Caminho: " + " -> ".join([vertice_origem_nome, vertice_destino_nome]) + "\n")
        else:
            caminho, distancia = grafo.bellman_ford(vertice_origem, vertice_destino)
            if caminho:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END,
                                        f"Menor caminho de {vertice_origem_nome} para {vertice_destino_nome}: {distancia}\n")
                self.result_text.insert(tk.END, "Caminho: " + " -> ".join([vertice for vertice in caminho]) + "\n")
            else:
                self.result_text.insert(tk.END, "Não há caminho entre os vértices.\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = BellmanFordApp(root)
    root.mainloop()
