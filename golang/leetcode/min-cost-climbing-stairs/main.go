package main

import (
	"fmt"
	"math"
)

// func minCostClimbingStairs(cost []int) int {
// 	c := 0
// 	i := 0
// 	p := 0
// 	for {
// 		if i + 1 >= len(cost) {
// 			break
// 		}
// 		if i + 3 < len(cost) {
// 			p = nextStep(cost[i:i + 3])
// 		} else {
// 			p = nextStep(cost[i:i + 2])
// 		}

// 		c += cost[p]
// 		i += p + 1
// 	}

//     return c
// }

type path struct {
	pos	int
	tot int
}

//[1,100,1,1,1,100,1,1,100,1]
func minCostClimbingStairs(cost []int) int {
	for i := len(cost) - 3 ; i >= 0 ; i-- {
		cost[i] += int(math.Min(float64(cost[i+1]), float64(cost[i+2])))
	}

	return int(math.Min(float64(cost[0]), float64(cost[1])))
}


// func nextStep(cost []int) int {
// 	switch len(cost) {
// 	case 0:
// 		return -1
// 	case 1:
// 		return cost[1]
// 	case 2:
// 		if cost[1] <= cost[0] { 
// 			return 1
// 		}
// 		return 0
// 	default:
// 		if cost[1] <= cost[0] + cost[2] { 
// 			return 1
// 		}
// 		return 0
// 	}
// }

func main() {
	fmt.Println("minCostClimbingStairs([10,15,20]) ->", minCostClimbingStairs([]int{10,15,20}))
}
