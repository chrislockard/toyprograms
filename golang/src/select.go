package main

import (
	"fmt"
	"time"
)

func main() {
	//c1 := make(chan string, 1) //Creates a buffered channel with a capacity of one
	c1 := make(chan string)
	c2 := make(chan string)

	go func() {
		for {
			c1 <- "from 1"
			time.Sleep(time.Second * 2)
		}
	}()
	go func() {
		for {
			c2 <- "from 2"
			time.Sleep(time.Second * 3)
		}
	}()
	go func() {
		for {
			/* 	select picks the first channel ready to receive and receives from, 
				or sends to it.  If more than one are ready, select randomly picks one.
				If neither are ready, select blocks until one is available.
			*/
			select {
			case msg1 := <- c1:
				fmt.Println(msg1)
			case msg2 := <- c2:
				fmt.Println(msg2)
			}
		}
	}()

	var input string
	fmt.Scanln(&input)
}