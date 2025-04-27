def beam_search(map, k, heuristic_function, reconstruct_path):
    state_list = map.get_neighbours()

    parents = {}
    iteration = 0

    # Add initial states to the parent map
    for state in state_list:
        state_str = str(state)
        parents[state_str] = str(map)

    expansion_count = 0
    while True:
        iteration += 1
        cand_list = []

        for state in state_list:
            state_str = str(state)

            # Check if current state is a solution
            if state.is_solved():
                return reconstruct_path(map, state_str, parents), iteration, expansion_count

            # Get all neighbors of the current state
            neighbours = state.get_neighbours()

            for neighbour in neighbours:
                neighbour_str = str(neighbour)

                if neighbour_str not in parents:
                    expansion_count += 1
                    parents[neighbour_str] = state_str
                    cand_list.append(neighbour)

                if neighbour.is_solved():
                    return reconstruct_path(map, neighbour_str, parents), iteration, expansion_count


        # Sort candidates based on the heuristic function
        cand_list.sort(key=lambda x: heuristic_function(x))
        state_list = cand_list[:min(k, len(cand_list))]
