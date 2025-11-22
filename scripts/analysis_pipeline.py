"""
Analysis Pipeline — TUC/QCT
Author: A. Coherens
Description: Pipeline principal de análisis de coherencia, tiempo emergente y periodicidad.
License: MIT
"""

import numpy as np
import os
from src.coherence_core import coherence_metric, phase_alignment, evolve_coherence
from src.zero_state import ZeroState
from src.emergent_time import EmergentTime
from src.periodicity import verify_periodicity
from src.utils import helpers

# Carpeta de resultados
RESULTS_DIR = "pipeline_results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# ---------------------------------------------------
# Función principal del pipeline
# ---------------------------------------------------
def run_pipeline(N=50, steps=20, alpha=0.05, period_steps=10):
    """
    Ejecuta el pipeline completo: Cero Coherente → Evolución → Tiempo emergente → Periodicidad
    """
    print("=== TUC/QCT Analysis Pipeline ===")
    
    # 1️⃣ Inicializar Cero Coherente
    zero = ZeroState(N=N)
    print("Coherencia inicial:", zero.coherence())

    # 2️⃣ Inicializar tiempo emergente
    emergent = EmergentTime(zero.psi)
    
    # 3️⃣ Lista de estados para periodicidad
    psi_series = [zero.psi.copy()]
    
    # 4️⃣ Evolución de estados
    for step in range(steps):
        # Evolución hacia mayor coherencia
        zero.align(alpha=alpha)
        zero.perturb(strength=0.02)
        psi_series.append(zero.psi.copy())
        
        # Actualizar tiempo emergente
        t_now = emergent.update(zero.psi)
        print(f"Paso {step+1} — Tiempo emergente: {t_now:.6f}")
        
        # Guardar visualizaciones
        helpers.save_ascii_visual(f"state_step_{step+1}", zero.psi)
        helpers.save_placeholder_image(f"state_step_{step+1}")

    # 5️⃣ Verificación de periodicidad
    corr = verify_periodicity(psi_series, period_steps=period_steps)
    print(f"Correlación promedio a {period_steps} pasos: {corr:.6f}")

    # 6️⃣ Guardar resumen de resultados
    summary_path = os.path.join(RESULTS_DIR, "summary.txt")
    with open(summary_path, "w") as f:
        f.write(f"Coherencia final: {zero.coherence():.6f}\n")
        f.write(f"Tiempo emergente final: {emergent.t_eff:.6f}\n")
        f.write(f"Correlación promedio a {period_steps} pasos: {corr:.6f}\n")
    print(f"Resumen guardado en: {summary_path}")

# ---------------------------------------------------
# Mini-ejemplo de ejecución
# ---------------------------------------------------
if __name__ == "__main__":
    run_pipeline(N=50, steps=10, alpha=0.05, period_steps=5)
