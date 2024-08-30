import matplotlib.pyplot as plt
import numpy as np

sizes = [100001, 300001, 500001, 700001, 900001]

times_run_1 = [1.606, 6.326, 13.107, 14.514, 22.066]
times_run_2 = [2.430, 4.003, 14.924, 14.924, 21.622]
times_run_3 = [2.698, 8.562, 13.675, 17.465, 20.069]
times_run_4 = [1.309, 7.337, 14.881, 15.146, 22.464]
times_run_5 = [1.309, 4.271, 14.881, 17.712, 22.464]

average_times = [(r1 + r2 + r3 + r4 + r5) / 5 for r1, r2, r3, r4, r5 in zip(times_run_1, times_run_2, times_run_3, times_run_4, times_run_5)]

std_deviation = [np.std([r1, r2, r3, r4, r5]) for r1, r2, r3, r4, r5 in zip(times_run_1, times_run_2, times_run_3, times_run_4, times_run_5)]

plt.figure(figsize=(10, 6))

plt.plot(times_run_1, sizes, marker='o', color='gray', linestyle='--', alpha=0.4, label='Corrida 1')
plt.plot(times_run_2, sizes, marker='o', color='gray', linestyle='--', alpha=0.4, label='Corrida 2')
plt.plot(times_run_3, sizes, marker='o', color='gray', linestyle='--', alpha=0.4, label='Corrida 3')
plt.plot(times_run_4, sizes, marker='o', color='gray', linestyle='--', alpha=0.4, label='Corrida 4')
plt.plot(times_run_5, sizes, marker='o', color='gray', linestyle='--', alpha=0.4, label='Corrida 5')

plt.errorbar(average_times, sizes, xerr=std_deviation, fmt='o', color='blue', linestyle='-', linewidth=4, markersize=10, ecolor='black', elinewidth=1.5, label='Promedio')

plt.xlabel('Tiempo de ejecución (milisegundos)')
plt.ylabel('Tamaño de lista')
plt.title('Tiempos de ejecución de QuickSelect con Desviación Estándar')
plt.legend()
plt.grid(True)
plt.show()
