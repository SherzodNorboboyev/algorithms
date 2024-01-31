from collections import deque

def breadth_first(source: dict, start, end):
    queue = deque()
    queue += source[start]

    while queue:
        elem = queue.popleft()

        if elem == end:
            print(f'Found end {end}')
            return True
        else:
            queue += source.get(elem, [])
    return False

def dijkstra_algo(source: dict, start, end):
    raise ValueError('Not finished')
    def find_min_cost(costs):
        mn = float('inf')
        mn_node = None

        for node in costs:
            cost = costs.get(node, float('inf'))
            if cost < mn and node not in used:
                mn = cost
                mn_node = node

        return mn_node


    costs = {}
    parents = {}
    used = []

    for node in source[start].keys():
        costs[node] = source[start][node]

    node = find_min_cost(source[start])

    while node is not None:
        neighbors = source[node]
        cost = costs.get(node, float('inf'))

        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]

            if costs.get(neighbor, float('inf')) > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node

        used.append(node)
        node = find_min_cost(costs)


if __name__ == '__main__':
    # source = {
    #     'A': ['B', 'C', 'D'],
    #     'D': ['C', 'G', 'H'],
    #     'C': ['E', 'F', 'G'],
    #     'E': [],
    #     'F': ['I', 'J'],
    #     'G': [],
    #     'H': [],
    #     'I': [],
    #     'J': [],
    # }
    # breadth_first(source=source, start='A', end='E')

    source = {
        'A': ['B', 'C', 'D'],
        'D': ['C', 'G', 'H'],
        'C': ['E', 'F', 'G'],
        'E': [],
        'F': ['I', 'J'],
        'G': [],
        'H': [],
        'I': [],
        'J': [],
    }

    source = {}

    source['A'] = {}
    source['A']['B'] = 2
    source['A']['C'] = 6

    source['B'] = {}
    source['B']['D'] = 4
    source['B']['C'] = 3

    source['C'] = {}
    source['C']['D'] = 5
    source['C']['E'] = 6

    source['D'] = {}
    source['D']['F'] = 5

    source['E'] = {}
    source['E']['F'] = 0

    source['F'] = {}


    dijkstra_algo(source=source, start='A', end='E')
