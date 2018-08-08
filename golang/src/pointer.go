package main

import "fmt"

func zero(xPtr *int) {
	*xPtr = 0 //Dereference xPtr and set the value of xPtr integer to 0
}

func main() {
	x := 5
	/* 	Find the address of x and pass it to the zero function, 
		which expects a pointer to an integer.  &x returns a *int,
		which is what zero( *int) is expecting.
	*/
	zero(&x)
	fmt.Println(x)
}