For each x = nums[i] we decide:
    - we take the x and remove all x+1 and x-1 from nums; 
      - we earn x times its occurrences
    - or we skip it and take the next one

In other words, we calculate both case and take the max:
`res[i] = max(s + deleteAndEarn(ns[i]), deleteAndEarn(nums[i+1]))`;
where ns is the array without nums[i], nums[i] + 1 and nums[i] - 1

Constraints:

    1 <= nums.length <= 2 * 10^4
    1 <= nums[i] <= 10^4

