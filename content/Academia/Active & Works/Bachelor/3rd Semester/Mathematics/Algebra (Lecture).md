I collect here some of the notes of the lecture on Algebra I followed in the #3rd_Semester at the #LMU held by [A. Rosenschon](https://www.mathematik.uni-muenchen.de/~axr/).
## Recap
### Elementary Group Theory
Most of theorems of this section were present already in [[Linear Algebra II (Lecture)]]. 
- **Normal Divisor**
	- for $H \subseteq G$ subgr., $aH := \{ah : h \in H\}$, $Ha:= \{ha : h \in H\}$
		- $|aH| = |bH|$
		- $G =\bigsqcup_{a \in R \subseteq G} aH$
		- $aH = bH \Leftrightarrow aH \cap bH = \emptyset \Leftrightarrow a \in bH \Leftrightarrow b^{-1}a \in H$
	- $G/H := \{aH : a \in G\}$, $H \setminus G := \{Ha : a \in G\}$, $|G:H|:= |G/H|$, $|G/H| = H \setminus G$ 
	- $|G| = |G:H|\cdot |H|$ (Lagrange)
	- for $H \subseteq G$ subgr., $H \trianglelefteq G : \forall_{a \in G} aH = Ha$
	- Ways to prove $U \trianglelefteq G$:
		- for $\varphi: G \to G'$, $ker(\varphi)\trianglelefteq G$
		- $|G : H| = 2 \Rightarrow H \trianglelefteq G$, [link](https://math.stackexchange.com/questions/84632/subgroup-of-index-2-is-normal).
	- $G \to G, x \mapsto gxg^{-1}$ is a gr.autom.
- **Homomorphism and Isomorphism Theorems** 1.12 
	- for (i) $\varphi: G \to G'$ hom., (ii) $N \trianglelefteq G$ s.t. $N \subseteq ker(\varphi)$, (iii) $\pi: H \to G/N, a \mapsto aH$ then: 
		ex. uniq. $\overline{\varphi}: G/N \to G'$ s.t. $G \to^\pi G/N \to^\overline{\varphi} G'$, $G \to^\varphi G'$ [[groups_hom.png]] 
		- $\varphi$ surj, then $\overline{\varphi}: G / ker(\varphi) \to G'$ is isom.
	- $H \subseteq G$ subgr. $N \trianglelefteq G$, then (i) $HN \subseteq G$ subgr., (ii) $N \trianglelefteq HN$, (iii) $H \cap N \trianglelefteq H$, (iv) $H/H \cap N \cong HN/N$ (1st Isomorphism Theorem)
		- $HN := \{hn | h \in H \land n \in N\}$ 
	- for $N, H \trianglelefteq G$, $N \subseteq H \subseteq G$, then (i) $N \trianglelefteq H$, (ii) $H/N \trianglelefteq G/N$, (iii) $(G/N)(H/N)\cong G/H$ (2nd)
- ==Grothendieck==
- **Cyclical Groups**
	- ==...==
### Rings and Polynomials
Most of these theorems are present in [[Linear Algebra II (Lecture)]] already, though I list some of them here again:
- for $\varphi$ hom, $\varphi$ inj. $\Leftrightarrow \varphi$ surj. ==No, find the right version==
	- for $|R| < \aleph_0$ comm, $\forall_{a \in R} a | 0 \lor a \in R^\times$ (B.9.1.a)
- **Rings and Polynomial Rings in one Variable**
	- def. of Ring: for a group $(R, +)$ with $e = 0$ and a monoid $(R, \cdot)$ with $e = 1$ it holds $(a + b)c = ac + ab$ and $c(a + b) = ca + cb$. It is comm. if $ab = ba$.
		- if $0 = 1$, then $R = \{0\}$
	- $R^\times = \{a \in R | \exists_{b \in R} ab = ba = 1\}$, $(R^\times, \cdot_{R})$ is a group.
	- For $(R_i)_{i \in I}$ a family of rings, $\prod_{i \in I} R_i$ is ring with component-wise $+$ and $\cdot$.
	- $R[X] \simeq (R^{(\mathbb{N})}, +_{R^\omega}, \cdot_{R^\omega})$
		- $R^{(\mathbb{N})} = \{(a_i)_{i \in I} : \forall_{i \in I}a_i \in R \land |\{a_i \in (a_i)_{i \in I} : a_i \not = 0\}| < \aleph_0\}$ with $+$ and $\cdot$ from $R^\omega$. 2.2-2.3
	- $grad(f) = max\{i |: a_i \not = 0\}$
		- $grad(f + g) \le max\{grad(f), grad(g)\}$, $grad(fg) \le grad(f) + grad(g)$.
- **Ideal**
	- def. ideal $I \subset R$ s.t. $(I, +_R)$ subgroup of $(R, +)$ and $\forall_{r \in R} \forall_{i \in I}ra = ar \in I$
	- def. generator $(a_j)_{j \in J}$, if $I = \sum_{x \in X} Ra_i$, fin.gen. if $|(a_j)_{j \in J}| < \aleph_0$, principle if $(a)$.
	- 2.14: $p$ prime Ideal if $\forall_{a, b \in R} ab \in p \rightarrow (a \in p \lor b \in p)$, $m$ max. ideal if all ideals $I$, $\forall_{I \subset R} m \subseteq I \subseteq R \rightarrow (I = m \lor I = R)$. 
	- 2.15: $R$ comm., $I \subsetneq R$ prime iff $R/ I$ is ID. $I \subsetneq R$ max. ideal $\Leftrightarrow$ $R/m$ is a field.
		- for $I$ max., I prime. $p \mathbb{Z}$ max. $\Leftrightarrow$ $p$ prime.
- **Rings-homomorphisms and Factor-rings**
	- def hom. $\varphi: R \rightarrow S$ s.t. (i) $\varphi(a +_R b) = \varphi(a) +_S \varphi(b)$, (ii) $\varphi(ab) = \varphi(a)\varphi(b)$, (iii) $\varphi(1_R) = \varphi(1_S)$.
		- $ker(\varphi)$ is an ideal, $im(\varphi)$ is a subr., $\varphi$ determines a gr. hom. $R^\times \rightarrow S^\times$. $ker(\varphi) = \{0\} \Rightarrow \varphi$ inj.
	- ==Homomorphiesatz==
	- ==Chinese Restsatz==
- **Prime Factorisation**
	- def. let $\delta : R \setminus \{0\} \rightarrow \mathbb{N}$ s.t.  $a, b \in R$, $b \not = 0$ there is $q, r \in R$ s.t. $a = qb + r$ where $\delta(r) > \delta (g) \lor r = 0$, then $R$ is eucl. ring and $\delta$ a norm. 2.17
	- $R$ eucl $\Rightarrow R$ PID
	- $p \in R \setminus R^\times$  irr. if $\forall_{x, y \in R} p = xy \rightarrow x \in R^\times \lor y \in R^\times$
	- $p \in R \setminus R^\times$ prime if $\forall_{x, y \in R} p|xy \rightarrow p|x \lor p|y$
	- (i) $(p)$ max. $\Rightarrow p$ prime, (ii) $p$ prime $\Rightarrow p$ irr. (iii) $R$ PID: $p$ irr. $\Leftrightarrow p$ prime $\Leftrightarrow (p)$ max. 2.20
	- $R$ PID, $0 \not = a \in R \setminus R^\times$, then $a = p_1 \cdot p_2 \cdot ... \cdot p_n$. unique up to order and mult. with units. 2.22
	- def Fact. Ring: $\forall_{0 \not = a \in R \setminus R^\times}$ if (i) $a = p_1 \cdot p_2 \cdot ... \cdot p_n$ **or** (ii) $a = i_1 \cdot i_2 \cdot ... \cdot i_m$ irr elem. 2.23
		- $R$ Fact. Ring $p$ prime $\Leftrightarrow p$ irr.
		- $R$ eucl. $\Rightarrow R$ PID $\Rightarrow$ $R$ Fact Ring
		- $ggT(x_1, ..., x_n) = \prod_{p \in \mathbb{P}} p^{min\{v_p(x_1), ..., v_p(x_n)\}}$ 
		- $(x_1, ..., x_n) = (d) \Rightarrow d = ggT(x_1, ..., x_n)$, $(x_1) \cap ... \cap (x_n) = (v) \Rightarrow v = kgV(x_1, ..., x_n)$
			- in an $ID$ there could be no $gcd$ bc not every ideal is principal. 2.26
	- for $R$ is PID, $|R| < \aleph_0 \Rightarrow R$ is a field, [link](https://math.stackexchange.com/questions/470401/number-of-element-in-a-principal-ideal-domain-can-be-25-36-35-15).
	- $R[X]$ PID $\Rightarrow R$ is a filed, [link](https://math.stackexchange.com/questions/1733335/prove-that-if-rx-is-a-pid-then-r-is-a-field?noredirect=1&lq=1).
	- $\mathfrak{p}$ pr. ideal $\Rightarrow R/ \mathfrak{p}$ ID (B.9.1.c)
	- $\mathfrak{m}$ max. ideal $\Rightarrow R/\mathfrak{m}$ is a field. (B.7.1.a)
- **Roots of Polynomials**
	- $K$ a field $grad(f) = n \ge 0$ then $f$ has max. $n$ roots, exactly $n$ if $f = \prod^n_{i = 1}(X- a_i) \in K[X]$.
	- $f \in K[X]$, $f(\alpha)= 0$, then $\alpha$ mult. root $\Leftrightarrow f'(\alpha) = 0 \Leftrightarrow ggT(f, f')(\alpha) = 0$.
	- $M = R \times R \setminus \{0\} = \{(a, b) : a, b \in R \land b \not = 0\}$, $(a, b) \sim (a', b') \Leftrightarrow ab' = a'b$, with the fraction operation define the the quotient field, called $Q(R)$. 2.28 Also $\frac{a}{b} = \epsilon \prod_{p \in P} p^{v_p(x)}$.
	- $v_p(f) := min \{v_p(c_i): i \in \mathbb{N}\}$,  (==Gauss-lemma==) $R$ fact. Ring $v_p(fg ) = v_p(f) + v_p(g)$.
	- (Gauss) $R$ fact. $\Rightarrow R[X]$ fact.: $q \in R[X]$ pr. $\Leftrightarrow q \in R$ pr. $\lor (q$ primitive in $R[X] \land$ prime in $Q(R)[X]$.
		- $R$ fact. $q$ primitive in $R[X]$: $q$ irr in $R[X] \Leftrightarrow q$ irr. in $Q(R)[X]$.
	- for $f, g \in\mathbb{Q}[X]$, $cont(fg) = cont(f) \cdot cont(g)$, [link](https://math.stackexchange.com/questions/3537338/if-f-g-in-mathbbqx-with-fg-in-mathbbzx-then-the-product-of-any).
		- $cont(f)$ is the $gcd(a_1, ..., a_n)$ for all coefficients of $f$., [wiki](https://en.m.wikipedia.org/wiki/Primitive_part_and_content).
	- **Irreducibility Criteria** for $R$ fac. ring with quotientfield and $f$ primitive.
		- (Eisenstein) $f = \sum_{i = 0}^n a_iX^i$ primitive, $grad(f) > 0$ and there is $p$ prime in $R$, s.t. $\lnot p | a_n$, $\forall_{0 \le i < n}p | a_i$, $\lnot p^2 | a_0$, then $f$ irr. in $R[X]$. 2.34
		- (Red. mod. $p$) $p \in R$, $0 \not = f = \sum_{i = 0}^n a_i X^i \in R[X]$ s.t. $\lnot p | a_n$ and $\pi: R[X] \rightarrow (R/(p))[X], \sum_{i = 0}^n a_iX^i \mapsto \sum^n_{i = 0}\overline{a_i}X^i$ for $\overline{a_i}:= a + (p)$. If $\pi(f)$ irr. then $f$ irr in Q(R)[X], if $f$ also primitive, then $f$ irr. in $R[X]$. 2.35
	- **Methods** (Sol. 9.2): for $R$ fac., $f = \sum_{k = 0}^d a_k X^k \in R[X]$, $d \ge 2$., check red. of $f$ in $Q(R)[X]$ 
		1. _Eisenstein_: check for all $p \in \mathbb{P}$ s.t. $p | a_0$, if it works, it is irr., else continue
		2. _Roots_: check poss. roots in $Q(R)$, i.e. $\frac{a}{b} \in Q(R)$ s.t. $gcd(a, b) = 1$, $a|a_0$, $b|a_n$, if none, continue
		3. _Degree_: if $d \le 3$, $f$ has no roots $\Leftrightarrow$ $f$ irr. (if no roots, conclude)
		4. _Reduction_: if $R = \mathbb{Z}$, $\lnot 2 | a_d$, then $\overline{f} \in \mathbb{F}_2[X]$ irr. $\Rightarrow f \in \mathbb{Q}[X]$ irr., try further red.., else continue
			- recall irr. pol. of $d \le 4$ in $\mathbb{F}_2[X]$ ([link](https://math.stackexchange.com/questions/32197/find-all-irreducible-monic-polynomials-in-mathbbz-2x-with-degree-equal)): for $d \le 3$, try $\overline{f}(0), \overline{f}(1)$, else
				- $x^4 + x^3 + x^2 + x + 1$ and $x^4 + x^n + 1$ for $n \in \{1, 2, 3\}$ 
		5. _Absurdum_: if $d = 4$, $f$ norm., no roots, try $f = (X^2 +  aX + b) (X^2 + cX + d)$ get cont., else
		6. $R = \mathbb{Z}$, $d \le 5$ with roots $\xi_i \in \mathbb{C} \setminus \mathbb{Q}$, if $\forall_{i , j}\xi_i \cdot \xi_j \not \in \mathbb{Q}$, $f$ irr.
		7. $f$ irr. $\Leftrightarrow f^\flat$ irr. (Wiederholungsblatt 6.a, Tut.B.9-10)
			- $f^\flat$ is $f$ with the order of the coefficients inverted, this can help to apply Eisenstein.
### Algebraic Field Extensions
- **Characteristic**
	- def. for $R$ ID $\varphi: \mathbb{Z} \rightarrow R, n \mapsto n \cdot 1_R$, for $p \in \mathbb{N}$ s.t. $(p) = ker(\varphi)$ then $char(R) = p$.
		- $R \subseteq S$ subr. $\Rightarrow char(R) = char(S)$
	- def. prime field $P=\bigcap\{L : L \subseteq K$ subfield$\} \subseteq K$, smallest subfield of $K$.
		- (i) $char(K) = p > 0 \Leftrightarrow P \simeq \mathbb{F}_p$, (ii) $char(K) = 0 \Leftrightarrow P \simeq \mathbb{Q}$.
			- (iii) any field contains some $\mathbb{F}_p$ or a $\mathbb{Q}$ up to isomorphism.
- **Field-Extentions**
	- $L/K$ ext. if $K$ is a subfield of $L$. Note that $L$ is a $K$-VS.
		- $[L:K] = dim_K (L)$
			- $[L:K] = [L:E][E:K]$
				- $[L: K] \in \mathbb{P} \Rightarrow K = E \lor E = L$
	- $L/K$, $\alpha \in L$ algebraic on $K$ if ex. $f \in K[X]$ s.t. $f(\alpha) = 0$. $L/K$ alg. if all $\alpha \in L$ is alg. 
		- $\varphi_\alpha : K[X] \rightarrow L, g \mapsto g(\alpha)$, $\alpha$ alg. on $K$ iff $ker(\varphi_\alpha) \not = \{0\}$.
		- $\alpha \in L$ alg., ex! $f \in K[X]$ s.t. (i) norm., (ii) $ker(\varphi_\alpha) = (f)$, then $(f)$ prime, $f$ min. of $\alpha$
			- $f$ is the min. poly. of $\alpha$ if it is normed, irr. and has $\alpha$ as a root.
		- All finite extensions are algebraic. 3.7
		- $L/K$ alg. $\Leftrightarrow$ each subring $R$, s.t. $K \subseteq R \subseteq L$ is a field B.6.4
	- $K((\alpha_i)_{i \in I}):= \bigcap\{E$ fi.$: \forall_{i \in I}(\alpha_i \in E) \land K \subseteq E \subseteq L\}$ for $(\alpha_i)_{i \in I} \subseteq L$
		- $K(\alpha_1, ..., \alpha_n) = Q(K[\alpha_1, ..., \alpha_n])$ 3.9
		- Method: find $(\alpha + 1)^{-1} \in \mathbb{Q}(a)$, for $f(\alpha) = 0$, $f$ min.pol. B.6.2.b
			1. $f(x - 1)(\alpha + 1) = 0$, rewrite the equation in order to get $\frac{1}{\alpha + 1} = ...$ 
	- $K[\alpha] = im(\varphi_\alpha)$, $f$ min of $\alpha$ then $K[X]/ker(\varphi_\alpha) \cong K[\alpha]$, hence $[K[\alpha]:K] = deg(f)$. 3.8
	- $L/K$ fin.gen. if $L = K(\alpha_1, ..., \alpha_n)$, $L/K$ simple if $L = K(\alpha)$ 3.10
		- if $\alpha$s alg. in $L$: (i) $K[\alpha_1, ..., \alpha_n] = K(\alpha_1, ..., \alpha_n)$, (ii) $L/K$ finite (alg. + fin. gen = finite) 3.11
		- $K \subseteq E \subseteq L$, $\alpha$ alg. on $E$, $E/K$ alg.: (i) $\alpha$ alg. on $K$, (ii) $L/K$ alg. $\Leftrightarrow L/E$, $E/K$ alg. 3.12
	- Method: $\mathbb{Q}(\alpha_1, ..., \alpha_n)$, find deg. and basis, B.6.1
		1. guess the min.pol., it is normed, irr. and has $\alpha_1$ as a root, repeat for each $\alpha_n$
			- multiply the degrees and compute the basis: $\{1, a\}, \{1, b\} \rightsquigarrow \{1, a, b, a\cdot b\}$.
	- $[\mathbb{Q}(\sqrt{2}, \sqrt[2]{2}, ..., \sqrt[n]{2}) : \mathbb{Q})] = lcm(2, ..., n)$, $\mathbb{Q}(\sqrt{2}, \sqrt[2]{2}, ..., \sqrt[n]{2}) = \mathbb{Q}(\sqrt[lcd(2, .., n)]{2})$ 
- **Algebraic Closure**
	- (Kronecker) for $K$ field and $f \in K[X]$, there is $L/K$ s.t. $\exists_{\alpha \in L}f(\alpha) = 0$.
		- $f = g(X - \alpha) \in L[X]$, then after less than $deg(f)$ steps $f$ is red in lin. fact. $L_n$ 3.14
	- $K$ alg. cl. if all non-const $f \in K[X]$ have a root, i.e. $f = c \prod^n_{i = 1}(X - \alpha) \in K[X]$, $deg(f) = n$, 3.15
		- $K$ alg. cl. $\Rightarrow |K| \ge \aleph_0$
		- $K$ alg. cl. $\Rightarrow$ ($L$ alg. cl $\rightarrow$ $L = K$)
		- each $K$ has an alg. closure $\overline{K}$. 3.17
	- Let $L$ field, $\sigma : K \rightarrow L$ hom., $f \in K[X]$ min of $\alpha$,  $\sigma' : K(\alpha) \rightarrow L$ s.t. $\sigma'|_K = \sigma$:
		- (a): $f^\sigma \in L[X] \land f^\sigma(\sigma'(\alpha) = 0$
		- (b): for $\beta \in L$, $f^\sigma(\beta) = 0$, then $\sigma'$ s.t. $\sigma'(\alpha) = \beta$ is unique.
		- $|\{\sigma':\}| = |\{\alpha: f^\sigma(\alpha = 0\}| \le deg(f^\sigma) = deg(f)$ 3.18
	- For $K'$ alg. ext. of $K$, $\sigma: K \rightarrow \overline{K}$:
		- (a): $\sigma'$ s.t. $\sigma': K' \rightarrow \overline{K}$ and $\sigma'|_K = \sigma$ exists
		- (b): if $K'$ alg. cl. and $\overline{K}/\sigma(K)$ alg. then $\sigma'$ is an isom.
	- If $\overline{K}$, $\overline{K'}$ alg. cl. and ext. of $K$ and $\sigma = id_K$, then $\sigma' : \overline{K} \rightarrow \overline{K'}$ ex. and is isom. 3.20
	- $|K| < \aleph_0 \Rightarrow |\overline{K}| = \aleph_0$ also $|K| \ge \aleph_0 \Rightarrow |\overline{K}| = \aleph_0$, [wiki](https://en.wikipedia.org/wiki/Algebraic_closure).
- **Splitting Fields**
	- $K$ field, $(f_i)_{i \in I} \subset K[X]$, $L$ is called spl.fi. if (i) any $f_i$ splits in lin. factors, (ii) $L = K[\alpha_1, ..., \alpha_n]$ roots of $f_i$s. $L/K$ is then called normal.
	- spl.fi. of $f \in K[X]$ is $K[\alpha_1, ..., \alpha_n]$ for $\alpha$s the roots fo $f$. For more polynomials, let $f = f_1 \cdot ... \cdot f_m$.
	- (Compactness) let $L$ be spl.fi. of $(f_i)_{i \in I}$ for $I = \aleph_0$, let $\mathcal{J}: = \{J: J \subsetneq I \land |J| < \aleph_0\}$ and $A_J = \{\alpha : \exists_{f_j \in J} f_j(\alpha) = 0\}$, $L = \bigcup_{J \in \mathcal{J}} K(A_J)$. 3.31.iii
	- Every two spl.fi. of the same polynomials are isomorphic.
	-  $K \subseteq L$ alg. ex. tfae:
		- $L/K$ norm.
		- irr. $f \in K[X]$ s.t. $\exists_{\alpha \in L}f(\alpha) = 0$ splits in lin. fact.
		- $\sigma: L \rightarrow \overline{L}$ defines a $K$-autom. of $L$.
	- $[L:K] = 2 \Rightarrow L/K$ norm.
	- $N$ normal closure of alg. ext. $L/K$ if (i) $L \subseteq N$ alg., (ii) $N/K$ norm., (iii) $N$ minimal. 3.25
		- $L/K$ alg. then:
			- unique up to isom normal closure $N/K$
			- $L/K$ finite $\Rightarrow N/K$ finite
			- if $M/L$ alg., $M/K$ norm. then ex. norm. cl. $N$ of $L/K$ s.t. $L \subseteq N \subseteq M$, $K = (\{\sigma_i(L)\ i \in I\})$ for $(\sigma_i)_{i \in I}$ $K$-hom. $\sigma_i : L \rightarrow M$. $N$ is unique as a subfi. of $M$. 3.25
	- $|L| < \aleph_0 \Rightarrow L/K$ norm. (tut.13.5)
	- Method: find the spl.fi. of $f$:
		1. _Roots_: find the roots of $f$, call them $\alpha_1, ..., \alpha_n$.
		2. _Minimise_: try to find the smallest set of roots s.t. $K(\alpha_i, ..., \alpha_j)$ contains all roots
	- Methods: for $L$ spl.fi. for $f = X^n + a \in \mathbb{Q}[X]$, find $L$ and compute $[L: \mathbb{Q}]$ B.9.3.b
		1. _Roots_: those are $(\zeta_n^j)_{j \in [0, n-1]}$, for $\zeta_n = exp(\frac{2 \pi i}{n}) \in \mathbb{C}$.
		2. _Splitting field_: then $L = \mathbb{Q}((\zeta_n^j \sqrt[n]{a})_{j \in [0, n-1]}) = \mathbb{Q}(\sqrt[n]{a}, \zeta_n)$
		4. _Degree_: must divide $n \cdot (n-1)$ if $n$ prime ==check==
			- _Min. Pol._: $f$ irr., $[\mathbb{Q}(\sqrt[n]{a}): \mathbb{Q}] = deg(f) = n$.
			- compute $[\mathbb{Q}(\sqrt[n]{a}, \zeta_n): \mathbb{Q}(\sqrt[n]{a})]$, recall $[\mathbb{Q}(\zeta_p) : \mathbb{Q}] = p-1$ (for $p \in \mathbb{P}$)
-  **Separable Field Extensions**
	- $f \in K[X]$ sep. if $f$ has no mult. root in $\overline{K}$
		- $\alpha \in \overline{K}$ is mult. root of $f \in K[X] \Leftrightarrow ggt(f, f')(\alpha) = 0$
		- $f \in K[X]$ irr. then $f$ not sep. in $\overline{K} \Leftrightarrow f ' = 0$ 3.26
	- $char(K)= 0 \land f \in K[X]$ irr. $\Rightarrow f$ sep.
		- $|K| < \aleph_0 \land f \in K[X]$ irr. $\Rightarrow f$ sep., [link](https://math.stackexchange.com/questions/2660459/every-irreducible-polynomial-over-a-finite-field-is-separable), 3.27
	- $char(K) = p \in\mathbb{P}\setminus\{0\}$:
		- $f$ not sep. $\Leftrightarrow f' = 0 \Leftrightarrow \exists_{g \in K[X]} f = g(X^p)$ ($deg(g) = \frac{deg(f)}{p} \Rightarrow K(a^p) \subsetneq K(a)$)
		- (Frobenius) $\forall_{a, b \in K} (a + b)^p = a^p + b^p$, $F: K \rightarrow K, a \mapsto a^p$ inj., $K$ perf. $\Rightarrow F$ aut.
	- Defs: 3.28
		- $L/K$ alg., $\alpha \in L$ sep. over $K$ if for $f \in K[X]$ sep. $f(\alpha) = 0$
		- $L/K$ alg. is sep. if any $\alpha \in L$ sep. over $K$.
		- $K$ perfect if all $L/K$ alg. are sep., [wiki](https://en.wikipedia.org/wiki/Perfect_field)
			- (i) $char(K) = 0 \Rightarrow K$ perf., (ii) $|K| < \aleph_0 \Rightarrow K$ perf. (iii) $\overline{K}$ per. (iv) alg.ext. of per. is per.
	- $L/K$ alg. sep.deg. is $[L:K]_s := |Hom_K(L, \overline{K})|$, for $Hom_K(L, \overline{K})$ set of $K$-hom. 3.30
		- $L/K$ norm. $\Rightarrow [L:K] = |Aut_K(L)| = |Hom_K(L, \overline{K}) = [L, K]_s$, see [[Algebra (Lecture)#Galois Theory]].
		- $\varphi: L \to \overline{K}$ is $K$-hom. if $\varphi|_K = id_K$.
	- $K(\alpha)/K$, $f \in K[X]$ min of $\alpha$ then 3.31
		- $[L:K]_s = |\{\beta \in \overline{K} : f(\beta) = 0\}|$
		- $\alpha$ sep. over $K \Leftrightarrow [L:K]_s = [L:K]$
		- if $char(K) = p \in \mathbb{P} \setminus\{0\}$ and mult. of $\alpha$ in $f$ is $p^r$, then $[L:K] = p^r[L:K]_s$
	- $K \subseteq E \subseteq L$ alg. ext., $[L:K]_s = [L:E]_s[E:K]_s$ 3.32
		- $char(K) = 0 \Rightarrow [L:K] = [L:K]_s \Rightarrow L/K$ sep.
		- $char(K) \in \mathbb{P} \setminus \{0\} \Rightarrow \exists_{r \in\mathbb{N}} [L:K] = p^r [L:K]_s$
		- always: $[L:K]_s | [L:K]$
	- $L/K$ fin., then $L/K$ sep. $\Leftrightarrow$ $L = K(\alpha_1, ..., \alpha_n)$ for $\alpha_1, ..., \alpha_n \in L$ sep. over $K \Leftrightarrow [L:K]_s = [L:K]$
	- $L/K$ alg., let $\mathcal{A} \subseteq L$ s.t. $K(\mathcal{A}) = L$, then $L/K$ sep. $\Leftrightarrow$ any $\alpha \in \mathcal{A}$ sep. over $K \Rightarrow [L:K]_s = [L:K]$.
	- if $E/K$, $L/E$ alg. then $L/K$ sep. $\Leftrightarrow L/E$, $E/K$ sep. 3.35
	- $(H, \cdot_K) \subseteq (K^\times, \cdot_K)$ subgr. $\Rightarrow H$ cycl.
- **Theorem of the Primitive Element**: $L/K$ fin. sep. ext. $\Rightarrow \exists_{\alpha \in L}L = K(\alpha)$. Also $\alpha$ is primitive to $L/K$.
- **Finite Fields**
	- For $p^n$, $p \in \mathbb{P}$, ex. unique up to isom. $\mathbb{F}$ s.t. $|\mathbb{F}| = p^n$.
		- For $\mathbb{F}_{p^n}$ is spli.fi. of $X^{p^n}-X \in \mathbb{F}_p[X]$
		- $\mathbb{F}_p \subseteq \mathbb{F}_{p^n} \subseteq \overline{\mathbb{F}_p}$ holds, hence $\mathbb{F}_p \subseteq \mathbb{F}_{p^n}  \subseteq \mathbb{F}_{p^m} \subseteq \overline{\mathbb{F}_p} \Leftrightarrow n |m$
			- extensions $\mathbb{F}_{p^n} \subseteq \mathbb{F}_{p^m}$ are the only extensions of finite fields with char. $p$.
	- $|K| < \aleph_0 \Rightarrow \exists_{p \in \mathbb{P}}\exists_{n \in \mathbb{N}} K \cong \mathbb{F}_{p^k}$ [wiki](https://en.wikipedia.org/wiki/Finite_field).
### Galois Theory
True love makes non-Galois couples: not normal or inseparable. And if you claim your lover to be perfect, be aware that they are separable to anyone. #jokes
- $L/K$ is gal. $:= L/K$ norm. and sep., a gal. gr. $Gal(L/K) = Aut_K(L)$, [[Algebra (Lecture)#Galois Examples]].
	- $L/K$ normal, then:
		- recall: $L/K$ norm. $\Rightarrow Hom_K(L, \overline{K}) = Aut_K(L)$ 3.23.c
		- $|Aut_K(L)| = |Hom_K(L, \overline{K})| = [L : K]_s \le [L: K]$
	- $L/K$ separable, then:
		- ($\Leftrightarrow$) $|Aut_K(L)| = [L : K]$
	- $L/K$ gal. $\Leftrightarrow |Gal(L/K)| = [L:K]$
	- $L/K$ gal. fin. $\Rightarrow L= K(\alpha_1, ..., \alpha_n) = K[\alpha_1, ...,\alpha_n]$, for $\sigma \in Gal(L/K)$ is uniq. def. by  $\sigma(\alpha_1), ..., \sigma(\alpha_n)$.
	- $f \in K[X]$, root $\alpha \in L$, $\sigma \in Gal(L/K) \Rightarrow f(\sigma(\alpha))= 0$
		- $0 = f(\alpha) \sum^n_{i = 0}a_i \alpha^i \in L$, $0 = \sigma(0) = \sigma(f(\alpha)) = \sigma(\sum^n_{i = 0}a_i \alpha^i) = \sum^n_{i = 0}a_i \sigma(\alpha^i) = f(\sigma(\alpha))$.
	- $L/K$ gal., $K \subseteq E \subseteq L$: 
		- (i) $L/E$ gal., $Gal(L/E) \subseteq Gal(L/K)$ subgr. 
		- (ii) if $E/K$ gal. $\Rightarrow Gal(L/K) \rightarrow Gal(E/K), \sigma \mapsto \sigma|_E$ is surj. hom.
	- $L$ field, $G \subseteq Aut(L)$, then $L^G := \{a \in L | \forall_{\sigma \in G}\sigma(a) = a\}$ (fixkö. of $G$): 4.4
		- (i) $|G|< \aleph_0 \Rightarrow (L/L^G$ gal. $\land G = Gal(L/L^G)$
		- (ii) $|G| \ge \aleph_0 \land L/L^G$ alg. $\Rightarrow  L/L^G$ gal. $\land G \subseteq Gal(L/L^G)$ subgr.
	- $L/K$ norm.: 4.5
		- (i) $L/L^{Aut_K(L)}$ gal. $\land Gal(L/L^{Aut_K(L)}) = Aut_K(L)$
		- (ii) if $L/K$ sep. then $K = L^{Aut_K(L)}$
	- for $\psi: E \mapsto Gal(L/E)$, $\phi: H \mapsto L^H$, then $\phi \circ \psi = id$
	- (Gal.-Cor.) $L/K$ gal., $L^H/K$ norm. ($\Rightarrow$ gal.) $\Leftrightarrow H \trianglelefteq G$ $\Rightarrow H = ker(Gal(L/K) \rightarrow Gal(L^H/K), \sigma \mapsto \sigma|_{L^H})$ 4.6
		- if $L/K$ fin. sep. then $|\{K': K \subseteq K' \subseteq L\}| < \aleph_0$
			- if also $N/K$ norm.cl. then $N/K$ fin. gal. and $[N:K] = |Gal(N/K)| < \aleph_0$.
	- Method: find $Gal(f)$, $L$ spl.fi. of $f$ in $K$, and all $E$ s.t. $K \subseteq E \subseteq L$
		1. _Galois Ext._ $L$ is a spl.fi., hence $L/K$ is norm., prove it to be sep.
			- $char(K) = 0 \Rightarrow L/K$ sep.
			- $L/K$ fin., then $L/K$ sep. $\Leftrightarrow$ $L = K(\alpha_1, ..., \alpha_n)$ for $\alpha_1, ..., \alpha_n \in L$ sep. over $K \Leftrightarrow [L:K]_s = [L:K]$
			- $L/K$ alg., let $\mathcal{A} \subseteq L$ s.t. $K(\mathcal{A}) = L$, then $L/K$ sep. $\Leftrightarrow$ any $\alpha \in \mathcal{A}$ sep. over $K
		2. _Degree_: find $[L:K]$, conclude $[L:K] = |Gal(f)|$
		3. _Elements_: 
			1. let $\sigma(\alpha_i) = \alpha_j$
			2. determine $\sigma(\alpha_j)$ using that $\sigma$ is a $K$-automorphism.
			3. combine a fixed $\alpha_i$ with any $\alpha_j$, and check wether they are automorphism
			4. Stop when $\alpha_j$ are finished or you already got $[L:K]$ many automorphism.
		4. _Isomorphic Class_: check isomorphisms with the groups in the table using the listed methods
		5. _Galois Correspondence_: subfields of $L$ correspond to subgroups of $Gal(f)$
			1. for $\sigma \in Gal(f)$, $L^{\langle \sigma \rangle}$ are exactly the subfields
			2. to compute $L^{\langle \sigma \rangle}$ consider $\sigma(a_1 \beta_1 + ... + a_n \beta_n)$ for $\beta_1, ..., \beta_n$ the basis of $L/K$ and recall $L^G := \{a \in L | \forall_{\sigma \in G}\sigma(a) = a\}$, for instance if $\sigma(a + b \sqrt{2} + c \sqrt{3} + d \sqrt{6})$$= a - b\sqrt{2} + c \sqrt{3} + d\sqrt{6}$, then $L^{\langle \sigma \rangle} = \mathbb{Q}(\sqrt{3})$.
- **Roots of the Unit**
	- for $f_n := X^n -1 \in K[X]$ for $n \in \mathbb{N}\setminus \{0\}$
		- $U_n := \{\alpha \in \overline{K}: \alpha^n = 1\}$ subgr. of $(\overline{K}^\times, \cdot)$, $U_n$ cycl. 4.9
		- $\lnot char(K) | n \Rightarrow |U_n| = n \land (U_n, \cdot_{\overline{K}}) \cong (Z/(n), +)$.
			- if $\lnot char(K) | n$ then $X^n -1 \not = 0 \land (X^n -1)' = nX^{n-1} \not = 0$ hence $f_n$ sep. and $|U_n| = n$.
			- $\zeta \in U_n$ pr. if $\langle \zeta \rangle = U_n$ or equivalently $ord(\zeta) = n$.
			- for $\zeta$ pr. $U_n = \{1,\zeta, ..., \zeta^{n-1}\}$, $K[\zeta]/K$ is spl.fi. of $x^n -1$
		- if $p = char(K) | n$, $n = p^rm$, $\lnot p | m$ then $x^m -1$ sep., since $x^n -1 = (x^n-1)^{p^r}$, $x^n-1$ and $x^m -1$ share all roots. From now on assume $\lnot char(K) | n$.
		- $a \in G$, $ord(a) = n \in \mathbb{N} \Rightarrow \forall_{m \in \mathbb{Z}} ord(a^m) = \frac{m}{gcd(m, n)}$
			- if $G = \langle a \rangle$ then $G = \langle a^m \rangle \Leftrightarrow gcd(m, n) = 1$
		- $\varphi: \mathbb{N} \setminus \{0\} \rightarrow \mathbb{N}, n \mapsto |\{m : 1 \le m \le n \land gcd(m, n) = 1\}|$ $= |\{$gen., of $\mathbb{Z}/(n)\}| =$ $|\mathbb{Z}/(n)^\times| =  |\{$gen., of $U_n\}| = |\{\zeta \in U_n : \zeta$ pr. $\}|$ (Euler-$\varphi$-function)
			- $\varphi(1) = 1, \varphi(2) = 1, \varphi(3) = 2$ 
			- $gcd(m, n) = 1 \Rightarrow \varphi(m \cdot n) = \varphi(m) \cdot \varphi(n)$
			- $n = p_1^{v_1} \cdot ... \cdot p_r^{v_r}$ for $v_i > 0$ $\Rightarrow \varphi(n) = \prod_{i = 1}^r p_i^{v_1 -1}$
			- $n = \sum_{d | n \land d > 0} \varphi(d)$
		- for $\lnot char(K) | n$ and $(\zeta_i)_{i \in [1, ..., \varphi(n)]}$ pr. $\phi_n := \prod_{i = 1}^{\varphi(n)}(x - \zeta_i) = \prod_{d | n} \phi_d$ 4.11 (circ. div. pol.)
			- $\phi_4 = (x -i)(x +i)$
			- for all $n \in \mathbb{N}$, $\phi_n \in \mathbb{Q}[X]$ is irr.
		- for $d | n$, $P_d := \{\zeta_d : \zeta_d$ pr.$\} \subseteq U_n$, $U_n := \bigsqcup_{d|n}P_d$, $x^n - 1 = \prod_{d|n} \prod_{\zeta \in P_d} (x - \zeta) = \prod_{d |n} \phi_d$ 
			- $M_d := \{g \in \mathbb{Z}/(n) : ord(g) = d\}$, $\bigsqcup_{d|n} M_d = \mathbb{Z}/(n)$ 
		- $\lnot char(K) | n$, $\zeta_n$ pr., then $X^n - 1$ sep., $K(\zeta_n)$ spl.fi of $X^n - 1$, i.e. fin.gal. ==check note 4.13==.
		- for $n \ge 1$, $\zeta \in \overline{\mathbb{Q}}$, $\zeta$ pr. then $f= \phi_n$, also $\phi_n \in \mathbb{Q}[X]$ irr. 4.15 ==?==
		- $\zeta \in \overline{\mathbb{Q}}$, $\zeta = \sqrt[n]{u}$ primitive for $u \in \mathbb{Q}^\times$, then (i) $\mathbb{Q}(\zeta)/\mathbb{Q}$ gal., (ii) $[\mathbb{Q}(\zeta)/ \mathbb{Q}] = \varphi(n)$, (iii) $Gal(\mathbb{Q}(\zeta)/\mathbb{Q}) \cong \mathbb{Z}/(n)^\times$.
			- call gal. $L/K$ abelian if $Gal(L/K)$ is abelian. [[Algebra (Lecture)#Example with $ zeta$]].
- **Roots Extensions**
	- $char(K) = 0$, $L/K$ is rad. if there are $K_1 \subseteq ... \subseteq K_r = L$ s.t. $K_{i + 1} = K_i(\sqrt[n_i]{a_i})$ 4.18
		- $L/K$ rad. $\Rightarrow L/K$ fin.
		- $char(K) = 0$, $L/K$ rad. then ex. $M/K$ s.t. $K \subseteq L \subseteq M$ s.t. $M/K$ rad. gal. 4.20
		- $L/K$ gal. rad., $char(K) = 0$, then $Gal(L/K)$ is quot. of a gr. $G$ s.t. (i). 4.21
			- (i): exists $G_i \subseteq G$ subgr. s.t. $\langle e \rangle = G_r \trianglelefteq G_{r-1} \trianglelefteq ... \trianglelefteq G_0 = G$, $G_i/G_{i + 1}$ ab. ($G$ solvable)
		- $char(K)=0$, $f \in K[X]$ is sol. with rad. if ex. $M/K$ rad. with all roots of $f$. 4.22
			- $f \in K[X]$ sol.w.rad. $\Rightarrow Gal(f)$ quot.gr. of $G$ s.t. (i)
				- $f \in K[X]$ solv.w.rad. $\Leftrightarrow Gal(f)$ is solv. (not proved)
### Advanced Group Theory
- $X$ a set, $S(X)$ the set of bij. on $X$, $S(X)$ is a gr. on $\circ$, $G$ operates on $X$ if ex. $\Phi: G \to S(X)$ hom.
	- for $g \in G$, $x \in X$ write $g \cdot x = \Phi(g)(x)$, also $\Phi(1)= id_X = 1 \cdot x = id_X(x) = x$
	- $g_1, g_2 \in G$, write $g_1 g_2 \cdot x = \Phi(g_1 g_2)(x) = \Phi(g_1)(\Phi(g_2)(x)) = g_1 \cdot (g_2 \cdot x)$.
	- Within these two rules, $\cdot$ can be freely chosen (similarly to the $\lambda \cdot v$ for a VS)
	- $Gal(f)$ oper. on roots of $f$.
- $G$ oper. on $X$, for $x \in X$ def:
	- $O_x = \{g\cdot x : g \in G\} \subseteq X$ (orbit of $x$)
		- $X = \bigsqcup_{x \in R \subseteq X} O_x$
	- $G_x = \{g \in G : \forall_{x \in X} g \cdot x = x\} \subseteq G$ (stabilisator of $x$)
		- $G_x$ subgr of $G$, 5.3
	- for $|G| < \aleph_0$, $G$ oper. on $G$ with $g \cdot x = gxg^{-1}$ 5.6.a
		- $O_x = \{gxg^{-1} : g \in G\}$
		- $G_x = \{g \in G: gx = xg\}$
		- $Z(G) := \{g \in G : \forall_{x \in G}g x = x g\}$
			- (i) $Z(X) \trianglelefteq G$, (ii) $G$ ab. $\Leftrightarrow Z(G) = G$, (iii) $x \in Z(G) \Leftrightarrow G_x = G \Leftrightarrow |O_x| = 1$, (iv) $|G| = |Z| + \sum_{|O_x| > 1}|O_x|$ 
	- $G/G_x \cong O_x$ ($\Leftrightarrow |G : G_x| = |O_x|$), since $gG_x \mapsto g\cdot x$ bij. 5.5
		- $|X| = \sum_{O_x \text{ disj.}}|O_x| = \sum_{O_x\text{ disj.}}|G /G_x|$
		- $|G| = |G_X| + \sum_{|O_x| > 1} |O_x|$ Tut.12.1.a
		- obv. $G_x = G \Leftrightarrow |O_x| = 1$
		- $|G| =p^k$, for $p \in \mathbb{P}$, $k \ge 1$ then $Z \not = \{1\}$
- $|G| =p^2 \Rightarrow G$ abel. 5.6.c
- $|G| =p^r \cdot m$, $\lnot p | m$, a syl.-$p$-subgr of $G$ is $U \subseteq G$ s.t. $|U| = p^r$, i.e. max. $p$-subgr.
- $|G| = p^r \cdot m$, $\lnot p |m$, then for any $1 \le s \le r$ $G$ has a subgr $U_s$ s.t. $|U_s| = p^s$  (Syl.-I)
	- for $p \in \mathbb{P}$, $p | |G| \Rightarrow G$ has an elem. of order $p$. (Special Theorem of Cauchy)
- $|G| = p^r \cdot m$, $\lnot p | m$, $\forall_{s \in [1, r]}\exists_{g \in G} g U_sg^{-1} \subseteq U_r$ (Syl.-II)
	- for $P, P'$ syl.-$p$-subgr. then $\exists_{g \in G} g P'g^{-1} = P$
	- $P$ the only syl.-$p$-subgr $\Leftrightarrow P \trianglelefteq G$, (i.e. $\exists_{g \in G} gPg^{-1} = P$).
- $s_p |m$ and $s_p \equiv \overline{1}^p$ (mod. $p$) (Syl. III) 
	- $|G| =p^r \cdot m$, $\lnot p | m$, $s_p = |\{P :$ syl.-$p$- subgr. of $G\}|$
- Method: prove there is no simple group of order $n$, tut.B.13.1
	1. _Sylow Subgruops_: consider the factorisations of the from $|G| =p^r \cdot m$, $\lnot p | m$,
	2. _Sylow III_: for each $p$, $m$ found above determine possible $s_p$ s.t. $s_p |m$ and $s_p \equiv \overline{1}^p$.
	3. _Absurdum_: assume for each $p$ found in 1., assume $s_p \not =1$ and get contradiction
	4. _Sylow II_: since there is one $p$ s.t. $s_p = 1$, then use $P$ the only syl.-$p$-subgr $\Leftrightarrow P \trianglelefteq G$.
- $N \trianglelefteq G$, $H \trianglelefteq N$ and $H$ syl.subgr. of $N$, $\Rightarrow H \trianglelefteq G$, tut.B.13.2 (weaker transitivity) 
- **Classification of Groups of Small Order**
	- **Abelian Groups**
		- (a) for $A$ an ab.gr. s.t. $|A| = p^k$ then ex.uniq. a partition $l_0, ..., l_s$, $\sum_{i = 0}^s l_i = k$, $1 \le l_0 \le ... \le l_s \le k$ s.t. $A \cong \mathbb{Z}/p^{l_0} \mathbb{Z} \oplus ... \oplus \mathbb{Z}/p^{l_s} \mathbb{Z}$.
		- (b) for $A$ an ab.gr. s.t. $|A| = p \cdot q$, $p \not = q$ then $A \cong \mathbb{Z}/p \mathbb{Z} \oplus \mathbb{Z}/q \mathbb{Z} \cong \mathbb{Z}/p\cdot q \mathbb{Z}$.
	- **Groups through Generators and Relations**
		- $G = \langle \alpha, \beta | \alpha^3 = 1 = \beta^2, \beta \alpha = \alpha^2\beta \rangle$ is the gr. generated by $\alpha, \beta$ s.t. $\beta \alpha = \alpha^2 \beta$.
			- Questions are: (i) is one of the conditions redundant? (ii) is it a trivial gr.?
			- $G \cong S_3$ for $\alpha = (123), \beta = (12)$
		- $D_n = \langle \alpha, \beta | \alpha^n = 1 = \beta^2, \beta \alpha = \alpha^{-1}\beta \rangle$ (gr. of symm. of an $n$-sided reg. polygon)
			- $D_3 = \langle \alpha, \beta | \alpha^3 = 1 = \beta^2, \beta \alpha = \alpha^{-1}\beta = \alpha^2 \beta \rangle \cong S_3$
			- max. ord. of the first rotation $\alpha$ is $\frac{ord(D_n)}{2}$
				- for $ord(G)$ equal $6$ or $10$ this is enough, for $8$ it might still be $\mathbb{Z}/(2) \oplus \mathbb{Z}/(4)$.
			- the reflection $\beta$ has ord. $2$.
				- this information is not very helpful since there is such a $\beta$ in each possible group.
			- $\beta \alpha = \alpha^{-1} \beta$ 
				- this shall be checked for $ord(G) = 8$.
				- recall $D_n$ is not abelian
		- $Q = \langle \alpha, \beta | \alpha^4 = 1 \beta^4, \alpha^2 = \beta^2, \beta \alpha = \alpha^3 \beta \rangle$, $|Q| = 8$
			- $Q = \langle \begin{smallmatrix} 0 & 1 \\ -1 & 0 \end{smallmatrix}, \begin{smallmatrix} 0 & i \\ i & 0 \end{smallmatrix}\rangle \subseteq GL_2(\mathbb{C})$
			- $Q = \{\pm 1, \pm i, \pm j, \pm k\}$, $i^2 = j^2 = k^2 = -1$, [yt](https://youtu.be/QgGlKJkp5PM?si=Jv6lX39O7iOyNJsW),
				- $i \rightsquigarrow j \rightsquigarrow k \rightsquigarrow i$ to get $+$ (i.e. $ij = k$ snd inverse for $-$, i.e. $i k = -j$)
				- for $\alpha \in \{\pm i , \pm j, \pm k\}$, $\langle \alpha \rangle = \{1, \alpha, -1, - \alpha\}$.
		- $p>2$ prime, $|G| = 2p \Rightarrow G \cong \mathbb{Z}/2p\mathbb{Z}$ or $G \cong D_p$. 5.19
		- $G$ not ab., $|G| = 8$ $\Rightarrow G \cong Q \lor F \cong D_4$ 5.20
		- ![[Finite Groups.jpeg]]
- **Solvable Groups**
	- $G$ sol. if ex. $(G_i)_{i \in [0, r]}$ s.t. (i) $G_i \subseteq G$ subgr., (ii) $\{e\} = G_r \trianglelefteq ... \trianglelefteq G_1 \trianglelefteq G_0 = G$, (iii) $G_i / G_{i + 1}$ ab.
		- $G$ ab. $\Rightarrow$ $G$ sol. ($G_0 = \{e\}$, $G_1 = G$, $G_0/G_1 \cong G$ ab.)
	- For $U \subseteq G$ subgr., $N \trianglelefteq G$, then: 5.23
		- $G$ sol. $\Rightarrow G/N$ sol.
		- $G$ sol. $\Rightarrow U$ sol.
		- $N, N/G$ sol. $\Rightarrow G$ sol.
	- $|G| = p^k \cdot q^l \Rightarrow G$ sol. (Burnside)
		- we only proved: $|G| = p^k \Rightarrow G$ sol. 5.24
	- $|G| = 2n + 1 \Rightarrow G$ sol. (Feit-Thompson) (nor proved)
- **Simple Groups**
	- $G$ sim. if $G \not = H \not = \{e\} \Rightarrow H \not \trianglelefteq G$  i.e. there's no non-trivial norm.div. 5.25
		- $\mathbb{Z}/p\mathbb{Z}$ sim.
	- $A_5$ sim. 5.26
		- $n \ge 5 \Rightarrow S_n$ not sol
		- $A_5$ is smallest s.t. (i) not ab., (ii) sim.
### Polynomials with $S_n$ as Galois Group
- $Gal(f) \cong S_n$ for $n \ge 5$ $\Rightarrow f$ not sol. with rad.
	- since $Gal(f)$ permutes roots of $f$,  $Gal(f) \subseteq S_n$ subrgr.
	- since $n \ge 5$, $S_n$ not sol.
- for $n \ge 2$: 6.1
	- (i) $S_n = \langle (12), (123...n)\rangle$
	- (ii) if ex. $H$ s.t. (iia) $H \subseteq S_n$ trans.subgr. and contains a transp. and $(n -1)$-cycle, then $H = S_n$
	- for $1 \ge i, j \ge n$, $i \not = j$ ex. $\sigma \in H$ s.t. $\sigma(i) = j$ then $H$ trans subgr.
- $p \in \mathbb{P}$, $f \in \mathbb{Q}[X]$ irr. s.t. $deg(f) = p$ and has exactly 2 not-real roots, then $Gal(f) \cong  S_p$ 6.2
- $Gal(X^{p^n} - X) = Gal(\mathbb{F}_{p^n}/\mathbb{F}_p)$ cycl.,
	- if $m | |Gal(f)|$, ex. an elem. of order $m$.
		- for $f \in \mathbb{F}_p[X]$ irr., $\exists_{\sigma \in Gal(f)} ord(\sigma) = n$
	- $|Gal(\mathbb{F}_{p^n})| = n$, $\mathbb{F}_{p^n} / \mathbb{F}_p$ is simple and separable (since $\mathbb{F}_p$ is finite)
- $\mathbb{F}_{p^n}/\mathbb{F}_p$ fin. sep., if $\mathbb{F}_{p^n} = \mathbb{F}_p[\alpha]$, $f \in \mathbb{F}_p[X]$ is min. of $\alpha$, so $f$ irr. of deg. $n$.
	- $\forall_{p \in \mathbb{P}}\forall_{n \ge 1} \exists_{f \in \mathbb{F}_p[X]} f$ irr.$\land deg(f) = n$.
- $A$ fac.ring., $\mathfrak{p} \subseteq A$ pr.ideal, $\overline{A} = A/\mathfrak{p}$, $K = Q(A)$, $k = Q(\overline{A})$. For $f \in A[X]$ primitive, let $\overline{f} \in \overline{A}$ be $f$ $mod(p)$, then: (i) $\overline{f}$ sep $\Rightarrow f$ sep., (ii) $Gal(\overline{f}) \subseteq Gal(f)$ subgr. 6.4 (not proved)
- $\forall_{n \ge 1} \exists_{f \in \mathbb{Q}[X]} deg(f) = n \land Gal(f) \cong S_n$ 

##### Examples
For [[Algebra (Lecture)#Galois Theory]] I decided to write down some of the examples too, I collect them here:
###### Galois Examples
- (a). $L = \mathbb{Q}(\sqrt{p})$, $K = \mathbb{Q}$, since $f = x^2 -p \in \mathbb{Q}[X]$ hence norm., $char(\mathbb{Q}) = 0 \Rightarrow L/K$ sep. Also $[L:K] = 2 \Rightarrow |Gal(L/K)| = 2 \Rightarrow Gal(L/K) \cong \mathbb{Z}_2$, elem. in $Gal(L/K)$ premute roots ($\pm \sqrt{p}$) of $f$, i.e. $\sqrt{p} \mapsto \sqrt{p}$ and $\sqrt{p} \mapsto -\sqrt{p}$ (uniq. def. by $\alpha$s)
- (b). $f = (x^2 -2)(x^2 - 3) \in \mathbb{Q}[X]$ has zer. kö. $\mathbb{Q}[\sqrt{2}, \sqrt{3}] = L$, $[L:\mathbb{Q}] = 4$. $L/K$ is gal., $\Rightarrow |Gal(L/\mathbb{Q})| = [L: \mathbb{Q}] = 4$. Elements perm. roots, (22:33, 2-2:33, 22:3-3, 2-2:3-3), $Gal(L/K) = \{id, \sigma, \tau, \sigma\tau\} \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.
- (c) $f = x^3 -2 \in \mathbb{Q}[X]$, let $\omega$ s.t. $\omega^2 + \omega + 1 = 0$, roots of $f$ is $\{\sqrt[3]{2}, \sqrt[3]{2}\omega, \sqrt[3]{2}\omega^2\}$, $L = \mathbb{Q}(\sqrt[3]{2}, \omega)$ is zer.kö. of $f$, $[L: \mathbb{Q}] = 6$, $Gal(L/\mathbb{Q})$ prem. the roots, hence $Gal(L/\mathbb{Q}) = S_3$ (smallest non-abelian), gal. gr. must not be abelian. The extension between, $[\mathbb{Q}(\sqrt[3]{2}): \mathbb{Q}] = 3$, $\mathbb{Q}(\sqrt[3]{2} \subset \mathbb{R}$, $\sigma(\sqrt[3]{2}) \in \mathbb{R}$ hence $\sigma(\sqrt[3]{2}) = \sqrt[3]{2}$, hence $|Gal(\mathbb{Q}(\sqrt[3]{2}) /\mathbb{Q})| = 1 \not = 3 = [\mathbb{Q}(\sqrt[3]{2}): \mathbb{Q}]$, hence it is not a gal. ext.
- $p \in \mathbb{P}$, $r, n \in \mathbb{N}\setminus \{0\}$, $q = p^r$, $q\ = p^{rn}$, $\mathbb{F}_p \subseteq \mathbb{F}_q \subseteq \mathbb{F}_q' \subseteq \overline{\mathbb{F}_p}$ and $\mathbb{F}_q \subseteq \mathbb{F}_{q'}$ sep. ($\Leftarrow$ finite), (norm. $\Leftarrow \mathbb{F}_q'$ zer.kö. for $X^q - X \in \mathbb{F}_q[X]$) $\Rightarrow |Gal(\mathbb{F}_{q'}/\mathbb{F}_q)| = n$, see script for conclusion.
###### Galois Correspondence Examples
- (a) $L = \mathbb{Q}(\sqrt{2}, \sqrt{3})/\mathbb{Q}$ is gal. and $Gal(L/\mathbb{Q}) = \{id, \sigma, \tau, \sigma\tau\}$ as in [[Algebra (Lecture)#Galois Examples]] (b). For the other examples, see the script.

###### Example with $\zeta$
- $n = 12$, $\zeta = \sqrt[12]{u}$ prim. for $u \in \mathbb{Q}^\times$, $\varphi(12) = \varphi(3 \cdot 2^2) = \varphi(3)\varphi(2^2) = 2 \cdot 2 = 4$. $\mathbb{Z}^\times = \{1, 5, 7, 11\}$, $Gal(\mathbb{Q}(\zeta)/\mathbb{Q}) = \{\sigma_m : m \in \mathbb{Z}^\times\} =: G$ for $\sigma_m: \zeta \mapsto \zeta^m$. $\sigma_{11} = \sigma_3 \circ \sigma_7$. Also note $G \cong \mathbb{Z}/(2) \times \mathbb{Z}/(2)$. Also $\mathbb{Q}(\zeta)/\mathbb{Q}$ has three non trivial fields in between: $\mathbb{Q}(\zeta)^{\langle \sigma_5 \rangle}$, $\zeta^3 \sqrt[4]{u} = \pm i$, hence $\mathbb{Q}(\zeta)^{\langle \sigma_5 \rangle} = \mathbb{Q}(i)$. The second field is: $\mathbb{Q}^{\langle \sigma_7 \rangle}$, $\zeta^2 = \sqrt[6]{u} = \frac{-1 \pm \sqrt{-3}}{2}$, then $\mathbb{Q}(\zeta)^{\langle \sigma_7 \rangle} = \mathbb{\sqrt{-3}}$. $\mathbb{Q}(\zeta)^{\langle \sigma_{11} \rangle}$, similarly $\mathbb{Q}^{\langle \sigma_11 \rangle} = \mathbb{Q}(\sqrt{3})$. 
