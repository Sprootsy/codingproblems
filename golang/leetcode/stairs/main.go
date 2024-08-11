package main

import "fmt"

func climbStairs(n int) int {
    if n == 0 {
        return 0
    }
    
	c := 1
	p := 1
	t := 0

	for i := 1; i < n; i++ {
		t = c
		c += p
		p = t
	}

	return c
}


func main() {

	r := climbStairs(2)
	fmt.Println(2, "->", r)
}