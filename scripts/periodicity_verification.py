"""
Periodicity Verification Script — TUC/QCT
Author: A. Coherens
Description: Verificación detallada de periodicidad de coherencia (~3.4 años simulados)
License: MIT
"""

import numpy as np
import os
from src.zero_state import ZeroState
from src.periodicity import verify_periodicity
from src.utils import helpers

# Carpeta de resultados
PERIODICITY_DIR = "periodicity_results"
os.makedirs(PERIODICITY_DIR, exist_ok=True)

# ---------------------------------------------------
# Función principal de verificación
# ---------------------------------------------------
def periodicity_check(N=50, total_steps=100, period_steps=34):
    """
    Simula evolución de Cero Coherente y calcula periodicidad.
    
    Args:
        N (int): Número de nodos
        total_steps (int): Pasos de simulación
        period_steps (int): Pasos equivalentes a ~3.4 años
    """
    print("=== Periodicity Verification ===")
    
    zero = ZeroState(N=N)
    psi_series = [zero.psi.copy()]
    
    # Evolución simple del Cero Coherente
    for step in range(total_steps):
        zero.perturb(strength=0.02)
        zero.align(alpha=0.05)
        psi_series.append(zero.psi.copy())
        
        # Guardar visualizaciones intermedias
        helpers.save_ascii_visual(f"periodicity_step_{step+1}", zero.psi)
        helpers.save_placeholder_image(f"periodicity_step_{step+1}")
    
    # Calcular periodicidad
    correlation = verify_periodicity(psi_series, period_steps=period_steps)
    print(f"Correlación promedio a {period_steps} pasos: {correlation:.6f}")
    
    # Guardar reporte
    report_path = os.path.join(PERIODICITY_DIR, "periodicity_report.txt")
    with open(report_path, "w") as f:
        f.write(f"Pasos totales: {total_steps}\n")
        f.write(f"Correlación promedio a {period_steps} pasos: {correlation:.6f}\n")
    print(f"Reporte guardado en: {report_path}")

# ---------------------------------------------------
# Mini-ejemplo de ejecución
# ---------------------------------------------------
if __name__ == "__main__":
    periodicity_check(N=50, total_steps=50, period_steps=10)
