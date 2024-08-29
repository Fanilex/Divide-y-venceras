package main

import (
	"fmt"
	"math/rand"
	"time"
)

//ordena + selecciona

func countingSort(arr []int, exp int) []int {
	n := len(arr)
	output := make([]int, n)
	count := make([]int, 10)

	for i := 0; i < n; i++ {
		index := (arr[i] / exp) % 10
		count[index]++
	}

	for i := 1; i < 10; i++ {
		count[i] += count[i-1]
	}

	for i := n - 1; i >= 0; i-- {
		index := (arr[i] / exp) % 10
		output[count[index]-1] = arr[i]
		count[index]--
	}

	return output
}

func radixSort(arr []int) []int {
	max := getMax(arr)

	for exp := 1; max/exp > 0; exp *= 10 {
		arr = countingSort(arr, exp)
	}
	return arr
}

func getMax(arr []int) int {
	max := arr[0]
	for _, num := range arr {
		if num > max {
			max = num
		}
	}
	return max
}

func findMedianByRadixSort(arr []int) int {
	sortedArr := radixSort(arr)
	mid := len(sortedArr) / 2
	if len(sortedArr)%2 == 0 {
		return (sortedArr[mid-1] + sortedArr[mid]) / 2
	}
	return sortedArr[mid]
}

func main() {
	sizes := []int{100001, 200001, 300001, 400001, 500001, 600001, 700001, 800001, 900001, 1000001}
	for _, size := range sizes {
		arr := rand.Perm(size)

		start := time.Now()
		median := findMedianByRadixSort(arr)
		elapsed := time.Since(start)

		fmt.Printf("Tamaño de lista: %d, Mediana: %d, Tiempo de ejecución: %s\n", size, median, elapsed)
	}
}
