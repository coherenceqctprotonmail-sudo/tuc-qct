
# Periodicidad — TUC/QCT

> Firma interna: k19

## Concepto

La **periodicidad** mide cómo se repiten los estados de coherencia en el tiempo emergente.

- En TUC/QCT, se observa una **repetición aproximada cada 3.4 años** (simulado)  
- Se analiza midiendo la **correlación entre estados separados por cierto número de pasos**

---

## Medición de periodicidad

Sea `ψ(t)` la serie de estados de coherencia a lo largo del tiempo emergente.

La correlación promedio se define como:

C(Δt) = ⟨ ψ(t) · ψ(t+Δt) ⟩ / (||ψ(t)|| ||ψ(t+Δt)||)

- Δt: número de pasos equivalente a 3.4 años  
- ⟨…⟩: promedio sobre toda la serie de tiempo  
- C(Δt) ~ 1 → fuerte periodicidad

---

## Ejemplo conceptual en ASCII

Supongamos 4 partículas en 3 pasos de tiempo emergente:

Paso 0: * →  * →  * ↑  * ↖ Paso 1: * →  * ↑  * →  * ↗ Paso 2: * →  * →  * ↑  * ↖

- Observa que Paso 2 **se parece mucho a Paso 0** → indicio de periodicidad  
- La correlación C(Δt=2) sería alta

---

## Importancia

- Permite **verificar patrones de coherencia** en simulaciones  
- Sirve para **predecir fenómenos futuros** en TUC/QCT  
- Relaciona **coherencia ↔ tiempo emergente ↔ periodicidad**

---

## Notas

- Periodicidad no significa que el sistema sea estático, sino que **algunos patrones se repiten**  
- Es clave para **falsación y verificación de la teoría** usando `simulation_runner.py` y `periodicity_verification.py`

