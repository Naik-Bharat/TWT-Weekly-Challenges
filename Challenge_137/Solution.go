package main

import "fmt"

func main() {
	T := 0
	fmt.Scanln(&T)
	for i := 0; i < T; i++ {
		var str string
		fmt.Scanln(&str)
		count := 0
		for start, end := 0, len(str)-1; start < end; {
			if fmt.Sprintf("%c", str[start]) == "B" && fmt.Sprintf("%c", str[end]) == "A" {
				count++
				start++
				end--
			} else if fmt.Sprintf("%c", str[start]) == "B" {
				end--
			} else if fmt.Sprintf("%c", str[end]) == "A" {
				start++
			} else {
				start++
				end--
			}
		}
		println(count)
	}
}
