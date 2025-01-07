import math
import plotext as plt
import numpy as np
import sympy as sp

'''
> PROGETTO NUMERICA: PLOTTER RADICI DI FUNZIONI

> INFORMAZIONI: 
  - AUTORE:   Pascal Galli
  - CLASSE:   I1B
  - VERSIONE: 03.01.2025

> PROCEDURA

 1. Inserire la funzione 
 2. Trasformarla in funzione calcolabile in PY (^ == **)
 3. Chiedere se vuole un metodo preciso o usare il migliore
 4. Chiedere se vuole un intervallo preciso o calcolare tutti gli zeri
    4.1. Intervallo:
         4.1.1: Metodo preciso: calcola lo zero con il metodo
         4.1.2: Metodo migliore: calcola gli zeri con ogni metodo e vedere il migliore
    4.2. Tutti gli zeri:
         4.2.1: Metodo preciso: calcola lo zero con il metodo
         4.2.2: Metodo migliore: calcola gli zeri con ogni metodo e vedere il migliore
 5. Una volta trovati gli zeri chiedere se plottare il grafico con gli zeri
    o plottare un animazione dove si va vedere il metodo mentre lavora trovando gli zeri
 6. Plottare il grafico/animazione
'''

# ------------------------ FUNCTION ------------------------
def transformPyFunction(func):
    # Trasforma la funzione inserita in una forma calcolabile in Python
    new_func = func.replace("^", "**")
    return new_func


def findDerivative(func):
    # Calcola la derivata simbolica della funzione
    x = sp.symbols('x')
    funzione = sp.sympify(func)
    derivata = sp.diff(funzione, x)
    return str(derivata)


# ------------------------ PLOTTER CLASS ------------------------
class Plotter:
    @staticmethod
    def plotFunction(func, zeros=[]):
        # Grafico della funzione
        x_vals = np.linspace(-10, 10, 500)
        y_vals = [Algorythms.calculateY(func, x) for x in x_vals]

        plt.plot(x_vals, y_vals, label="Funzione")

        # Disegna assi
        plt.plot(x_vals, [0] * len(x_vals), color='gray', marker='.', label='Asse x')  # Asse x
        plt.plot([0] * len(y_vals), y_vals, color='gray', marker='.', label='Asse y')  # Asse y

        # Aggiungi zeri
        if zeros:
            plt.scatter(zeros, [0]*len(zeros), marker='o', color='red', label='Zeri')

        plt.title("Grafico della funzione")
        plt.show()


# ------------------------ ALGORYTHMS ------------------------
class Algorythms:
    function = None

    def __init__(self, function):
        self.function = function

    # --- FUNCTIONS ---
    @staticmethod
    def calculateY(func, x):
        secure_env = {"x": x, "math": math}
        return eval(func, {"__builtins__": None}, secure_env)

    # Metodo della secante
    def secantMethod(self, x0, x1, tol=1e-6, max_iter=100):
        for _ in range(max_iter):
            y0 = self.calculateY(self.function, x0)
            y1 = self.calculateY(self.function, x1)
            if abs(y1 - y0) < tol:
                return None  # Evita divisione per zero
            x2 = x1 - y1 * (x1 - x0) / (y1 - y0)
            if abs(x2 - x1) < tol:
                return x2
            x0, x1 = x1, x2
        return None

    # Metodo della tangente (Newton-Raphson)
    def newtonRaphson(self, x0, tol=1e-6, max_iter=100):
        x = sp.symbols('x')
        funzione = sp.sympify(self.function)
        derivata = sp.diff(funzione, x)
        for _ in range(max_iter):
            f_val = self.calculateY(self.function, x0)
            f_der = self.calculateY(str(derivata), x0)
            if abs(f_der) < tol:
                return None  # Evita divisione per zero
            x1 = x0 - f_val / f_der
            if abs(x1 - x0) < tol:
                return x1
            x0 = x1
        return None

    # Metodo di bisezione
    def bisectionMethod(self, a, b, tol=1e-6, max_iter=100):
        if self.calculateY(self.function, a) * self.calculateY(self.function, b) >= 0:
            return None  # Controlla che ci sia un cambiamento di segno
        for _ in range(max_iter):
            c = (a + b) / 2
            if abs(self.calculateY(self.function, c)) < tol or (b - a) / 2 < tol:
                return c
            if self.calculateY(self.function, c) * self.calculateY(self.function, a) < 0:
                b = c
            else:
                a = c
        return None

    # Metodo di regula falsi
    def regulaFalsiMethod(self, a, b, tol=1e-6, max_iter=100):
        for _ in range(max_iter):
            fa = self.calculateY(self.function, a)
            fb = self.calculateY(self.function, b)
            c = (a * fb - b * fa) / (fb - fa)
            fc = self.calculateY(self.function, c)
            if abs(fc) < tol:
                return c
            if fa * fc < 0:
                b = c
            else:
                a = c
        return None


# ------------------------ MAIN ------------------------
func_input = input("Insert function: ")
func = transformPyFunction(func_input)

# Visualizza la derivata
derivative = findDerivative(func)
print("Derivata:", derivative)

fFunc = Algorythms(func)

# Metodo di scelta
method = input("Vuoi usare il metodo della Secante (S), Tangente (T), Bisezione (B) o Regula Falsi (R)? [S/T/B/R]: ").upper()
interval_choice = input("Vuoi fornire un intervallo specifico? (y/n): ").lower()

zeros = []

if interval_choice == 'y':
    x0 = float(input("Inserisci x0: "))
    x1 = float(input("Inserisci x1: "))
    if method == 'S':
        zero = fFunc.secantMethod(x0, x1)
    elif method == 'T':
        zero = fFunc.newtonRaphson(x0)
    elif method == 'B':
        zero = fFunc.bisectionMethod(x0, x1)
    elif method == 'R':
        zero = fFunc.regulaFalsiMethod(x0, x1)
    zeros.append(zero)
else:
    for x in np.linspace(-10, 10, 10):
        if method == 'S':
            zero = fFunc.secantMethod(x, x + 0.1)
        elif method == 'T':
            zero = fFunc.newtonRaphson(x)
        elif method == 'B':
            zero = fFunc.bisectionMethod(x, x + 0.1)
        elif method == 'R':
            zero = fFunc.regulaFalsiMethod(x, x + 0.1)
        if zero is not None and zero not in zeros:
            zeros.append(zero)

print("Zeri trovati:")
for i, z in enumerate(zeros):
    print(f"Zero {i+1}: {z:.4f}")

plot_choice = input("Vuoi plottare la funzione con gli zeri trovati? (y/n): ").lower()
if plot_choice == 'y':
    Plotter.plotFunction(func, zeros)

# ------------------------ FINE CODICE ------------------------