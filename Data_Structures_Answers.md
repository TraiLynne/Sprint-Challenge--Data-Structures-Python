Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
   1. O(1)
   2. it only takes a constant 2 steps to append, i believe
   
2. What is the space complexity of your ring buffer's `append` function?
   1. O(1)

3. What is the runtime complexity of your ring buffer's `get` method?
   1. O(n) because of the loop

4. What is the space complexity of your ring buffer's `get` method?
   1. O(n)

5. What is the runtime complexity of the provided code in `names.py`?
   1. runtime: 12.62616515159607 seconds
   2. Ok , it is a nested loop with an if statement looking a lot like selection sort so ... O(n^2)

6. What is the space complexity of the provided code in `names.py`?
   1. O(n^2)

7. What is the runtime complexity of your optimized code in `names.py`?
   1. runtime: 0.007782936096191406 seconds 
   2. Best: O(min(len(s), len(t)), worst: O(len(s) * len(t))
   3. I googled this, no lie, 
      1. https://eastonlee.com/blog/2017/03/06/common-python-operation-time-complexity/
      2. https://stackoverflow.com/questions/30845469/time-complexity-of-python-set-intersection-for-n-sets

8. What is the space complexity of your optimized code in `names.py`?
   1. O(1)
