class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def rowSearch(k,i,j):
            if i > j: return False

            middle = i + (j-i)//2
            if matrix[k][middle] == target:
                return True
            if matrix[k][middle] < target:
                return rowSearch(k, middle+1, j)
            if matrix[k][middle] > target:
                return rowSearch(k, i, middle-1)

        def binarySearch(i,j):
            if i > j:
                return False
            middle = i + (j-i)//2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                return rowSearch(middle,0,len(matrix[middle])-1)
            if target < matrix[middle][0]:
                return binarySearch(i,middle-1)
            if target > matrix[middle][-1]:
                return binarySearch(middle+1,j)
            
        return binarySearch(0,len(matrix)-1)