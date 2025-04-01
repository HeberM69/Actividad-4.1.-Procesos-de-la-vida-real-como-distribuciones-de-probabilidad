import numpy as np
import matplotlib.pyplot as plt
from fitter import Fitter

# 1. Datos de 10 canciones (duración en segundos)
durations = np.array([215, 212, 192, 208, 191, 205, 192, 240, 218, 214])

# 2. Graficamos el histograma
plt.hist(durations, bins=5, density=True, alpha=0.6, color='b', edgecolor='black', linewidth=1.5)
plt.xlabel("Duración (s)")
plt.ylabel("Frecuencia relativa")
plt.title("Histograma de duración de canciones")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# 3. Ajustamos la distribución con Fitter
f = Fitter(durations, distributions=['norm', 'expon', 'lognorm', 'gamma'])
f.fit()

# 4. Obtener la mejor distribución
best_distribution = f.get_best()
best_dist_name = list(best_distribution.keys())[0]  # El nombre de la mejor distribución
best_dist_params = best_distribution[best_dist_name]  # Los parámetros de la mejor distribución

# Redondeamos los parámetros a 3 decimales
best_dist_params_rounded = {key: round(value, 3) for key, value in best_dist_params.items()}

# 5. Mostrar la mejor distribución
plt.text(0.95, 0.95, f"{best_dist_name}\nParametros: {best_dist_params_rounded}", 
         fontsize=10, color='black', verticalalignment='top', horizontalalignment='right',
         transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

# Mostrar la gráfica
plt.show()
