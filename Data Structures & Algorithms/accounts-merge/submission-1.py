class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                if email not in graph:
                    graph[email] = []
                email_to_name[email] = name

                if email != first_email:
                    graph[email].append(first_email)
                    graph[first_email].append(email)

        visited = set()
        result = []

        def dfs(email, group):
            visited.add(email)
            group.append(email)

            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, group)

        for email in graph:
            if email not in visited:
                group = []
                dfs(email, group)
                name = email_to_name[email]
                result.append([name] + sorted(group))

        return result 

        