Derivación Paso a Paso: Born-Oppenheimer y Tiempo Emergente — TUC/QCT

Este tutorial muestra cómo se puede derivar el **tiempo emergente** a partir del **formalismo Born-Oppenheimer** en el marco de la **Teoría Unificada de la Coherencia (TUC/QCT)**.


---

## 1️⃣ Concepto básico

El formalismo **Born-Oppenheimer (BO)** separa las **dinámicas rápidas** de las **lentas** en un sistema:

- Partículas “lentas”: generan un **fondo de coherencia**  
- Partículas “rápidas”: se mueven sobre este fondo  

En TUC/QCT:

- El **Cero Coherente** es el fondo  
- Las **perturbaciones y cambios de coherencia** generan **tiempo emergente**

---

## 2️⃣ Paso 1: Ecuación sin tiempo

Partimos de una **ecuación maestra sin tiempo** (timeless):

H Ψ = 0

- `H`: Hamiltoniano total del sistema  
- `Ψ`: estado total (partículas lentas + rápidas)  

> Concepto: el universo en su estado más fundamental **no tiene tiempo**.

---

## 3️⃣ Paso 2: Separación BO

Separamos `Ψ` en partes lenta (`ψ_slow`) y rápida (`χ_fast`):

Ψ(x, y) = χ_fast(x; y) ψ_slow(y)

- `y`: coordenadas lentas (Cero Coherente)  
- `x`: coordenadas rápidas (partículas excitadas)  

> Analogía simple: `ψ_slow` es el **cielo de fondo**; `χ_fast` son los **pájaros que vuelan**.

---

## 4️⃣ Paso 3: Ecuación efectiva para `ψ_slow`

Al aplicar BO y promediar sobre las partículas rápidas:

⟨χ_fast| H | χ_fast⟩ ψ_slow = E_eff ψ_slow

- `E_eff` depende de la coherencia de las partículas lentas  
- Aquí empieza a emerger **una dinámica efectiva de tiempo**  

---

## 5️⃣ Paso 4: Tiempo Emergente

Definimos **tiempo emergente t** a partir de cambios en la **fase de ψ_slow**:

i ℏ ∂ψ_slow / ∂t = H_eff ψ_slow

- `H_eff`: Hamiltoniano efectivo  
- Cada cambio en coherencia → paso de tiempo  
- Así, el **tiempo aparece como un parámetro derivado**, no fundamental

> Concepto sencillo: el reloj solo avanza cuando las partículas se mueven y cambian su coherencia.

---

## 6️⃣ Paso 5: Ejemplo conceptual en ASCII

Supongamos 4 partículas lentas:

Fondo Cero Coherente:

→  * →  * →  * →


Partículas rápidas:

↑  * ↖  * →  * ↗


- Evolución rápida → cambios en coherencia del fondo  
- Tiempo emergente aumenta según los cambios  
- Cuando todas las partículas lentas se alinean → coherencia máxima → tiempo estable

---

## 7️⃣ Paso 6: Conceptos clave

| Concepto                     | Explicación |
|-------------------------------|------------|
| Separación BO                 | Divide dinámicas rápidas/lentas |
| Hamiltoniano efectivo `H_eff` | Hamiltoniano sobre fondo de coherencia |
| Tiempo emergente `t`          | Surge de cambios en coherencia |
| Cero Coherente                 | Fondo de partículas lentas, sin tiempo fundamental |
| Perturbaciones                | Cambios que generan movimiento y tiempo |

---

## 8️⃣ Paso 7: Resumen

1. Partimos de un **universo sin tiempo**  
2. Separamos partículas lentas y rápidas (BO)  
3. Promediamos sobre rápidas → Hamiltoniano efectivo  
4. Definimos **tiempo emergente** a partir de la fase de partículas lentas  
5. Cada cambio de coherencia genera **un paso de tiempo**  

> Así, TUC/QCT conecta **coherencia ↔ tiempo ↔ dinámica universal**.

---

## 9️⃣ Próximos pasos

- Implementar esta derivación en **simulaciones de `simulation_runner.py`**  
- Visualizar evolución de coherencia y tiempo emergente  
- Preparar ejemplos interactivos para estudiantes avanzados

> Fin de la derivación paso a paso
