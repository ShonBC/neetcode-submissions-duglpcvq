class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        track key: frequency of each letter (o(26) for 26 letters) and value: group list

        if frequescy array in seen, add to group
        else add key value to seen 
        '''

        ans = {}
        for w in strs:
            track = [0]*26
            for i in w:
                track[ord(i) - 97] += 1
            track = tuple(track)
            if track in ans:
                ans[track].append(w)
            else:
                ans[track] = [w]
        return [ans[i] for i in ans]