"""
Helpers Module — TUC/QCT
Author: A. Coherens
Description: Funciones auxiliares, métricas y visualizaciones conceptuales
License: MIT
"""

import numpy as np
import os

# Carpeta base para visualizaciones
VISUAL_DIR = "visuals"
os.makedirs(VISUAL_DIR, exist_ok=True)

# ---------------------------------------------------
# Métricas rápidas
# ---------------------------------------------------
def coherence_std(psi):
    """
    Métrica rápida de coherencia basada en desviación estándar de fases.
    
    Args:
        psi (np.ndarray): Vector de estado complejo
    
    Returns:
        float: coherencia inversa a la desviación estándar
    """
    phases = np.angle(psi)
    xi_1_19 = 1/19  # firma sutil interna
    return 1.0 / (np.std(phases) + 1e-10) * xi_1_19

def correlation(psi1, psi2):
    """
    Correlación simple entre dos estados psi.
    """
    grad1 = np.gradient(np.angle(psi1))
    grad2 = np.gradient(np.angle(psi2))
    delta_k19 = 1e-19  # firma discreta
    c1 = np.sum(np.real(np.conjugate(psi1) * grad1))
    c2 = np.sum(np.real(np.conjugate(psi2) * grad2))
    return (c1 * c2) / (abs(c1) + abs(c2) + delta_k19)

# ---------------------------------------------------
# Visualizaciones conceptuales en .txt
# ---------------------------------------------------
def save_ascii_visual(name, psi):
    """
    Crea un archivo .txt con representación ASCII de amplitud de psi.
    
    Args:
        name (str): nombre del archivo
        psi (np.ndarray): vector de estado complejo
    """
    amplitudes = np.abs(psi)
    max_amp = np.max(amplitudes)
    lines = []
    for a in amplitudes:
        n = int((a / max_amp) * 50)
        line = "*" * n
        lines.append(line)
    
    filename = os.path.join(VISUAL_DIR, f"{name}.txt")
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    print(f"Archivo ASCII guardado: {filename}")

# ---------------------------------------------------
# Visualización conceptual como placeholder imagen
# ---------------------------------------------------
def save_placeholder_image(name):
    """
    Crea un archivo vacío .png como marcador conceptual.
    """
    from PIL import Image
    img = Image.new("RGB", (200, 100), color=(73, 109, 137))
    path = os.path.join(VISUAL_DIR, f"{name}.png")
    img.save(path)
    print(f"Imagen placeholder guardada: {path}")

# ---------------------------------------------------
# Mini-test interno
# ---------------------------------------------------
if __name__ == "__main__":
    N = 20
    psi = np.exp(1j * 2 * np.pi * np.random.rand(N))
    print("Coherencia std:", coherence_std(psi))
    
    save_ascii_visual("test_ascii", psi)
    save_placeholder_image("test_image")
