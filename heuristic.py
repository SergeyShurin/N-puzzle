def match_priority(state, graph):
    new_list = list(state)
    dist = len(state)
    counter = 1
    while (counter < len(state) - 1):
        if (state[counter - 1] == counter):
            dist -= 1
        # else: return dist
        counter += 1
    return dist

def linear_conflict(state, graph, mask):
    for elem in mask:
        if (state[elem] != mask[elem] and state[elem] != 0): return 1
    return 0

def manhattan_distance(state, graph):
    # graph.draw(state)
    mask = dict(enumerate(graph.final_state))
    
    # counter = 0
    dist = 0
    # graph.draw(state)
    for elem in mask:
        # counter += 1
        # print("on position", elem, "should", mask[elem], "current", state[elem])
        cur_pos = state.index(mask[elem])
        # print(mask[elem], "on position", cur_pos)
        pos1 = elem
        pos2 = cur_pos
        x1, y1 = pos1 % graph.size, pos1 // graph.size
        x2, y2 = pos2 % graph.size, pos2 // graph.size
        dist1 = abs(x1 - x2)
        dist2 = abs(y1 - y2)
        # if dist1 == 1: dist1 = 0
        # if dist2 == 1: dist2 = 0
        if (dist1 + dist2 == 1 and state[elem] != 0): dist += 2 
        dist += dist1 + dist2
        # print("distacse between ", pos1, "(", y1, x1, ") and", pos2, "(", y2, x2, ") =", abs(x1 - x2) + abs(y1 - y2))
    return dist


# def manhattan_distance(state, graph, mask):
#     # graph.draw(state)
#     new_list = list(state)
#     # print(mask)
#     # counter = 0
#     dist = 0
#     # graph.draw(state)
#     for elem in mask:
#         # counter += 1
#         # print("on position", elem, "should", mask[elem], "current", state[elem])
#         cur_pos = state.index(mask[elem])
#         # print(mask[elem], "on position", cur_pos)
#         pos1 = elem
#         pos2 = cur_pos
#         x1, y1 = pos1 % graph.size, pos1 // graph.size
#         x2, y2 = pos2 % graph.size, pos2 // graph.size
#         dist1 = abs(x1 - x2)
#         dist2 = abs(y1 - y2)
#         # if dist1 == 1: dist1 = 0
#         # if dist2 == 1: dist2 = 0
#         if (dist1 + dist2 == 1 and state[elem] != 0): dist += 2 
#         dist += dist1 + dist2
#         # print("distace between ", pos1, "(", y1, x1, ") and", pos2, "(", y2, x2, ") =", abs(x1 - x2) + abs(y1 - y2))
#     return dist
