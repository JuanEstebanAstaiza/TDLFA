import tkinter as tk
from tkinter import ttk, messagebox
from regex_to_nfa import regex_to_nfa, infix_to_postfix  # Importamos las funciones que ya creamos
from nfa_to_dfa import nfa_to_dfa  # Asumiendo que el código nfa_to_dfa también está implementado
from validate import validate_string  # Para validar cadenas con el DFA
from error_handling import validate_regex, RegexError  # Para validar la expresión regular

def validate_input():
    regex = regex_entry.get()
    test_strings = text_input.get("1.0", tk.END).strip().split("\n")

    if not regex:
        messagebox.showerror("Error", "Por favor, ingrese una expresión regular.")
        return

    try:
        # Validar la expresión regular (esto podría ser una verificación de sintaxis)
        validate_regex(regex)

        # Convertir la expresión regular de infija a postfija
        postfix = infix_to_postfix(regex)
        print(f"Expresión postfija: {postfix}")

        # Construir el NFA usando la expresión postfija
        nfa = regex_to_nfa(postfix)

        if not nfa:
            messagebox.showerror("Error en la Construcción", "No se pudo construir el NFA correctamente.")
            return

        # Convertir el NFA a DFA
        dfa = nfa_to_dfa(nfa)

        if not dfa:
            messagebox.showerror("Error en la Construcción", "No se pudo construir el DFA correctamente.")
            return

        # Limpiar el área de resultados
        results.delete("1.0", tk.END)

        # Validar las cadenas de entrada usando el DFA construido
        for string in test_strings:
            print(f"Validando cadena: '{string}'")  # Depuración para ver la cadena completa
            is_accepted = validate_string(dfa, string)
            result = f"'{string}': {'Aceptada' if is_accepted else 'Rechazada'}\n"
            results.insert(tk.END, result)

    except RegexError as e:
        messagebox.showerror("Error en la Expresión Regular", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {str(e)}")

# Crear la ventana principal
root = tk.Tk()
root.title("Validador de Expresiones Regulares")

# Etiqueta y entrada para la expresión regular
ttk.Label(root, text="Expresión Regular:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
regex_entry = ttk.Entry(root, width=50)
regex_entry.grid(row=0, column=1, padx=10, pady=5)

# Etiqueta y área de texto para las cadenas de entrada
ttk.Label(root, text="Cadenas a Validar (una por línea):").grid(row=1, column=0, padx=10, pady=5, sticky="nw")
text_input = tk.Text(root, width=50, height=10)
text_input.grid(row=1, column=1, padx=10, pady=5)

# Botón de validación
validate_button = ttk.Button(root, text="Validar", command=validate_input)
validate_button.grid(row=2, column=1, padx=10, pady=5, sticky="e")

# Etiqueta y área de texto para mostrar los resultados
ttk.Label(root, text="Resultados:").grid(row=3, column=0, padx=10, pady=5, sticky="nw")
results = tk.Text(root, width=50, height=10, state="normal")
results.grid(row=3, column=1, padx=10, pady=5)

# Iniciar la aplicación
root.mainloop()
