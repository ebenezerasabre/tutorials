import java.util.Arrays;

public class Merge {
	int [] merged = {0};
	int[] s_a;
	int[] s_b;
	int i = 0;
	int j = 0;
	int n, m, tmp;
	int counter = 0;

	public Merge(int[] s_a, int[] s_b){
		this.s_a = s_a;
		this.s_b = s_b;
		this.n = s_a.length;
		this.m = s_b.length;
		
		System.out.println("constructor");


	}


	public void merge_sort(){

		System.out.println("called 1");



		 while(i < n && j < m){

			if(s_a[i] < s_b[j]){
				tmp = s_a[i];
				i = i + 1;
			}
		       
		
			else if(s_a[i] > s_b[j]){
				tmp = s_b[j];
				j = j + 1;
			} else {
				tmp = s_a[i];
				i = i + 1;
				j = j + 1;
			}

		
			if(merged.length == 0 ||  merged[i] != tmp){
				merged[counter] = tmp;
				counter++;
			}
		
		 }
		 
		 
		 // case s_a longer than array b
		 // add the other elements	 
		 while(i < n ){
			if(merged.length == 0 || merged[counter - 1] !=  s_a[i]){
				merged[counter] = s_a[i];
				counter++;
				i = i + 1;
			}
		 }

		 while(j < m ){
			if(merged.length == 0 || merged[counter - 1] !=  s_b[j]){
				merged[counter] = s_b[j];
				counter++;
				j = j + 1;
			}
		 }

		 

	}

	public void show_merged(){
		System.out.println(Arrays.toString(merged));
	}


	public static void main(String[] args){
		int[] s_b = {1,2,3,4,5};
		int[] s_a = {6,7,8,9,10,11,12,13};
		Merge mrg = new Merge(s_a, s_b);
		mrg.merge_sort();
		mrg.show_merged();


		System.out.println("hello, world");
	}
}


