package main

import "fmt"
import "math"

type Circle struct {
	x, y, r float64
}

type Rectangle struct {
	x1, y1, x2, y2 float64
}

func distance(x1, y1, x2, y2 float64) float64 {
	a := x2 - x1
	b := y2 - y1
	return math.Sqrt(a*a + b*b)
}

func circleArea(c Circle) float64 {
	return math.Pi * c.r * c.r
}

func circleAreaChange(c *Circle) float64 {
	return math.Pi * c.r * c.r + 1
}

func (c *Circle) area() float64 {
	return math.Pi * c.r *c.r
}

func (r *Rectangle) area() float64 {
	l := distance(r.x1, r.y1, r.x1, r.y2)
	w := distance(r.x1, r.y1, r.x2, r.y1)
	return l * w
}

func main() {
	// var c Circle //one method of instantiating a struct
	//c := new(Circle) //another method
	//c := Circle{0, 0, 1} //another method, if we know the order of fields
	c := Circle{x: 0, y: 0, r:1} //yet another method
	fmt.Println(c.x, c.y, c.r) // print fields using dot notation

	//Accessing fields 
	c.x = 10
	c.y = 5

	//Arguments are copied in Go, changing fields inside circleArea will not modify
	//the original variable
	fmt.Println(circleArea(c))

	//circleAreaChange() WILL change the fields of c since we pass a reference to it.
	fmt.Println(circleAreaChange(&c))

	//circleReceiver allows for calling a method on an object:
	fmt.Println(c.area())

	//define a Rectangle
	r := Rectangle{0, 0, 10, 10}
	fmt.Println(r.area())
}