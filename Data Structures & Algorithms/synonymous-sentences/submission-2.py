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

        # map each to all its possible replacement
        choices = {}
        visited = set()

        for word in graph:
            if word not in visited:
                # start a new synonym group
                group = []
                dfs(word, visited, group)
                group.sort()

                # every member can use the entire group
                
                for member in group:
                    choices[member] = group

        # split the text
        words = text.split()

        # store completed sentences here
        result = []

        def backtrack(index, sentence):
            if index == len(words):
                result.append(" ".join(sentence))
                return

            #get the original word at this position
            word = words[index]

            # get its synonym, or keep only the original word
            # if it has no synonym group.

            options = choices.get(word, [word])

            for option in options:

                # add a word to the working list
                sentence.append(option)

                # explore choose words for later positions
                # this call finished befor pop()
                backtrack(index + 1, sentence)

                # remove our choice to try the next one
                sentence.pop()

        # start at positon 0 with an empty working list
        backtrack(0, [])

        # return every generated sentence in dictionary order 
        return sorted(result)

