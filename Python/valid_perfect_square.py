class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # low, high = 0, num
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     square = mid * mid
        #     if square == num:
        #         return True
        #     elif square < num:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return False
        root = num**0.5
        if root  == int(root):
            return True
        else:
            return False
soln = Solution()

print(soln.isPerfectSquare(14)) # True
