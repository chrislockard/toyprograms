package main

import "fmt"

func makeEven() func() uint {
	i := uint(0)
	return func() (ret uint) {
		ret = i
		i += 2
		return
	}
}

func main() {
	for i := 1; i <= 10; i++ {
		nextEven := makeEven()
		fmt.Println(nextEven)
	}
}