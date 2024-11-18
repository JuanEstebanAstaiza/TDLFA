class DFAState:
    def __init__(self, name, nfa_states):
        self.name = name
        self.nfa_states = nfa_states
        self.transitions = {}
        self.is_final = any(state.is_final for state in nfa_states)

    def add_transition(self, symbol, state):
        self.transitions[symbol] = state

class DFA:
    def __init__(self):
        self.start_state = None
        self.states = []
        self.state_dict = {}

    def add_state(self, state):
        self.states.append(state)
        self.state_dict[frozenset(state.nfa_states)] = state

    def get_state(self, nfa_states):
        return self.state_dict.get(frozenset(nfa_states))

    def set_start_state(self, state):
        self.start_state = state

    def get_unmarked_state(self):
        for state in self.states:
            if not hasattr(state, 'marked'):
                return state
        return None

def epsilon_closure(nfa_states):
    stack = list(nfa_states)
    closure = set(nfa_states)

    while stack:
        state = stack.pop()
        if None in state.transitions:
            for next_state in state.transitions[None]:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)

    return closure

def move(nfa_states, symbol):
    result = set()
    for state in nfa_states:
        if symbol in state.transitions:
            result.update(state.transitions[symbol])
    return result

def nfa_to_dfa(nfa):
    dfa = DFA()

    # Cálculo del cierre epsilon para el estado inicial del NFA
    initial_closure = epsilon_closure([nfa.start_state])
    start_state = DFAState('q0', initial_closure)
    dfa.add_state(start_state)
    dfa.set_start_state(start_state)

    print(f"Estado inicial DFA: {start_state.name}, contiene NFA states: {[state.name for state in initial_closure]}")

    unmarked_states = [start_state]
    state_count = 1

    # Iterar sobre los estados no marcados
    while unmarked_states:
        current_dfa_state = unmarked_states.pop(0)
        current_dfa_state.marked = True
        print(f"Procesando estado DFA: {current_dfa_state.name}")

        # Recolectar todos los símbolos posibles de las transiciones de los estados NFA en el estado DFA actual
        symbols = set()
        for state in current_dfa_state.nfa_states:
            for symbol in state.transitions:
                if symbol is not None:  # Ignorar transiciones epsilon
                    symbols.add(symbol)

        # Procesar cada símbolo y crear nuevos estados del DFA si es necesario
        for symbol in symbols:
            next_nfa_states = epsilon_closure(move(current_dfa_state.nfa_states, symbol))
            print(f"Transición con símbolo '{symbol}' lleva a NFA states: {[state.name for state in next_nfa_states]}")

            if next_nfa_states:
                existing_state = dfa.get_state(next_nfa_states)

                if existing_state is None:
                    new_state = DFAState(f'q{state_count}', next_nfa_states)
                    dfa.add_state(new_state)
                    unmarked_states.append(new_state)  # Añadir a la lista de estados no marcados
                    current_dfa_state.add_transition(symbol, new_state)
                    print(f"Nuevo estado DFA creado: {new_state.name}, contiene NFA states: {[state.name for state in next_nfa_states]}")
                    state_count += 1
                else:
                    current_dfa_state.add_transition(symbol, existing_state)
                    print(f"Estado DFA existente encontrado: {existing_state.name}, reutilizado.")

    print("\nResumen de estados del DFA:")
    for state in dfa.states:
        print(f"Estado DFA: {state.name}, es final: {state.is_final}")
        for symbol, next_state in state.transitions.items():
            print(f"  {state.name} --{symbol}--> {next_state.name}")

    return dfa




# Ejemplo de uso
#if __name__ == "__main__":
 #   from regex_to_nfa import regex_to_nfa

  #  regex = "a.b|c*"
   # nfa = regex_to_nfa(regex)
    #dfa = nfa_to_dfa(nfa)

    #print(f"Start State: {dfa.start_state.name}")
    #for state in dfa.states:
     #   for symbol, transition_state in state.transitions.items():
      #      print(f"{state.name} --{symbol}--> {transition_state.name}")
       # if state.is_final:
        #    print(f"{state.name} es un estado final.")
