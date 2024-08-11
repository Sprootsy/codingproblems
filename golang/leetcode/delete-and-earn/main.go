package main

import (
	"fmt"
)

//copied
func deleteAndEarn(nums []int) int {
    numsMap := make([]int, 10001)
    dp := make([]int, 10001)
    for i := 0; i < len(nums); i ++ {
        numsMap[nums[i]] += nums[i]
    }
    
    dp[0] = numsMap[0]
    dp[1] = max(numsMap[1], numsMap[0])
    
    for i := 2; i < 10001; i ++ {
        dp[i] = max(dp[i-1], numsMap[i] + dp[i-2])   
    }
 
    return dp[10000]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println("deleteAndEarn([3,4,2]) = ", deleteAndEarn([]int{3,4,2}))
}
