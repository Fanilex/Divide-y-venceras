import matplotlib.pyplot as plt

times_radix_sort = [
    [10.5465, 61.1378, 32.0155, 37.3625, 59.2767],
    [10.5329, 20.7298, 40.7566, 47.063, 66.1663],
    [15.3329, 25.0674, 41.2327, 59.2861, 62.7924],
    [9.2193, 31.5068, 39.3373, 60.0939, 62.1213],
    [10.8332, 23.8034, 51.8323, 51.2114, 62.2959]
]

times_quickselect = [
    [1.606, 6.326, 13.107, 14.514, 22.066],
    [2.430, 4.003, 14.924, 14.924, 21.622],
    [2.698, 8.562, 13.675, 17.465, 20.069],
    [1.309, 7.337, 14.881, 15.146, 22.464],
    [1.309, 4.271, 14.881, 17.712, 22.464]
]

times_mediana_de_medianas = [
    [4.419209, 7.092333, 9.038042, 8.571125, 10.7345],
    [3.714125, 11.649834, 14.64, 24.522375, 23.632834],
    [5.038583, 11.860542, 9.337333, 21.045875, 26.563833],
    [5.220083, 11.729125, 15.831417, 19.445292, 20.132458],
    [3.6425, 9.798458, 15.221958, 18.783917, 17.916125]
]

sizes = [100001, 300001, 500001, 700001, 900001]

average_times_radix_sort = [sum(times) / len(times) for times in zip(*times_radix_sort)]
average_times_quickselect = [sum(times) / len(times) for times in zip(*times_quickselect)]
average_times_mediana_de_medianas = [sum(times) / len(times) for times in zip(*times_mediana_de_medianas)]

plt.figure(figsize=(10, 6))

# Ordena + Select (Radix Sort)
plt.plot(average_times_radix_sort, sizes, marker='o', linestyle='-', color='red', linewidth=2, label='Radix Sort')

# QuickSelect
plt.plot(average_times_quickselect, sizes, marker='o', linestyle='-', color='green', linewidth=2, label='Quickselect')

# Mediana de Medianas
plt.plot(average_times_mediana_de_medianas, sizes, marker='o', linestyle='-', color='blue', linewidth=2, label='Mediana de Medianas')

plt.xlabel('Tiempo de ejecución promedio (milisegundos)')
plt.ylabel('Tamaño de lista')
plt.title('Comparación de tiempos de ejecución entre algoritmos')
plt.legend()
plt.grid(True)
plt.show()
