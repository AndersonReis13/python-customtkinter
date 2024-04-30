
# Equipe : joabe, Anderson Silva, jefferson, Jhon Willian

# É necessário instalar a biblioteca forex_python ultilizando o 'pip install forex-python'.

import tkinter as tk
from forex_python.converter import CurrencyRates


def converter():
    try:
        valor_em_reais = float(entry_reais.get())

        c = CurrencyRates()
        taxa_de_cambio = c.get_rate('BRL', 'USD')
        valor_em_dolares = valor_em_reais / taxa_de_cambio

        label_resultado.config(text=f"Valor em dólares: {valor_em_dolares:.2f}")
    except ValueError:
        label_resultado.config(text="Por favor, insira um valor válido.")

root = tk.Tk()
root.title("Conversor de Real para Dólar")

label_reais = tk.Label(root, text="Valor em Reais:")
label_reais.grid(row=0, column=0, padx=20, pady=30)

entry_reais = tk.Entry(root,)
entry_reais.grid(row=0, column=1, padx=30, pady=30)

botao_converter = tk.Button(root, text="Converter", command=converter,background='cyan',)
botao_converter.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

label_resultado = tk.Label(root, text="")
label_resultado.grid(row=2, column=0, columnspan=2, padx=30, pady=30)

root.mainloop()
