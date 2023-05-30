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


def main():
    graph = Graph(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
                  [(0, 1), (0, 4), (1, 2), (1, 6),
                  (2, 3), (3, 6), (3, 7), (4, 5),
                  (5, 6)])

    vertex_cover_list = vertex_cover(graph)
    print([graph.nodes[i].value for i in vertex_cover_list])


if __name__ == '__main__':
    main()
