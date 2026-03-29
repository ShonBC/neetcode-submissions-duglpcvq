class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        define sliding window of size k
        take average of the vals in window
        if avg >= thresh then incresase count by 1
        return count
        Time Complexity: O(n) n = len(arr)
        Space Complexity: O(min(len(arr), k))
        '''
        window = deque()
        count = 0
        L = 0
        for R in range(len(arr)):
            window.append(arr[R])
            if R - L > k - 1:
                window.popleft()
                L += 1
            if R - L == k - 1:
                avg = sum(window) / k
                if avg >= threshold:
                    count += 1
        return count
            