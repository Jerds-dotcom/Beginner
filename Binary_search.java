public class Binary_search{
    public static void main(String[] args){
        int[] array = {1, 2, 3, 4, 5, 6, 7};
        int target = 5;
        int result = binarySearch(array, target);
        System.out.print(result);
    }

    private static int binarySearch(int[] array, int target){
        int left = 0;
        int right = array.length - 1;
        
        while (left <= right){
            int mid = (left + right)/2;
            if (array[mid] == target){
                return mid;
            } else if (array[mid] < target){
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}