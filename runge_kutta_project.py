import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Método de Runge Kutta de cuarto orden
def runge_kutta_4th_order(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]
    k1_values = []
    k2_values = []
    k3_values = []
    k4_values = []

    for i in range(n):
        x_n = x_values[-1]
        y_n = y_values[-1]
        k1 = h * f(x_n, y_n)
        k2 = h * f(x_n + h / 2, y_n + k1 / 2)
        k3 = h * f(x_n + h / 2, y_n + k2 / 2)
        k4 = h * f(x_n + h, y_n + k3)
        y_n_plus_1 = y_n + (k1 + 2 * k2 + 2 * k3 + k4) / 6

        # Guardar los valores calculados
        k1_values.append(k1)
        k2_values.append(k2)
        k3_values.append(k3)
        k4_values.append(k4)

        x_values.append(x_n + h)
        y_values.append(y_n_plus_1)

    k1_values.append("")
    k2_values.append("")
    k3_values.append("")
    k4_values.append("")

    return x_values, y_values, k1_values, k2_values, k3_values, k4_values


def test_function(f, exact_solution, x0, y0, h, x_end):
    n = int((x_end - x0) / h)
    x_values, y_values, k1_values, k2_values, k3_values, k4_values = runge_kutta_4th_order(f, x0, y0, h, n)
    exact_values = [exact_solution(x) for x in x_values]
    errors = [abs(y_exact - y_approx) for y_exact, y_approx in zip(exact_values, y_values)]

    # Tabla con los resultados
    data = {'x': x_values, 'y_runge_kutta': y_values, 'y_analítico': exact_values, 'error_abs': errors, 'k1': k1_values,
            'k2': k2_values, 'k3': k3_values, 'k4': k4_values}

    df = pd.DataFrame(data)
    print(df)

    # Gráfica representativa
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, 'bo-', label='Solución Aproximada (RK4)')
    plt.plot(x_values, exact_values, 'r-', label='Solución Exacta')
    plt.plot(x_values, errors, 'g--', label='Error Absoluto')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Prueba del Método de Runge Kutta de 4to Orden para {f.__name__}')
    plt.legend()
    plt.grid(True)
    plt.show()


# dy/dx = 4e^(0.8x) - 0.5y
def f(x, y):
    return 4 * np.exp(0.8 * x) - 0.5 * y


def exact_solution(x):
    # Solución analítica
    return (4 / 1.3) * (np.exp(0.8 * x) - np.exp(-0.5 * x)) + np.exp(-0.5 * x) * 2


# Ejecutar pruebas
if __name__ == "__main__":
    x0 = 0  # Valor inicial de x
    y0 = 2  # Valor inicial de y
    h = 0.5  # Distancia
    x_end = 4  # Valor final de x

    print("Prueba con la función (dy/dx = 4e^(0.8x) - 0.5y):")
    test_function(f, exact_solution, x0, y0, h, x_end)
