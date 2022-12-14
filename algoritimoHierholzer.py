def printCircuit(adj):
 
    # adj represents the adjacency list of
    # the directed graph
    # edge_count represents the number of edges
    # emerging from a vertex
    edge_count = dict()
 
    for i in range(len(adj)):
 
        # find the count of edges to keep track
        # of unused edges
        edge_count[i] = len(adj[i])
 
    if len(adj) == 0:
        return # empty graph
 
    # Maintain a stack to keep vertices
    curr_path = []
 
    # vector to store final circuit
    circuit = []
 
    # start from any vertex
    curr_path.append(0)
    curr_v = 0 # Current vertex
 
    while len(curr_path):
 
        # If there's remaining edge
        if edge_count[curr_v]:
 
            # Push the vertex
            curr_path.append(curr_v)
 
            # Find the next vertex using an edge
            next_v = adj[curr_v][-1]
 
            # and remove that edge
            edge_count[curr_v] -= 1
            adj[curr_v].pop()
 
            # Move to next vertex
            curr_v = next_v
 
        # back-track to find remaining circuit
        else:
            circuit.append(curr_v)
 
            # Back-tracking
            curr_v = curr_path[-1]
            curr_path.pop()
 
    # we've got the circuit, now print it in reverse
    return circuit

# This code is contributed by sanjeev2552, available at https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/ and was adepted by Felipe Góes