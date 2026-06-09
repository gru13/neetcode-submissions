class Solution {

    int BinarySearch(int[] array, int low , int high, int element){
        if(high < low){
            return -1;
        }
        int mid = (low + high) / 2;
        if (array[mid] == element){
            return mid;
        }
        if(array[mid] > element){
            return BinarySearch(array, low, mid-1, element);
        }else{
            return BinarySearch(array, mid+1, high, element);
        }
    }

    public int search(int[] nums, int target) {
        return BinarySearch(nums, 0, nums.length-1, target);
    }
}
