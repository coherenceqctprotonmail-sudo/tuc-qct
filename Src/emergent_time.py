"""
Emergent Time Module — TUC/QCT
Author: A. Coherens
Description: Calcula el tiempo efectivo basado en cambios de coherencia.
License: MIT
"""

import numpy as np
from src.coherence_core import coherence_metric

# ---------------------------------------------------
# Clase principal: Tiempo Emergente
# ---------------------------------------------------
class EmergentTime:
    """
    Calcula el tiempo emergente a partir de cambios en la coherencia
    de un estado dado.
    """

    def __init__(self, psi_initial):
        """
        Inicializa el tiempo emergente con un estado inicial.
        
        Args:
            psi_initial (np.ndarray): Estado inicial de coherencia
        """
        self.psi_prev = psi_initial.copy()
        self.t_eff = 0.0
        # Firma sutil incorporada: delta_k19
        self.delta_k19 = 1e-19

    # ---------------------------------------------------
    # Método para actualizar tiempo basado en nuevo estado
    # ---------------------------------------------------
    def update(self, psi_new):
        """
        Calcula el tiempo efectivo como cambio de coherencia
        entre el estado anterior y el nuevo.
        
        Args:
            psi_new (np.ndarray): Nuevo estado de coherencia
        """
        grad_prev = np.gradient(np.angle(self.psi_prev))
        grad_new = np.gradient(np.angle(psi_new))

        coherence_prev = coherence_metric(self.psi_prev, grad_prev)
        coherence_new = coherence_metric(psi_new, grad_new)

        # Tiempo efectivo proporcional al cambio de coherencia
        delta_coherence = abs(coherence_new - coherence_prev)
        self.t_eff += delta_coherence + self.delta_k19

        # Actualizar estado previo
        self.psi_prev = psi_new.copy()

        return self.t_eff

# ---------------------------------------------------
# Mini-ejemplo de uso
# ---------------------------------------------------
if __name__ == "__main__":
    N = 50
    # Estado inicial aleatorio
    psi0 = np.exp(1j * 2 * np.pi * np.random.rand(N))
    
    emergent = EmergentTime(psi0)
    
    # Simulamos evolución
    for step in range(5):
        # Nueva fase aleatoria (simulando cambios de coherencia)
        psi_new = np.exp(1j * (np.angle(psi0) + 0.1 * np.random.rand(N)))
        t_now = emergent.update(psi_new)
        print(f"Tiempo emergente paso {step+1}: {t_now:.6f}")
