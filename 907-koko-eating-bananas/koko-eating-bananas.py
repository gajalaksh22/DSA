class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def can_finish(piles,speed,h):
            hours = 0
            for pile in piles:
                hours += (pile+speed-1) // speed
            if hours > h:
                return False
            return hours <= h
        low = 1
        high = max(piles)
        while low < high:
            mid = (low+high) // 2
            if can_finish(piles,mid,h):
                high = mid
            else:
                low = mid + 1
        return low


        