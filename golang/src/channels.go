package main

import (
	"fmt"
	"time"
)

func pinger(c chan string) {
	for i := 0; ; i++ {
		c <- "ping" //send string "ping" to channel c
	}
}
func printer(c chan string) {
	for {
		msg := <- c //receive from channel c and store in variable msg
		fmt.Println(msg) //alternative: fmt.Println(<-c)
		time.Sleep(time.Second * 1)
	}
}
func ponger(c chan string) {
	for i := 0; ; i++ {
		c <- "pong"
	}
}
func main() {
	var c chan string = make(chan string)

	go pinger(c)
	go ponger(c)
	go printer(c)

	var input string
	fmt.Scanln(&input)
}