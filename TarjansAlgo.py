#Tarjan’s Algorithm: Strongly Connected Components

LeetCode 1192 - Critical Connections in a Network [hard]

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

CODE

from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def make_graph(connections):
            graph = defaultdict(list)
            for edge in connections:
                a, b = edge
                graph[a].append(b)
                graph[b].append(a)
            return graph

        graph = make_graph(connections)

        id, node, prev_node = 0, 0, -1  # at first there is no prev_node. we set it to -1
        ids = [0 for _ in range(n)]  # tracks ids of nodes
        low_links = [0 for _ in range(n)]  # tracks low link value (default value is the index)
        visited = [False for _ in range(n)]  # tracks DFS visit status

        bridges = []
        self.dfs(node, prev_node, bridges, graph, id, visited, ids, low_links)

        return bridges

    def dfs(self, node, prev_node, bridges, graph, id, visited, ids, low_links):
        visited[node] = True
        low_links[node] = id
        ids[node] = id
        id += 1

        for next_node in graph[node]:
            if next_node == prev_node:
                continue
            if not visited[next_node]:
                self.dfs(next_node, node, bridges, graph, id, visited, ids, low_links)
                low_links[node] = min(low_links[node], low_links[next_node])  # on callback, generates low link values
                if ids[node] < low_links[next_node]:  # found the bridge!
                    bridges.append([node, next_node])
            else:
                # tried to visit an already visited node, which may have a lower id than the current low link value
                low_links[node] = min(low_links[node], ids[next_node])
