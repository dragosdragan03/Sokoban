from collections import defaultdict

def lrta_star(initial_state, heuristic_function):

    h_table = {}

    visit_count = defaultdict(int)
    visit_count[str(initial_state)] += 1

    current_state = initial_state
    path = [current_state]

    iteration = 0
    expansion_count = 0

    while not current_state.is_solved():
        iteration += 1
        neighbors = current_state.get_neighbours()

        if not neighbors:
            return None

        # Check if the current state is in h_table
        current_state_str = str(current_state)
        if current_state_str not in h_table:
            expansion_count += 1
            h_table[current_state_str] = heuristic_function(current_state)

        min_f = float('inf')
        candidates = []

        for neighbor in neighbors:
            state_str = str(neighbor)
            if state_str not in h_table:
                expansion_count += 1
                h_table[state_str] = heuristic_function(neighbor)

        # Find the neighbors with minimum f-value
        for neighbor in neighbors:
            neighbor_str = str(neighbor)
            f_value = 1 + h_table[neighbor_str]

            if f_value < min_f:
                min_f = f_value
                candidates = [neighbor]
            elif f_value == min_f:
                candidates.append(neighbor)

        # pick the one with lowest visit count from candidates
        best_neighbor = min(candidates, key=lambda n: visit_count[str(n)])

        h_table[current_state_str] = min_f

        # Move to the best neighbor
        current_state = best_neighbor
        visit_count[str(current_state)] += 1

        path.append(current_state)

        if iteration % 200 == 0:
            path = []
            current_state = initial_state

    return path, iteration, expansion_count