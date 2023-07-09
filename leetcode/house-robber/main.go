package main

import "fmt"


func rob(nums []int) int {
	n := len(nums)
	p1, p2, cur := 0, 0, 0

	for i := 0 ; i < n ; i++ {
		cur = max(p2 + nums[i], p1)
		p2 = p1
		p1 = cur
	}
	return cur
}

// func robHelper(nums []int, i int) int {
// 	if i < 0 {
// 		return 0
// 	}

// 	if m[i] >= 0 {
// 		return m[i]
// 	}
// 	s2 := robHelper(nums, i - 2)
// 	s1 := robHelper(nums, i - 1)
// 	res := max(s2 + nums[i], s1)
// 	m[i] = res
// 	return res
// }

func max(v1, v2 int) int {
	if v1 > v2 {
		return v1
	}
	return v2
}


func main() {
	fmt.Println("rob([1,2,3,1]) =", rob([]int{1,2,3,1}) )
}

