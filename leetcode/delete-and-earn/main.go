package main

import "fmt"

func deleteAndEarn(nums []int) int {
    return deleteAndEarnHelper(nums, nums, 0)
}

func deleteAndEarnHelper(nums, rest []int, i int) int {
	if len(rest) < 1 {
		return 0
	}
	n := rest[0]
	n1 := delete(rest, 0)
	fmt.Println("i = ", i, "nums =", nums, ", rest =", rest, ", n1 =", n1, ", n =", n)
	earn := n + deleteAndEarnHelper(nums, n1, i + 1)
	alt := 0
	if i < len(nums) {
		skip := rest[1:]
		skip = append(skip, rest[0])
		alt = deleteAndEarnHelper(nums, skip, i + 1)
	}
	fmt.Println("i =", i, ", nums =", nums, ", rest =", rest, ", n1 =", n1, ", n =", n, ", earn =", earn, ", alt = ", alt)
	return max(earn, alt)
}

func delete(nums []int, i int) []int {
	d := nums[i]
	res := []int{}
	for idx, x := range nums {
		if x != d + 1 && x != d - 1 && idx != i {
			res = append(res, x)
		}
	}
	return res
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
