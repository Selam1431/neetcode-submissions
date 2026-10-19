class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float('inf')] * n

        price[src] = 0

        for _ in range(k + 1):
            temp = price.copy()

            for start, finish, cost in flights:
                if price[start] != float('inf'):
                    new_price = price[start] + cost
                    temp[finish] = min(temp[finish], new_price)

            price = temp

        if price[dst] == float('inf'):
            return -1
        return price[dst]
        
















        