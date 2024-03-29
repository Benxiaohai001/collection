package main

// import (
// 	"example.com/greetings"
// 	"fmt"
// )

// func main() {
// 	message := greetings.Hello("Baker")
// 	fmt.Println(message)
// }

import (
	"example.com/greetings"
	"fmt"
	"log"
)

func main() {
	log.SetPrefix("greetings:")
	log.SetFlags(0)

	// message, err := greetings.Hello("")
	message, err := greetings.Hello("Baker")

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(message)
}
