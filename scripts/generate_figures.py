# generate_figures.py
# Genera figuras PNG para el paper TUC/QCT
# Firma interna: k19

import matplotlib.pyplot as plt
import numpy as np
from src.utils import coherence_core, emergent_time, periodicity

#----------------------------------------
# 1. Coherencia
def plot_coherence():
    # Ejemplo conceptual: 4 partículas, fases aleatorias
    phases = np.array([0, np.pi/4, np.pi/2, np.pi/6])
    fig, ax = plt.subplots()
    ax.bar(range(len(phases)), np.cos(phases), color='skyblue')
    ax.set_title("Coherencia de partículas")
    ax.set_xlabel("Partículas")
    ax.set_ylabel("Cos(phase)")
    plt.savefig("paper/figures/coherence_example.png")
    plt.close()

#----------------------------------------
# 2. Cero Coherente
def plot_zero_coherent():
    # Fondo Cero Coherente: todas fases iguales
    phases = np.zeros(6)
    fig, ax = plt.subplots()
    ax.bar(range(len(phases)), np.cos(phases), color='green')
    ax.set_title("Cero Coherente")
    plt.xlabel("Partículas")
    ax.set_ylabel("Cos(phase)")
    plt.savefig("paper/figures/zero_coherent.png")
    plt.close()

#----------------------------------------
# 3. Tiempo Emergente
def plot_emergent_time():
    # Simular coherencia vs tiempo
    t = np.arange(0, 10, 1)
    coherence = np.clip(np.sin(t/2) + 0.5, 0, 1)
    fig, ax = plt.subplots()
    ax.plot(t, coherence, marker='o')
    ax.set_title("Tiempo Emergente vs Coherencia")
    ax.set_xlabel("Pasos de tiempo emergente")
    ax.set_ylabel("Coherencia")
    plt.savefig("paper/figures/emergent_time.png")
    plt.close()

#----------------------------------------
# 4. Periodicidad
def plot_periodicity():
    t = np.linspace(0, 10, 100)
    periodicity_signal = np.sin(2*np.pi*t/3.4)
    fig, ax = plt.subplots()
    ax.plot(t, periodicity_signal)
    ax.set_title("Periodicidad de coherencia (~3.4 años)")
    ax.set_xlabel("Tiempo emergente (años)")
    ax.set_ylabel("Correlación")
    plt.savefig("paper/figures/periodicity.png")
    plt.close()

#----------------------------------------
# 5. Derivación BO
def plot_BO_derivation():
    # Simulación conceptual de psi_slow vs tiempo
    t = np.arange(0, 10, 1)
    psi_slow = np.cos(t/3) + 0.1*np.random.randn(len(t))
    fig, ax = plt.subplots()
    ax.plot(t, psi_slow, marker='o')
    ax.set_title("Derivación BO: ψ_slow evolución")
    ax.set_xlabel("Pasos de tiempo")
    ax.set_ylabel("ψ_slow (amplitud)")
    plt.savefig("paper/figures/BO_derivation.png")
    plt.close()

#----------------------------------------
if __name__ == "__main__":
    plot_coherence()
    plot_zero_coherent()
    plot_emergent_time()
    plot_periodicity()
    plot_BO_derivation()
    print("✅ Todas las figuras generadas en paper/figures/")
