from queue import *
import draw as draw

def breadth_first_search(graph, start):
    print("\nbreadth_first_search:\n")
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start[0]] = None
    while not frontier.empty():
        current = frontier.get()

        if (check_valid(current[0])):
            break

        for next in graph.neighbors(current):
            if next[0] not in came_from:
                frontier.put(next)
                came_from[next[0]] = current[0]
    draw.print_result(graph, frontier, came_from)
    # return came_from

def dijkstra_search(graph, start):
    print("\ndijkstra_search:\n")
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start[0]] = None
    # mask = create_mask(graph)
    level = {}
    level[start[0]] = 0
    
    while not frontier.empty():
        current = frontier.get()
        current_level = level[current[0]] + 1

        if (check_valid(current[0])):
            # graph.draw(current[0])
            break
        
        for next in graph.neighbors(current):
            if next[0] not in came_from:
                # priority_match = match_priority(next[0], graph, mask)
                # priority_dist = manhattan_distance(next[0], graph, mask)
                frontier.put(next, current_level)
                came_from[next[0]] = current[0]
                level[next[0]] = current_level
    draw.print_result(graph, frontier, came_from)
    # return came_from

def gready_search(graph, start, heuristic):
    print("\ngready_search:\n")
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start[0]] = None
    # mask = create_mask(graph)
    
    while not frontier.empty():
        current = frontier.get()

        if (check_valid(current[0])):
            break
        
        for next in graph.neighbors(current):
            if next[0] not in came_from:
                priority = heuristic(next[0], graph)
                # priority_match = match_priority(next[0], graph)
                # priority_dist = manhattan_distance(next[0], graph)
                # print(priority_match)
                # print(priority_dist)
                frontier.put(next, priority)
                came_from[next[0]] = current[0]
    draw.print_result(graph, frontier, came_from)
    # return came_from

def a_star(graph, start, heuristic):
    print("\nA*:\n")
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start[0]] = None
    # mask = create_mask(graph)
    cost = {}
    cost[start[0]] = 0
    
    while not frontier.empty():
        current = frontier.get()
        current_cost = cost[current[0]] + 1

        if (check_valid(current[0])):
            break
        
        for next in graph.neighbors(current):
            # priority_match = match_priority(next[0], graph)
            # priority_dist = heuristic(next[0], graph)
            priority = heuristic(next[0], graph)
            if (next[0] not in came_from or
                priority + current_cost < cost[next[0]]):
                # print(priority_match)
                # print(priority_dist)
                frontier.put(next, priority + current_cost)
                came_from[next[0]] = current[0]
                cost[next[0]] = current_cost + priority
    draw.print_result(graph, frontier, came_from)
    # return came_from

def check_valid(state):
    new_list = list(state)
    new_list.pop()
    result = [i for i in range(1, len(new_list) + 1)]
    return new_list == result

# def create_mask(graph):
#     mask = {}
#     state = graph.final_state
#     mask[0] = state[0]
#     counter = 1
#     while (counter < graph.size):
#         mask[graph.size * counter] = state[graph.size * counter]
#         mask[counter] = state[counter]
#         counter += 1
#     return mask

