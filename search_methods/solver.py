from sokoban.map import Map

from search_methods.lrta_star import lrta_star
from search_methods.beam_search import beam_search
from search_methods.heuristic import calculate_distances

class Solver:

    def __init__(self, map: Map) -> None:
        self.map = map

    def solve(self):
        raise NotImplementedError

    @staticmethod
    def reconstruct_path(initial_state, solution_state, parents):
        path = [solution_state]
        current_str = solution_state
        initial_str = str(initial_state)

        while current_str != initial_str:
            parent_str = parents[current_str]
            path.append(parent_str)
            current_str = parent_str

        path.reverse()

        return path

    def solve_lrta_star(self):
        return lrta_star(self.map, calculate_distances)

    def solve_beam_search(self):
        return beam_search(self.map, 99, calculate_distances, self.reconstruct_path)


