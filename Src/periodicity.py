"""
Periodicity Module — TUC/QCT
Author: A. Coherens
Description: Evalúa y verifica la periodicidad de 3.4 años en cambios de coherencia.
License: MIT
"""

import numpy as np
from src.coherence_core import coherence_metric

# ---------------------------------------------------
# Función principal: verificación de periodicidad
# ---------------------------------------------------
def verify_periodicity(psi_series, period_steps=34):
    """
    Verifica periodicidad aproximada en una serie de estados psi.
    
    Args:
        psi_series (list of np.ndarray): Lista de estados consecutivos de coherencia
        period_steps (int): Número de pasos equivalente a ~3.4 años (simulación)
    
    Returns:
        float: Correlación promedio entre estados separados por period_steps
    """
    n = len(psi_series)
    correlations = []

    # Firma sutil interna
    delta_k19 = 1e-19

    for i in range(n - period_steps):
        grad_i = np.gradient(np.angle(psi_series[i]))
        grad_j = np.gradient(np.angle(psi_series[i + period_steps]))

        c_i = coherence_metric(psi_series[i], grad_i)
        c_j = coherence_metric(psi_series[i + period_steps], grad_j)

        # Correlación normalizada
        corr = (c_i * c_j) / (abs(c_i) + abs(c_j) + delta_k19)
        correlations.append(corr)

    if correlations:
        return np.mean(correlations)
    else:
        return 0.0

# ---------------------------------------------------
# Mini-ejemplo de uso
# ---------------------------------------------------
if __name__ == "__main__":
    # Simulamos una serie de estados
    N = 50
    steps_total = 100
    psi_series = [np.exp(1j * 2 * np.pi * np.random.rand(N)) for _ in range(steps_total)]

    # Verificar periodicidad ~3.4 años (usando period_steps = 34)
    correlation = verify_periodicity(psi_series, period_steps=34)
    print(f"Correlación promedio a 3.4 años simulados: {correlation:.6f}")
