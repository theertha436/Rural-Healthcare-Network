def perform_clustering(data):

    n = len(data)
    graph = {i: [] for i in range(n)}

    # Directed edges (based on PHC + distance rule)
    for i in range(n):
        for j in range(n):
            if i != j:
                if data.iloc[i]["PHC"] == data.iloc[j]["PHC"]:
                    if abs(data.iloc[i]["Distance"] - data.iloc[j]["Distance"]) <= 10:
                        graph[i].append(j)

    # Step 1: DFS order
    visited = set()
    stack = []

    def dfs(v):
        visited.add(v)
        for nei in graph[v]:
            if nei not in visited:
                dfs(nei)
        stack.append(v)

    for i in range(n):
        if i not in visited:
            dfs(i)

    # Step 2: Transpose graph
    transpose = {i: [] for i in range(n)}
    for u in graph:
        for v in graph[u]:
            transpose[v].append(u)

    # Step 3: DFS on transpose
    visited.clear()
    cluster_id = 0
    clusters = {}

    def dfs2(v):
        visited.add(v)
        clusters[v] = cluster_id
        for nei in transpose[v]:
            if nei not in visited:
                dfs2(nei)

    while stack:
        node = stack.pop()
        if node not in visited:
            dfs2(node)
            cluster_id += 1

    data["Cluster"] = data.index.map(clusters)

    return data