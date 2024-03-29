

public class Treasure {

	int n;
	int k;
	int startIndex = 0;
	int currentSum = 0;
	int maxProfit = 0;
	int[] v = {0};


	public Treasure(int k, int[] v){
		this.n = v.length;
		this.k = k;
		this.v = v;
	}

	public int search(){
		// iterate treasure up to k continuosly
		int i;
		for(i=0; i < k; i++){
			currentSum += this.v[i];
		}
		maxProfit = currentSum;

		// iterate remainder of treasures
		for(i=k; i < n; i++){
			currentSum = currentSum - v[i-k] + v[i];
			if(currentSum > maxProfit){
				maxProfit = currentSum;
				startIndex = i - k + 1;
			}
		}
		return startIndex;
	}


	public static void main(String[] args){
		int[] v = {1,2,3,4,5,6,7,8,9,10};
		Treasure tr = new Treasure(5, v);
		System.out.println("hello, world");
		System.out.println("StartIndex => " + tr.search());
	}
}
