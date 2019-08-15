
def draw_path(graph, parents, start):
    counter = 0
    while (parents[start] != None):
        counter += 1
        # graph.draw(start)
        start = parents[start]
    print('{:<41} {}'.format("Number of moves required to transition", counter))

def print_result(graph, opened_set, general_set):
    draw_path(graph, general_set, graph.final_state)
    print('{:<41} {}'.format("Total number of states in the opened set", opened_set.len()))
    print('{:<41} {}'.format("Maximum number of states in memory", len(general_set)))