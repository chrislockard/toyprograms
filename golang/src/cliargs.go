package main

import (
	"fmt"
	"flag"
	"math/rand"
)

func main() {
	//Flags
	max := flag.Int("max", 6, "the max value")
	//Parse
	flag.Parse()
	//Generate random number
	fmt.Println(rand.Intn(*max))
}