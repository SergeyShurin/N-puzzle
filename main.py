import graph as graph
import bfs_algo as bfs
import sys
import re
import heuristic as h

arguments = sys.argv[1:]
arg_count = len(arguments)
if (arg_count == 0):
    a = 0
elif (arg_count == 1):
    fd = open(arguments[0], 'r')
    content = fd.read()
    content = re.sub(r'(?m)#.*\n?', '\n', content).split()
    size = int(content[0])
    initial_state_array = content[1::]
    if (len(initial_state_array) == size * size):       
        initial_state = []
        for elem in initial_state_array:
            initial_state.append(int(elem))
        initial_state = tuple(initial_state)
        zero_index = initial_state.index(0)
    else:
        print("Invalid format")
else:
    print("Usage: python3 main.py [file_name]")


example_graph = graph.Graph(initial_state, size, zero_index)

came_from = bfs.breadth_first_search(example_graph, (initial_state, zero_index))
came_from = bfs.dijkstra_search(example_graph, (initial_state, zero_index))
came_from = bfs.gready_search(
    example_graph,
    (initial_state, zero_index),
    h.manhattan_distance)
came_from = bfs.gready_search(
    example_graph,
    (initial_state, zero_index),
    h.match_priority)
came_from = bfs.a_star(example_graph,
    (initial_state, zero_index),
    h.manhattan_distance)
came_from = bfs.a_star(example_graph,
    (initial_state, zero_index),
    h.match_priority)


# example_graph.strip()

