// memoization


const fib = (n, memo = {}) => {
	if (n in memo) return memo[n]; // using n as key in memo object
	if(n <= 2) return 1;
	memo[n] = fib(n -1, memo) + fib(n -2, memo);
	return memo[n];
};

console.log(fib(7));
console.log(fib(8));
console.log(fib(50));




