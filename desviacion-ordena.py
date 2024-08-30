import matplotlib.pyplot as plt
import numpy as np

sizes = [100001, 300001, 500001, 700001, 900001]

times_run_1 = [10.5465, 61.1378, 32.0155, 37.3625, 59.2767]
times_run_2 = [10.5329, 20.7298, 40.7566, 47.063, 66.1663]
times_run_3 = [15.3329, 25.0674, 41.2327, 59.2861, 62.7924]
times_run_4 = [9.2193, 31.5068, 39.3373, 60.0939, 62.1213]
times_run_5 = [10.8332, 23.8034, 51.8323, 51.2114, 62.2959]

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
plt.title('Tiempos de ejecución de Ordena + Select con Desviación Estándar')
plt.legend()
plt.grid(True)
plt.show()
