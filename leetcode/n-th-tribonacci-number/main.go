package main

import "fmt"

func tribonacci(n int) int {
    if n == 0 {
        return 0
    }
    if n == 1 || n == 2 {
        return 1
    }

    t, c := 1, 1
    p1, p2 := 0, 1

    for i := 2 ; i < n ; i++ {
        t = c
        c += p2 + p1
        p1 = p2
        p2 = t
    }

    return c
}

func main() {
	fmt.Println("tribonacci(2) ->", tribonacci(2))
	fmt.Println("tribonacci(3) ->", tribonacci(3))
	fmt.Println("tribonacci(4) ->", tribonacci(4))
}

