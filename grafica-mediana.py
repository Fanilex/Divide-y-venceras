import matplotlib.pyplot as plt

sizes = [100001, 300001, 500001, 700001, 900001]

times_run_1 = [4.419209, 7.092333, 9.038042, 8.571125, 10.7345]
times_run_2 = [3.714125, 11.649834, 14.64, 24.522375, 23.632834]
times_run_3 = [5.038583, 11.860542, 9.337333, 21.045875,26.563833]
times_run_4 = [5.220083, 11.729125, 15.831417, 19.445292,20.132458]
times_run_5 = [3.6425, 9.798458, 15.221958, 18.783917,17.916125]

average_times = [(r1 + r2 + r3 + r4 + r5) / 5 for r1, r2, r3, r4, r5 in zip(times_run_1, times_run_2, times_run_3, times_run_4, times_run_5)]

plt.figure(figsize=(10, 6))

plt.plot(times_run_1, sizes, marker='o', color='gray', linestyle='--', alpha=0.4, label='Corrida 1')
plt.plot(times_run_2, sizes, marker='o', color='gray', linestyle='--', alpha=0.4, label='Corrida 2')
plt.plot(times_run_3, sizes, marker='o', color='gray', linestyle='--', alpha=0.4, label='Corrida 3')
plt.plot(times_run_4, sizes, marker='o', color='gray', linestyle='--', alpha=0.4, label='Corrida 4')
plt.plot(times_run_5, sizes, marker='o', color='gray', linestyle='--', alpha=0.4, label='Corrida 5')

plt.plot(average_times, sizes, marker='o', color='blue', linestyle='-', linewidth=4, markersize=10, label='Promedio')

plt.xlabel('Tiempo de ejecución (milisegundos)')
plt.ylabel('Tamaño de lista')
plt.title('Tiempos de ejecución de Ordena + Select para diferentes tamaños de lista')
plt.legend()
plt.grid(True)
plt.show()
