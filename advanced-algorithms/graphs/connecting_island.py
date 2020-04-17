import heapq

def adjacent_graph(num_island: int, bridge_config: list):
    graph_adjacents = [[] for _ in range(num_islands + 1)]  # To have the same index as the islands, skip 0

    for bridge in bridge_config:
        left_side = bridge[0]
        right_side = bridge[1]
        conn_cost = bridge[2]

        graph_adjacents[left_side].append((right_side, conn_cost))
        graph_adjacents[right_side].append((left_side, conn_cost))

    return graph_adjacents

def min_connections(graph: list):
    nodes_visited = [False for _ in range(len(graph) + 1)]
    connection_cost = 0

    initial_node = 1
    connections = [(0, initial_node)]

    while len(connections) > 0:
        cost, current_node = heapq.heappop(connections)

        if nodes_visited[current_node]:
            continue
        else:
            connection_cost += cost
            for neighbor, node_cost in graph[current_node]:
                heapq.heappush(connections, (node_cost, neighbor))

            nodes_visited[current_node] = True

    return connection_cost


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = min_connections(adjacent_graph(num_islands, bridge_config))

    if output == solution:
        print("Pass")
    else:
        print("Fail")

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6
test_case = [num_islands, bridge_config, solution]
test_function(test_case)
