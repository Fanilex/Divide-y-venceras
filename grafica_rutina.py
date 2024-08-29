import matplotlib.pyplot as plt

# Datos de tamaños de lista
sizes = [
    100001, 200001, 300001, 400001, 500001, 600001, 700001, 800001, 900001,
    1000001
]

# Tiempos de ejecución de cada corrida
times_run_1 = [
    0.001606, 0.004271, 0.006326, 0.008454, 0.019107, 0.022562, 0.014514,
    0.010026, 0.022066, 0.021622
]
times_run_2 = [
    0.002430, 0.003932, 0.004003, 0.009567, 0.009393, 0.021088, 0.014924,
    0.015146, 0.017712, 0.019019
]
times_run_3 = [
    0.002698, 0.008562, 0.012893, 0.009291, 0.017675, 0.027200, 0.017465,
    0.019118, 0.012069, 0.024902
]
times_run_4 = [
    0.001309, 0.007337, 0.011917, 0.009387, 0.014881, 0.013283, 0.009581,
    0.021242, 0.022464, 0.026093
]
times_run_5 = [
    0.001309, 0.007337, 0.011917, 0.009387, 0.014881, 0.013283, 0.009581,
    0.021242, 0.022464, 0.026093
]

# Calcular el promedio de los tiempos de ejecución
average_times = [(r1 + r2 + r3 + r4 + r5) / 5 for r1, r2, r3, r4, r5 in zip(
    times_run_1, times_run_2, times_run_3, times_run_4, times_run_5)]

# Graficar los tiempos de ejecución
plt.figure(figsize=(10, 6))
plt.plot(sizes, times_run_1, marker='o', label='Corrida 1')
plt.plot(sizes, times_run_2, marker='o', label='Corrida 2')
plt.plot(sizes, times_run_3, marker='o', label='Corrida 3')
plt.plot(sizes, times_run_4, marker='o', label='Corrida 4')
plt.plot(sizes, times_run_5, marker='o', label='Corrida 5')
plt.plot(sizes, average_times,
        marker='o',
        color='black',
        linestyle='--',
        label='Promedio')

plt.xlabel('Tamaño de lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title(
    'Tiempos de ejecución de Quickselect para diferentes tamaños de lista')
plt.legend()
plt.grid(True)
plt.show()
