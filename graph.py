class Graph:
    def __init__(self, initial_state, size, zero_pos):
        self.state = initial_state
        self.nodes = {}
        self.size = size
        self.zero = zero_pos
        self.final_state = self.__get_final_state()

    def __get_final_state(self):
        state = [i for i in range(1, self.size * self.size + 1)]
        state[self.size * self.size - 1] = 0
        return tuple(state)

    def __swap(self, to, zero, state):
        l = list(state)
        l[to], l[zero] = l[zero], l[to]
        return (tuple(l), to)

    def drop(mylist, n):
        del mylist[0::n]
        print(mylist)

    def strip(self):
        counter = 0
        final_state = list(self.final_state[self.size:])
        final_state = [item for index, item in enumerate(final_state) if index % self.size != 0]
        counter = 0
        initial_state = list(self.final_state[self.size:])
        initial_state = [item for index, item in enumerate(initial_state) if index % self.size != 0]
        self.size -= 1
        self.final_state = final_state
        self.initial_state = initial_state
        # self.draw(self.final_state)
        # self.draw(self.initial_state)

    def draw(self, node):
        i = 0
        while i < len(node):
            print(node[i], end=' ' if ((i + 1) % self.size) else '\n')
            i += 1
        print('')

    def neighbors(self, state):
        zero = state[1]
        neighbors = []
        results = []
        if (zero // self.size != 0):
            results.append(zero - self.size)
        if (zero // self.size != self.size - 1):
            results.append(zero + self.size)
        if (zero % self.size):
            results.append(zero - 1)
        if (zero % self.size != self.size - 1):
            results.append(zero + 1)
        for res in results:
            neighbors.append(self.__swap(res, zero, state[0]))
        self.nodes[state[0]] = neighbors
        return neighbors




class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}
    
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)