import java.math.*;
import java.util.regex.*;

public class search {
	public static boolean binarySearchIt(int[] array, int x){
		int left = 0;
		int right = array.length -1;
		while(left <= right){
			int mid = left + ((right - left) / 2);
			if(array[mid] == x){
				return true; 		// elem found
			} else if(x < array[mid]){
				right = mid -1;
			} else {
				left = mid + 1;
			}

		}
		return false;
	}

	public static void main(String[] args){
		int[] arr = {1,3,5,7,9,11,13,15,17,19};
		System.out.println("called -> " + binarySearchIt(arr, 13));
	}

}
