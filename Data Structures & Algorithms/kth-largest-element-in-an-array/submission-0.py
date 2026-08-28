class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.heap = nums

        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

        return self.heap[0]


        