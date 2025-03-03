Graph = [[0, 5], [1, 2], [3, 4],[2, 3], [3, 0], [11, 13], [13, 15], [11, 17]]

def add_edge(initial_node, connect_node):
    Graph.append([initial_node, connect_node])

def check_link(a, b, graph):
    start = a
    end = b
    position = start
    path = list()
    while position != end:
        for i in graph:
            if position in i:
                path.append(position)
                graph.remove(i)
                if end in i:
                    return "YES", path
                i.remove(position)
                position = int(i[0]) 
            elif position not in set(i for l in graph for i in l):
                position = path[-1]
                path.remove(path[-1])
                if path == [] and position not in set(i for l in graph for i in l):
                    return 'Узлы не связаны'

    return 0

print(check_link(0, 4, Graph))