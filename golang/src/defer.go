package main

import "fmt"

func first() {
	fmt.Println("First")
}

func second() {
	fmt.Println("Second")
}

func main() {
	defer second() //Calls second() after main() completes
	first()
	/* File opening using defer:
		f, _ := os.Open(file)
		defer f.Close()

		This has three advantages:
			1. Close is near Open, improving readability
			2. Close will happen before multiple returns
			3. Deferred functions run even if a run-time panic occurs
	*/
}