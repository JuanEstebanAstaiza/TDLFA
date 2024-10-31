from regex_to_nfa import regex_to_nfa
from nfa_to_dfa import nfa_to_dfa
from validate import validate_string
from error_handling import validate_regex, RegexError

def main():
    regex = input("Introduce la expresión regular: ")
    try:
        validate_regex(regex)
        nfa = regex_to_nfa(regex)
        dfa = nfa_to_dfa(nfa)
        string = input("Introduce la cadena para validar: ")
        if validate_string(dfa, string):
            print("La cadena es aceptada.")
        else:
            print("La cadena no es aceptada.")
    except RegexError as e:
        print(f"Error en la expresión regular: {e}")

if __name__ == "__main__":
    main()
