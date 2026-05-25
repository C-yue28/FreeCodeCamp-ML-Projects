import random

my_history = []
opp_history = []
pattern_memory = {}
counters = {"R": "P", "P": "S", "S": "R"}

def player(prev_play):
    if prev_play != "":
        opp_history.append(prev_play)
        
        window_size = 4
        if len(my_history) > window_size:
            past_my = my_history[-(window_size+1):-1]
            past_opp = opp_history[-(window_size+1):-1]
            
            state_key = ",".join(m+o for m, o in zip(past_my, past_opp))
            opp_next_action = opp_history[-1]
            
            if state_key not in pattern_memory:
                pattern_memory[state_key] = {"R": 0, "P": 0, "S": 0}
            pattern_memory[state_key][opp_next_action] += 1

    if len(opp_history) < 5:
        guess = random.choice(["R", "P", "S"])
        my_history.append(guess)
        return guess

    prediction = None
    for current_window in range(4, 0, -1):
        recent_my = my_history[-current_window:]
        recent_opp = opp_history[-current_window:]
        current_state = ",".join(m+o for m, o in zip(recent_my, recent_opp))
        
        if current_state in pattern_memory:
            prediction = max(pattern_memory[current_state], key=pattern_memory[current_state].get)
            break 

    if not prediction:
        prediction = max(set(opp_history), key=opp_history.count)

    guess = counters[prediction]
    my_history.append(guess)
    return guess