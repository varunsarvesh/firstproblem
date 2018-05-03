graph = {
    'n': ['e', 's', 't'],
    'e': ['t', 'c'],
    'c': [],
    't': [],
    's': []
}


def allpaths(graph, start, path=[]):
    path = path + [start]
    for node in graph[start]:
        allpaths(graph, node, path)
    else:
        n = path[len(path) - 1]
        if len(graph[n]) == 0:
            if path[len(path) - 1] == 'c' or path[len(path) - 1] == 't':
                print(path, " initial to final is possible ")
            else:
                print(path, " initial to final is not possible ")


allpaths(graph, 'n')