# Sliding Window

The sliding window technique is used to solve problems that require finding a
subset of contiguous elements inside an array. For example: finding the longest
substring, or finding the minimum set of elements that adds to a number.

The window size can be either fixed (easiest case) or variable.
In general, 2 pointers are used to keep track of the window and they are moved
depending on the condition to be satisfied.

## Fixed length

1. define `l = 0`, `r = k` and `ans` (either min or max value).
2. compute the result; you may also need to keep track of previous results with
   a min/max function.
3. increase l and r by 1.
4. repeat from step 2 until end of array is reached.

## Variable Window

1. define `l = 0`, `r = 0` (depending on minimum window size) and `ans` 
   (either min or max possible value).
2. increase `r` first, until the condition is not satisfied.
3. increase `l` by one until the condition is satisfied again or `l==r`.
4. repeat from step 2 until end of array is reached.

**N.B.** step 2 might never be satisfied, so it's required to check if the
loop did enter step 3, otherwise the default result is returned.
