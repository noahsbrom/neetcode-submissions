class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        n = len(nums)
        frequency_buckets = [[] for _ in range(n)]
        for num, count in c.items():
            frequency_buckets[count-1].append(num)
        
        ans = []
        for i in range(n-1, -1, -1):
            for num in frequency_buckets[i]:
                ans.append(num)
                k -= 1
            # unique answer -> length of bucket will not exceed remaining k;
            # otherwise, we could pull from bucket in more than one way
            if k == 0:
                return ans