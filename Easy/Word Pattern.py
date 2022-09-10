class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.strip().split()
        if len(words) != len(pattern):
            return False
        else:
            w_p_hashmap = {}
            for i, char in enumerate(pattern):
                w_p_hashmap[char] = words[i]
            hashmap = {}
            w_hashmap = {}
            for i, char in enumerate(pattern):
                hashmap[char] = pattern.count(char)
                w_hashmap[words[i]] = words.count(words[i])
                if hashmap[char] != w_hashmap[words[i]] or w_p_hashmap[char] != words[i]:
                    return False
            return True