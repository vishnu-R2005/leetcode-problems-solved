class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            groups = defaultdict(list)

            for word in strs:
                # Frequency array for 26 lowercase letters
                count = [0] * 26

                for ch in word:
                    count[ord(ch) - ord('a')] += 1

                # Lists can't be dictionary keys, so convert to tuple
                groups[tuple(count)].append(word)

            return list(groups.values())