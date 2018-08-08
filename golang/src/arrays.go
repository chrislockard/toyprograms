package main

import "fmt"

func main() {
	var y [5]int
	y[4] = 100
	fmt.Println(y)

	x := [5]float64{98, 93, 77, 82, 83}
	
	var total float64 = 0
	for _, value := range x {
		total += value
	}
	fmt.Println(total / float64(len(x)))
}