package main 

import "fmt"

func main() {
	fmt.Println("Enter Distance (Feet): ")
	var input float64
	fmt.Scanf("%f", &input)

	output := input * 0.3048

	fmt.Println(input, "feet is equal to", output, "meters!")
}