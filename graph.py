from typing import Mapping, NewType

Graph = NewType('Graph', Mapping[str, list[str]])


def bsf(graph: Graph, node: str) -> list:
    '''
    Breath First Search
    `NOTE`: order of keys in param `graph` will affected the result
    '''
    result = []
    visited = []
    queue = []

    # add first node
    visited.append(node)
    queue.append(node)

    while queue:
        # remove queue and add to result
        result.append(queue.pop(0))

        # find next nodes
        for neighbor in graph:

            # skip when next node visited
            if neighbor in visited:
                continue

            # mark as visited and add it to queue
            visited.append(neighbor)
            queue.append(neighbor)

    return visited


def dsf(graph: Graph, node: str) -> list:
    '''
    Deep First Search
    `NOTE`: order of keys in param `graph` won't affected the result
    '''

    # mark current node as visited
    visited = []
    visited.insert(0, node)

    # find next nodes of current node
    for neighbor in graph[node]:

        # merge all visited nodes
        visited += dsf(graph, neighbor)

    return visited


def get_first_node(graph: Graph) -> str:
    '''
    Get the first key of object `graph`
    '''
    return list(graph.keys())[0]
