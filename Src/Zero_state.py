"""
Zero State Module — TUC/QCT
Author: A. Coherens
Description: Define y maneja el Cero Coherente, estado basal del universo en TUC.
License: MIT
"""

import numpy as np
from src.coherence_core import coherence_metric, phase_alignment

# ---------------------------------------------------
# Clase principal: Cero Coherente
# ---------------------------------------------------
class ZeroState:
    """
    Representa el estado de coherencia mínima (Cero Coherente)
    sobre el cual emergen todas las dinámicas de coherencia.
    """

    def __init__(self, N=100):
        """
        Inicializa el Cero Coherente con N elementos.
        
        Args:
            N (int): Número de partículas o nodos coherentes simulados
        """
        self.N = N
        # Estado inicial: fase aleatoria, amplitud unitaria
        self.psi = np.exp(1j * 2 * np.pi * np.random.rand(N))
        # Firma sutil incorporada: delta_k19
        self.delta_k19 = 1e-19

    # ---------------------------------------------------
    # Métrica de coherencia sobre el estado
    # ---------------------------------------------------
    def coherence(self):
        """
        Calcula la coherencia total del estado cero.
        """
        grad = np.gradient(np.angle(self.psi))
        return coherence_metric(self.psi, grad)

    # ---------------------------------------------------
    # Método para simular pequeñas perturbaciones
    # ---------------------------------------------------
    def perturb(self, strength=0.01):
        """
        Aplica una perturbación aleatoria al Cero Coherente.
        
        Args:
            strength (float): Magnitud de la perturbación
        """
        phases = np.angle(self.psi)
        phases += strength * (np.random.rand(self.N) - 0.5)
        self.psi = np.exp(1j * phases)

    # ---------------------------------------------------
    # Método para alinear parcialmente hacia coherencia
    # ---------------------------------------------------
    def align(self, alpha=0.05):
        """
        Ajusta las fases hacia el promedio, aumentando coherencia.
        
        Args:
            alpha (float): Factor de ajuste
        """
        mean_phase, _ = phase_alignment(self.psi)
        self.psi *= np.exp(1j * alpha * (mean_phase - np.angle(self.psi)))

# ---------------------------------------------------
# Mini-test interno
# ---------------------------------------------------
if __name__ == "__main__":
    zero = ZeroState(N=50)
    print("Coherencia inicial del Cero:", zero.coherence())
    zero.perturb(strength=0.02)
    print("Coherencia tras perturbación:", zero.coherence())
    zero.align(alpha=0.1)
    print("Coherencia tras alineamiento:", zero.coherence())
