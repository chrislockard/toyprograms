package main

import (
	"fmt"
	"time"
	"math/rand"
)

func f(n int) {
	for i := 0; i < 10; i++ {
		fmt.Println(n, ":", i)
		amt := time.Duration(rand.Intn(250)) //set a random time duration
		time.Sleep(time.Millisecond * amt) //sleep the goroutine for amt milliseconds
	}
}

func main() {
	for i := 0; i< 10; i++ {
		go f(i)
	}
	var input string
	fmt.Scanln(&input)
}