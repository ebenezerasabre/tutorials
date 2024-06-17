// memoization

// fibonacci
const fib = (n, memo={}) => {
	if(n in memo) return memo[n];
	if(n <= 2) return 1;
	memo[n] = fib(n -1, memo) + fib(n -2, memo);
	return memo[n]
}

/*
console.log(fib(8));
console.log(fib(20));
console.log(fib(50));
console.log(fib(7));
*/

// 3 essences of an attractive man
// 1. He is comfortable in his own skin
// 2. He knows where is he going
// 3. He has fun while he is going there

// Grid Traveller



const gridTraveler = (m, n, memo={}) => {
	const key = n + ',' + m;
	if (key in memo) return memo[key];
	if (m == 1 && n == 1) return 1;
	if (m == 0 || n == 0) return 0;
	//	 go down		go right
	//return gridTraveler(m - 1, n) + gridTraveler(m, n -1);
	memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo);
	return memo[key];
}

console.log(gridTraveler(1, 1)); // 1
console.log(gridTraveler(2, 3)); // 3
console.log(gridTraveler(3, 2)); // 3
console.log(gridTraveler(3, 3)); // 6
console.log(gridTraveler(18, 18)); 














