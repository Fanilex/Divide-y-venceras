package main
import "fmt"
import "math/rand"
import "time"

func seleccion(arr []int, izq, der, k int) int {
	if izq == der { // caso base
		return arr[izq]
	}

	indicePivote := particionar(arr, izq, der)

	if k == indicePivote {
		return arr[k]
	} else if k < indicePivote {
		return seleccion(arr, izq, indicePivote-1, k)
	} else {
		return seleccion(arr, indicePivote+1, der, k)
	}
}

// Función para particionar la lista de randoms
func particionar(arr []int, izq, der int) int {
	indicePivote := izq + rand.Intn(der-izq+1)
	valorPivote := arr[indicePivote]
	arr[indicePivote], arr[der] = arr[der], arr[indicePivote] 

	indiceAlmacen := izq
	for i := izq; i < der; i++ {
		if arr[i] < valorPivote {
			arr[indiceAlmacen], arr[i] = arr[i], arr[indiceAlmacen]
			indiceAlmacen++
		}
	}

	arr[indiceAlmacen], arr[der] = arr[der], arr[indiceAlmacen] 
	return indiceAlmacen
}

func mediana(arr []int) int {
	n := len(arr)
	if n%2 == 1 {
		return seleccion(arr, 0, n-1, n/2) // Si el tamaño de la lista es impar
	} else {
		return (seleccion(arr, 0, n-1, n/2-1) + seleccion(arr, 0, n-1, n/2)) / 2 // Si el tamaño de la lista es par
	}
}

func medirTiempo(arr []int) float64 {
	inicio := time.Now()
	mediana(arr)
	duracion := time.Since(inicio).Seconds()
	return duracion
}

func main() {
	rand.Seed(time.Now().UnixNano())

	tamaños := []int{100001, 200001, 300001, 400001, 500001, 600001, 700001, 800001, 900001, 1000001}
	for _, tamaño := range tamaños {

		// Generar lista de numeros random
		arr := rand.Perm(tamaño)

		// Se buscó como imprimir ya el tiempo de ejecución
		tiempo := medirTiempo(arr)

		valorMediana := mediana(arr)

		fmt.Printf("Tamaño de lista: %d, Mediana: %d, Tiempo de ejecución: %.6f segundos\n", tamaño, valorMediana, tiempo)
	}
}
