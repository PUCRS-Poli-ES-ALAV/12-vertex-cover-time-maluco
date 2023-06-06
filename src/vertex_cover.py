import itertools

from graph import Graph


def vertex_cover(graph: Graph) -> list[int]:
    vertex_list = []
    edges = iter(list(graph.edges))

    while (edge := next(edges, None)) is not None:
        vertex_list += [edge[0], edge[1]]

        edges = filter(
            lambda x: x[0] not in edge and x[1] not in edge, edges
        )

    return list(vertex_list)


def vertex_cover_optimal(graph: Graph) -> list[int]:
    r = range(len(graph.nodes))

    for i in r:
        for perm in itertools.permutations(r, i + 1):
            if _is_vertex_cover(graph, perm):
                return perm
    
    return []


def _is_vertex_cover(graph: Graph, nodes: tuple[int]):
    connected_nodes = set()

    for i in nodes:
        connected_nodes.add(i)
        for edge in graph.get_edges_from(i):
            connected_nodes.add(edge[0])

            if len(connected_nodes) == len(graph.nodes):
                return True
    
    return False


def main():
    graph = Graph(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
                  [(0, 1), (0, 4), (1, 2), (1, 6),
                  (2, 3), (3, 6), (3, 7), (4, 5),
                  (5, 6)])

    print([graph.nodes[i].value for i in vertex_cover(graph)])
    print()
    print([graph.nodes[i].value for i in vertex_cover_optimal(graph)])

if __name__ == '__main__':
    main()
