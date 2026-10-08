class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}
        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(current, target, visited, products):
            if current == target:
                return products
            visited.add(current)

            for neighbour, value in graph[current]:
                if neighbour not in visited:
                    answer = dfs(
                        neighbour,
                        target,
                        visited,
                        products * value
                    )

                    if answer != -1.0:
                        return answer

            return -1.0

        result = []

        for start, target in queries:
            if start not in graph or target not in graph:
                result.append(-1.0)

            else:
                visited = set()
                answer = dfs(start, target, visited, 1)
                result.append(answer)

        return result