class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Time Complexity: O(nlog(n)) from sorting (log(n)) and itterating through lists
        Space Complexity: O(n) n = len(position)
        '''

        pair = [(pos, vel) for pos, vel in zip(position, speed)]
        pair.sort(reverse=True)
        time2goal = [] # Track the new positions each itteration   
        for pos, vel in pair:
            time2goal.append((target - pos) / vel) # How long it would take to get to target
            if len(time2goal) >= 2 and time2goal[-1] <= time2goal[-2]:
                # If the most recent time2goal is <= the previous time2goal
                # then remove the slower
                time2goal.pop()
        return len(time2goal)