import tkinter as tk
from tkinter import ttk, messagebox

# Taxas fixas em relação ao Real (BRL)
TAXAS = {
    "BRL": 1.0,
    "USD": 5.20,
    "EUR": 6.15,
    "GBP": 6.90,
    "JPY": 0.035,
    "CAD": 3.90,
    "ARS": 0.006
}

class ConversorMoedas:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Moedas")
        self.root.geometry("480x360")
        self.root.resizable(False, False)

        self.criar_interface()

    def criar_interface(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame,
            text="Conversor de Moedas",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        ttk.Label(frame, text="Valor").pack(anchor="w")
        self.valor_entry = ttk.Entry(frame)
        self.valor_entry.pack(fill="x")

        ttk.Label(frame, text="Moeda de origem").pack(anchor="w", pady=(10, 0))
        self.origem = ttk.Combobox(
            frame,
            values=list(TAXAS.keys()),
            state="readonly"
        )
        self.origem.pack(fill="x")
        self.origem.set("BRL")

        ttk.Label(frame, text="Moeda de destino").pack(anchor="w", pady=(10, 0))
        self.destino = ttk.Combobox(
            frame,
            values=list(TAXAS.keys()),
            state="readonly"
        )
        self.destino.pack(fill="x")
        self.destino.set("USD")

        ttk.Button(
            frame,
            text="Converter",
            command=self.converter
        ).pack(pady=15)

        self.resultado = ttk.Label(
            frame,
            text="",
            font=("Arial", 12),
            wraplength=380,
            justify="center"
        )
        self.resultado.pack(pady=10)

    def converter(self):
        try:
            valor = float(self.valor_entry.get())
            moeda_origem = self.origem.get()
            moeda_destino = self.destino.get()

            # Converte para BRL
            valor_brl = valor * TAXAS[moeda_origem]

            # Converte de BRL para moeda destino
            resultado = valor_brl / TAXAS[moeda_destino]

            self.resultado.config(
                text=f"Resultado: {resultado:.2f} {moeda_destino}"
            )

        except ValueError:
            messagebox.showwarning(
                "Erro",
                "Digite um valor numérico válido."
            )

if __name__ == "__main__":
    root = tk.Tk()
    ConversorMoedas(root)
    root.mainloop()
