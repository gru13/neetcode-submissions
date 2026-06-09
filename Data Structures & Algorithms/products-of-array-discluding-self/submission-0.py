class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_pf = [1]*len(nums)
        for i in range(1, len(nums)):
            product_pf[i] = product_pf[i-1]*nums[i-1]
        
        product_sf = [1]*len(nums)
        for i in range(-2, -len(nums)-1, -1):
            product_sf[i] = product_sf[i+1]* nums[i+1]
        
        product = []
        for a, b in zip(product_pf, product_sf):
            product.append(a*b)

        return product