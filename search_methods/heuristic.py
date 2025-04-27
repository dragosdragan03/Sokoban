import sys

# verify the neighbours. if the position has minimum 2 walls around it, it is not a valid cell
def is_valid_cell(map_instance, position):
    x, y = position
    # Check if the position is an obstacle (wall)
    if (x, y) in map_instance.obstacles:
        return False

    north_wall = (x+1, y) in map_instance.obstacles or x+1 >= map_instance.length
    south_wall = (x-1, y) in map_instance.obstacles or x-1 < 0
    east_wall = (x, y+1) in map_instance.obstacles or y+1 >= map_instance.width
    west_wall = (x, y-1) in map_instance.obstacles or y-1 < 0

    # North-South opposite walls are allowed
    if north_wall and south_wall and not east_wall and not west_wall:
        return True

    # East-West opposite walls are allowed
    if east_wall and west_wall and not north_wall and not south_wall:
        return True

    # Count the total walls
    wall_count = sum([north_wall, south_wall, east_wall, west_wall])

    # If there are fewer than 2 walls, it's valid
    if wall_count < 2:
        return True

    return False

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# function to calculate the box in wich target to go
# each box it will have a target
def box_target_distance(map_instance):
    box_shortest_distances = {}
    for box_name, box in map_instance.boxes.items():

        if not is_valid_cell(map_instance, (box.x, box.y)):
            box_shortest_distances[box_name] = sys.maxsize
            continue

        shortest_distance = float('inf')

        for target in map_instance.targets:
            distance = manhattan_distance((box.x, box.y), target)
            if distance < shortest_distance:
                shortest_distance = distance

        box_shortest_distances[box_name] = shortest_distance

    return box_shortest_distances

# the minimm distance to each box
def player_box_distance(map_instance):
    player_box_distances = {}
    for box_name, box in map_instance.boxes.items():
        player_box_distances[box_name] = manhattan_distance((map_instance.player.x, map_instance.player.y), (box.x, box.y))

    return player_box_distances

# this function return the sum all of the distances
def calculate_distances(stare):
    box_target = box_target_distance(stare) # each box where should be placed
    player_box = player_box_distance(stare) # each box distance to player

    total_distance = 0

    for box_name, box in stare.boxes.items():

        box_pos = (box.x, box.y)
        box_target_dist = box_target[box_name]
        player_box_dist = player_box[box_name] * 1.5

        if box_pos in stare.targets:
            continue

        # Calculate the distance from the player to the box and then to the target
        total_distance += box_target_dist + player_box_dist

    return total_distance