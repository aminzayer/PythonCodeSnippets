## 2024-05-23 - Exponential Complexity in Recursive Lambdas

**Learning:** Python's lambdas are powerful but dangerous when used for recursion without memoization. A simple recursive Fibonacci lambda `fibonacci = lambda n: n if n < 2 else fibonacci(n-1) + fibonacci(n-2)` has O(2^n) time complexity, making it unusable for n > 35.

**Action:** Always prefer iterative solutions or `functools.reduce` for "one-liner" implementations of recursive algorithms. If recursion is necessary, use `functools.lru_cache` (though tricky with lambdas) or define a proper function. For `fibonacci`, `reduce` provides a clean O(n) functional alternative.
