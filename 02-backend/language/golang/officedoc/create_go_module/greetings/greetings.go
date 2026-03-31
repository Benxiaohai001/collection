package greetings

import (
	"errors"
	"fmt"
	"math/rand"
)

// func Hello(name string) string {
// 	message := fmt.Sprintf("Hi, %v. Welcome!", name)
// 	return message
// }

func Hello(name string) (string, error) {
	if name == "" {
		return "", errors.New("empty name")
	}

	// message := fmt.Sprintf("Hi, %v. Welcome!", name)
	message := fmt.Sprintf(randomFormat(), name)
	return message, nil
}

func Hellos(names []string) (string, error) {
	// A map to associate each name with messages.
	messages := make(map[string]string)
	// Loop through the received slice of names, calling the Hello function to get a message for each name.
	for 
}

func randomFormat() string { // Add a new function randomFormat to greetings.go, which returns one of three greeting messages selected at random.小写字母开头的函数名表示私有函数，不能导出
	formats := []string{ // 切片，相当于一个list
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"Hail, %v! Well met!",
	}

	return formats[rand.Intn(len(formats))]
}
