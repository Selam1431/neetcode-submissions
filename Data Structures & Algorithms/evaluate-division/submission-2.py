class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}

        # Build the graph.
        for equation, value in zip(equations, values):
            a = equation[0]
            b = equation[1]

            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        # Search for a path and multiply its division values.
        def dfs(current, target, visited, product):
            if current == target:
                return product

            visited.add(current)

            for neighbor, value in graph[current]:
                if neighbor not in visited:
                    answer = dfs(
                        neighbor,
                        target,
                        visited,
                        product * value
                    )

                    if answer != -1.0:
                        return answer

            return -1.0

        result = []

        # Answer each query with a fresh search.
        for start, target in queries:
            if start not in graph or target not in graph:
                result.append(-1.0)
            else:
                visited = set()
                answer = dfs(start, target, visited, 1.0)
                result.append(answer)

        return result