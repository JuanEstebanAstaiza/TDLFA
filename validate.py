def validate_string(dfa, string):
    current_state = dfa.start_state
    print(f"Estado inicial: {current_state.name}")

    for char in string:
        print(f"Procesando carácter: {char}")
        if char in current_state.transitions:
            current_state = current_state.transitions[char]
            print(f"Transición a estado: {current_state.name}")
        else:
            print("No se encontró una transición para este carácter. Cadena no aceptada.")
            return False

    if current_state.is_final:
        print("Cadena aceptada.")
        return True
    else:
        print("Cadena no aceptada. Estado actual no es final.")
        return False
