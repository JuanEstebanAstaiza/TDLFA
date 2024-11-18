class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}
        self.is_final = False

    def add_transition(self, symbol, state):
        if symbol not in self.transitions:
            self.transitions[symbol] = []
        self.transitions[symbol].append(state)


class NFA:
    def __init__(self):
        self.start_state = None
        self.final_state = None
        self.states = []

    def add_state(self, state):
        self.states.append(state)

    def set_start_state(self, state):
        self.start_state = state

    def set_final_state(self, state):
        state.is_final = True
        self.final_state = state


def create_basic_nfa(symbol):
    start = State('start')
    end = State('end')
    start.add_transition(symbol, end)

    nfa = NFA()
    nfa.add_state(start)
    nfa.add_state(end)
    nfa.set_start_state(start)
    nfa.set_final_state(end)
    return nfa


def concatenate(nfa1, nfa2):
    nfa1.final_state.is_final = False
    nfa1.final_state.add_transition(None, nfa2.start_state)

    concatenated_nfa = NFA()
    concatenated_nfa.start_state = nfa1.start_state
    concatenated_nfa.final_state = nfa2.final_state
    concatenated_nfa.states = nfa1.states + nfa2.states
    return concatenated_nfa


def union(nfa1, nfa2):
    start = State('start')
    end = State('end')

    start.add_transition(None, nfa1.start_state)
    start.add_transition(None, nfa2.start_state)
    nfa1.final_state.add_transition(None, end)
    nfa2.final_state.add_transition(None, end)

    nfa1.final_state.is_final = False
    nfa2.final_state.is_final = False

    union_nfa = NFA()
    union_nfa.add_state(start)
    union_nfa.add_state(end)
    union_nfa.states += nfa1.states + nfa2.states
    union_nfa.set_start_state(start)
    union_nfa.set_final_state(end)
    return union_nfa


def kleene_star(nfa):
    start = State('start')
    end = State('end')

    start.add_transition(None, nfa.start_state)
    start.add_transition(None, end)
    nfa.final_state.add_transition(None, nfa.start_state)
    nfa.final_state.add_transition(None, end)

    nfa.final_state.is_final = False

    kleene_nfa = NFA()
    kleene_nfa.add_state(start)
    kleene_nfa.add_state(end)
    kleene_nfa.states += nfa.states
    kleene_nfa.set_start_state(start)
    kleene_nfa.set_final_state(end)
    return kleene_nfa

def infix_to_postfix(infix):
    precedence = {'*': 3, '.': 2, '|': 1}
    output = []
    stack = []
    previous_char = None

    for char in infix:
        if char.isalnum():
            if previous_char and (previous_char.isalnum() or previous_char == '*' or previous_char == ')'):
                # Insertar concatenación implícita
                while stack and stack[-1] not in '()|' and precedence['.'] <= precedence[stack[-1]]:
                    output.append(stack.pop())
                stack.append('.')
            output.append(char)
        elif char == '(':
            if previous_char and (previous_char.isalnum() or previous_char == '*' or previous_char == ')'):
                # Insertar concatenación implícita antes de '('
                while stack and precedence['.'] <= precedence[stack[-1]]:
                    output.append(stack.pop())
                stack.append('.')
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Sacar el '('
        else:  # | o *
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)
        previous_char = char

    while stack:
        output.append(stack.pop())

    return ''.join(output)


def regex_to_nfa(postfix):
    stack = []
    for char in postfix:
        print(f"Procesando carácter: {char}")  # Depuración
        if char.isalnum():
            nfa = create_basic_nfa(char)
            stack.append(nfa)
            print(f"NFA creado para símbolo: {char}")
        elif char == '*':
            if stack:
                nfa = stack.pop()
                stack.append(kleene_star(nfa))
                print("Aplicada estrella de Kleene.")
        elif char == '.':
            if len(stack) >= 2:
                nfa2 = stack.pop()
                nfa1 = stack.pop()
                concatenated_nfa = concatenate(nfa1, nfa2)
                stack.append(concatenated_nfa)
                print("NFA concatenado.")
        elif char == '|':
            if len(stack) >= 2:
                nfa2 = stack.pop()
                nfa1 = stack.pop()
                union_nfa = union(nfa1, nfa2)
                stack.append(union_nfa)
                print("NFA unido (OR).")

    # Depuración: Verificar los estados y transiciones del NFA resultante
    if stack:
        nfa = stack[-1]
        print("\nResumen de estados del NFA:")
        for state in nfa.states:
            for symbol, transitions in state.transitions.items():
                for next_state in transitions:
                    print(f"{state.name} --{symbol}--> {next_state.name}")
        return nfa
    else:
        print("Error: la pila está vacía, no se pudo construir el NFA.")
        return None











