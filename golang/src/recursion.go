package main

import "fmt"

func factorial(x uint) uint {
	if x == 0 {
		return 1
	}

	return x * factorial(x-1)
}

func main() {
	var i uint
	fmt.Println("Enter a number:")
	fmt.Scan(&i)
	fmt.Println("The factorial of", i, "is", factorial(i))
}