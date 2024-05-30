
**Les graphes sont des structures de données relationnelles.

Les bases de la théorie des graphes remontent au $XVIII^{ème}$ siècle, où Euler a résolu le problème des $7$ ponts de Königsberg en le ramenant à la recherche d'un chemin passant une unique fois par chaque arc d'un graphe (appelé ultérieurement chemin _eulérien_) :

![[Pasted image 20240404080117.png]]

<u>Question :</u> Peut-on trouver un chemin dans le graphe qui passe une et une seule fois par chaque arête ?

Aujourd'hui, les graphes ont de très nombreuses applications :

- Réseaux sociaux 

- GPS 

- Internet 

- Graphes de flot de contrôle

- réseaux 

## I. Définition des graphes orientés et non orientés

### 1. Graphes non orientés


<u>Définition :</u>

Un graphe non orienté $G$ est un couple $(S,A)$ avec $S$ un ensemble non vide dont les éléments sont appelés des sommets. A un ensemble de paires non ordonnés $\{x, y\}$ avec $x \ne y$ où $(x,y) \in S$ dont les éléments sont appelés des arêtes. 

<u>Exemple de graphe non orienté :</u> 

![[Pasted image 20240404081646.png]]

$S = \{ 0,1,2,3,4,5,6\}$ et $A = \{ \{0,6\} , \{1,3\} , \{1,2\} , \{1,4\} , \{3,4\} , \{2,4\} , \{5,4\} \}$ 

<u>Modifications possibles de la définition :</u>

<u>Boucles :</u> Liaison d’un sommet x à lui même (on n’impose plus $x \ne y$)

<u>Multi-arêtes :</u> plusieurs arêtes entre deux sommets

On parle à ce moment là de multigraphes. Souvent, on ne considère que les graphes finis $(S$ est fini$)$.

<u>Vocabulaire :</u> 

- Deux sommets reliés par une arête sont adjacents

- Les sommets adjacents avec un sommet $x$ sont les voisins de $x$.

- une arête $\{x,y\}$ est incidente aux sommets $x$ et $y$.

<u>Notation :</u>

Arête $\{x,y\} \iff \{y,x\} \iff xy \iff yx$ 

<u>Propriété :</u> nombre maximal d'arêtes d'un graphe non orienté.

$|A| \le \frac{|S|(|S| - 1)}{2}$

<u>Preuve :</u>  

$\binom{|S|}{2} = \frac{|S|(|S| - 1)}{2}$

- On retire le premier sommet aux $n-1$ autres

- On retire le deuxième sommet aux $n-2$ autres

- $…$

- On retire le dernier sommet aux $0$ autres $\displaystyle \sum_{i=0}^{|S| - 1}i$

<u>Exemples concrets de graphes non orientés :</u> 

- Graphe de Facebook : 

Sommets $S$ = utilisateurs 

Arête $A$ = $2$ utilisateurs “amis”

$|A| \simeq 10^{11}$ arêtes

- <u>Graphes d'intervalles :</u>

![[Pasted image 20240404090146.png]]

Utile pour les problèmes d’ordonnances.

$|A|$ = nombre d’arêtes 

$|S|$ = nombre de sommets

### 2. Graphes orientés


<u>Définition :</u> 

Un graphe orienté $G$ est un couple $(S,A)$ avec $S$ l’ensemble non vide de sommets et $A$ un ensemble de couples $(x,y)$  ordonnés $($avec $x \ne y)$ avec $x$ et $y$ éléments de $S$ dont les éléments sont des arcs.

<u>Exemple de graphe orienté :</u> 

![[Pasted image 20240404081721.png]]

$S = \{ 0,1,2,3,4,5,6\}$ et $A = \{ \{1,3\} , \{3,4\} , \{4,1\} , \{4,2\} , \{2,4\} , \{1,2\} , \{5,2\} \{0,6\} \{6,0\}\}$ 

On peut éventuellement modifier cette définition pour autoriser les boucles et les multi-arcs. 

<u>Notation :</u>

$(x,y)$ un arc $\iff x \rightarrow y$

<u>Vocabulaire :</u> 

Si on a un arc $x \rightarrow y$ :

- $x$ est le prédécesseur de $y$

- $y$ est le successeur de $x$

<u>Propriété :</u> nombre maximal d'arcs d'un graphe orienté

$|A| \le |S| \times (|S| - 1)$

<u>Exemples concrets de graphes orientés :</u> 

- <u>Graphe d’Instagram :</u>

Sommets $S$ = utilisateurs

arc $x \rightarrow y$ = x est abonné à y

- <u>Graphes de flot de contrôle :</u>

Arc $x \rightarrow y$ = si le bloc d’instructions $y$ peut s’exécuter juste après $x$. 

## II. Vocabulaire de la théorie des graphes

### 1. Degrés dans un graphe

- <u>Dans un graphe non orienté :</u>

<u>Définition :</u> 

Dans un graphe non orienté, le degré d’un sommet $x$ noté $d(x)$ est le nombre d’arêtes incidentes à $x$ (= le nombre de voisins de $x$).

On a $0 \le d(x) < |S|$

Le degré d’un graphe est le degré maximal d’un de ses sommets.

<u>Propriété :</u> Graphe $G = (S,A)$

$\sum_{x \in d(x)}d(x) = 2|A|$

- <u>Dans un graphe orienté :</u>

<u>Définition :</u>

Pour un sommet $x$ d’un graphe :

- Le degré sortant de $x$, noté $d_{+}x$ est est le nombre de successeurs de $x$. 

- Le degré entrant de $x$, noté $d_{-}x$ est est le nombre de prédécesseurs de $x$

<u>Propriété :</u> Graphe $G = (S,A)$

$\sum_{x \in S)}d_{-}(x) = \sum_{x \in d(x)}d_{+}(x) = |A|$

### 2. Notion de sous-graphe


<u>Définition :</u>

Un sous-graphe d’un graphe $G = (S,A)$ est un graphe $G’ = (S’,A’)$ avec $S’ \subset S$ et $A’ \subset A$

Un sous-graphe induit est un graphe $G’ = (S’,A’)$, avec $S’ \subset S$ et $A’$ est exactement l’ensemble des arêtes/arcs qui relient deux sommets de $S’$ dans $G$.

<u>Exemple :</u> 

<u>Gauche :</u> un sous graphe (sommets noirs et arêtes pleines) ; <u>Droite :</u> un sous-graphe induit
![[Pasted image 20240404080327.png]]

<u>Propriété :</u> 

Il y a $2^{|S|} - 1$ sous-graphes induits d’un graphe $G = (S,A)$ 

### 3. Graphes isomorphes

<u>Définition :</u>

Un isomorphisme entre $2$ graphes $G = (S,A)$ et $G’ = (S’,A’)$ est une bijection $\varphi : S \rightarrow S'$   telle que :
$$\begin{equation} {\forall(x,y) \in S}= \begin{cases} x,y \in A \iff \varphi(x) \times \varphi(y) \in A’ \\ x \rightarrow y \in A \iff \varphi(x) \rightarrow \varphi(y) \in A’ \end{cases} \end{equation}$$
<u>Exemple :</u> 
![[Pasted image 20240404080347.png]]

### 4. Chemins dans un graphe


<u>Définition :</u>

Dans un graphe $G = (S,A)$, un chemin de longueur n est une suite $S_{0},S_{1}, … , S_n$ de sommets tels que$$\begin{equation} {\forall i \in [|0,n-1|]}= \begin{cases} (S_{i},S_{i+1}) \in A \\ \{S_{i},S_{i+1}\} \in A \end{cases} \end{equation}$$
Un chemin de longueur n possède n arêtes/arcs et n+1 sommets. On accepte les chemins de longueur 0. 

![[Drawing 2024-04-10 10.18.08.excalidraw]]

<u>Chemins :</u>

- $1,2,3,4,6$

- $3,7,6,8,9,6,5$

- $6,5,4,6,5$

- $3,4,3$

- $6$

- $…$

<u>Définition :</u>

Un chemin est dit élémentaire si il ne comporte pas deux fois le même sommet (les $S_i$ sont distincts).

Un chemin est dit simple s’il ne passe pas deux fois par le même arc/la même arête (les $(S_i,S_{i+1}) et \{S_i,S_{i+1} \}$ sont distinctes)

Un chemin élémentaire est forcément simple, la réciproque est fausse

<u>Définition (cycle/circuit) :</u>

(Un cycle est dans les graphes non orientés et le circuit est son équivalent dans un graphe orienté.)

Un cycle est un chemin simple de longueur supérieure à 1 dont les deux extrémités sont le même sommet.

<u>Cycles (en reprenant le schéma précédent) :</u>

- $3,4,6,7,3$

- $6,9,8,6$

- $3,7,6,4,3$

- $6,4,5,6$

- $3,7,6,8,9,6,4,3$

<u>Définition :</u>

Un graphe est dit cyclique s’il comporte au minimum un cycle et est dit acyclique sinon.

### 5. Notion d'accessibilité dans un graphe

<u>Définition :</u>

Le sommet $y$ est dit accessible depuis le sommet $x$ s’il existe un chemin allant de $x$ à $y$.

![[Drawing 2024-04-10 10.39.48.excalidraw]]

Le sommet $5$ est accessible depuis $1,2,3,4,5$. Le sommet $1$ n’est pas accessible depuis $3$.

<u>Propriété :</u> 

La relation d’accessibilité dans un graphe non orienté est une relation d’équivalence. 

<u>Preuve  :</u>

- réflexif : un sommet est accessible depuis lui-même (chemin vide).

- symétrie : vrai car dans un graphe non orienté, si on a une arête $xy$, on a aussi $yx \in A$ donc si $y$ accessible depuis $x$, le même chemin “à l’envers” donne $x$ accessible depuis $y$.

- transitivité : si on a un chemin $x = S_0,…,S_n = y$ et un chemin $y = p_0,..,p_m =2$ alors le chemin $x = S_0,…,S_n,p_1,…,p_m = 2$ relie $x$ à $2$ donc $2$ est accessible depuis $x$.

Dans les graphes orientés, la symétrie n’est plus vérifiée donc ce n’est pas une relation d’équivalence.

<u>Les propriétés suivantes sont équivalentes :</u>

- il existe un chemin allant du sommet $x$ au sommet $y$.
   
- il existe un chemin simple allant du sommet $x$ au sommet $y$.

- il existe un chemin élémentaire allant du sommet $x$ au sommet $y$.

On les numérotent de $1$ à $3$ pour la preuve suivante.

<u>Preuve :</u>

On a déjà $(3) \Rightarrow (2)$ et $(2) \Rightarrow (1)$. Montrons que $(1) \Rightarrow (3)$.

Soit $x = S_0,…,S_n = y$ de longueur minimale. Par l’absurde, si on a deux sommets de chemin $S_i = S_j$ avec $i < j$. Alors $x = S_0,…,S_i,S_{j+1},…,S_n = y$ est un chemin plus petit ce qui contredit la minimalité de la longueur.

Donc le chemin $x = S_0,…,S_n = y$ est élémentaire.

### 6. Connexité


<u>Dans les graphes non orientés :</u>

<u>Définition :</u>

Un graphe non orienté $G = (S,A)$ est dit connexe s’il existe un chemin de $x$ à $y$ pour tous sommets $x,y \in S$.

<u>Exemple :</u>

![[Drawing 2024-04-10 11.02.14.excalidraw]]

Le graphe de gauche est connexe, le graphe de droite ne l’est pas. 

<u>Définition :</u>

Les composantes connexes d’un graphe non orienté sont les sous-graphes induits par les classes d’équivalences de la relation d’accessibilité.

<u>En reformulant :</u>

- la composante connexe $C_x$ d’un sommet $x$ contient tous les sommets accessibles depuis $x$.

- $y \in C_x \Rightarrow C_x = C_y$

- les composantes d’un graphe sont les sous-graphes induits connexes et maximaux (en nombre de sommets).

- Un graphe connexe possède 1 composante connexe.

<u>Propriété :</u> 

$G = (S,A)$. Soient $x$ et $y$ tels que $\{x,y\} \notin A$. On ajoute une arête $xy$ dans $G$.

<u>2 cas possibles :</u>

- $x$ était accessible depuis $y$ : le nombre de composantes connexes ne change pas, et il existe un cycle passant par $xy$.

- $x$ et $y$ n’appartenaient pas à la même composante connexe : le graphe a une composante connexe en moins et il n’y a aucun cycle passant par l’arête $xy$.

<u>Dans un graphe orienté :</u>

<u>Définition :</u>

Un graphe orienté, $G = (S,A)$ est dit fortement connexe s’il existe un chemin reliant $x$ à $y$ pour tout sommets $x,y \in S$

<u>Définition :</u>

Un graphe orienté est dit faiblement connexe quand l’oubli de l’orientation donne un graphe non orienté connexe.

<u>Propriété :</u>

La relation R définie sur les graphes orientés par 

$xRy \iff x$ accessible depuis $y$ et $y$ accessible depuis $x$ 

est une relation d’équivalence.

<u>Définition :</u>

Les composantes fortement connexes d’un graphe orienté sont les sous-graphes induits par les classes d’équivalences de cette relation $R$.

<u>Exemples :</u> 

(un graphe fortement connexe et un non fortement connexe (sommet noir non accessible depuis le sommet gris))
![[Pasted image 20240404080530.png]]

### 7. Coloration de graphes

<u>Définition :</u>

Une k-coloration d’un graphe $G = (S,A)$ est une application $\varphi : S \rightarrow [\![0,k-1]\!]$ telle que $\{x,y\} \in A \Rightarrow \varphi(x) \neq \varphi(y)$, la valeur $\varphi(x)$ est appelé couleur de $x$

<u>Définition :</u>

Un graphe $G$ est dit k-colorable s’il existe une k-coloration. Le nombre chromatique $X(G)$ d’un graphe $G$ est le plus petit $k$ tel que $G$ est k-colorable.

<u>Exemple d'application aux graphes d'intervalles :</u>

- Sommets = intervalles

- Voisins = intervalles incompatibles

- <u>Coloration :</u> 2 intervalles incompatibles ont des couleurs différentes.

![[Pasted image 20240404080645.png]]

## III. Graphes particuliers

### 1. Graphes non orientés ayant une forme particulière

- <u>Graphe entièrement déconnecté :</u> 

Graphe composé entièrement de sommets et d’aucune arête. Il possède $|S|$ composantes connexes.

- <u>Graphe complet :</u> 

Possède une arête entre chaque couple de sommets possible. On le note $K_n$ avec $n$ le nombre de sommets. Il possède donc $\displaystyle \frac{n(n-1)} 2$ arêtes, il est connexe.

- <u>Graphe chemin :</u> 

Ne possède que un “chemin”. On note $P_n$ le graphe chemin à $n$ sommets. $\{i,j\} \in A \iff i = j + 1$.

![[Drawing 2024-04-11 08.16.05.excalidraw]]

- <u>Graphe cycle :</u> 

On note $C_n$ le graphe cycle à n sommets numérotés dans $[\![0,n-1]\!]$. $\{i,j\} \in A \iff i = j + 1$ (modulo n)
  ![[Drawing 2024-04-11 08.19.19.excalidraw]]
On peut donner des définitions équivalentes pour les graphes orientés.

### 2. Graphes ayant des propriétés particulières


- <u>Graphes creux / denses :</u>

Si peu d’arêtes/d’arcs, on dit que le graphe est creux, sinon il est dense.

- <u>Graphes bipartis :</u>

Un graphe $G = (S,A)$ est dit biparti s’il existe une partition de S en deux ensemble $S_1,S_2$ telle que pour toute arête $\{x,y\} \in A, x \in S_1$ et $y \in S_2$ (ou l’inverse).

<u>Propriété :</u>

Un graphe est biparti si et seulement si il est 2-colorable.

- <u>Graphes bipartis complets :</u> 

$K_{n,p}$ est le graphe biparti à $n+p$ sommets avec $n$ le nombre de sommets de $S_1$ et $p$ le nombre de sommets de $S_2$. Chacun des $n$ sommets de $S_1$ est relié par une arête à chacun des $p$ sommets de $S_2$.

<u>Exemple :</u>

![[Pasted image 20240404080725.png]]

- <u>Graphes planaires :</u>

On peut représenter le graphe dans le plan sans qu’aucune arête ne se croise. Le plus petit graphe complet non planaire est $K_5$, biparti complet est $K_{3,3}$.

- <u>Graphes eulériens :</u>

Un chemin eulérien de $G$ est un chemin simple qui contient toutes les arêtes de $G$. 

Un cycle (circuit pour un graphe orienté) eulérien est un chemin eulérien dont les extrémités sont identiques.

Un graphe est eulérien s’il possède au moins un cycle eulérien. 

- <u>Graphes hamiltoniens :</u>

Un chemin hamiltoniens de $G$ est un chemin élémentaire qui contient tous les sommets de $G$. 

Un cycle (circuit pour un graphe orienté) hamiltonien est un chemin hamiltonien élémentaire sauf aux extrémités.

Un graphe est hamiltonien s’il possède au moins un cycle hamiltonien. 

### 3. Arbres dans la théorie des graphes

<u>Définition :</u>

Dans la théorie des graphes, un arbre est défini comme étant un graphe connexe et acyclique (non positionnel).

<u>Propriété :</u> 

Un graphe non orienté acyclique à $n$ sommets possède au plus $n-1$ arêtes.

<u>Lemme :</u>

Tout graphe non orienté acyclique possède un sommet qui a un degré inférieur ou égal à $1$.

<u>Preuve du lemme :</u>

On raisonne par l’absurde. Supposons que tous les sommets d’un graphe non orienté acyclique sont de degré au moins $2$. Construisons un chemin depuis n’importe quel sommet du graphe, en se déplaçant à chaque fois vers un sommet différent de celui dont on venait (possible car de degré supérieur ou égal à $2$). 

Comme le nombre de sommets est fini, on finit forcément par tomber sur un sommet déjà dans le chemin. Donc il y a un cycle, absurde. 

<u>Preuve de la propriété :</u>

Par récurrence, montrons $H_n$ : “Un graphe non orienté acyclique à $n$ sommets possède au plus $n-1$ arêtes.”

<u>Initialisation :</u> Un graphe à $1$ sommet possède $0$ arête.

<u>Hérédité :</u> Supposons $H_n$. 

D’après le lemme, un graphe non orienté acyclique à $n+1$ sommets possède un sommet de degré inférieur ou égal à $1$.

Le graphe induit sur $S\backslash\{x\}$ avec $x$ un sommet de degré inférieur ou égal à $1$ est aussi acyclique et a $n$ sommets et par hypothèse de récurrence a donc au plus $n-1$ arêtes.

Donc $G$ a au plus : $n-1 + d(x)$ arête (avec $d(x)$ le degré du sommet $x$) donc $G$ a au plus n arêtes.

<u>Propriété :</u>

Un graphe non orienté connexe à $n$ sommets possède au moins $n-1$ arêtes.

<u>Preuve par récurrence sur n :</u>

<u>Initialisation :</u> Un graphe connexe à $1$ sommet possède $0$ arête.

<u>Hérédité :</u> Soit $G = (S,A)$ un graphe connexe à $n \ge 2$ sommets. Tout sommet est de degré non nul. 

- Si $G$ a un sommet de degré $1$, noté $x$.  Le sous-graphe induit par $S \backslash \{x\}$ est connexe à $n-1$ sommets. Donc par hypothèse de récurrence, il a au moins $n-2$ arêtes donc $G$ a au moins $n-2 + d(x) = n-1$ arêtes.

- Sinon, tous les sommets sont de degré supérieur ou égal à 2.

$\displaystyle |A| = \frac 1 2 \times \sum_{x \in S} d(x) \ge \frac{1}2 \times 2n \ge n$

<u>Caractérisation des arbres :</u>

Les propriétés suivantes sont équivalentes :

- $G$ est un arbre.

- $G$ est acyclique et a $|S|-1$ arêtes.

- $G$ est connexe et a $|S|-1$ arêtes.

- $G$ est minimalement connexe (impossible d’enlever une arête en conservant la connexité).

- $G$ est maximalement acyclique (impossible d’ajouter une arête sans créer de cycle).

- Pour tous sommets $x,y$ de $G$, il existe un unique chemin élémentaire reliant $x$ et $y$.

<u>Définition :</u>

Un graphe acyclique est une forêt. Les composantes connexes d’une forêt sont les arbres. 

<u>Définition :</u>

Les arbres enracinés sont les arbres pour lesquels on a distingué un sommet particulier appelé la racine.

<u>Définition :</u>

Un arbre couvrant d’un graphe $G = (S,A)$ est un arbre dont l’ensemble des sommets est $S$. 

![[Drawing 2024-04-11 09.50.24.excalidraw]]

<u>Propriété :</u>

Tout graphe connexe admet un arbre couvrant.

<u>Preuve :</u>

Considérons l’algorithme suivant :

- Entrée : graphe $G = (S,A)$ connexe

- Algorithme :
``` Pseudo-code
G' = (S,A'=A)
Tant que G' n'est pas minimalement connexe :
	Choisir une arête de xy appartenant à A' telle que le graphe (S,A'\xy) 
	est connexe
	A' <- A'\xy
Renvoyer G'
```

<u>Correction de l’algorithme :</u>

<u>Invariant :</u> $G’$ est connexe 

- Avant la boucle, vrai car $G$ est connexe par précondition.

- Si l’invariant est vrai en entrée d’une itération,  il est vrai en sortie car $S’$ n’a pas changé et on a retiré une arête choisie telle que $G’$ reste connexe.

- Si la boucle termine, on a bien en sortie $G’$ connexe.

<u>Variant :</u> $|A’|$

- positif car c’est un cardinal

- strictement décroissant car on retire un élément à chaque itération

De plus, en sortie de boucle, $G’$ est minimalement connexe donc c’est un arbre et il a le même ensemble de  sommets que $G$ donc c’est un arbre couvrant de $G$.

L’existence et la correction de cet algorithme montre la propriété.

### 4. Graphes pondérés

<u>Données sur les arcs/arêtes :</u>

![[Drawing 2024-04-17 10.55.12.excalidraw]]

<u>Définition :</u>

Un graphe non orienté/orienté pondéré est un triplet $(S,A,\omega)$ avec $S$ l’ensemble des sommets, $A$ l’ensemble des arêtes/arcs et $\omega$ est une application de $A$ dans $\mathbb{R}$ qui à une arête/arc associe son poids $\omega$ est appelée fonction de pondération. Généralement, on étend $\omega$ en définissant 

$$\begin{equation} \begin{cases} \omega(xy) \\ \omega(x \rightarrow y)\end{cases}  = + \infty \end{equation}$$
 si $$\begin{equation} \begin{cases} xy \\ x \rightarrow y\end{cases}  \notin A \end{equation}$$

<u>Exemples :</u>

- Graphes probabilistes

- Graphes routiers

- Internet 

<u>Définition :</u>

Soit $c$ le chemin $S_{0},S_{1,}…,S_{n}$ le poids du chemin $c$ est défini comme
$\omega$(c) = $\displaystyle \sum_{i = 0}^{n-1}\omega (S_{i},S_{i+1})$.

## IV. Représentation des graphes

### 1. Matrice d'adjacence


<u>Définition :</u>

Soit $G = (S,A)$ un graphe. La matrice d’adjacence de $G$ est une matrice $M = (m_{i,j})$ avec $0 \le i < |S|$ et $0 \le j < |S|$ telle que $(m_{i,j}) = 1$ si $$ \begin{equation} \begin{cases} S_{i} \rightarrow S_{j}\\ S_{i} \times S_{j}\end{cases}  \in A \end{equation}$$et $0$ sinon.

<u>Exemples :</u>

![[Pasted image 20240404080859.png]]

<u>Propriété :</u>

La matrice adjacente d’un graphe non orienté est symétrique.

<u>Propriété :</u>

Il n’y a que des $0$ sur la diagonale (puisque les boucles ne sont pas autorisées dans la définition simple des graphes non orienté/graphe orienté).

<u>Complexité spatiale :</u>

Matrice d’adjacence d’un graphe $G = (S,A)$ a une complexité spatiale de $|S|^2$

Plus adaptée pour les graphes denses.

<u>Complexité temporelle :</u>

- déterminer si $2$ sommets sont voisins/successeur $\mathcal{O}(1)$

- Trouver tous les voisins/successeurs d’un sommet : $\mathcal{O}(|S|)$

- trouver tous ces prédécesseurs $\mathcal{O}(|S|)$

<u>Avantage :</u> même complexité

<u>Inconvénient :</u> pas terrible 

<u>Implémentation :</u>

- <u>OCaml :</u>

```OCaml 
type matrice_adjacente = int array array
```

- <u>C :</u>

Tableau statique de taille fixée (nombre maximum de sommets) linéarisé.

<u>Exemple :</u> Nombre maximal de sommets est $20$

``` C
typedef int mat_adj[400];

struct graphe_s {
	int nb_sommets;
	mat_adj matrice;
};
```

### 2. Liste d'adjacence

<u>Définition :</u>

Cette représentation consiste à stocker, pour chaque sommets du graphe, la liste de ses voisins/successeurs. 

![[Drawing 2024-04-17 11.33.37.excalidraw]]

<u>Complexité spatiale :</u>

$\mathcal{O}(|S| + |A|)$

Plus appropriée pour les graphes creux.

<u>Complexité temporelle :</u>

- Déterminer si $S_{j}$ voisins /successeur de $S_{i}$ : $\mathcal{O}(d(S_{i}))$

- Trouver les successeurs/voisins d’un sommet $S_{i}$ : $\mathcal{O}(d(S_{i}))$

- Trouver les prédécesseurs : $\mathcal{O}(|S| + |A|)$

<u>Implémentation :</u>

- <u>Ocaml :</u>

``` OCaml
type liste_adj = int list array
```

- <u>C :</u>

``` C
//max 20 sommets

typedef int lst_adj[20][21];

struct graphe_s {
	int nb_sommets;
	lst_adj adj;
};
```

Le $21$ vient soit d’une sentinelle à la fin, soit du degré au début.

### 3. Sérialisation


- Première ligne : $|S|$

- Les lignes suivantes sont des $x,y$ représentant $x \rightarrow y \in A$.

## V. Parcours de graphes

- Si aucune contrainte, on peut regarder les sommets dans l’ordre de numérotation.

	Mais cela n’apporte aucune information sur les arêtes.

-  Généralement, on parcourt un graphe de voisins en voisins.

	<u>2 manières de faire :</u>

	-  Le parcours en profondeur

	-  Le parcours en largeur

Pour ne pas tourner en rond, on stocke les sommets déjà vus.

Cette structure doit permettre un test d’appartenance efficace :

- Tableau associatif 

- Tableau de taille $|S|$ que l’on rempli de true/false.

<u>Mesures de la complexité :</u> notions d'ordre d'un graphe et de taille d'un graphe.

<u>Parcours général d'un graphe :</u>

Si les étiquettes des sommets ne sont pas des entiers naturels consécutifs.

- On attribue aux sommets de nouvelles étiquettes $0,1,2,3,…,|S|-1$

- On garde dans une structure de données (tableau/tableau associatif) les correspondances étiquette/numérotation.

### 1. Parcours en profondeur

<u>Algorithme :</u>

- Entrée : $G = (S,A)$ et sommet $dep \in S$
	vus $\leftarrow$ { } (tableau associatif vide, tableau de taille $|S|$ rempli de false)

```Pseudo-code
Fonction explorer (sommet s)
	Si S n'appartient pas à vus : (Pas d'association de clés/indice s=false)
		traitement de s
		vus <- ajouter s (ajouter association de clés/indice s = true)
		Pour chaque voisin/successeur v de s :
			explorer(v)
explorer(dep)
```

<u>Complexité :</u>

- Création de vus : $\mathcal{O}(|S|)$

- Fonction explorer : 
	→ Chaque sommet est vu au plus 1 fois.
	→  Test d’appartenance à vus est en $\mathcal{O}(1)$.
	→  Pour un sommet $s$ fixé, le nombre d’itérations de la boucle (= nombre d’appels récursifs lancés) est en $\mathcal{O}(d(s))$ en supposant avoir utilisé la liste d’adjacence de $G$. 
	→ L’ajout de $s$ à vus est en $\mathcal{O}(1)$

<u>Total :</u>

$\displaystyle \mathcal{O}(|S|) + \sum_{s \in S}(\mathcal{O}(d(s)) + \mathcal{O}(1)) = \mathcal{O}(|S| + |A|)$ si traitement en $\mathcal{O}(1)$.

<u>Exemple :</u>

![[Drawing 2024-04-18 08.31.51.excalidraw]]

Parcours en profondeur depuis $0$ : $0,1,2,3,7,8,4$

Seuls les sommets accessibles depuis le départ sont traités.

<u>Arborescence du parcours :</u>
![[Drawing 2024-04-18 08.41.26.excalidraw]]

### 2. Parcours en largeur

<u>Algorithme :</u> graphe $G = (S,A)$ et sommet $dep \in S$.

```Pseudo-code
vus <- { }
f <- file vide
f <- enfiler(dep)
vus <- ajouter(dep)
Tant que f non vide :
	s <- defiler(f)
	traitement de s
	Pour chaque voisin/successeur de s :
		si v n'appartient pas à vus :
			f <- enfiler(v)
			vus <- ajouter(v)
```

<u>Complexité :</u> $\mathcal{O}(|S|+ |A|)$ (même calcul que pour le parcours en profondeur)

En reprenant le même graphe que pour le parcours précédent, le parcours en largeur donne : $0,1,2,3,4,7,8$

<u>Arborescence :</u>
![[Drawing 2024-04-18 08.53.22.excalidraw]]

<u>Définition :</u>

Soit $G = (S,A)$ un graphe. La distance $D(x,y)$ d’un sommet $x \in S$ à un sommet $y \in S$ est la longueur minimale en nombres d’arêtes/arcs d’un chemin allant de $x$ à $y$. Si un tel chemin n’existe pas, $D(x,y) = +\infty$

<u>Propriété :</u>

S’il existe un arc $y \rightarrow y’$ alors pour tout sommet $x$.

$D(x,y’) \le D(x,y) + 1$

<u>Propriété du parcours en largeur depuis sommet dep :</u>

Si $D(dep,x) < D(dep,y) < \infty$ 

alors $x$ sera traité avant $y$.

<u>Preuve :</u> 

Il faut montrer l’invariant suivant : 

Un sommet est dit :

- ouvert si $s$ est dans file f.

- fermé si $s$ est dans vus mais pas f.

- vierge si $s$ n’est pas dans vus.

L’invariant, valable à la fermeture d’un sommet $s_k$, en ayant numéroté les sommets dans l’ordre de leur ouverture $s_{0},…,s_{n}$.

(1) La file a la forme $s_{k+1},…,s_{k+p}$ avec $D(dep,s_{k}) \le D(dep,s_{k+1}) \le \dots \le D(dep,s_{k+p}) \le D(dep,s_{k}) + 1$

(2) Si $D(dep,s_{i}) \le D(dep,s_{k})$, alors $s_i$ est fermé.

(3) Si $D(dep,s_{i}) = D(dep,s_{k})$, alors $s_i$ n’est pas vierge.

### 3. Algorithme générique

Si on remplace la file par une pile.

![[Drawing 2024-04-18 09.15.04.excalidraw]]

Il faut autoriser le fait d’avoir plusieurs fois le même sommet dans la pile pour retrouver le parcours en profondeur.

Algorithme générique de parcours de $G = (S,A)$ depuis sommet $dep \in S$ :

```Pseudo-code
PARCOURS (G, depart) :
    a_traiter <- structure vide
	 a_traiter <- ajouter(dep)
    vus <- {}
    Tant que a_traiter est non vide :
		s <- retirer un sommet de a_traiter
		Si s n'appartient pas à vus :
			vus <- ajouter s
			traitement de s
			POUR chaque voisin v de s :
				a_traiter <- ajouter(v)
```

Si `a_traiter` est une pile, le parcours est en profondeur.
Une file, le parcours est en largeur. 
D'une stratégie aléatoire, le parcours est quelconque.

### 4. Applications des parcours


<u>Déterminer si un graphe non orienté est connexe :</u>

→ vérifier à la fin du parcours si tous les sommets sont dans vus.


<u>Trouver les composantes connexes :</u>

→ les sommets dans vus à l’issue d’un parcours sont dans la même composante.
	
→ on recommence le parcours avec d’autres sommets tant que nécessaire.


<u>Distance d’un sommet x à y :</u>

→ on garde un tableau de distances, au début rempli de $+ \infty$ sauf distance de $x$ à $x = 0$.

→ au moment où on regarde les voisins $v$ d’un sommet $s$, on met à jour $distance[v] = distance[s] + 1$.

→ largeur


<u>Détecter si G a un cycle impliquant dep :</u>

→ On regarde si au moment d’explorer les voisins d’un sommet $s$, un de ces voisins est $dep$, en conservant le sommet d’où l’exploration de $s$ a été lancée (si c’est $dep$ ce n’est pas un cycle).


<u>Biparti :</u>

Au départ, on place $dep$ dans une partition quelconque.

Quand on explore les voisins $v$ de $s$ :

- Si $v$ est déjà dans une partition, on vérifie que ce n’est pas celle de $s$.

- Sinon, on attribue à $v$ la partition opposée.

<u>Tri topologique :</u>

<u>Définition :</u>

Un ordre topologique sur un graphe orienté $G$ est une relation d’ordre totale $\prec$ sur les sommets de $G$ telle que si $x → y$ est un arc, alors $x \prec y$.

<u>Propriété :</u>

Un graphe orienté admet un ordre topologique si et seulement s’il est acyclique.

<u>Définition :</u>

Faire un tri topologique d’un graphe orienté acyclique consiste à trouver une énumération des sommets qui respecte l’ordre topologique.

<u>Exemple :</u>

Chaussettes $\prec$ pantalon $\prec$ chaussures $\prec$ chemise $\prec$ montre $\prec$ cravate $\prec$ veste $\prec$ ceinture
