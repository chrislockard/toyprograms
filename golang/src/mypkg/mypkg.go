package mypkg

import "fmt"

//Prints "Aloha from mypkg" to verify packages are working as expected.
func Aloha() {
	fmt.Println("Aloha from mypkg")
}

//Finds the average of a series of numbers
func Average(xs []float64) float64 {
	total := float64(0)
	for _, x := range xs {
		total += x
	}
	return total / float64(len(xs))
}