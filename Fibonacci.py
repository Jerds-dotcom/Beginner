def fib(n, memoization = {}):
	if n in memoization:
		return memoization[n]
	if n <= 2:
		return n
	memoization[n] = fib(n-1, memoization) + fib(n-2, memoization)
	return memoization[n]
