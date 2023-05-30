from dataclasses import dataclass, field
from typing import Any


class Graph():
    nodes: list['Node'] = field(default_factory=list)
    edges: dict[tuple[int, int], float] = field(default_factory=dict)

    # Shorthand constructor for undirected and unweighted graph.
    def __init__(self, nodes: list[Any], edges: list[tuple[int, int]]):
        self.nodes = [Node(v) for v in nodes]
        self.edges = {}

        for e in edges:
            self.edges[(e[0], e[1])] = 0
            self.edges[(e[1], e[0])] = 0

    def add_node(self, value: Any) -> int:
        self.nodes.append(Node(value))
        return len(self.nodes) - 1

    def get_edges_from(self, i: int) -> list[tuple[int, float]]:
        if not self._is_legal_node_idx(i):
            return None

        res = []

        for (_, t) in filter(lambda s, _: s == i, res):
            res.append(t, res[(i, t)])

        return res

    def add_edge(self, i: int, j: int, w: float):
        if not self._is_legal_node_idx(i) or not self._is_legal_node_idx(j):
            return None

        self.edges[i, j] = w

    def _is_legal_node_idx(self, i: int):
        return i < len(self.nodes)


@dataclass
class Node:
    value: Any