package main

import "fmt"

func main() {
	slice1 := []int{1,2,3}
	slice2 := append(slice1, 4, 5)
	fmt.Println("Slice 1:", slice1)
	fmt.Println("Slice 2:", slice2)
	fmt.Println("Appended:", slice1, slice2)

	slice3 := []int{1,2,3}
	slice4 := make([]int, 2)
	copy(slice4, slice3)
	fmt.Println(slice3, slice4)
}