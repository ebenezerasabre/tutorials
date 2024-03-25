

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Arrays;

public class QuickSort {
	static int[] arr;

	// pass a seq, left, right, pivot to func
	public QuickSort(int[] arr){
		this.arr = arr;
		quicksort(arr, 0, arr.length - 1);
	}

	public void quicksort(int[] arr, int left, int right){

		if(left >= right){
			return;
		}
	
		int pivot = arr[(left + right ) / 2];
		int index = partition(left, right, pivot);
		System.out.println("pivot-> " + pivot + ", index -> " + index);
		quicksort(this.arr, left, index - 1);  // quicksort on left half
		quicksort(this.arr, index + 1, right); // quicksort on right half


	}

	int partition(int left, int right, int pivot){
		while(left <= right){
			
			while(this.arr[left] < pivot){
				left++;
			}
			System.out.println("left-> " + left);

			while(this.arr[right] > pivot){
				right--;
			}
			System.out.println("right-> " + right);

			if(left <= right){
				//swap(arr, left, right);
				swap(left, right); // swap elements
				left++;
				right--;
			}
		}
		return left; // new partition point

	}

	 void swap(int left, int right){
		int temp = this.arr[right];
		this.arr[right] = this.arr[left];
		this.arr[left] = temp;
	}

	public void show_arr(){
		System.out.println("arr -> " + Arrays.toString(this.arr));
	}


	public static void main(String[] args){
		int[] arr = {1,2,44,23,90,19,39,11,22,55,27,31,33,14};
	
		System.out.println("Hello, world");
		System.out.println("arr -> " + Arrays.toString(arr));
		QuickSort qs = new QuickSort(arr);
		qs.show_arr();
	
	
	}
}





