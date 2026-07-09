class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            letter_count = [0] * 26
            for ch in s:
                letter_count[ord(ch) - ord('a')] += 1
            # use tuple because list is not hashable
            groups[tuple(letter_count)].append(s)
        return list(groups.values())