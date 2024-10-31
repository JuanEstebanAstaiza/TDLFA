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

    initial_closure = epsilon_closure([nfa.start_state])
    start_state = DFAState('q0', initial_closure)
    dfa.add_state(start_state)
    dfa.set_start_state(start_state)

    unmarked_state = dfa.get_unmarked_state()
    state_count = 1

    while unmarked_state is not None:
        unmarked_state.marked = True
        for symbol in set(symbol for state in unmarked_state.nfa_states for symbol in state.transitions if symbol is not None):
            next_nfa_states = epsilon_closure(move(unmarked_state.nfa_states, symbol))
            existing_state = dfa.get_state(next_nfa_states)

            if existing_state is None:
                new_state = DFAState(f'q{state_count}', next_nfa_states)
                dfa.add_state(new_state)
                unmarked_state.add_transition(symbol, new_state)
                state_count += 1
            else:
                unmarked_state.add_transition(symbol, existing_state)

        unmarked_state = dfa.get_unmarked_state()

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
