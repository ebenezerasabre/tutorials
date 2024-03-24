import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;



public class BinarySearch {

	public static boolean bsr(int[] arr, int x, int left, int right){
		if(left > right){
			System.out.println("left > right called");
			return false;
		}
		//int mid = left + ((right -left) / 2);
		int mid = (left + right ) / 2;
		System.out.println("mid = " + mid);
		if (arr[mid] == x) {
			System.out.println("arr[mid] == x called");
			return true;
		} else if(x < arr[mid]) {
			System.out.println("x < arr[mid] called");
			return bsr(arr, x, left, mid - 1);
		} else { // x > arr[mid]{
			System.out.println("x > arr[mid] called");
			return bsr(arr, x, mid + 1, right); 
		}
	}


	public static void main(String[] args){
		BinarySearch bs = new BinarySearch();
		int[] arr = {1,2,3,4,5,6,7,8,9};
		int left = 0;
		int right = arr.length - 1;
		System.out.println("Hello, world, bool = " + bs.bsr(arr, 3, left, right));
	}
}
