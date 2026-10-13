class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # build the graph
        graph = {}

        for word1, word2 in synonyms:
            if word1 not in graph:
                graph[word1] = []

            if word2 not in graph:
                graph[word2] = []

            graph[word1].append(word2)
            graph[word2].append(word1)

        def dfs(word, visited, group):
            visited.add(word)
            group.append(word)

            for neighbour in graph[word]:
                if neighbour not in visited:
                    dfs(neighbour, visited, group)

        choices = {}
        visited = set()

        for word in graph:
            if word not in visited:
                group = []
                dfs(word, visited, group)
                group.sort()

                for member in group:
                    choices[member] = group

        words = text.split()
        result = []

        def backtrack(index, sentence):
            if index == len(words):
                result.append(" ".join(sentence))
                return

            word = words[index]

            options = choices.get(word, [word])

            for option in options:
                sentence.append(option)

                backtrack(index + 1, sentence)

                sentence.pop()

        backtrack(0, [])
        return result



