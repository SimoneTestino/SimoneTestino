I followed this course by, Prof. Benno van den Berg during my [[5th Semester]] at the [[ILLC Amsterdam]] for my [[M.Sc. Logic (UvA)]]. A full description of the course can be found in the MasterMath website at [link](https://elo.mastermath.nl/course/view.php?id=1031). I also collect other works I do in [[Category Theory]].
#### Assignments
- [Overleaf: CatTh, 1](https://www.overleaf.com/read/mxzfynhjhmcv#6beb48)
- [Overleaf: CatTh, 2](https://www.overleaf.com/read/nfqswxwwbxyq#c8c101)
- [Overleaf: CatTh, 3](https://www.overleaf.com/read/xnntfcybtrrd#f4a180)

I use [https://q.uiver.app](https://q.uiver.app/) to draw the diagrams.
## Lecture Notes
#### Category
- A cath. $\mathcal{C}$ is a tuple of:
	1. $\mathcal{C}_0$ collection of _objects_ of $\mathcal{C}$
	2. $\mathcal{C}_1$ of _morphisms/arrows_ in $\mathcal{C}$
		- hence, for $f \in Mor(\mathcal{C})$, then $dom(f), cod(f) \in Ob(\mathcal{C})$
		- $f: A \to B := f \in Mor(\mathcal{C}) \land dom(f) = A \in Ob(\mathcal{C}) \land cod(f) = B \in OB(\mathcal{C})$
	- hence, $\mathcal{C}$ is a directed-multi-graph
	3. s.t. $\forall_{A \in Ob(\mathcal{C})} \exists_{1_A \in Mor(\mathcal{C})} 1_A: A \to A$
	4. if $\exists_{f: A \to B} \exists_{g: B \to C} \top \to \exists_{g \circ f: A \to C} \top$
		1. s.t. $f \circ 1_A = f = 1_B \circ f$ and $h \circ (g \circ f) = (h \circ g ) \circ f$ 
- for $\mathcal{C}_1 \ni f: A \to B$
	1. $f$ epi if $\forall_{C \in \mathcal{C}_0}\forall_{\mathcal{C}_1 \ni g, h: B \to C} gf = hf \to g = h$
	2. $f$ mono if $\forall_{C \in \mathcal{C}_0}\forall_{\mathcal{C}_1 \ni g, h: C \to B} fg= fh \to g = h$
- A category is uniquely defined by:
	1. $Ob(C)$ a class
	2. $Mor(\mathcal{C})$ a class of the form $\{(A_1, B_1), ...\}$ for $A_i \in Ob(\mathcal{C})$
	4. $\circ: Mor(\mathcal{C}) \times Mor(\mathcal{C}) \to Mor(\mathcal{C})$
		- by ex.1 specifying what is the identity of each object, is not necessary, since they're unique
- $\mathcal{C}$ is loc.small if $ZFC \models \forall_{A, B \in Ob(\mathcal{C})}\exists_{x} x = Mor(A, B)$
- $\mathcal{C}$ is small if $Ob(\mathcal{C})$ and $Mor(\mathcal{C})$ are sets.
- a _Monoid_ is a one-obj. loc.small category
- a small category without parallel arrows is a preorder
	- write $A \le B$ if $\exists_{f: A \to B} \top$.
	- by def. of cat. given above, "$\le$" is trans. and refl.
- for $\mathcal{C}$ cat., $f: A \to B$ is iso. if ex. $g: B \to A$ s.t. $g \circ f = 1_A \land f \circ g = 1_B$
	- $g$ is unique and called the _inverse_ of $f$
- $Hom_{\mathcal{C}}(A, B)$ all arrows from $A$ to $B$, (homset)
-  $f : A \to B$ is split.epi if ex $g: B \to A$ s.t. $fg = 1_B$ 
	- ($g$ is called a section of $f$, and $f$ a retraction of $g$)
- for $P \in \mathcal{C}_0$, $P$ proj., if $\forall_{X, Y \in \mathcal{C}_0}\forall_{\mathcal{C}_1 \ni f: P \to X, g: Y \to X} \text{epi.}(g) \to \exists_{\mathcal{C}_1 \ni h: P \to X} g\circ h = f$
#### Functor
- A functor $F$, is $F_0: \mathcal{C}_0 \to \mathcal{D}_0$ and $F_1: \mathcal{C}_1 \to \mathcal{D}_1$ s.t.:
	1. $\forall_{f: X \to Y} F_1(f) : F_0(X) \to F_0(Y)$
	2. $\forall_{f, g \in \mathcal{C}_1}((X \to^f Y \to^g Z) \to F_1(gf) = F_1(g) F_1(f))$
	3. $\forall_{X \in \mathcal{C}_0}F_1(1_X) = 1_{F_0(X)}$
- Functors preserve isomorphisms, 2.3
- A Functor preserves a property $P$ if $\forall_{x \in \mathcal{C}_0 \cup \mathcal{C}_1} P(F(x)) \to P(x)$, 2.4
- for $F$ let $\forall_{A, B \in \mathcal{C}_0} F_{A, B}: \mathcal{C}(A, B) \to \mathcal{D}(F(A), F(B))$:
	1. if surj. $F$ is full
	2. if inj. $F$ if faithful
		- if $F$ faithful, then $F$ reflects epsi and monos. 2.6
	3. if bij. $F$ is fully faithful
- _Product Category_: $\mathcal{C} \times \mathcal{D}$
	1. $Ob(\mathcal{C} \times \mathcal{D}) := \{(C_0, D_0): C_0 \in Ob(\mathcal{C}) \land D_0 \in \mathcal{D}\}$
	2. $Hom_{\mathcal{C}\times \mathcal{D}}((C_0, D_0),(C_1, D_1)) := Hom_\mathcal{C}(C_0, C_1) \times Hom_\mathcal{D}(D_0, D_1))$ 
	3. $(g_0, g_1) \circ (f_0, f_1) := (g_0 \circ f_0, g_1 \circ f_1)$ 
- _Opposite Category:_ $\mathcal{C}^{op}$
	1. $Ob(\mathcal{C}^{op}) := Ob(\mathcal{C})$
	2. $Hom_{\mathcal{C}^{op}}(A, B) := Hom_{\mathcal{C}}(B, A)$ 
	3. $g \circ_{\mathcal{C}^{op}} f := f \circ_{\mathcal{C}} g$ 
- Duality principle: of any definition, I can always find a dual (co-)
	- initial / terminal object
		- Terminal objects are unique up to unique isomorphism
	- $f: A \to B$ is a mono iff. $fg = fh \to g = h$
		- mono are "often" inj.func
			- proved for $\textbf{Set}$
			- in $\textbf{Cat}$: $F$ mono iff. $F$ inj.on.obj. and faithful, ex.1
	- $f: A \to B$ is epi iff. $gf = hf \to g = h$
		- epi are "often" surj.func
			- proved for $\textbf{Set}$
			- in $\textbf{Cat}$: $F$ surj.onobj. and full $\Rightarrow$ $F$ full., ex.1
- **Functorial Structures**
	- Example: $R$ a ring, $M_2(R)$ the $2 \times 2$ matrixes with components in $R$,
		- is $M_2: \textbf{Ring} \to \textbf{Ring}$, $f: R \to S$, $M_2(f) : M_2(R) \to M_2(S), M_s(f) \left(\begin{smallmatrix} a,\; b\\ c, \; d \end{smallmatrix}\right) =  \left(\begin{smallmatrix} f(a), f(b)\\ f(c), f(d) \end{smallmatrix}\right)$ 
	- $F: \mathcal{C} \to \mathcal{D}$, if $\alpha \in \mathcal{C}_1$ iso, then $F(\alpha)$ iso.
#### Natural Transformation
- for $\mathcal{C}, \mathcal{D}$ ex. $[\mathcal{C}, \mathcal{D}]$ cat. s.t. $[\mathcal{C}, \mathcal{D}]_0 = Hom_{\textbf{Cat}}(\mathcal{C}, \mathcal{D})$, $[\mathcal{C}, \mathcal{D}]_1$ are _natural transformations_
	- for $F, G: \mathcal{C} \to \mathcal{D}$ a nat.tr. $\sigma : F \Rightarrow G$ is a fam. of morph. $\forall_{C \in \mathcal{C}_0}\sigma_C : F(C) \to G(C)$ s.t.
		1. for $\forall_{C, C' \in \mathcal{C}_0} \exists_{\alpha \in Hom_\mathcal{C}(C, C')} Diag.Comm.$, (Naturality Condition)
			1. $Diag$: $F(C) \to^{F(\alpha)}FC' \to^{\sigma_{C'}} G(C')$ and $F(C) \to^{\sigma_C} G(C) \to^{G(\alpha)} G(C')$ 
	- if $\sigma: F \Rightarrow G$ in $[\mathcal{C}, \mathcal{D}]$ is iso. iff $\forall_{C \in \mathcal{C}_0} iso.(\sigma_C)$ 
	- $\circ: [\mathcal{D}, \mathcal{E}] \times [\mathcal{C}, \mathcal{D}] \to [\mathcal{C}, \mathcal{E}]$, functor composition is the object part of a functor (see diag), 3.3
#### Equivalence of Categories
- $\mathcal{C} \simeq \mathcal{D}$ if there are functors $F: \mathcal{C} \to \mathcal{D}$, $G: \mathcal{C} \to \mathcal{D}$ s.t.
	1. $G \circ F \cong 1_\mathcal{C} \in [\mathcal{C}, \mathcal{C}]_0$
	2. $F \circ G \cong 1_\mathcal{D} \in [\mathcal{D}, \mathcal{D}]_0$ 
	- it is called _equivalence_ and $G$ is the _pseudo-inverse_
	- also $\cong$ is natural isomorphism of categories
- Equivalence _preserves_ and _reflects_ terminal objects (and most other properties)
- $F: \mathcal{C} \to \mathcal{D}$ is an equivalence iff:, 3.6
	1. $F$ is essentially surjective and...
		- that is: $\forall_{D \in \mathcal{D}_0} \exists_{C \in \mathcal{C}_0} F_0(C) \cong D$
	2. ... $F$ is fully faithful
		- $F$ is full and faithful
- $\mathcal{C}, \mathcal{D}, \mathcal{E}$ sm.cat., $\mathcal{D} \simeq \mathcal{E} \to [\mathcal{C}, \mathcal{D}] \simeq [\mathcal{C}, \mathcal{E}]$, ex.2.2
#### Limits
- for $F: \mathcal{C} \to \mathcal{D}$ , a _cone_ is $(D, \mu)$ s.t.  $D \in \mathcal{D}_0$, nat.tr. $\mu: \Delta_D \Rightarrow F$ (cone), s.t.
	1. $(\mu_C: D \to F(C): C \in \mathcal{C}_0)$ with nat.req.,  4.1
	- $\Delta_D : \mathcal{C}\ \to \mathcal{D}$, if $\forall_{C \in \mathcal{C}_0} (\Delta_D)_0(C) = D$ and $\forall_{f \in \mathcal{C}_1}(\Delta_D)_0 = 1_D$ 
	- for $D \in \mathcal{D}_0$, $\Delta_g: \Delta_D \to \Delta_{D'}$ s.t. $(\Delta_g)_C = g$
		- hence $\Delta: \mathcal{D} \to [\mathcal{C}, \mathcal{D}]$
-  $(D, \mu) \to (D', \mu')$, is a map $g: D \to D'$ s.t. $\mu' \circ \Delta_g = \mu$ (map of cones), 4.1
- a lim.cone for $F$ is term.obj of $Cone(F)$ (limiting cone). 4.2
- a lim.con for $!: \textbf{0} \to \mathcal{D}$ is term.obj. in $\mathcal{D}$
	- $Cone(!) \cong \mathcal{D}$ 
- **Product Category** 4.1.2
	- let $F: \mathbf{2} \to \mathcal{D}$, a product is the vertex of the limiting cone, called $(A \times B, \pi)$.
	- $\mathbf{2}$ only has elements $A, B$ and only reflexive arrows.
- **Equalizer** 4.1.3
	- for $F: \mathbf{\hat{2}} \to \mathcal{D}$ let $(D, \mu)$ be a cone, if it is limiting $\mu_A$ is an equalizer.
		- $D \to^{\mu_A} A \to^{f, g} B$.
	- $\mathbf{\hat{2}}$ is $A \to^{f, g} b$
- **Pullbacks**: 4.1.4
	- for $F: J \to \mathcal{D}$, a let $(W, p)$ be the lim.cone, its diagram is the pullback diagram
	- $J$ has $x, y, z$ as objects and arrows $y \to^b z$ and $x \to^a z$.
- $\mathcal{C}$ has lim.of.sh. $\mathcal{I}$ if $\forall_{F: \mathcal{I} \to \mathcal{C}} \exists_{(D,\mu \in Cone(F))} \text{lim.cone.}(D, \mu)$, 4.3
- if $\mathcal{C}$ is s.t. $\forall_{\text{sm.cat}(\mathcal{I})} \mathcal{C} \text{ lim.of.sh}(\mathcal{I})$ it is said _complete_.
	- if only on all $\mathcal{I}$ s.t. $|\mathcal{I}_0| < \aleph_0$ it is fin.compl.
		- fin.compl.cat are also called _lex_, _left exact_ or _cartesian_.
	- $\mathcal{C}$ has ...
		- prod. if complete on all $F: \mathbf{2} \to \mathcal{C}$
		- equal. if complete on all $F: \mathbf{\hat{2}} \to \mathcal{C}$
		- pullb. if complete on all $F: J \to \mathcal{C}$
	- for $M: \mathcal{I} \to \mathcal{C}$, and $(C, \mu)_M$ lim.cone, say it _preserved_ by $F: \mathcal{C} \to \mathcal{D}$ if $(F(C), F\mu)$ lim.con, 4.4
		- $F\mu := \{F(\mu_I): I \in \mathcal{I}_0\}$ 
		- $F$ pres.lim.of.shape.$\mathcal{I}$ if it preserves every lim.cone of $G: \mathcal{I} \to \mathcal{C}$
			- it preserves small/finite limits if it preserves limits of shape $\mathcal{I}$ for each $\mathcal{I}$ small/finite.
- _complete categories_:
	- sets, top, grps, ring, ab.gr, vs. over a fixed field, cat. (fields are not!)
- **Colimits** 4.2
- a colimiting cocone for $F$ is a limiting cone for $F^{op}$.
	- $(\nu, D)_F$ s.t. $\nu: F \Rightarrow \Delta_D$ init.obj. in $Cocone(F)$.
	- a colimiting cocone for $F: \mathbf{2} \to \mathcal{C}$, denoted $A + B$ or $A \sqcup B$
	- $\mathcal{C}$ is cocomplete if all $\mathcal{I}$ small have colimits of for diagrams $\mathcal{I} \to C$.
- coprod. of proj. is proj., ex.3.1.b
#### Complete Categories
- if $\mathcal{C}$ has small products and equalizers, then $\mathcal{C}$ is complete, 5.1
	- also for $< k$ for $k$ a cardinal
	- also co- version
- if $\mathcal{C}$ has term.obj and pullb. it has binary prod. and equal, 5.3
- tfae: 5.4
	- $\mathcal{C}$ fin.compl.
	- $\mathcal{C}$ has fin.prod. and equil.
	- $\mathcal{C}$ has pullb. and a term.obj.
- $\mathcal{D}$ has lim.of.sh.$\mathcal{I}$, then so does any $[\mathcal{C}, \mathcal{D}]$, 5.5
	- $\forall_{\mathcal{C}}\text{compl.}(\mathcal{D})\to\text{compl.}([\mathcal{C}, \mathcal{D}])$ 
- for $F: \mathcal{C} \to \mathcal{D}$ an equiv. and $\mathcal{I}$ a cat., $F$ preserves and reflects limits of $\mathcal{I}$, 5.6
- if $\mathcal{D}$ complete has lim.of.sh.$\mathcal{I}$, does $\mathcal{C}$
	- $\text{compl.}(\mathcal{D}) \land \text{equiv.}(F: \mathcal{C} \to \mathcal{D}) \to \text{compl.}(\mathcal{C}$
- if $\text{small.}(\mathcal{C}) \land \text{compl.}(\mathcal{C})$, then $\mathcal{C}$ is a preorder
#### Cartesian Closed Categories
- in $\mathbf{Set}$, for $\mathcal{C}_1 \ni f: X \to Y$ mono:
	- $X, Y \in \mathcal{C}_0$ are iso. if $\exists_{f, g \in \mathcal{C}_1} f: X \to Y \land g: Y \to X \land \text{mono.}(f) \land \text{mono.}(g)$
	- for $f: X \to Y$, there is a coproduct diagram with $f$ and $g: Z \to Y$
	- given the AC, every epi is split.
- **Exponentials**: for $\mathcal{C}$ and $X, Y \in \mathcal{C}_0$, $X \times Y$ and $1_X$ are ==distinguished==
	- $X^Y \in \mathcal{C}_0$, $\mathcal{C}_1 \ni ev: X^Y \times Y \to X$ s.t. $\forall_{A \in \mathcal{C}_0} \forall_{\mathcal{C}_1 \ni h: A \times Y \to X} \exists!_{ \mathcal{C}_1 \ni H : A \to X^Y} ev \circ (H \times 1_Y) = h$, 6.1
		- equivalently $\text{Hom}_\mathcal{C}(A, X^Y) \to \text{Hom}_\mathcal{C}(A \times Y , X) : H \mapsto ev \circ( H \times 1_y)$ is a bij.
	- $\mathcal{C}$ is _ccc_ if it has fin.prod. and every $X^Y$ exists.
	- in $\mathbf{Cat}$ _ccc_ holds with $\mathcal{D}^\mathcal{C} := [\mathcal{C}, \mathcal{D}]$, $ev_0(F, C) = F(C)$, $ev_1(\sigma, f) = \sigma_C(f)$
		- (note, nat.tr. are precisely such $\sigma$)
	- for $\mathcal{C}$ with fin.prod., is called _exponentiable_ if all exponentials exists
	- 6.6?
- **Natural Numbers Object**
	- in $\mathcal{C}$ with term.obj. $1$, a nat.num.obj. is $(0, N, S) \in \mathcal{C}_1 \times \mathcal{C}_0 \times \mathcal{C}_1$ s.t.:
		1. $1 \to^0 N$, $N \to^S N$ 
		2. $\forall_{1 \to^x X \to^f X} \exists!_{\varphi: N \to X}\text{diag.comm.}$
	- in $\mathcal{C}$ with _ccc_ and nat.num.obj. $(0, N, S)$ call $f: N^k \to N$ a num.th.fun. corresponding to $F: \mathbb{N}^k \to \mathbb{N}$ if $\forall_{(n_1, ..., n_k) \in \mathbb{N}^k}f \circ \langle S^{n_1}, ..., S^{n_k} \rangle = S^{F(n_1, ..., n_k)}$ 
		- PA can be done within this frame
#### Presheaves
- for $\mathcal{C}$ sm.cat., the presh.$\mathcal{C}$ is $\hat{\mathcal{C}}:=[\mathcal{C}^{op}, \mathbf{Set}]$, 7.1
	- $\hat{\mathcal{C}}$ is complete and cocomplete, limits calculated pointwise
	- for $\mathcal{D}$ with pullb., $\sigma \in [\mathcal{C}, \mathcal{D}]_0$ is mono iff $\forall_{C \in \mathcal{C}_0} \text{mono.}(\sigma_C)$, 7.3
		- for $\mathcal{D}$ with pusho., $\sigma \in [\mathcal{C}, \mathcal{D}]_0$ is epi iff $\forall_{C \in \mathcal{C}_0}\text{epi.}(\sigma_C)$

- **Yoneda Lemma**: 7.2
	- for $\mathcal{C}$ loc.sm.cat, $\text{Hom}_\mathcal{C}: \mathcal{C}^{op} \times \mathcal{C} \to \mathbf{Set}$, hence $\text{Hom}_\mathcal{C}(A, B) \in \mathbf{Set}$
	- also, for $(\mathcal{C}^{op} \times \mathcal{C})_1 \ni (f, g): (A, B) \to (A', B')$, $\text{Hom}_\mathcal{C}(A, B) \to \text{Hom}_\mathcal{C}(A', B')$ s.t. $(h: A \to B) \mapsto g \circ h \circ f: A' \to B'$.
	- since $\mathbf{Set}^{\mathcal{C}^{op}}$ is an exp.cat., $\text{Hom}_\mathcal{C}$ corresponds to $y: \mathcal{C} \to \mathbf{Set}^{\mathcal{C}^{op}}$
		- since $y: \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$, first take $C \in \mathcal{C}$, then $D \in \mathcal{C}^{op}$.
		- so, for $C \in \mathcal{C}_0$, we have $(y_C)(D) := (y(C))(D) = \text{Hom}_\mathcal{C}(D, C)$
		- and, for $\mathcal{C}_1 \ni f: D \to D'$, get $(y_C)(D') \to (y_C)(D)$, comp.w. $f$
		- and, for $\mathcal{C}_1 \ni g: C \to C'$, get $\mathcal{C}_2 \ni y_g: y_C \to y_{C'}$ s.t. $(y_g)_D: (y_C)(D) \to (y_{C'})(D)$, com.w. $g$
	- $\forall_{F \in [\mathcal{C}^{op}, \mathbf{Set}]_0}\forall_{C \in \mathcal{C}_0} \text{bij.}(\alpha_{C, F}: \mathbf{Set}^{\mathcal{C}^{op}}(y_C, F) \to F(C))$, $(\sigma: y_C\to F) \to (\sigma_C)(1_C)$ s.t. (Yoneda)
		1. for $\mathcal{C}_1 \ni g: C' \to C$, $\mathbf{Set}^{\mathcal{C}^{op}} \ni \mu F \Rightarrow F$, diag.com. [[Yoneda_Naturality.jpeg]] (Naturality)
		2. $\mathcal{C}(C, C'):= \{f \in \mathcal{C}_1: f: C \to C'\}$, 7.4
		- hence, $\alpha$ os a nat.iso. s.t. $(\mathcal{C}^{op} \times \mathbf{Set}^{\mathcal{C}^{op}} \to^{ev} \mathbf{Set}) \cong^\alpha \mathcal{C}^{op} \times \mathbf{Set}^{\mathcal{C}^{op}} \to^{y \times 1}(\mathbf{Set}^{\mathcal{C}^{op}})^{op} \times \mathbf{Set}^{\mathcal{C}^{op}} \to^{\text{Hom}} \mathbf{Set}$
		- $X \in \hat{\mathcal{C}}$ is repr. if $\exists_{C \in \mathcal{C}} X \cong y_C$, 7.5
		- for $X \in \hat{\mathcal{C}}$, $y \downarrow X$ is a comm.cat. if
			- $(y \downarrow X)_0 := \{(C, \mu): C \in \mathcal{C}_0 \land \hat{\mathcal{C}}_1 \ni \mu: y_C \to X\}$
			- $(y \downarrow X)_1 := \{(C,\mu) \to (C', \nu) |f: c \to C' \land \nu \circ y_f = \mu\}$
		- $U_X: y\downarrow X\to\mathcal{C}, (C, \mu) \mapsto C, f \mapsto f$
		- $y\circ U_X: y \downarrow X \to \mathbf{Set}^{\mathcal{C}^{op}}$, recall $\Delta_X: y \downarrow X \to \hat{\mathcal{C}}$ 
		- $\rho_X: y \circ U_X \to \Delta_X$
		- $(X, \rho_X)$ is colimiting cocone in $\hat{\mathcal{C}}$, 7.6
			- _every presheaf is a colimit of representables_
		- $\hat{F}:=F \circ U_X$, so $\hat{F}: y \downarrow X \to \mathcal{D}$ 
		- $y$ is inj. and fully faithful, 7.7
	- $\hat{\mathcal{C}}$ is _ccc_
		- as an example of limit, take the exponentials
			- for $C \in \mathcal{C}_0$, $Y^X(C) := \hat{\mathcal{C}}(y_C \times X, Y)$
			- for $\mathcal{C}_1 \ni f: C \to C'$, $Y^X(f): Y^X(C) \to Y^ X(C')$ ==?==
	- $\forall_{X \in \hat{\mathcal{C}}_0} \exists_{C \in \mathcal{C}_0} X \cong y_C \to \text{proj.}(X)$, ex.3.1.c
	- a presh is proj. iff it is a retract of a copr. of repres.
#### Presheaves as a Topos
- a _topos_ is a ccc.w.fin.lim with a subobject classifier
- for $\mathcal{E}$ cat.fin.lim. a subo.cl. is a $t: T \to \Omega$ s.t.:
	1. $t$ is mono
	2. $\forall_{m \in \mathcal{E}_1} \text{mono.}(m) \to \exists!_{\mathcal{E} \ni \phi: B \to \Omega} t \circ \psi = \phi \circ m$
		- $\phi$ is _classifies_ $m$, or the subobject represented by $m$
		- since $t$ is mono, there is a unique such $\psi$ too.
	- hence, $T$ is terminal, 8.3
	- call $t: T \to \Omega$ subo.cl. or also just $\Omega$
- for $X \in \mathcal{E}_0$, def. $\{\mathcal{E}_1 \ni f: A \to X | A \in \mathcal{E}_0 \land \text{mono.}(f)\}$ and order
	1. $(m: A \to X) \le (n: B \to X):= \exists_{\mathcal{E}_1 \ni k: A \to B}n \circ k = m$
		- $k$ is then unique and mono, 8.4
	- for $k$ iso, we get eq.classes which we call subo., write $\text{Sub}_\mathcal{E}(X)$
		- if $\text{Sub}_\mathcal{E}(X)$ is a set, call $\mathcal{E}$ _well-powered_, this we assume for $\mathcal{E}$.
	- in $\mathbf{Set}$, if $m: A \to X$ inj., $A \cong Im(m) \subseteq X$
	- for $\mathcal{E}_1 \ni f: Y \to X$, $f^*: \text{Sub}_\mathcal{E}(X) \to \text{Sub}_\mathcal{E}(Y)$ 
		- $f^* \in \mathbf{Cat}_1$ and monotone
		- if $\mathcal{E}$ small, $\text{Sub}_\mathcal{E}: \mathcal{E}^{op} \to \mathbf{Set}$
		- having a subo.cl. is eq. to saying that $\text{Sub}_\mathcal{E}$ is repr.
		- hence, $\text{Sub}(-): \mathcal{E}^{op} \to \mathbf{Set}, A \mapsto \text{Sub}(A), f \mapsto f^*$ lec.10.1.5:36
		- $\mathcal{E}$ has subo.cl. if $\text{Sub}(-)$ is representable lec.10.1.6:19
			- ex. $\Omega \in \mathcal{E}_0$ s.t. $\mathcal{E}(-, \Omega) \cong \text{Sub}_\mathcal{E}(-)$ nat.iso.
- for $A \in \mathcal{E}_0$, $A$ is pow.obj. of $X \in \mathcal{E}_0$ if $\mathcal{E}(Y, A) \cong \text{Sub}_\mathcal{E}(X \times Y)$ s.t.
	1. $\mathcal{E}_1 \ni f: Y \to A, g: Z \to Y$ and $f$ corr. to the subo. $U$ of $X \times Y$, then $fg: Z \to A$ corr. to the subo. $(id_X \times g)^*(U)$ of $X \times Z$.
		- correspondence is given by the subo.cl., 
	- note $\mathcal{E}(Y, A), \text{Sub}_\mathcal{E}(X \times Y) \in \mathbf{Set}_0$, hence "$\cong$" only requires a bij.
	- pow.obj. are unique up to iso., usually denoted with $\mathcal{P}(X)$
- **Subobject Classifiers in Presheaves**
- if $X \in \hat{\mathcal{C}}_0$, a subpresh $Y$ of $X$ is s.t.:
	1. $\forall_{C \in \mathcal{C}_0} Y(C) \subseteq X(C)$
	2. $\forall_{f \in \mathcal{C}_1} Y(f) = X(f)|_{Y(cod(f))}$
	- let $\text{SubPSh}_\mathcal{C}(X)$ be the set of all supresh. on $\mathcal{C}$ of $X$
- $\text{Sub}_\mathcal{C} (X) \cong \text{SubPSh}_\mathcal{C}(X)$
- let $\Omega$ s.t. $\Omega(C) \in \text{SubPSh}_{\hat{\mathcal{C}}}(y_C)$, $\Omega(f)$ is defined by pulling back along $y_f$
	- if $R$ is a _sieve_ on $C$, then $R \ni f: C' \to C \to \forall_{g: C'' \to C'} fg = y_C(g)(f) \in R$
	- $R\leftrightsquigarrow \Omega(C) \in \text{SubPSh}_{\hat{\mathcal{C}}}(y_C)$
	- for $R\ni f: C' \to C$, $f^*(R) = \{g: D \to C' | fg \in R_C\}$
	- hence $\Omega = \{R : \text{sieve.on.}C(R) \}$, $\Omega(f)(R) = f^*(R)$
	- $t: 1 \to \Omega, 1(C) \mapsto \text{max.sieve.on.}C$
		- $\text{max.sieve.on.}C$ is the unique one containing $id_C$
- for $\mathcal{E}$ a topos, we have $\text{Hom}_{\mathcal{E}}(Y, \Omega^X) \cong \text{Hom}_\mathcal{E}(X \times Y, \Omega) \cong \text{Sub}_\mathcal{E}(C, \times Y)$ natuarally in $\mathcal{E}$.
#### Adjunctions
- $\mathbf{Cat}_1 \ni F: \mathcal{C} \to \mathcal{D}, G: \mathcal{D} \to \mathcal{C}$, an adj. is a nat.bij $m$ or $F \dashv G$ s.t.:
	1. $\forall_{C \in \mathcal{C}_0}\forall_{D \in \mathcal{D}_0} m_{C, D} :\mathcal{D}(FC, D) \to \mathcal{C}(C, GD)$
		- hence maps $\mathcal{C}_1 \ni f: FD \to C$, $\mathcal{D}_1 \ni g: D \to GC$ are called _transposes_ of each others
		- write $\overline{f} := m(f) = g$, note $\overline{\overline{f}} = \overline{g} = f$.
	2. $\forall_{\mathcal{C}_1 \ni f : C \to C'}\forall_{\mathcal{D}_1 \ni g: D \to D'}\forall_{\mathcal{D}_1 \ni \alpha:FC \to D} Gg \circ \overline{\alpha} \circ f = \overline{g \circ \alpha \circ F f}$ (Naturality)
		- this is eq. to $f =1$, $g = 1$ s.t. $Gg \circ \overline{\alpha} = \overline{g \circ \alpha}$ and $\overline{\alpha} \circ f = \overline{\alpha \circ F f}$.
- for adj. as above, fix $D \in \mathcal{C}_0$, by nat. $\mathcal{C}^{op} \to \mathbf{Set}: C \mapsto \mathcal{D}(FC, D)$ is repr. by $GD$.
	- by Yon. $\mathcal{D}_1 \ni \varepsilon_D = m^{-1}_{GD, D}: FGD \to D$, s.t. $m^{-1}_{C, D}(\beta) = \varepsilon_D \circ F \beta$
	- dually: for $C \in \mathcal{C}_0$, $\eta_C = m_{C, FC}(1_{FC}: C \to GFC)$ s.t. $m_{C, D}(\alpha) = G\alpha \circ \eta_C$ 
- $\{\eta_C: C \in \mathcal{C}_0\} \rightsquigarrow (1_C \Rightarrow GF)$ and $\{\varepsilon_D : D \in \mathcal{D}_0\} \rightsquigarrow (FG \Rightarrow 1_D)$, 9.2
	- call $\eta$ the unit and $\varepsilon$ the 
	- if $m_{C,D}$ is inv. of $m_{C, D}^{-1}$ iff $G \Rightarrow^{\eta \star G} GFG \Rightarrow^{G \circ \varepsilon} G = 1_G$ and $F \Rightarrow^{F \circ \eta} FGF \Rightarrow^{\varepsilon \star F} F = 1_F$ 
		- $\eta \star G := \{\eta_{GD} | D \in \mathcal{D}_0\}$ and $G \circ \varepsilon := \{G(\varepsilon_D) | D \in \mathcal{D}_0\}$ 
- for $\mathbf{Cat}_1 \ni F: \mathcal{C} \to \mathcal{D}, G: \mathcal{D} \to \mathcal{C}$, $\eta: 1_\mathcal{C} \Rightarrow GF$ and $\varepsilon: FG \Rightarrow 1_\mathcal{D}$ s.t. 
	1. $(G \circ \varepsilon) \cdot (\eta \star G) = 1_G$
	2. $(\varepsilon \star F) \cdot ( F \circ \eta) = 1_F$ 
	- then: $F \dashv G$ with $\eta$ unit and $\varepsilon$ counit, 9.3
- $F: \mathcal{C} \to \mathcal{D}$ eq.cat. with $G$ ps.inv, for $\mu: 1_\mathcal{C} \Rightarrow GF$, $\nu: FG \Rightarrow 1_\mathcal{D}$, then $F \dashv G$ with unit $\mu$ and one with counit $\nu$ (not nec. at the same time), 9.4
- if $F \dashv G$ then $F$ pres.colim., $G$ pres.lim.
	- $F$ pres. init.obj.
	- if $F$ has right.adj., let $M: \mathcal{E} \to \mathcal{C}$, then $\hat{F}: \text{Cocone}(M) \to \text{Cocone}(FM)$ has right.adj. too, 9.7
#### Monads and Algebras
- for $F: \mathcal{C} \to \mathcal{D}$ and $F \dashv G$, let $T = GF: \mathcal{C} \to \mathcal{C}$, 
	1. note nat.tr. $\eta: 1_\mathcal{C} \Rightarrow T$ 
	2. also $\mu: T^2 \Rightarrow T$, for $\mu_C = T^2(C) = GFGFC \to^{G_{(\varepsilon_{FC})}} GFC = T(C)$ 
	3. see diag. 10.1
- for $\mathcal{C}$ cat, a monad is $(T, \eta, \mu)$ s.t.:
	1. $T: \mathcal{C} \to \mathcal{C}$
	2. $\eta: 1_\mathcal{C} \Rightarrow T$ nat.tr.
	3. $\mu: T^2 \Rightarrow T$
	4. and s.t. 10.1 holds
	- note that it is in fact a monoid ==?==
- for $(T, \eta, \mu)$ on a cat. $\mathcal{C}$, the cat. $T$-Alg is:
	1. $(\mathbf{Alg}_{\mathcal{C}, T})_0:= \{(X, h) | X \in \mathcal{C}_0 \land \mathcal{C}_1 \ni h: (T(C) \to X \land T^2(C) \to^{T(h)}$ $T(X) \to^h X = T^2(X) \to^{\mu_X} T(X) \to^h X \land X \to^{\eta_X} T(X) \to^h X = 1_X\}$
	2. $(\mathbf{Alg}_{\mathcal{C}, T})_1 := \{(X, h) \to (Y, k) | f: X \to Y \land f \circ h = k \circ T(f)\}$
- there is an adj. $F \dashv G$ between $\mathcal{C}$ and $\mathbf{Alg}_{\mathcal{C}, T}$ and it is ge. by $T = GF$., 10.4
- for $F: \mathcal{C} \to \mathcal{D}$ and $F \dashv G$, let $K: \mathcal{D} \to \mathbf{Alg}_{\mathcal{C}, T}$ s.t.
	1. $K_0(D) = (GFG(D) \to^{G(\varepsilon_D)} G(D))$ 
	2. $K_1(f: D \to D') = G_1(f)$
	-  nat. of $\varepsilon$ proves well-definability.
	- call $G:\mathcal{D} \to \mathcal{C}$ monadic (or that $\mathcal{D}$ over $\mathcal{C}$ is) if $K$ is an equiv.
#### Presheaves Revisited
- for $\mathcal{C}$ sm.cat, let $X \in \hat{\mathcal{C}}_0$ recall $\int_\mathcal{C} X:= y \downarrow X$, call it _category of elements_.
- $x: (y_C \to X) \leftrightsquigarrow x \in X(C)$, we can then think of $(C, x) \in (\int_\mathcal{C} X)_0$ with $x \in X(C)$ 
- for $U: y\downarrow X \to \mathcal{C}$ forg.fun., def. $y \circ U : y \downarrow X \to \text{Psh}(\mathcal{C})$
	- $(X, \rho)$ is a lim.cocone on $y \circ U$, 11.2
	- $\forall_{(C, x) \in (y \downarrow X)_0} \exists_{(y \downarrow X)_1 \ni yU(C, x)} yU(C, x) = y_C \to X = x$
	- _every presheaf is a colimit of representables_
- **Kan Extensions**
	- for $\mathcal{C}$ sm.cat., $y: \mathcal{C} \to \text{PSh}(\mathcal{C})$ is s.t. 
		1. $\forall_{\mathcal{E} \in \mathbf{Cat}_0}\text{loc.sm.cat}(\mathcal{E}) \land \text{cocom.}(\mathcal{E})\to \forall_{\mathbf{Cat}_1 \ni F: \mathcal{C} \to \mathcal{E}} \exists_{\mathbf{Cat}_1 \ni F_!: \text{PSh}(\mathcal{C}) \to \mathcal{E}} F_! \circ y \cong F$, 11.3
		- call $F_!$ the _left Kan extension_
	- for $f: \mathcal{C} \to \mathcal{D}$ for $\mathcal{C}, \mathcal{D}$ sm.cat., the prec.fun. $f^*: \hat{\mathcal{D}} \to \hat{\mathcal{C}}$, $f^*(Q)(C) = Q(fC)$, has both adj., 11.5