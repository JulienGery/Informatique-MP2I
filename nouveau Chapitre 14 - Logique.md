
<u>Objectif :</u> formaliser le discours, le raisonnement, la démonstration.

La logique définit formellement :

- le langage qu'on utilise : aspects syntaxiques

- son interprétation : aspects sémantiques

<u>Définition :</u>

La logique propositionnelle manipule des propositions qui peuvent être soit vraies soit fausses.

<u>Exemples :</u>

$p_{1}$ = “Il pleut”, $p_{2}$ = “Je prends mon parapluie”.

La logique propositionnelle combine ces faits élémentaires à l’aide de connecteurs logiques.

<u>Exemple :</u>

“Il pleut et je prends mon parapluie” : $p_{1} \land p_{2}$

“Puisqu’il, pleut, alors je ne prends pas mon parapluie” : $p_{1} \rightarrow \lnot p_{2}$

<u>Logique du premier ordre :</u>

<u>Exemple :</u>  $2 \leq x < 10$

La logique du premier ordre ajoute des prédicats.

<u>Exemple :</u> $I(a,b)$ : prédicat indiquant si $a < b$

On peut ensuite exprimer des phrases plus complexes.

<u>Reprise du premier exemple :</u> $2 \leq x < 10 = I(x,10) \land \lnot I(x,2)$

On ajoute à cela les quantificateurs pour pouvoir formaliser tout raisonnement.

<u>Exemple :</u> 

“Tous les hommes sont mortels. Socrate est un homme. Donc Socrate est mortel.”

<u>Prédicats :</u>

- $H(x)$ signifie que $x$ est un homme.

- $M(x)$ signifie que $x$ est mortel.

On ne peut pas écrire M(tous les hommes) car “tous les hommes” n’est pas élémentaire. On utilise donc le quantificateur $\forall$.

<u>Formule correspondant à ce discours :</u>

$(\forall x (H(x) \rightarrow M(x)) \land H(Socrate)) \rightarrow M(Socrate)$


## I. Syntaxe des formules 

### 1. Définition des formules propositionnelles


<u>Définition :</u>

Une variable propositionnelle est une proposition élémentaire, qui ne peut prendre que deux états, appelés valeurs de vérité.

L’ensemble des variables propositionnelles est noté $\mathcal V$.

<u>Définition :</u>

Deux symboles $\top$ (top) et $\bot$ (bottom) représentent des propositions élémentaires toujours vraie (pour $\top$) et toujours fausse (pour $\bot$).

<u>Définition inductive :</u> l'ensemble des formules propositionnelles $\mathcal P$ :

- Les constantes logiques sont les formules propositionnelles $\top \in \mathcal P$ et $\bot \in \mathcal P$.

- Les variables propositionnelles sont des formules propositionnelles $\mathcal V \subset\mathcal P$.

- Si $\varphi \in \mathcal P$, alors $\lnot \varphi \in \mathcal P$ avec $\lnot$ le connecteur logique de négation d’arité 1.

- Si $\varphi_{1}$ et $\varphi_{2} \in \mathcal P$ alors :

$(\varphi_{1} \land \varphi_{2}) \in P$ avec $\land$ le connecteur de conjonction (“et”).

$(\varphi_{1} \lor \varphi_{2}) \in P$ avec $\lor$ le connecteur de disjonction (“ou”).

$(\varphi_{1} \rightarrow \varphi_{2}) \in P$ avec $\rightarrow$ le connecteur de d’implication.

$(\varphi_{1} \leftrightarrow  \varphi_{2}) \in P$ avec $\leftrightarrow$ le connecteur de d’équivalence.

Cette définition est non ambigüe :

- $((\varphi_{1} \land \varphi_{2}) \land \varphi_{3})$

- $(\varphi_{1} \land (\varphi_{2} \land \varphi_{3}))$

On autorise le fait d’écrire une formule sans les $()$ extérieures. 

<u>Exemple :</u> $\varphi_{1} \land \varphi_{2}$ est considéré comme syntaxiquement correcte.

<u>Remarque :</u> D’autres définitions inductives existent.

### 2. Représentation arborescente d’une formule 


Toute formule propositionnelle admet une représentation arborescente.

Les variables propositionnelles et $\top$ et $\bot$ sont représentés par des feuilles.

![[Excalidraw/Drawing 2024-05-14 09.00.21.excalidraw]]

<u>Exemple :</u> $x,y,z \in \mathcal V$ 
<u>formule :</u> $((x \land \lnot y) \lor \lnot(y \lor z))$

Pour retrouver la formule propositionnelle depuis sa représentation arborescente, on effectue un parcours infixe($\varphi$ à droite des noeuds $\lnot$)

![[Excalidraw/Drawing 2024-05-14 09.09.40.excalidraw]]

<u>Remarque :</u> 

L’arité des connecteurs correspond au nombre de fils des noeuds. 

<u>Implémentation des formules propositionnelles :</u>

```Ocaml
type `a formule =
	|Top
	|Bottom
	|Var_prop of `a
	|Non of formule
	|Et of formule * formule
	|Ou of formule * formule
	|Impl of formule * formule
	|Equiv of formule * formule
```

En C, on utilise une définition classique d’arbre.

```C
struct formule_s {
	char* etiq;
	struct formule_s* gauche;
	struct formule_s* droite;
};
```

On doit vérifier à la main que la formule implémentée est syntaxiquement correcte.

### 3. Fonctions inductives sur l'ensemble des formules propositionnelles


Taille d’une formule $\varphi$, notée $|\varphi|$ :

$|\top| = |\bot| = 1$

$|x| = 1$ avec $x \in \mathcal V$

$|\lnot \varphi| = 1 + |\varphi|$ avec $\varphi \in \mathcal P$

$|\varphi_{1} \diamond \varphi_{2}| = 1 + |\varphi_{1}| + |\varphi_{2}|$ avec $\diamond \in$ {$1,\lor,\rightarrow,\leftrightarrow$} et $\varphi_{1},\varphi_{2} \in \mathcal P$


Hauteur d’une formule $\varphi,h(\varphi)$ :

$h(\bot) = h(\top) = 0$

$h(x) = 0$ avec $x \in \mathcal V$

$h(\lnot \varphi) = 1 + h(\varphi)$ avec $\varphi \in \mathcal P$

$h(\varphi_{1} \diamond \varphi_{2}) = 1 + max(h(\varphi_{1}), h(\varphi_{2}))$ avec $\varphi_{1},\varphi_{2} \in \mathcal P$ et $\diamond \in$ {$1,\lor,\rightarrow,\leftrightarrow$}


Sous-formules d’une formule propositionnelle $\varphi$, notée $SF(\varphi)$ :

$SF(\top) = {\top}, SF(\bot) = {\bot}$

$SF(x) =$ {$x$} avec $x \in \mathcal V$

$SF(\lnot \varphi) = {\lnot \varphi} \cup SF(\varphi)$ avec $\varphi \in \mathcal P$

$SF((\varphi_{1} \diamond \varphi_{2})) = {(\varphi_{1} \diamond \varphi_{2})} \cup SF(\varphi_{1}) \cup SF(\varphi_{2})$ avec $\varphi_{1},\varphi_{2} \in \mathcal P$ et $\diamond \in$ {$1,\lor,\rightarrow,\leftrightarrow$}


Substitution d’une variable propositionnelle x par une formule $\psi$ dans une formule $\varphi$, notée $\varphi[\psi/x]$.

$\psi[\varphi/x] = \bot, \top[\psi/x] = \top$

$x[\psi/x] = \psi$

$x’[\psi/x] = x’$ avec $x’ \in \mathcal V$ et $x’ \neq x$

$\lnot \varphi[\psi/x] = \lnot(\varphi[\psi/x])$ avec $\varphi \in \mathcal P$

$(\varphi_{1} \diamond \varphi_{2})[\psi/x] = (\varphi_{1}[\psi/x]) \diamond (\varphi_{2}[\psi/x])$ avec $\diamond \in$ {$1,\lor,\rightarrow,\leftrightarrow$} et $\varphi_{1},\varphi_{2} \in \mathcal P$

### 4. Logique du premier ordre


Permet de manipuler des objets qui ne sont pas de nature logique(termes) sur lesquels on appliquera des prédicats.


<u>Définition :</u>

Un domaine est constitué de :

- un ensemble de symboles de variables $X$.

- un ensemble de symboles de fonctions, d’arité a, $S_{f}^a$.

- un ensemble de symboles de prédicats, d’arité a, $S_{p}^a$.

<u>Définition inductive des termes :</u>

- Toute variable de $X$ est un terme.

- Si $t_{0},t_{1},…,t_{a}$ sont des termes, et $f \in S_{f}^a$., alors $f(t_{1},t_{2},…,t_{a})$ est un terme.

<u>Définition :</u>

Un atome est le résultat de $p(t_{1},…,t_{a})$ avec $p \in S_{p}^a$ et $t_{1},..,t_{a}$ des termes.

<u>Définition :</u>

- Le quantificateur existentiel $\exists$ exprime qu’une propriété est vraie pour au moins un élément du domaine.

- Le quantificateur universel $\forall$ exprime qu’une propriété est vraie pour tous les éléments du domaine.

<u>Définition inductive d'une formule du premier ordre :</u>

- Tout atome est une formule du premier ordre.

- si \varphi une formule du premier ordre, alors \lnot \varphi aussi

- Si $\varphi_{1},\varphi_{2}$ formules du premier ordre, alors $(\varphi_{1} \diamond \varphi_{2})$ aussi avec $\diamond \in$ {$\land,\lor,\rightarrow,\leftrightarrow$}.

- Si x est une variable du domaine, $\varphi$ une formule du premier ordre, alors $(\forall x . \varphi)$ et $(\exists x . \varphi)$ formules du premier ordre.

<u>Exemple :</u>

$(\forall A,\forall B, A \cap B \subseteq A) \land (\varnothing \subseteq A$) est une formule du premier ordre sur le domaine suivant :

$X =$ {$A,B$}, $S_{f} =$ {$\varnothing$ d’arité $0$, $\cap$ d’arité $2$}, $S_{p} =$ {$\subseteq$ d’arité $2$}.

<u>Représentation arborescente de la formule :</u>

![[Excalidraw/Drawing 2024-05-15 10.39.58.excalidraw]]

<u>Vocabulaire :</u>

- Dans $\forall x . \varphi$ et $\exists x$ . $\varphi$, la portée de $x$ est $\varphi$.

- Une variable $x$ qui appartient à la suite d’un $\forall x .$ ou $\exists x .$ est dite liée, sinon elle est libre. Une même variable peut avoir des occurrences libres et liées.

## II. Sémantique du calcul propositionnel


<u>Objectif :</u> Interpréter les formules propositionnelles, leur donner un sens.


### 1. Valeurs de vérité d'une formule propositionnelle


<u>Définition :</u>

L’ensemble {$V,F$} est appelé valeurs de vérité.

<u>Définition :</u>

On appelle valuation toute fonction $\mathcal V \mapsto$ {$V,F$} qui à chaque variable propositionnelle lui associe une valeur de vérité. 

<u>Propriété :</u> 

Il existe $2^n$ valuations pour une formule à $n$ variables propositionnelles.

<u>Définition :</u>

On appelle fonction booléenne d’arité $n$, toute fonction de {$V,F$}$^n \mapsto$ {$V,F$}. On peut associer une fonction booléenne a chaque connecteur (¬,∨,∧,→,↔).

<u>Fonctions booléennes des connecteurs :</u>

Soit $f_{\lnot}$ la fonction booléenne associée au connecteur de négation $\lnot.$

$$\begin{equation} \begin{cases} f_{{\lnot}}(V) = F \\ f_{{\lnot}}(F) = V \end{cases} \end{equation}$$

Soit $f_{\land}$ la fonction booléenne associée à $\land$.

$$\begin{equation} \begin{cases} f_{\land}(F,F) = F \\ f_{\land}(F,V) = F \\ f_{\land}(V,F) = F \\ f_{\land}(V,V) = V \end{cases} \end{equation}$$

On définit de même $f_{V}, f_{\rightarrow}$ et $f_{\leftrightarrow}$.

On peut représenter le résultat d’une fonction booléenne par une table de vérité. Chaque ligne de cette table correspond à une valuation possible.

<u>Définition inductive de l'évaluation d'une formule propositionnelle par une valuation :</u>

Pour toute formule propositionnelle $v$, l’évaluation de $\varphi$ par $v$ consiste à déterminer la valeur de vérité de $\varphi$ en appliquant les fonctions booléennes associées aux connecteurs. On note $[\![\varphi]\!]_{v}$

Définition inductive de  $[\![\varphi]\!]_{v}$:

- $[\![\top]\!]_{v} = V$

- $[\![\bot]\!]_{v} = F$

- $[\![x]\!]_{v} = v(x)$

- $[\![\lnot \varphi]\!]_{v} = f_{\lnot}([\![ \varphi]\!]_{v})$ 

- $[\![\varphi_{1} \diamond \varphi_{2}]\!]_{v} = f_{\diamond}([\![\varphi_{1}]\!]_{v},[\![\varphi_{2}]\!]_{v})$ avec $\diamond \in$ {$\land,\lor,\rightarrow,\leftrightarrow$}.

<u>Exemple :</u>

$\varphi = ((x \rightarrow y) \lor (\lnot x \land y )) \land (x \lor \lnot y)$ valuation $v$ telle que $v(x) = F, v(y) = F$

$[\![\varphi]\!]_{v} = f_{\land}(f_{v}(f_{\rightarrow}([\![x]\!]_{v},[\![y]\!]_{v}), f_{\land}(f_{\lnot}([\![x]\!]_{v}),[\![y]\!]_{v})),f_{v}([\![x]\!]_{v},f_{\lnot}([\![y]\!]_{v}))) = V$.

Si on souhaite trouver $[\![\varphi]\!]_{v}$ pour toute valuation $v$, on dresse la table de vérité (faire comme au chapitre 0 de maths, chaque ligne est une instruction et on les assemble pour obtenir l’expression voulue dans la table de vérité).

La table de vérité est une représentation de la fonction d’évaluation d’une formule.

<u>Propriété :</u> 

Il existe $2^{2^n}$ tables de vérité distincts pour les formules propositionnelles à $n$ variables propositionnelles.

<u>Définition :</u>

On appelle modèle de $\varphi$ toute valuation $v$ telle que $[\![\varphi]\!]_{v} = V$. L’ensemble des modèles de $\varphi$ est noté $Mod(\varphi)$.

<u>Définition :</u>

Une formule propositionnelle est dite :

- satisfiable si elle admet un modèle.

- Une tautologie si toute valuation de la formule est un modèle.

- Une antilogie si elle admet aucun modèle.

Méthodologie pour déterminer si une formule $\varphi$ est satisfiable, tautologique, antilogique :

Dresser la table de vérité de $\varphi$.

<u>Notation :</u>

Si $\varphi$ est tautologique, on note $\vDash \varphi$.

<u>Remarque sur les constantes logiques :</u>

- $\bot$ est une antilogie

- $\top$ est une tautologie

### 2. Équivalence et conséquence sémantique


<u>Définition :</u>

On dit qu’une formule $\psi$ est une conséquence sémantique d’une formule $\varphi$ si pour toute valuation $v$ telle que $[\![\varphi]\!]_{v} = V$, alors $[\![\psi]\!]_{v} = V$. Autrement dit, $Mod(\varphi) \subseteq Mod(\psi)$. On note alors $\varphi \vDash \psi$.

<u>Exemple :</u>

$x \land y \vDash x \rightarrow y$.

On le vérifie avec la table de vérité (toutes les valeurs vraies dans la colonne $x \land y$ doivent être vraie dans la colonne de $x \rightarrow y$, ici c’est le cas).

<u>Propriété :</u>

Si $\varphi_{1} \vDash \varphi_{2}$ et $\varphi_{2}  \vDash \varphi_{3}$ alors  $\varphi_{1} \vDash \varphi_{3}$.

<u>Généralisation :</u>

Soit $\Gamma$ un ensemble de formules. On note $\Gamma F \psi$ et on dit que $\psi$ est une conséquence sémantique de l’ensemble $\Gamma$ si pour toute valuation $v$ telle que pour toute formule $\varphi$ de $\Gamma$ alors $[\![\varphi]\!]_{v} = V$, alors $[\![\psi]\!]_{v} = V$.

<u>Exemple :</u>

Montrons que {$x \rightarrow y, y \rightarrow z$} $\vDash$ {$x \rightarrow z$}

$\Gamma =$ {$x \rightarrow y, y \rightarrow z$}. Il faut que les où il y a V et V dans les lignes $x \rightarrow y$ et $y \rightarrow z$ soit également vrai dans la ligne $x \rightarrow z$. On utilise une table de vérité.

<u>Définition :</u>

Deux formules $\varphi$ et $\psi$ sont dites sémantiquement équivalentes si pour toute valuation v, $[\![\varphi]\!]_{v} = [\![\psi]\!]_{v}$. Autrement dit, $Mod(\varphi) = Mod(\psi)$. On note $\varphi \equiv \psi$.

<u>Propriété :</u>

$\varphi \equiv \psi$ si et seulement si $\varphi \vDash \psi$ et $\psi \vDash \varphi$.

<u>Propriété :</u>

$\equiv$ est une relation d’équivalence.

<u>Propriété :</u>

Si $\varphi_{1} \equiv \varphi_{2}$ et $x \in \mathcal V$. alors $\varphi_{1}[\psi/x] \equiv \varphi_{2}[\psi/x]$ et $\psi[\varphi_{1}/x] \equiv \psi[\varphi_{2}/x]$.

<u>Équivalences sémantiques fondamentales :</u> 

- Implication : $\varphi \rightarrow \psi \equiv \lnot \varphi \lor \psi$.

- Lois de Morgan : $\lnot(\varphi \land \psi) \equiv \lnot \varphi \lor \lnot \psi$ et $\lnot(\varphi \lor \psi) \equiv \lnot \varphi \land \lnot \psi$.

- Contraposition : $\varphi \rightarrow \psi \equiv \lnot \psi \rightarrow \lnot \varphi$.

- Curryfication : $(\varphi \land \psi) \rightarrow \theta \equiv \varphi \rightarrow (\psi \rightarrow \theta)$.

- Double implication : $\varphi \leftrightarrow \psi \equiv (\varphi \rightarrow \psi) \land (\psi \rightarrow \varphi)$.

- Disjonction de cas :  $(\varphi \rightarrow \psi) \land (\lnot \varphi \rightarrow \psi) \equiv \psi$.

- Absurde : $(\lnot \varphi \rightarrow \bot) \equiv \varphi$.

- Tiers exclus : $\varphi \land \lnot \varphi \equiv \bot$ et $\varphi \lor \lnot \varphi \equiv \top$.

- Double négation : $\lnot \lnot \varphi \equiv \varphi$.

- Elément neutre : $\varphi \land \top \equiv \varphi$ et $\varphi \lor \bot \equiv \varphi$.

- Elément absorbant : $\varphi \land \bot \equiv \bot$ et $\varphi \lor \top \equiv \top$.

- Commutativité : $\varphi \land \psi \equiv \psi \land \varphi$ et $\varphi \lor \psi \equiv \psi \lor \varphi$.

- Associativité : $(\varphi \land \psi) \land \theta \equiv \varphi \land (\psi \land \theta)$ et $(\varphi \lor \psi) \lor \theta \equiv \varphi \lor (\psi \lor \theta)$.

- Distributivité : $\varphi \land (\psi \lor \theta) \equiv (\varphi \land \psi) \lor (\varphi \land \theta)$ et $\varphi \lor (\psi \land \theta) \equiv (\varphi \lor \psi) \land (\varphi \lor \theta)$.

- Idempotence : $\varphi \land \varphi \equiv \varphi$ et $\varphi \lor \varphi \equiv \varphi$.

<u>Exemple :</u>

Le problème est : trois personnes mangent ensemble : $A,B,C$. On sait que : 

- $(1)$ si $A$ prend un dessert, $B$ aussi.

- $(2)$ soit $B$, soit $C$ prennent un dessert, mais pas les deux.

- $(3)$ $A$ ou $C$ prend : un dessert.

- $(4)$ si $C$ prend un dessert, $A$ aussi.

La question est : qui a pris un dessert ?

<u>Résolution :</u>

On introduit les variables propositionnelles suivantes :

- $a$ représentant “$A$ prend un dessert”.

- $b$ représentant “$B$ prend un dessert”.

- $c$ représentant “$C$ prend un dessert”.

Les conditions du problème avec ces variables s’écrivent ainsi :

- $(1)$ $a \rightarrow b$.

- $(2)$ $(b \lor c) \land \lnot(b \land c)$.

- $(3)$ $a \lor c$.

- $(4)$ $c \rightarrow a$.

La formule $\varphi$ représentant le problème est :

$\varphi = (a \rightarrow b) \land ((b \lor c) \land \lnot(b \land c)) \land (a \lor c) \land (c \rightarrow a)$.

<u>Simplification :</u>

$\varphi \equiv (\lnot a \lor b) \land (b \lor c) \land (\lnot b \lor \lnot c) \land (a \lor c) \land (\lnot c \lor a)$.

$\varphi \equiv (\lnot a \lor b) \land (b \lor c) \land (\lnot b \lor \lnot c) \land ()a \lor (c \land \lnot c))$.

$\varphi \equiv (\lnot a \lor b) \land (b \lor c) \land (\lnot b \lor \lnot c) \land a$.

$\varphi \equiv a \land b \land (b \lor c) \land (\lnot b \lor \lnot c)$.

$\varphi \equiv a \land b \land \lnot c$.

Donc “$A$ prend un dessert” et “$B$ prend un dessert” et “$C$ ne prend pas de dessert”.

### 3. Systèmes complets de connecteurs


On a défini l’ensemble $\mathcal P$ avec les connecteurs {$\lnot,\land,\lor,\rightarrow,\leftrightarrow$}. Mais les règles d’équivalences fondamentales nous permettent d’écrire des formules propositionnelles en n’utilisant que {$\lnot,\land,\lor$}.

<u>Définition :</u>

Un ensemble de connecteurs forment un système complet si toute formule propositionnelle peut être écrite en utilisant uniquement ces connecteurs.

<u>Théorème :</u>

Le système {$\lnot,\land,\lor$} est complet.

Pour le montrer, on dresse les $2^{2^2} = 16$ tables de vérité existantes et pour chaque table, on trouve une formule utilisant uniquement ces trois connecteurs qui correspond.


|  x  | y   | $\varphi$ | /                                   |
| :-: | --- | --------- | ----------------------------------- |
|  F  | F   | V         | valuation $= \lnot x \land \lnot y$ |
|  F  | V   | V         | valuation $= \lnot x \land y$       |
|  V  | F   | F         | valuation $=  x \land \lnot y$      |
|  V  | V   | F         | valuation $= x \land y$             |
	On écrit chaque ligne à l’aide des connecteurs $\land$ et $\lnot$. On fait ensuite une disjonction $(V)$ entre les lignes où la valeur de vérité est $V$. Ici, $\varphi = (\lnot x \land \lnot y) \lor (\lnot x \land y)$.

## III. Problème SAT

### 1. Formes normales

<u>Objectif :</u> normaliser les formules propositionnelles.

#### a. Formes normales simples

<u>Définition :</u> 

Un littéral est soit une variable propositionnelle soit la négation d’une variable propositionnelle.

<u>Exemple :</u> $(x \land (\lnot y \lor z)) \rightarrow \lnot(\lnot x \land \lnot z)$. Les littéraux sont les variables munis des symboles adjacents ($\lnot$ inclus).

<u>Définition :</u>

Une formule propositionnelle mise sous forme normale négative ne contient que des conjonctions, disjonctions, et littéraux. 

<u>Exemple :</u>  La formule précédente n’est pas une forme normale négative.

$( x \land (\lnot y \lor z)) \lor y$ en est une tandis que $x \land \lnot(y \lor z)$ n’en est pas une.

<u>Méthode de mise sous forme normale négative :</u>

- On trouve une formule équivalente sémantiquement en retirant les $\rightarrow$ et les $\leftrightarrow$ pour ne garder que $\land,\lor ,\lnot$.

- Retirer les $\lnot$ qui ne sont pas sur des variables en utilisant les lois de Morgan.

- Retirer les doubles négations.

<u>Définition :</u>

- Une clause conjonctive est une conjonction de littéraux.

- Une clause disjonctive est une disjonction de littéraux.

<u>Remarque :</u>

$\bot$ est le neutre pour $\lor$, donc $\bot$ est considéré comme une clause disjonctive. De même $\top$ est le neutre de $\land$ donc $\top$ est considéré comme une clause conjonctive.

<u>Définition :</u>

Une formule en forme normale conjonctive est une conjonction de clauses disjonctives. 

<u>Exemple :</u> 

- $x \land (y \lor z) \land (\lnot x \lor \lnot z)$ est en forme normale conjonctive.

- $x \land y$ est en forme normale conjonctive (somme de deux clauses).

- $x \lor y$ est en forme normale conjonctive (une seule clause).

Une forme normale conjonctive est aussi en forme normale négative.

<u>Méthode pour mettre une formule propositionnelle en forme normale conjonctive :</u>

- Mettre la formule en forme normale conjonctive.

- Utiliser les équivalences fondamentales (distributivité notamment).

<u>Exemple :</u> $x \lor (y \land \lnot z) \equiv (x \lor y) \land (x \lor \lnot z)$ 

<u>Définition :</u>

Une formule en forme normale disjonctive est une disjonction de clauses conjonctives.

<u>Exemple :</u> 

- $(x \land y) \lor (\lnot x \land z) \lor y$ est en forme normale disjonctive (trois clauses conjonctives séparées par des $\lor$).

- $x \lor y$ est en forme normale disjonctive.

- $x \land y$ est en forme normale disjonctive (à 1 clause).

Une forme normale disjonctive est aussi en forme normale négative.

<u>Méthode pour mettre une formule propositionnelle en forme normale disjonctive :</u>

- Mettre la formule en forme normale négative.

- Utiliser les équivalences fondamentales (distributivité notamment).

<u>Exemple :</u> $x \land (y \lor \lnot z) \equiv (x \land y) \lor (x \land \lnot z)$.

Souvent, la mise en forme normale (conjonctive ou disjonctive) augmente la taille de la formule.

<u>Solution alternative pour implémenter une formule :</u>

On utilise une liste (la formule) contenant des listes (les clauses) contenant des entiers (littéraux) positifs (variable) et négatifs (négation des variables).

<u>Exemple :</u> $(x \land y \land z) \lor ( x \land \lnot y) \lor \lnot z$ est en forme normale disjonctive.

On pose par exemple : $x \leftrightarrow 1, y \leftrightarrow 2, z \leftrightarrow 3$. L’implémentation de cette formule donne : 

$[[1;2;3];[1;-2];[-3]]$

#### b. Formes normales canoniques

<u>Méthode pour trouver une forme normae disjonctive et forme normale conjonctive canoniques :</u>

On dresse la table de vérité.

<u>Exemple :</u> $\varphi = (x \land \lnot z) \rightarrow (\lnot x \land \lnot(y \land \lnot z))$.

| x   | y   | z   | $\varphi$ | /                                     |
| --- | --- | --- | --------- | ------------------------------------- |
| F   | F   | F   | V         | $\lnot x \land \lnot y \land \lnot z$ |
| F   | F   | V   | V         | $\lnot x \land \lnot y \land z$       |
| F   | V   | F   | V         |                                       |
| F   | V   | V   | V         |                                       |
| V   | F   | F   | F         |                                       |
| V   | F   | V   | V         |                                       |
| V   | V   | F   | F         |                                       |
| V   | V   | V   | V         |                                       |
<u>Forme normale disjonctive (=V) :</u>
$\varphi \equiv (\lnot x \land \lnot y \land \lnot z) \lor (\lnot x \land \lnot y \land z) \lor (\lnot x \land y \land \lnot z) \lor (\lnot x \land y \land z) \lor (x \land \lnot y \land z) \lor (x \land y \land z)$
<u>Forme normale conjonctive (=F) :</u> 

$\varphi \equiv \lnot(x \land \lnot y \land \lnot z) \land \lnot(x \land y \land \lnot z) \equiv (\lnot x \lor y\lor z) \land (\lnot x \lor \lnot y \lor z)$

<u>Forme normale disjonctive canonique :</u>

- Chaque valuation donne une clause conjonctive.

- La forme normale disjonctive canonique est une disjonctin entre tous les modèles (lignes V) de la formule.

<u>Forme normale conjonctive canonique :</u>

- On fait une conjonction des négations des valuations donnant F

- Appliquer les lois de Morgan et la double négation sur chaque valuation.

<u>Définition :</u> 

Un min-terme sur l’ensemble $\mathcal V$ est une conjonction de $|\mathcal V|$ dans laquelle chaque variable apparait une fois.

<u>Définition :</u>

La forme normale disjonctive canonique est une disjonction de min-termes différents.

<u>Définition :</u>

Un max-terme sur l’ensemble $\mathcal V$ est une disjonction de $|\mathcal V|$ littéraux dans laquelle chaque variable apparait une fois.

<u>Définition :</u>

La forme normale conjonctive est une conjonction de max-termes différents.

<u>Théorème :</u>

Toute formule propositionnelle est équivalente à une unique forme normale disjonctive canonique et une unique forme normale conjonctive canonique ( à ordre près des min-termes/max-termes).

<u>Intérêt :</u>

Soit $\varphi$ une formule propositionnelle. 

$\varphi$ tautologie $\Leftrightarrow$ sa forme normale disjonctive canonique contient tous les min-termes $\Leftrightarrow$ sa forme normale conjonctive contient aucun max-termes

$\varphi$ antilogie $\Leftrightarrow$ sa forme normale disjonctive canonique contient rien $\equiv$ $\bot$ $\Leftrightarrow$ sa forme normale conjonctive contient tous les max-termes

$\varphi$ satisfiable $\Leftrightarrow$ sa forme normale disjonctive canonique contient au moins un min-termes $\Leftrightarrow$ sa forme normale conjonctive contient au moins un max-termes

Donc si on possède les formes normales canoniques d’une formule, on détermine si elle sont satisfiable en $\mathcal O(1)$.

<u>Inconvénient :</u> 

Taille des formes normales  : Il y a $2^n$ (avec $n = |\mathcal V|$) lignes dans la table, donc 2^n termes répartis dans les formes normales, donc au moins 1 forme normale canonique a une taille exponentielle.

### 2. Problème K-SAT


<u>Définition :</u>

Un problème SAT est un problème de décision qui détermine si une formule propositionnelle est satisfiable.

SAT($\varphi$) avec $\varphi$ une formule propositionnelle : Renvoie Vrai si $\varphi$ est satisfiable, Faux sinon.

<u>Complexité :</u>

Le problème SAT est NP-complet (on suppose qu’il n’existe aucun algorithme avec une complexité pire des cas non exponentielle).

<u>Définition :</u>

Un problème K-SAT est la restriction du problème SAT aux forme normale conjonctive dont chaque clause comporte au plus $k$ littéraux.

<u>Exemple :</u> $\varphi = (\lnot a \lor b) \land (b \lor c) \land (\lnot b \lor \lnot c) \land ( a \lor c) \land (\lnot c \lor a)$.

Le problème des desserts est une instance de 2-SAT.

#### a. Cas particuliers de 1-SAT et 2-SAT

- <u>Problème 1-SAT :</u> 

Si on a $\varphi = x \land … \land \lnot x \land …$ avec $x \in \mathcal V$ alors $\varphi$ est insatisfiable.

$\varphi$ est satisfiable si et seulement si pour chaque variable propositionnelle, $\varphi$ ne contient jamais cette variable et sa négation.

La complexité est linéaire en la taille de la formule.

- <u>Problème 2-SAT :</u> 

On représente le problème par un graphe. Chaque clause est de la forme $(l_{1} \lor l_{2})$ 
Or $l_{1} \lor l_{2} \equiv \lnot l1 \rightarrow l_{2} \equiv \lnot l_{2} \rightarrow l_{1}$.

Dans le graphe orienté, on aura donc deux sommets $\lnot l_{1}$ et $l_{2}$ avec un arc $(\lnot l_{1}, l_{2})$ et $2$ sommets $\lnot l_{2} et l_{1}$ avec un arc $(\lnot l_{2}, l_{1})$ et ce pour chaque clause.

<u>Exemple :</u> Problème des desserts

![[Excalidraw/Drawing 2024-05-23 08.25.10.excalidraw]]

<u>Théorème :</u> 

Une instance de 2-SAT est satisfiable si et seulement si dans le graphe associé, aucune composante fortement connexe ne contient à la fois une variable propositionnelle et sa négation.

<u>Preuve :</u>

Supposons qu’il existe une composante fortement connexe qui contient $x \in \mathcal V$ et aussi $\lnot x$.

Il y a donc un chemin allant de $x$ à $\lnot x$ et un allant de $\lnot x$ à $x$ donc $\varphi \vDash \lnot x \leftrightarrow x$ (car $x \rightarrow \lnot x$ et $\lnot x \rightarrow x$ par transitivité de $\rightarrow$).

Or $\lnot x \leftrightarrow x \equiv \bot$ donc $\varphi \vDash \bot$ donc $\varphi$ admet aucun modèle donc $\varphi$ insatisfiable.

(Sens $\Leftarrow$). On note $C_{l}$ la composante fortement connexe de $l$. On s’intéresse au graphe des composantes fortement connexes, orienté et acyclique. (preuve par l’absurde). Ce graphe admet un ordre topologique $\prec$. Montrons que la valuation $v$ suivante est un modèle de $\varphi$.
$$\begin{equation} \begin{cases} v(X) = V \text{ si } C_{\lnot x} \prec C_{x} \\ v(X) = F \text{ si } C_{x} \prec C_{\lnot x}\end{cases} \end{equation}$$
(On est bien toujours dans $1$ des $2$ cas car $C_{x} \neq C_{\lnot x}$).

Soit $(l \lor l’)$ une clause de la forme normale conjonctive de $\varphi$. Il faut donc montrer que v satisfait $l \lor l’$, donc que v satisfait l oy v satisfait l’. Supposons par l’absurde que $v(l) = v(l’) = F$. 

$v(l) = F$ donc $C_{l} \prec C_{\lnot l}$
$v(l’) = F$ donc $C_{l’} \prec C_{\lnot l’}$

Or si $l \lor l’$ est une clause, alors $(\lnot l, l’)$ est un arc $C_{\lnot l} \preceq C_{l’}, (\lnot l’, l)$ est un arc donc $C_{\lnot l’} \preceq C_{l}$. Par transitivité de $\prec$ on trouve $C_{l} \prec C_{l} \preceq C_{l'} \prec C_{\lnot l’} \preceq C_{l}$, impossible donc $v$ est un modèle de $\varphi$.

<u>Complexité :</u>

- Construction du graphe : $|S| = 2 \times |\mathcal V|$, $|A| = 2 \times \text{nombre de clauses}$, $\mathcal O(|S| + |A|)$.

- recherche des composantes fortement connexes : $\mathcal O(|S| + |A|)$.

- vérification des composantes : $\mathcal O(|S|)$

<u>Total :</u> $\mathcal O(|S| + |A|)$, même ordre de grandeur que la taille de formule, donc linéaire en taille de la formule.

#### b. Algorithme de Quine

La résolution de K-SAT pour $k > 2$ a un complexité exponentielle : on utilise un algorithme de recherche exhaustive

- soit une recherche par force brute : teste pour chaque valuation existante, s’il s’agit d’un modèle donc cela revient à construire la table de vérité.

	$2^{|V|}$ valuations à tester

	Evaluer la formule $\varphi$ pour une valuation se fait en $\mathcal O(|\varphi|)$

- soit une recherche par retour sur trace (backtracking), c'est l'algorithme de Quine.

<u>Principe :</u>

On part d’une formule $\varphi$ (à la racine de l’arbre). On choisit une variable propositionnelle $x$ de $\varphi$.

- 1ère branche de l’arbre :

	 On détermine $\varphi[\bot/x]$. On élimine les constantes logiques. On recommence l’algorithme avec la formule ainsi obtenue.

	- 2ème branche :

		On détermine $\varphi[\top/x]$. On élimine les constantes.  On recommence.

On s’arrête quand la formule est $\top$ ou $\bot$ (aucune variable, feuilles).

Règles d’élimination des constantes logiques de Quine :

$\lnot \bot \equiv \top$
$\lnot \top \equiv \bot$
$\top \rightarrow \varphi \equiv \varphi$
$\varphi \rightarrow \top \equiv \top$
$\bot \rightarrow \varphi \equiv \bot$
$\varphi \rightarrow \bot \equiv \varphi$
$\top \lor \varphi \equiv \top$
$\varphi \lor \top \equiv \top$
$\bot \lor \varphi \equiv \varphi$
$\varphi \lor \bot \equiv \varphi$
$\top \land \varphi \equiv \varphi$
$\varphi \land \top \equiv \varphi$
$\bot \land \varphi \equiv \bot$
$\varphi \land \bot \equiv \bot$
$\top \leftrightarrow \varphi \equiv \varphi$
$\varphi \leftrightarrow \top \equiv \varphi$
$\bot \leftrightarrow \varphi \equiv \lnot \varphi$
$\varphi \leftrightarrow \bot \equiv \lnot \varphi$

![](Excalidraw/Pasted_image_20240523093547.png)

<u>Proposition :</u> 

- Toutes les feuilles sont à $\bot \Leftrightarrow \varphi$ antilogie.

- Au moins une feuille est $\top \Leftrightarrow \varphi$ satisfiable.

- Toutes les feuilles sont $\top \Leftrightarrow \varphi$ tautologie.

Se montre par induction structurelle.

<u>Terminaison :</u>

- à chaque substitution, le nombre de variables propositionnelles diminue strictement (de $1$ variable).

- à chaque élimination, la taille de la formule diminue strictement (on vérifie les règles une par une).

- On prend l’ordre lexicographique (nombre de variables, taille de la formule)

	 - On vérifie aisément la stricte décroissance.

	 - ensemble bien fondé

donc termine.

#### c. Réduction d’un problème à SAT

<u>Méthodologie :</u>

<u>Exemple :</u> Est-il possible de colorer un graphe $G$ en utilisant au plus $K$ colonnes ?

<u>Etape 1 :</u>

On introduit toutes les variables propositionnelles.

<u>Exemple :</u> On a besoin de $|S| \times k$ variables. $x_ {i,c}$ signifiant le sommet $i$ est colorié avec la couleur $c$.

<u>Etape 2 :</u>

On établit la liste des conditions à respecter pour résoudre le problème.

<u>Exemple :</u> 

- Chaque sommet est coloré avec $1$ couleur. 

- $2$ sommets adjacents ne doivent pas avoir la même couleur.

<u>Etape 3 :</u>

Transformer chaque condition en une formule propositionnelle.

<u>Etape 4 :</u>

On résout SAT($\varphi$) avec $\varphi$ la conjonction de toutes les formules obtenues pour les conditions.