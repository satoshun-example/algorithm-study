package main

import (
	"fmt"
	"strconv"
)

func factorial(x int) int {
	if x <= 1 {
		return 1
	}
	return x * factorial(x-1)
}

func potentialMaxValue() int {
	return 100000000
}

func main() {
	factorialMap := make(map[int]int)
	for i := 0; i < 10; i++ {
		factorialMap[i] = factorial(i)
	}

	for i := 3; i <= potentialMaxValue(); i++ {
		v := 0
		for _, c := range strconv.Itoa(i) {
			v += factorialMap[int(c-'0')]
		}
		if v == i {
			fmt.Println(i)
		}
	}
}
