#### Rappel et paramétrisation
# Techniques de dérivée numérique

<br>

## I. Rappel des fondamentaux

Le problème de la dérivée numérique est d'approximer la valeur de la dérivée première d'une fonction $f(x)$ au point d'intérêt $x$, soit $f'(x)$, en utilisant des valeurs de la fonction en des points voisins.

La définition de la dérivée en un point $x$ est donnée par la limite :
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

Le principe repose sur l'approximation de cette limite en utilisant une valeur finie et petite pour le pas de comparaison $\mathbf{h}$.

$$
f'(x) \approx \frac{\text{Variation de la fonction}}{\text{Variation de } x}
$$

Plus le pas $h$ est petit, plus l'approximation est précise, sous réserve que les erreurs d'arrondi numérique ne deviennent pas dominantes.

---

## II. Paramètres de configuration

Une approximation de dérivée numérique est entièrement définie par les paramètres suivants :

### 1. La fonction à dériver : $f(x)$

* **Rôle :** C'est la fonction dont on cherche la pente (la dérivée) en un point.

### 2. Le point d'intérêt : $x$

* **Rôle :** C'est à $\mathbf{x}$ où l'on souhaite calculer la dérivée $\mathbf{f'(x)}$. $\mathbf{x}$ détermine la position du point d'intérêt $\mathbf{P} = (x, f(x))$.

### 3. Le pas de comparaison : $h$

* **Rôle :** Définit la distance entre le point d'intérêt $x$ et le(s) point(s) d'évaluation voisin(s) de la fonction.
* **Impact :** $h \downarrow$ $\implies$ **Précision** $\uparrow$

### 4. Paramétrisation des points de comparaison autour de P

* **Rôle :** Détermine les positions relatives des points de comparaison autour du point d'intérêt $x$

On cherche à approximer la dérivée au point $\mathbf{x}$ en utilisant les bornes d'un intervalle $[x_a, x_b]$ de largeur $h$ positionné autour de $\mathbf{x}$. 

On définit la position de l'intervalle à l'aide d'un facteur $\alpha \in [0, 1]$ :
- $x_a = \mathbf{x} - \alpha \cdot h$
- $x_b = \mathbf{x} + (1 - \alpha) \cdot h$



La formule de la dérivée est alors :

$$
f'(\mathbf{x}) \approx \frac{f(x_b) - f(x_a)}{h}
$$

| Valeur de $\alpha$ | Nom de la Méthode | Position de l'intervalle $[x_a, x_b]$ autour de $\mathbf{x}$ |
| :---: | :---: | :--- |
| $\mathbf{\alpha = 0.0}$ | **Différence avant** | $[\mathbf{x}, \mathbf{x} + h]$.|
| $\mathbf{\alpha = 0.5}$ | **Différence centrée** | $[\mathbf{x} - h/2, \mathbf{x} + h/2]$ |
| $\mathbf{\alpha = 1.0}$ | **Différence arrière** | $[\mathbf{x} - h, \mathbf{x}]$ |
| $\mathbf{\alpha \in ]0, 1[}$ | **Différence généralisée** | Permet d'approximer la dérivée en un point quelconque dans l'intervalle. |


## III. Conclusion

La technique de dérivée numérique est une méthode simple et efficace pour estimer la pente d'une fonction en un point donné. Le choix du pas $h$ et de la position relative $\alpha$ des points de comparaison influence directement la précision de l'approximation. 

La méthode de différence centrée ($\alpha = 0.5$) est souvent privilégiée pour sa meilleure précision, mais le choix final dépend des contraintes spécifiques du problème à résoudre.