def validate_string(dfa, string):
    current_state = dfa.start_state
    for char in string:
        if char in current_state.transitions:
            current_state = current_state.transitions[char]
        else:
            return False
    return current_state in dfa.final_states
