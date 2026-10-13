class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        graph = {}

        for word1, word2 in similarPairs:
            if word1 not in graph:
                graph[word1] = []

            if word2 not in graph:
                graph[word2] = []

            graph[word1].append(word2)
            graph[word2].append(word1)


        def dfs(current, target, visited):
            if current == target:
                return True

            visited.add(current)

            for neighbour in graph[current]:
                if neighbour not in visited:
                    if dfs(neighbour, target, visited):

                        return True

            return False

        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2:
                continue

            if word1 not in graph or word2 not in graph:
                return False

            visited =set()

            answer = dfs(word1, word2, visited)

            if answer == False:
                return False

        return True
        
        