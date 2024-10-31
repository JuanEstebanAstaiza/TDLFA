class RegexError(Exception):
    def __init__(self, message):
        super().__init__(message)

def validate_regex(regex):
    # Implementación para validar la estructura de la expresión regular
    if not regex:  # Ejemplo de validación simple
        raise RegexError("La expresión regular está vacía.")
