"""
DFS and BSF

https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/graphtheory/EulerianPathDirectedEdgesAdjacencyList.java

https://www.youtube.com/watch?v=8MpoO2zA2l4

A graph is represented as an adjacency list: graph[i] - is a list of nodes for given vertex i.
For example:

0 -> 1 -> 2 -> 3 -> 1

.........|

.........V

..........4

is represented as
[[1], [2], [3, 4], [1], []]
for node 0, there is an edge (0, 1); for node 2, there are edges (2, 3) and (2, 4); for node 4, there are no edges.
"""


def build_sample_graph():
    graph_list = [None] * 7

    graph_list[0] = [1, 6]
    graph_list[1] = [2]
    graph_list[2] = [3]
    graph_list[3] = [4, 0]
    graph_list[4] = [5]
    graph_list[5] = [0]
    graph_list[6] = [3]

    return graph_list


def array_to_string(array):
    res = ''
    size = len(array)
    for i in range(0, size - 1):
        res = str(array[i]) + ', '

    res = res + str(array[size - 1])
    return res


def print_graph(graph):
    n_nodes = len(graph)
    for i in range(0, n_nodes):
        nodes_str = array_to_string(graph[i])
        print(str(i) + ' -> ' + nodes_str)


def visit_node_implementation(node):
    """Visits a node in graph traversal (search)."""
    print(str(node))


def bsf(graph, visit_node, starting_node=0):
    """
    Performs breadth-first search algorithm on the graph.
    Note, here we visit edges, so it is OK for us to visit the same node more than once.
    """

    visited_edges = set()

    # next node to be visited at the head of the queue.
    queue = []

    next_nodes = graph[starting_node]

    visit_node(starting_node)
    for node in next_nodes:
        visited_edges.add((starting_node, node))
        queue.append(node)

    while len(queue) > 0:
        visited_node = queue.pop(0)

        # visit node
        visit_node(visited_node)
        next_nodes = graph[visited_node]

        for node in next_nodes:
            if not (visited_node, node) in visited_edges:
                queue.append(node)
                visited_edges.add((visited_node, node))


def dsf(graph, visit_node, starting_node=0):
    """
    Performs depth-first search algorithm on the graph.
    Note, here we visit edges, so it is OK for us to visit the same node more than once.
    """

    visited_edges = set()

    # next node to be visited is the last inserted element of the stack.
    stack = []

    next_nodes = graph[starting_node]

    visit_node(starting_node)
    for node in next_nodes:
        stack.append((starting_node, node))

    while len(stack) > 0:
        visited_edge = stack.pop()
        if visited_edge in visited_edges:
            continue

        visited_node = visited_edge[1]

        # visit node
        visit_node(visited_node)
        visited_edges.add(visited_edge)

        next_nodes = graph[visited_node]

        for node in next_nodes:
            if not (visited_node, node) in visited_edges:
                stack.append((visited_node, node))


def graph_demo():
    graph = build_sample_graph()
    print_graph(graph)
    print('\n\n')
    dsf(graph, visit_node_implementation)


def main():
    graph_demo()


if __name__ == "__main__":
    main()
