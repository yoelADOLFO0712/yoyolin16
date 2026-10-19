notas = [14, 16, 11, 18, 13]
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Nota maxima:", max(notas))
print("Nota minima:", min(notas))
print("Cantidad de notas:", len(notas))

from statistics import median, mode, stdev

print("Mediana de notas:", median(notas))

print("Moda de notas:", mode(notas))
print("Desviación estándar:", round(stdev(notas), 2))

print("Para ver si el usario a cambiado")
print("Prueba final de usario")