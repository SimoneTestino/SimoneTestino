The notes can be downloaded from [here](https://dspace.library.uu.nl/handle/1874/26292).
##### 1. Definitions
- $\langle K, b , R, \{S_x : x \in K\} \rangle$ is a _Veltman Prestructure_ if:
	1. $K \not = \emptyset$
	2. $b \in K \land \forall_{x \in K} x = b \lor bRx$
	3. $R$ is binary relations
	4. $S_x$ are binary relations on $K$ s.t. $\forall_{x, y, z \in K} y S_x z \to x R y$ 
		- $S[x] := S_x$
- $A \triangleright B$ iff $T + A$ is (relatively) interpretable in $T + B$, (it is axiomatised in the construction of BIL)
	- for $T + A := \{\varphi: \exists_{\varphi_1, ..., \varphi_n \in T}\exists_{\psi_1, ..., \psi_m \in A} \{\varphi_1, ..., \varphi_n, \psi_1, ..., \psi_m\}\vdash \varphi\}$, if theories are meant to be inferentially closed, otherwise, $T + A := T \cup A$.
- for $K \not = \emptyset$ and $\mathcal{L}$ the language, $\Vdash$ is a relation between $K$ and $\mathcal{L}$ with the =="usual clauses"==, together with: 
	- for $x \in K$, $A, B$ theories, $(x \Vdash A \triangleright B)\leftrightarrow (\forall_{y \in K} ((x R y \land y \Vdash A) \to \exists_{z \in K}(y S_x z \land z \Vdash B)))$ 
- for $V$ a Veltman prestructure, $\Vdash$ a forcing relation on $V$, $\langle V , \Vdash \rangle$ is a _Veltman Premodel_
- for $W, W'$ two Veltman Premodels, $\beta$ is a bisimulation if:
	1. $\beta$ is a relation between $K$ and $K'$
	2. $b \beta b'$
	3. $\forall_{x \in K} \forall_{x' \in K'} x \beta x' \to (\forall_{y \in K} (x R y \to \exists_{y' \in K'}(y \beta y' \land x' R y' \land \forall_{z' \in K'}(y' S_x z' \to \exists_{z \in K}( z \beta z' \land y S_x z))))$
	4. $\forall_{x \in K} \forall_{x' \in K'} x \beta x' \to (\forall_{y' \in K'} (x' R y' \to \exists_{y' \in K'}(y \beta y' \land x R y \land \forall_{z \in K}(y S_{x'} z \to \exists_{z' \in K'}( z' \beta z \land y' S_{x'} z'))))$
	5. $\forall_{x \in K} \forall_{x' \in K'} x \beta x' \to (x \Vdash p \leftrightarrow x' \Vdash p)$ for all atoms $p$
	- cf. [[Modal Logic (Lecture)#3. Expressive Power and Invariance]]
##### 2. Facts
- (i) bisimulating is an equivalence relation
- (ii) for $\beta$ a bisimulation between $W, W'$ and $x \in K$, $x' \in K'$ s.t. $x \beta x'$, then for any theory $A$ of the language $x \Vdash A \Leftrightarrow x' \Vdash' A$.
	- corresponds to J4, K1, K2.
##### 3. Some Principles & Correspondences for Veltman Prestructures
see [[Modal Logic (Lecture)#4. Frame Correspondence]]. These principles show the strong similarities between "$\triangleright$" and "$\to$".
- $\vdash \square ( A \to B) \to A \triangleright B$, (J1)
	- corresponds to: $x R y \to y S_x y$
- $\vdash (A \triangleright B \land B \triangleright C) \to A \triangleright C$, (J2)
	- Transitivity
	- corresponds to: for all $x \in K$, $S_x$ is transitive and $y S_x z \to x R z$
	- if we consider structures with (ii), J2 corresponds to (i).
- $\vdash (A \triangleright C \land B \triangleright C) \to (A \lor B) \triangleright C$, (J3)
- $\vdash A \triangleright B \to (\lozenge A \to \lozenge B)$, (J4)
	- corresponds to (ii)
- $\vdash (A \triangleright B \land \square(B \to C)) \to A \triangleright C$, (K1)
	- corresponds to (ii)
- $\vdash (A \triangleright B \land B \triangleright \bot) \to A \triangleright \bot$, (K2)
	- corresponds to (ii)
- $\vdash \lozenge A \triangleright A$, (J5)
	- corresponds to: $x R y \land y R z \to y S_x z$
##### 4. More Definitions
- $\langle K, b , R, \{S_x : x \in K\} \rangle$ is a _Veltman Structure_ if:
	1. $K \not = \emptyset$
	2. $b \in K \land \forall_{x \in K} x = b \lor bRx$
	3. $R$ is binary relations
	4. $S_x$ are transitive and reflexive binary relations $\{y \in K : x R y\}$ ($=: xR$)
	5. $\forall_{x, y, z \in K} (x R  y \land y R z) \to y S_x z$ (equivalently $R|_{xR} \subseteq S_x$)
		- 4. & 5. imply that $R$ is transitive
##### 5. Basic Interpretability Logic
- $\vdash A \Rightarrow \vdash \square A$ (L1)
- $\square (A \to B) \to (\square A \to \square B)$, (L2)
- $\square A \to \square \square A$, (L3)
- $\square (\square A \to A) \to \square A$, (L4)
- BIL is Prop. Modal Logic with L1-4 & J1-5
	- L3 is derived by L4 but also by J4-5
##### 6. Some Facts about BIL
- a Veltman Structure is upwards well-founded if $R$ is [upwards well-founded](https://en.wikipedia.org/wiki/Well-founded_relation).
- if a Veltman Structure is upwards well-founded, then BIL is valid.
- $BIL \vdash A \Leftrightarrow$ for all (finite) upwards well-founded Veltman Models $W$ and all $k$ of $W$, $k \Vdash A$ (Completeness Theorem, De Jongh, Veltman)
##### 7. Some Derivations in BIL
- $A \equiv B := A \triangleright B \land B \triangleright A$
- $\square^+A := A \land \square A$
- $\vdash \square^+ (C \leftrightarrow D) \to (AC \leftrightarrow AD)$, (K3)
	- ==what is AC?==
	- derived from J1, J2
- $\vdash A \equiv (A \lor \lozenge A)$, (K4)
	- derived from J1, J3, J5
- $\phi A:= A \lor \lozenge A$
- $\psi A := A \land \square \lnot A$
- (K5) is made from
	1. $\vdash \phi A \leftrightarrow \phi \phi A$
	2. $\vdash A \leftrightarrow \phi \psi A$
	3.  $\vdash \psi A \leftrightarrow \psi \psi A$
	4.  $\vdash \psi A \leftrightarrow \psi \phi A$
- $\vdash A \triangleright (A \land \square \lnot A)$, (K6)
	- it is an alternative for J5.
- $\vdash A \equiv (A \land \square \lnot A)$, (K7)
- $\vdash A \triangleright \bot \to \square \lnot A$, (K8)
	- derived from J4
- $\vdash \lozenge A \to \lnot (A \triangleright \lozenge A)$, (K9, Feferman Principle)
	- this is *not derivable* in BIL
- $\vdash \lozenge A \triangleright \lnot (A \triangleright \lozenge A)$, (K10)
	- is a weakening of K9 that is derivable in BIL