#### Rappel et paramétrisation
# Méthodes d'intégration numérique

<br>

## I. Rappel des fondamentaux

Le problème de l'intégration numérique est d'approximer la valeur d'une intégrale définie de la forme:
$$I = \int_{a}^{b} f(x) dx$$
en utilisant une somme finie. 

Le principe repose sur la **somme de Riemann**, qui divise l'intervalle $[a, b]$ en $N$ sous-intervalles de largeur $h$.

$$
I \approx \sum_{i=0}^{N-1} (\text{Aire Approximative sur } [x_i, x_{i+1}])
$$

Plus le nombre de sous-intervalles $N$ est grand (ou plus le pas $h$ est petit), plus l'approximation est précise. À la limite, lorsque $N \to \infty$ (ou $h \to 0$), la somme converge vers la valeur exacte de l'intégrale, qu'on nommera la valeur vraie $I_{\text{vrai}}$.



## II. Paramètres de configuration

Une intégration numérique est entièrement définie par les paramètres suivants :

### 1. La fonction à intégrer : $f(x)$

* **Rôle :** C'est la fonction dont on calcule l'aire sous la courbe.

### 2. Les Bornes d'intégration : $a$ et $b$

* **Rôle :** Définissent l'intervalle sur lequel l'intégration est effectuée.

### 3. La Résolution : le nombre de pas $N$

Le pas d'intégration $h$ est défini par $N$ qui contrôle la finesse de la discrétisation.
* **Rôle :** Contrôle la précision de l'approximation.
* **Relation :** $$h = \frac{b - a}{N}$$
* **Impact :**
    * $h \downarrow$ (ou $N \uparrow$) $\implies$ **Précision** $\uparrow$ et **Temps de Calcul** $\uparrow$.
    * Le choix optimal de $h$ est un compromis entre la précision souhaitée et les ressources de calcul.

### 4. Les méthodes d'approximation d'aire

* **Rôle :** Déterminent la forme de l'approximation de l'aire sous la courbe.
* **Approches :** Il existe plusieurs méthodes où chacune utilise un polynôme d'interpolation d'un certain degré pour approximer $f(x)$ sur chaque sous-intervalle $[x_i, x_{i+1}]$.

#### 4a. Méthode des rectangles

Approximation de l'aire par l'aire d'un rectangle de hauteur $f(x_i^*)$ (polynôme de degré 0).

$$
I \approx h \sum_{i=0}^{N-1} f(x_i^*)
$$

#### 4b. Méthode des trapèzes

Approximation de l'aire par l'aire d'un trapèze (polynôme de degré 1).

$$
I \approx \frac{h}{2} [f(x_0) + 2 \sum_{i=1}^{N-1} f(x_i) + f(x_N)]
$$

#### 4c. Méthode de Simpson

Approximation de l'aire par l'intégration d'un polynôme de degré 2.

$$
I \approx \frac{h}{3} [f(x_0) + 4 \sum_{i=1, 3, \dots}^{N-1} f(x_i) + 2 \sum_{i=2, 4, \dots}^{N-2} f(x_i) + f(x_N)]
$$


### 5. Paramétrisation de la position du point d'évaluation $\alpha$

* **Rôle :** Détermine la position du point d'évaluation dans chaque sous-intervalle.
* **Contrainte :** Cette paramétrisation est pertinente pour la **Méthode des rectangles** seulement qui repose sur le choix d'un point d'évaluation $x_i^*$ unique dans chaque sous-intervalle $[x_i, x_{i+1}]$.

On définit la position du point d'évaluation $x_i^*$ à l'aide d'un facteur $\alpha \in [0, 1]$ :

$$
x_i^* = x_i + \alpha \cdot h
$$

Où $x_i$ est la borne gauche du sous-intervalle.

| Valeur de $\alpha$ | Nom de la Méthode | Description |
| :---: | :---: | :--- |
| $\mathbf{\alpha = 0}$ | **Rectangle à gauche** | $x_i^* = x_i$. La hauteur est celle de la borne gauche. |
| $\mathbf{\alpha = 0.5}$ | **Point milieu** | $x_i^* = x_i + h/2$. Utilise le centre du sous-intervalle.  |
| $\mathbf{\alpha = 1}$ | **Rectangle à droite** | $x_i^* = x_i + h = x_{i+1}$. La hauteur est celle de la borne droite. |
| $\mathbf{\alpha \in ]0, 1[}$ | **Rectangle généralisé** | Permet une analyse de sensibilité ou une correction de biais (approche non standard). |

## III. Conclusion

Le choix de la méthode d'intégration numérique est un arbitrage entre la **précision** et le **coût de calcul**, entièrement contrôlé par la **méthode**,  le **pas $h$** et *$\alpha$* la **position relative du point d'évaluation**.
