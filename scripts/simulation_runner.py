"""
Simulation Runner — TUC/QCT
Author: A. Coherens
Description: Ejecuta simulaciones completas de coherencia, tiempo emergente y periodicidad.
License: MIT
"""

import os
import numpy as np
from datetime import datetime
from src.zero_state import ZeroState
from src.emergent_time import EmergentTime
from src.periodicity import verify_periodicity
from src.utils import helpers

# Carpeta principal de resultados
SIMULATION_DIR = "simulation_results"
os.makedirs(SIMULATION_DIR, exist_ok=True)

# ---------------------------------------------------
# Función para crear carpeta por experimento
# ---------------------------------------------------
def create_experiment_folder(base_dir, name=None):
    if name is None:
        name = datetime.now().strftime("exp_%Y%m%d_%H%M%S")
    path = os.path.join(base_dir, name)
    os.makedirs(path, exist_ok=True)
    return path

# ---------------------------------------------------
# Función de simulación completa
# ---------------------------------------------------
def run_simulation(N=50, steps=50, alpha=0.05, period_steps=10, experiment_name=None):
    """
    Ejecuta simulación completa:
    - Inicializa Cero Coherente
    - Evoluciona estado y calcula tiempo emergente
    - Verifica periodicidad
    - Guarda visualizaciones TXT + PNG y resúmenes
    """
    print("=== Running Full Simulation ===")
    exp_path = create_experiment_folder(SIMULATION_DIR, experiment_name)

    # Inicializar Cero Coherente
    zero = ZeroState(N=N)
    print(f"Coherencia inicial: {zero.coherence():.6f}")

    # Inicializar Tiempo Emergente
    emergent = EmergentTime(zero.psi)

    # Lista de estados para periodicidad
    psi_series = [zero.psi.copy()]

    # Carpeta de visualizaciones
    visuals_path = os.path.join(exp_path, "visuals")
    os.makedirs(visuals_path, exist_ok=True)

    # Evolución de estados
    for step in range(steps):
        zero.align(alpha=alpha)
        zero.perturb(strength=0.02)
        psi_series.append(zero.psi.copy())

        # Actualizar tiempo emergente
        t_now = emergent.update(zero.psi)
        print(f"Step {step+1} — Tiempo emergente: {t_now:.6f}")

        # Guardar visualizaciones
        helpers.save_ascii_visual(os.path.join(visuals_path, f"state_step_{step+1}"), zero.psi)
        helpers.save_placeholder_image(os.path.join(visuals_path, f"state_step_{step+1}"))

    # Verificación de periodicidad
    correlation = verify_periodicity(psi_series, period_steps=period_steps)
    print(f"Correlación promedio a {period_steps} pasos: {correlation:.6f}")

    # Guardar resumen de resultados
    summary_path = os.path.join(exp_path, "summary.txt")
    with open(summary_path, "w") as f:
        f.write(f"Experimento: {experiment_name}\n")
        f.write(f"Coherencia final: {zero.coherence():.6f}\n")
        f.write(f"Tiempo emergente final: {emergent.t_eff:.6f}\n")
        f.write(f"Correlación promedio a {period_steps} pasos: {correlation:.6f}\n")
    print(f"Resumen guardado en: {summary_path}")

    return exp_path

# ---------------------------------------------------
# Función para correr múltiples experimentos
# ---------------------------------------------------
def run_multiple_experiments(num_experiments=3, **kwargs):
    results = []
    for i in range(num_experiments):
        print(f"\n=== Experimento {i+1}/{num_experiments} ===")
        exp_name = f"experiment_{i+1}"
        path = run_simulation(experiment_name=exp_name, **kwargs)
        results.append(path)
    return results

# ---------------------------------------------------
# Mini-ejemplo de ejecución
# ---------------------------------------------------
if __name__ == "__main__":
    # Ejecuta 2 experimentos completos
    run_multiple_experiments(num_experiments=2, N=50, steps=10, alpha=0.05, period_steps=5)
