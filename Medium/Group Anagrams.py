class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            if "".join(sorted(word)) in hashmap:
                hashmap["".join(sorted(word))].append(word)
            else:
                hashmap["".join(sorted(word))] = [word]
        res = []
        for value in hashmap.values():
            res.append(value)
        return(res)
