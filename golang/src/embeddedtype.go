package main

import "fmt"

type Person struct {
	Name string
}

type Android struct {
	Person
	Model string
}

func (p *Person) Talk() {
	fmt.Println("Hi, my name is", p.Name)
}

func main() {
	a := new(Android)
	a.Person.Name = "Mario"
	a.Person.Talk() //Calling the Talk() method on Person object

	b := new(Android)
	b.Person.Name = "Luigi"
	b.Talk() //Call Person directly on Android object using anonymous fields, aka embedded types.
	// This demonstrates an "is-a" relationship instead of a "has-a" relationship
}