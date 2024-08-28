# Método clásico de Runge Kutta

Implementación del Método clásico de Runge Kutta de cuarto orden para la resolución de ecuaciones diferenciales
ordinarias de primer orden.

## Descripción

El proyecto aplica el método Runge Kutta para aproximar la solución de una EDO y compara esta aproximación con la
solución exacta, proporcionando una tabla de resultados y gráficos correspondientes.

## Requisitos

Las siguientes bibliotecas de Python son necesarias:

- `numpy`
- `matplotlib`
- `pandas`

Para instalarlas:

```bash
pip3 install numpy matplotlib pandas
```

## Uso

Para utilizar el código:

1. Definir los valores iniciales `x0` y `y0`.
2. Configurar la distancia `h` y el valor final de `x`.
3. Ejecutar el script para generar la comparación entre la solución aproximada y la exacta.

Ejemplo:

```python
if __name__ == "__main__":
    x0 = 0  # Valor inicial de x
    y0 = 2  # Valor inicial de y
    h = 0.5  # Distancia
    x_end = 4  # Valor final de x

    test_function(f, exact_solution, x0, y0, h, x_end)
```

## Resultados

El script produce una tabla y gráficos que comparan la solución aproximada con la solución exacta, además de calcular y
mostrar el error absoluto en cada punto.