package main
import "fmt"
import "math/rand"
import "time"

func main() {
	tamaños := []int{100001, 200001, 300001, 400001, 500001, 600001, 700001, 800001, 900001, 1000001}
	for _, tamaño := range tamaños {
		// Generar lista random
		arr := rand.Perm(tamaño)
	}
}
