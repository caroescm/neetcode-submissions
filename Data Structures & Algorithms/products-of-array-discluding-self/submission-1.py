class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        run_prod = 1

        for i in range(n):
            output[i] = run_prod
            run_prod= run_prod * nums[i]

        run_prod = 1

        for i in range(n - 1, -1, -1):
            output[i] *= run_prod
            run_prod = run_prod * nums[i]

        return output