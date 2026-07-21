class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for words in strs:
            key = "".join(sorted(words))

            if key not in group:
                group[key] =[]
            group[key].append(words)

        return list(group.values())