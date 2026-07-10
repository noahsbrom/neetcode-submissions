class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        keys = list(frequencies.keys())
        keys.sort(key=lambda k: frequencies[k], reverse=True)
        return keys[:k]
        