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


def regex_to_nfa(regex):
    stack = []
    for char in regex:
        if char.isalnum():
            stack.append(create_basic_nfa(char))
        elif char == '*':
            nfa = stack.pop()
            stack.append(kleene_star(nfa))
        elif char == '.':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            stack.append(concatenate(nfa1, nfa2))
        elif char == '|':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            stack.append(union(nfa1, nfa2))

    return stack.pop() if stack else None




#if __name__ == "__main__":
  #  regex = "a.b|c*"
 #   nfa = regex_to_nfa(regex)
   # print(f"Start State: {nfa.start_state.name}")
    #print(f"Final State: {nfa.final_state.name}")
    #for state in nfa.states:
        #for symbol, transitions in state.transitions.items():
          #  for transition_state in transitions:
                #print(f"{state.name} --{symbol}--> {transition_state.name}")
