package main

import (
	m "mypkg"
	"fmt"
)

func main() {
	m.Aloha()
	xs := []float64{1,2,3,4}
	avg := m.Average(xs)
	fmt.Println(avg)
}
