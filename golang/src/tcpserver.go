package main

import (
	"encoding/gob"
	"fmt"
	"net"
)

func server() {
	// Listen on a port
	lp, err := net.Listen("tcp", ":9999")
	if err != nil {
		fmt.Println(err)
		return
	}
	for {
		//Accept connection
		c, err := lp.Accept()
		if err != nil {
			fmt.Println(err)
			continue
		}
		//Handle the connection
		go handleServerConnection(c)
	}
}

func handleServerConnection(c net.Conn) {
	//Receive message
	var msg string
	err := gob.NewDecoder(c).Decode(&msg)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Received", msg)
	}
	c.Close()
}

func client() {
	//Connect to server
	c, err := net.Dial("tcp", "127.0.0.1:9999")
	if err != nil {
		fmt.Println(err)
		return
	}

	//Send message
	msg := "Hello Networked World"
	fmt.Println("Sending", msg)
	err = gob.NewEncoder(c).Encode(msg)
	if err != nil {
		fmt.Println(err)
	}
	c.Close()
}

func main() {
	go server()
	go client()

	var input string
	fmt.Scanln(&input)
}