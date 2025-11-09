---
draft: 
date: 2024-09-30
---
I followed this course by, Prof. [Nick Bezhanishvili]() during my [[5th Semester]] at the [[ILLC Amsterdam]] for my [[M.Sc. Logic (UvA)]]. I covered most of the material already in [[Modal Logic (Lecture)]]. The notes are from the book: _Modal Logic_ by P. Blackburn, M. de Rijke, Y. Venema, (2010), Cambridge University Press.

As general material I produced or used while following the course, I leave here some incomplete [[Introduction to Modal Logic (Lecture)#Lecture Notes]], I give here also the links to the [[Introduction to Modal Logic (Lecture)#Assignments]] and to [Final Exam's Solutions](https://www.overleaf.com/read/xkskcjnbhcjk#e9e8fa).
#### Assignments
1. [Overleaf: IML, 1](https://www.overleaf.com/read/qdtknhmjymqt#0a2005)
2. [Overleaf: IML, 2](https://www.overleaf.com/read/cpcbpxgshgwx#9933a8)
3. [Overleaf: IML, 3](https://www.overleaf.com/read/fhfgdcfdxfks#e50bb8)
4. [Overleaf: IML, 4](https://www.overleaf.com/read/nqzhrtkqwbjy#cd734e)
5. [Overleaf: IML, 5](https://www.overleaf.com/read/bnbpqggkwwdm#e2f4f5)
## Lecture Notes
- Bisimilarity & Invariance Lemma, as in: [[Modal Logic (Lecture)#3. Expressive Power and Invariance]].
	- converse of invariance lemma holds with $n$-bisimilarity for $n \in \mathbb{N}$. (see 2.24)
	- $\mathcal{M} = (M, R, V)$ is _image finite_ if $\forall_{x \in M} |R[x]| < \aleph_0$
		- $R[x] := \{y \in M : x R y\}$
	- for $\mathcal{M}$, $\mathcal{M}'$ image finite, $\forall_{x \in M}\forall_{x' \in M'} \mathcal{M}, x \equiv \mathcal{M}', x' \Rightarrow \mathcal{M}, x \underline{\leftrightarrow}\mathcal{M}', x'$ (Hennessy - Milner)
		- $\equiv$ often written as $\leftrightsquigarrow$
		- $\mathcal{M}, x \equiv \mathcal{M}', x' \Rightarrow \mathcal{M}, x \underline{\leftrightarrow}\mathcal{M}', x'$ often written as $x \equiv x' \Rightarrow x \underline{\leftrightarrow} x'$.
	- \[for $k \in ON$ the maximal complexity of a formula in $\mathcal{L}^k_{ML}$, a $k$-inductively defined modal logic, then $\forall_{x \in M}\forall_{x' \in M'} \mathcal{M}, x \equiv \mathcal{M}', x' \Rightarrow \mathcal{M}, x \underline{\leftrightarrow}^k \mathcal{M}', x'$ for $\underline{\leftrightarrow}^k$ the $k$-bisimulation, as defined in: [Overleaf: IML, 1](https://www.overleaf.com/read/qdtknhmjymqt#0a2005)\]
#### Types (from the Book)
- $\tau = (O, \rho)$ is a _modal similarity type_ for $O \not = \emptyset$, $\rho: O \to \mathbb{N}$, 1.11
	- elements of $O$ are _modal operators_
		- use $\triangle_0, \triangle_1, ...$ to denote its elements.
			- for $i \in \mathbb{N}$, $\triangledown_i(\varphi_1, ..., \varphi_n) := \lnot \triangle_i (\lnot \varphi_1, ..., \lnot \varphi_n)$ 
	- $\rho$ assigns to each operator $\triangle$ a finite arity.
- $ML(\tau, \Phi)$ is a _modal language_ for $\tau = (O, \rho)$ and a set of prop.lett $\Phi$, 1.12
	- $Form(\tau, \Phi)$ is given by $\langle p | \bot | \lnot \varphi | \varphi_1 \land \varphi_2 | \triangle (\varphi_1, ..., \varphi_{\rho(\triangle)}) \rangle$ 
- $\tau$-type at $w$ is $\{\varphi : \mathcal{M}, w \models\varphi\}$, 2.1
	- two $\tau$-types at $w$ and $w'$, for $w \in M, w' \in M'$, s.t. $\mathcal{M}, \mathcal{M}'$ have same mod.sim.type $\tau$, write $w \leftrightsquigarrow w'$ if $\tau$-type.$w$ is $\tau$-type.$w'$.
	- $\mathcal{M} \leftrightsquigarrow \mathcal{M}'$ iff $\bigcap_{w \in M} \{\varphi : \mathcal{M}, w \models\varphi\} = \bigcap_{w' \in M'} \{\varphi : \mathcal{M}', w' \models\varphi\}$
	- $\mathcal{M} \bigsqcup \mathcal{N}$ preserves all information.
- for $\tau$ mod.sim.type, $\mathcal{M}_i$ $\tau$-models, then $\forall_{\varphi \in \mathcal{L}_{\tau-ML}}\forall_{i \in I} \forall_{w \in M_i} \mathcal{M}_i, w \models \varphi \Leftrightarrow \bigcup_{i \in I}\mathcal{M}_i, w \models \varphi$, 2.3
#### 17.09, Filtrations
- A (generated) submodel $\mathcal{M}'$ of $\mathcal{M}$ is a model s.t.
	1. $W' \subseteq W$ 
	2. $R' = R \cap (W' \times W')$
	3. $V'(p) = V(p) \cap W'$ 
	(4.) $\forall_{w \in M'} wRv \to v \in W'$ 
	- $\mathcal{M'}$ is gen.sub, of $\mathcal{M}$, $x \in W'$, then $\mathcal{M}, x \underline{\leftrightarrow} \mathcal{M}', x$
- $\mathcal{M}$ is rooted if exists $w \in M$, a root, that generates the whole model, 2.5
- **Morphisms**
	- **Homo-** for $\mathcal{M}, \mathcal{M}'$ $\tau$-models, $f: \mathcal{M} \to \mathcal{M}'$ hom., if: , 2.7
		1. $\forall_{p \in \text{Prop}} \forall_{w \in W} w \in V(p) \to f(w) \in V'(p)$ 
		2. $$\forall_{n \in \mathbb{N}_0} \forall_{\triangle \in \tau} \rho(\triangle = n \to \forall_{W \subseteq M} |W| = n +1 \to W = (w_0, ..., w_n) \in R_\triangle \to (f(w_0), ..., f(w_n)) \in R_\triangle'$$
		- Modal formulas are not invariant under homomorphism, structure of the domain (_source_) is reflected in the image (_target_), not the riverse.
		- $\forall_{w \in M}\forall_{w' \in M'}\exists_{f: \mathcal{M} \to \mathcal{M}'} f(w) = w' \Rightarrow (\forall_{\varphi \in \mathcal{L}_{ML}} \mathcal{M}, w \models \varphi \Leftrightarrow \mathcal{M}', w' \models \varphi)$, 2.9
		- $\mathcal{M} \cong \mathcal{M}' \Rightarrow \mathcal{M} \leftrightsquigarrow \mathcal{M}'$, 2.9
	- **Bounded**: if
		1. $\forall_{w \in M} \forall_{p \in \text{Prop}} \mathcal{M}, w \models p \Leftrightarrow \mathcal{M}', f(w) \models p$ 
		2. $f$ is homom. to $R$
		3. $\forall_{w \in M} \forall_{v' \in M'} f(w) R v' \to \exists_{v \in M} wRv \land f(v) = v'$
		- let $f: \mathcal{M} \to \mathcal{M}'$ bound.morph., then $\forall_{\varphi \in \mathcal{L}_{ML}} \forall_{w \in M} \mathcal{M}, w \models \varphi \Leftrightarrow \mathcal{M}', f(w) \models \varphi$ 
			- for $\mathcal{M}, \mathcal{M}'$ models, $f: W \to W'$ a bound.morph., then $\mathcal{M}, x \underline{\leftrightarrow} \mathcal{M}', f(x)$
	- for $\{\mathcal{M}_i\}_{i \in I}$ for $\mathcal{M}_i$ model, the disj.union ([[On Disjoint Union]]) is a model $\mathcal{M}$ s.t.
		1. $W := \bigsqcup_{i \in I} W_i$, $R = \bigcup_{i \in I} R_i$, $V(p) = \bigcup_{i \in I} V_i(p)$ 
- [[Modal Logic (Lecture)#5. Finite Model Property]]:
	- _Modal Depth_:\is $deg$ defined as follows:
		1. (i) $deg(p) = 0$, (ii) $deg(\bot) = 0$, (iii) $deg(\lnot \phi) = deg(\phi)$, (iv) $deg(\phi \land \psi) = \max\{deg(\phi), deg(\psi)\}$ 
		2. (v) $deg(\triangle (\phi_1, ..., \phi_n)) = 1 + max\{deg(\phi_1), ..., deg(\phi)_n\}$ 
	- $w \underline{\leftrightarrow}_n w'$ i.e. bisimulate up to depth $n$.
		- if, for $\text{Prop} \subsetneq \mathcal{L}_{ML}$, $|\text{Prop}| < \aleph_0$, then $(\forall_{n \in \mathbb{N}} \mathcal{M}, w \underline{\leftrightarrow}_n \mathcal{M}', w') \Leftrightarrow (\forall_{\varphi \in \mathcal{L}_{ML}} \mathcal{M}, w \models \varphi \Leftrightarrow \mathcal{M}', w' \models \varphi)$, 2.30-1
	- for $\mathcal{M}$ rooted model in $w$, define:, 2.32
		1. $\forall_{w' \in M}ht(w') = 0 \to w' = w$
		2. $\forall{w' \in M} ht(w') = n + 1 \to \exists_{w'' \in M}ht(w'') = n \land w'' R w'$ 
		- $ht(\mathcal{M}) = \max\{ht(w') : w' \in M\}$ 
		- $\mathcal{M}|_k = (M|_k, R|_k, V|_k)$
			1. $M|_k = \{w' \in M : ht(w') \le k\}$, $R|_k = R|_{M|_k}$ and $V|_k = V|_{M|_k}$.
	- if $\tau$ has only diamonds, $\phi$ is sat. iff sat. on a finite mode, 2.34
	- **Filtrations** from 2.25
		- for $\Sigma \subseteq \mathcal{L}_{ML}$ cl.under subformulae, 2.36
		- $W_\Sigma := \{[x]: x \in W\}$
			- $[x]_{(\Sigma)} := \{y \in W : x \leftrightsquigarrow_\Sigma y\}$
				- $x \leftrightsquigarrow_\Sigma y := \forall_{\varphi\in \Sigma}(\mathcal{M}, x \models \varphi \Leftrightarrow \mathcal{M}, y \models \varphi)$
		- the filtration model $\mathcal{M}^f$, 2.36
			1. $W^f = W_\Sigma$
			2. $\forall_{x, y \in M} xRy \Rightarrow [x] R^f [y]$ 
			3. $\forall_{x, y \in M} ([x]R^f[y] \Rightarrow \forall_{\lozenge \varphi \in \Sigma}(\mathcal{M}, y \models \varphi \Rightarrow \mathcal{M}, x \models \lozenge \varphi))$
			4. $V^f(p) = \{[x]: \mathcal{M}, x \models p\}$
		- $\forall_{\Sigma \subseteq \mathcal{L}_{ML}} |\Sigma| < \aleph_0 \to\forall_{\varphi \in \Sigma}  \forall_{x \in W} \mathcal{M}, x \models \varphi \Leftrightarrow \mathcal{M}^f, [x] \models \varphi$, 2.39
			- $\forall_{\Sigma \subseteq \mathcal{L}_{ML}} |\Sigma| < \aleph_0 \to |M^f| \le 2^{|\Sigma|}$, 2.38
			- every formula that is satisfiable, is satisfiable in a finite model, 2.41
				- for $\Sigma_\phi$ the subformula-closure of $\{\phi\}$.
		- One can always define filtration through:, 2.39
			1. $[w] R^s [v] \Leftrightarrow \exists_{w' \in [w]} \exists_{v' \in [v]} w' R v'$ (smallest)
			2. $[w] R^l [v] \Leftrightarrow (\forall_{\Diamond \phi \in \Sigma} \mathcal{M},v \models \phi \Rightarrow \mathcal{M},w \models \Diamond \phi)$ (largest)
			- $R^s \subseteq R^f \subseteq R^l$ 
			- $[w] R^t [v] \Leftrightarrow \forall_{\Diamond \phi \in \Sigma}(( \mathcal{M}, v \models \phi \land \Diamond \phi) \to \mathcal{M}, w \models \Diamond \phi)$ 
				- $R$ trans. $\Rightarrow R^t$ trans.
				- for $R$ trans., define $C \subseteq M$, $(C, R|_C, V|_C)$ (cluster), 2.43
					- a cluser is _simple_, if $C = \{c\}$ s.t. $cRc$ and _proper_ if $|C| \ge 2$.
#### 24.09, IV. Trees
- a tree $(T,S)$ is a frame s.t. 
	1. $T$ is _rooted_ (i.e. $\forall_{t \in T}\exists!_{r \in T} rS^*t$)
		1. for $S^*$ the refl.trans.cl. of $S$
	2. $\forall_{t \in T} t \not = r \to \exists!_{t' \in T} t' S t$
	3. $\forall_{t \in T} \lnot t S^+ t$
		1. for $S^+$ the trans.cl. of $S$
- for $\mathcal{M} = (W, R, V)$, ex. $\mathcal{T} = (T, S, V)$ s.t. $f: T \to V$ surj. bounded morphism.
- a path in $\mathcal{M}$ is a seq. $(r, u_1, ..., u_n)$ s.t. $u_i R u_{i + 1}$ 
#### Standard Translation
#### 01.10, V. Frame Definability
- a class of frames $C$ is definable if there is a modal formula $\varphi$ s.t. $\mathcal{F} \models \varphi \Leftrightarrow \mathcal{F} \in \mathcal{C}$.
- recall bounded functions from [[Introduction to Modal Logic (Lecture)#17.09, Filtrations]].
	- for $f$ bounded morphism, s.t. $dom(f) = F$, $f(F)= G$, then $\forall_{\varphi \in\mathcal{L}_{ML}} \mathcal{F} \models \varphi \Rightarrow \mathcal{G} \models \varphi$.
		- "modally definable classes are closed under bounded morphisms."
- recall disjoint union from [[Introduction to Modal Logic (Lecture)#17.09, Filtrations]]. We define it now for frames.
	- for $C$ a definable class of frames: $\forall_{\mathcal{F}, \mathcal{G} \in C} \mathcal{F} \bigsqcup \mathcal{G} \in C$ 
- for $C$ FO.def.class of frames, then $C$ is mod.def. iff. $C$ is cl. under bounded morphic images, hgenerated subframes, disjoint unions and _reflects untrafitler extensions_ (Goldlatt - Thomson Theorem)
	- see [[Model Theory (Lecture)]] for ultrafilters, but also [[First Bachelor Thesis Concept]].
- Löb formula: $\square ( \square p \to p) \to \square p$ 
	- for $p = \bot$, $\square ( \square \bot \to \bot) \to \bot \Leftrightarrow \square \lnot \square \bot \to \square \bot$, if you prove smth _consistent_, it is _false_ (Gödel)
- **Gödel Logic** (GL)
	- $\mathcal{F}$ is conversely well-founded if there is no ascending infinite chain
		- (it is not FO-def.)
	- $\mathcal{F}$ not trans., $\mathcal{F}$ not conv.well.foud. then $\mathcal{F} \not \models \square ( \square p \to p) \to \square p$.
	- $\mathcal{F} \models \varphi \Leftrightarrow \forall_{p} \forall_x ST_x (\varphi)$ ==?==
#### 08.10, VI. Correspondence
- $(\mathcal{F}, V) \models \varphi \Leftrightarrow (\mathcal{F}, V) \models \forall_x ST_x(\varphi)$, this is the general form of correspondence
	- $\mathcal{F} \models \varphi(p_1, ..., p_n) \Leftrightarrow \mathcal{F} \forall_{p_1, ..., p_n} \forall_x ST_x (\varphi)$, with a second order quantification
	- for some, second order is not needed: $\mathcal{F} \models p \to \Diamond p \Leftrightarrow \mathcal{F} \models \forall_x xR x$
		- which is: $\forall_{p} \forall_x ST_x (p \to \Diamond p)$
-  $\forall_{\varphi \in \mathcal{L}_{ML}} \exists_{\alpha(x) \in \mathcal{L}_{FOL}} \forall_{\mathcal{F} = (M, R)} \mathcal{F} \models \varphi \Leftrightarrow \mathcal{F} \models \forall_x \alpha(x)$, call "$\forall_x \alpha(x)$" is a FO-correspondent of $\varphi$.
	- example: $\mathcal{F} \models \Diamond \top \Leftrightarrow \forall_{p_1, ..., p_n} \forall_x \exists_y (x R y \land y = y) \Leftrightarrow \mathcal{F} \models \forall_{x}\exists_y x R y$ 
		- $\varphi \in \mathcal{L}_{ML}$ is closed if $\forall_{p \in \text{Prop}}\dot p \not \in \varphi$ 
		- if $\varphi$ is closed, it has a FO-corr., which is effectively computable form $\varphi$.
- more clearly than in the book: [[Sahlqvist.pdf]]
- for $\varphi \in \mathcal{L}_{ML}$, write occurrences as $\dot p \in \varphi$, call it positive if $p$ is under an even number of negations in $\varphi$ 
	- I write $\dot p \in_+ \varphi$. occurrences are either positive or negative ("$\in_-$")
- $\varphi \in \mathcal{L}_{ML}$ is positive if $\forall_{p \in \text{Prop}} \dot p \in_+ \varphi$ 
	- formulae are positive, negative or either of the two.
	- clearly, $\forall_{\varphi \in \mathcal{L}_{ML}}pos.(\varphi) \Leftrightarrow neg.(\lnot \varphi)$
- for $\varphi \in \mathcal{L}_{ML}$, $p \in \text{Prop}$ s.t. $\dot p \in_+ \varphi$, let $V$ a val. on $\mathcal{F}$, and $V'$ a val. s.t. $\forall_{q \not = p}V'(q) = V(q)$ and $V(p) \subseteq V'(p)$, then $(\mathcal{F}, V), w \models \varphi \models \varphi \Rightarrow (\mathcal{F}, V'), w \models \varphi$.
	- $\Leftarrow$ for $\lnot p$.
- there always is a _minimal valuation_ that makes the formula false
#### 12.11, General Frames & Incomplete Logics
- $(W, R, A)$ is a general frame if $(W, R)$ is a kripke frame and $A \subseteq \mathcal{P}(X)$ s.t.
	1. $W, \emptyset \in A$
	2. $\forall_{U, V \in A} U \cup V \in A$
	3. $\forall_{U, V \in A} U \setminus V \in A$
	4. $\forall_{U \in A} \{x \in W: \exists_{y \in U} x R y\}  \in A$ 
		- $\Diamond_R U := \{x \in W: \exists_{y \in U} x R y\}$
- for $(W, R, A)$ a gen.fr. then:
	1. $\forall_{U, V \in A} U \cap V \in A$ 
	2.  $\forall_{U \in A} \{x \in W: R[x] \subseteq U\}  \in A$
		1. $R[x] := \{y : x R y\}$ 
		- $\square_R U := \{x \in W: R[x] \subseteq U\}$
- $(W,R,A, V)$ is a gen.mod. for $(W, R, A)$ a gen.fr and $V: \text{Prop} \to A$.
	- $[\![\varphi]\!]:= \{x \in W : \mathcal{M}, x \models \varphi \land \varphi \in A\}$
- $F = (W, R, A)$ gen.fr and $Log(F) := \{\varphi : F \models \varphi\}$ is a consistent normal modal logic.
- Define $K_t Tho$ (M)
	1. $\Diamond_F p \land \Diamond_F q \to \Diamond_F(p \land \Diamond_Fq) \lor \Diamond_F(p \land q) \lor \Diamond_F(\Diamond_F p \lor q)$ 
	2. $\Diamond_F \top$
	3. $\Box_P( \Box_P q\to q) \to \Box_P q$ 
	- (M) $\Box_F \Diamond_F p \to \Diamond_F \Box_F p$ 
- $K_t ThoM$ is an consistent and complete logic
#### 26.10 Completeness of PDL
Definition (Atom) let $\Sigma$ be a set of formulae, $A$ is an Atom if $A \subs \lnot FL(\Sigma) is consistent A \not \vdash_{\PDL} \bot$ and $A subsetneq B \subset \lnot \FL(\Sigma), then $B \vdahs_{\PDL} \bot$

Also define $At(\Sigma). = \{A | A$ is an atom in $\lnot FL(\Sigma)\}

Lemma let $A$ \in At(\Sigma), then:
1. \varphi \in \lnot FL(\Sigma): exatly one \varphi \in A or \lnot \varphi \in A
2. ... (sry missed those, but simple equivalence following the definitions of the ways combining programs given in \FL).
3. -
4. -
5. -
Lemma At(\Sigma) = \{\Gamma \cap \lnot FL(\Sigma) : for some MCS \Gamma\}
_Proof_ \Gamma \cap \lnot FL(\Sigma) is consistent \not \vdash \bot as $\Gamma \not \vdash \bot
suppose \Gamma \cap \lnot \FL(\Sigma) \subsetneq B \subseteq \lnot \FL(\Sigma), then there is a \varphi \in B$ but \varpgu \not \in \Gamma \cap \lnot FL(\Sigma), so \varphi \not \in \Gamma. We then. conclide \lnot \varphi \in \Gamma, so...

For the other direction, simple application of the Lindenbaum lemma.
$A \subseteq \Gamma \ca \lnto FL(\Sigma) \Rightarrow A = \Gamma \cap \lnot FL(\Sigma) as both are atoms.

Consider that all proof swe are doing are constructive by finiteness of \Sigma and hence of $\FL(\Sigma)$

Lemma if \varphi \in \lnot \FL(\Sigma) and $\{\varphi\} is consistent, \varphi \not \vdash \bot then there is aa $A \in At(\Sigma)$ s.t. \varphi \in A.
Proof by Lindenbaum

Definition (finite canonical model over $\Sigma$) "temporary definition".
Let $\Sigma$ be a finite set of formulas, the finite canonical model over $\Sigma$ is made by $(At(\Sigma), \{S_\pi\}_{\pi \in \Pi}, V^{\Sigma})$ where $V^\Sigma(p) = \{A \in At(\Sigma) : p \in A\}$. We then define $A S^\Sijgma_\pi B \Leftrightarrow \hat A \land \langle \pi \rangle \hat B$., where $\hat A := \bigwedge \{\varphi : \varphi \in A\}$. 

Note now: $S_{\pi_1 \cup \pi_2} \not = S_{pi_1} \cup S_{\pi_2}$ and $S_{\pi^*} \not = (S_{\pi})^*$ and we dont like it! We _massage_ the canonical model in order to prove this but still prove the Truths Lemma.

Lemma let $A$ \in At(\Sigma) and $\langle \pi \rangle 