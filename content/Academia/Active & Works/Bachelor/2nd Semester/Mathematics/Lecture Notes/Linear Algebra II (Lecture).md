Hold by Prof. Matheusz Michałek at the #UniKonstanz during the #2nd_Semester.
## Recap
### 11
#### 11.1 Scalar Produdct
- def. for $\mathbb{C}$ prove them all
- $|\langle v, w \rangle |^2 \le \langle v, v \rangle \langle w, w \rangle$ "$\sim$" $(xy)^2 = xx \cdot yy$ .8
- $\cos(\alpha) = \frac{\langle v, w \rangle}{||v||\cdot ||w||}$
#### 11.2
- $U^\bot := \{v \in V| \forall_{u \in U} u \bot v\}$
- for $U$ subsp. of $V$, there's maximally one $w \in U$ s.t. $v - w \in U^\bot$, $w$ is the orth. proj. of $v$ on $U$
- Gram-Schm. want $(w_i)_{i \in I}$ $W_1 = v_1$, $w_2 = v_2 - \frac{\langle v_2, w_1\rangle}{|w_1^2|}w_1$, $w_3 = v_3 - \frac{\langle v_3, w_1\rangle}{|w_1|^2}w_1 - \frac{\langle v_3, w_2 \rangle}{|w_2|^2}w_2$.
- $dim(U) + dim(U^\bot) = dim (V)$
- $A$ is orth. $\Leftrightarrow row(A)$ is ONB $\Leftrightarrow column(A)$ is ONB $\Leftrightarrow A^*A= I_n$ ($^*$ conj. trans.) .27
#### 11.3 Hermitian Matrix
- $\langle f(v) w \rangle = \langle v, f(w) \rangle \Leftrightarrow f$ is self adjoint
- $A$ selfadj. $\Leftrightarrow A^* = A$, in $S\mathbb{R}$ or hermitian in $\mathbb{C}$.
- $A$ selfadj. $\Rightarrow \lambda \in \mathbb{R}$ for any eigenval.
- $f$ selfadj. and $V \rightarrow V$ the eigenvec. of $f$ make an ONB, also $f$ diagonalisable .9.
- $A$ selfadj. $A = P^*DP$ for $D$ diag., $P$ orth. ($\Rightarrow A \approx D$)
### 12
#### 12.1 inf. sup, min. max
- Partial Ordering: reflexive, antisymmetrical and transitive
- $a \in ub(B) \Leftrightarrow \forall_{b \in B} a \preceq b$, $sup(B)$ is the smallest such $a$; $a =max(B) \Leftrightarrow a \in B \cap ub(B)$.
#### 12.2 Zorn's Lemma
- $a$ maximal element in $B$ $\Leftrightarrow b \in B \land \lnot \exists_{c \in B} b \prec c$.
- A chain of $A$ is a totally ordered subset of $A$
- Zorn's Lemma: let $(A, \preceq)$ s.t. any chain in $A$ has an $ub$ then $A$ has a maximal element.
- Cor. every vectorspace has a basis & every ideal is contained in a maximal ideal.
### 13
#### 13.1 Dualspace
- $V^* := Hom(V, \mathbb{K})$, dualbasis $v_i^*(v_i)=1$ and all the rest to $0$.
- $(\mathbb{K}^n)^* \cong \mathbb{K}^n$, .6 for the function
- $f^*: l \mapsto l \circ f$ and note: $(f \circ g)^* = g^* \circ f^*$, also $h: f \mapsto f^*$, $h$ is lin.
- $M(f^*, w^*, v^*) = M(f, w, v)^T$, "Transponieren heißt Komponenten dualisieren."
- $f:V \rightarrow W$: $dim(ker(f)) + dim(im(f^*)) = dim(V)$, $dim(im(f)) + dim(ker(f^*)) = dim(W)$
- $f$ inj. $\Leftrightarrow f^*$ surj. and vice versa
- ==dualdual?==
#### 13.2 Bilinear Function
- $b(\cdot, v_2)$ and $b(v_1, \cdot)$ linear, $b(v_1, v_2) \in W$ for $v_1 \in V_1$ and $v_2 \in V_2$. Too general
#### 13.3 Bilinear Forms
- $V \times V \rightarrow K$, denoted with $Bil(V)$, Darst. $(M(b, \underline{v}))_{i, j} = b(v_i, v_j)$
- $b^\rightarrow: v \mapsto b(\cdot, v)$, it fixes first the right variable, $b^\leftarrow$ does the opposite.
- $M(b, \underline{v}) = M(b^\leftarrow, \underline{v}, \underline{v}^*) = M(b^\rightarrow, \underline{v}, \underline{v}^*)^T$, and $b^\rightarrow = (b^\leftarrow)^*$
- $b$ not deg. $\Leftrightarrow b^\rightarrow$ inj. $\Rightarrow ker(b^\rightarrow) = 0 \Rightarrow (b(\cdot, v) = 0) \rightarrow v=0$.
#### 13.4 Quadratical Forms
- Quad forms $\cong$ Symmatrix $\cong$ Symm bilin. forms, 
- see 13.4.6, $b(v,v)$ converse is $\frac{1}{2}(q(v+w)- q(v) - q(w))$
#### 13.5 Cholesky
- See the scritp, remember the form of $D$ and $P$ and the ways to reform the quadratic form.
- in $P$ there can be blocks $\{\{1,1\},\{1, -1\}\}$ with correspondance of $\{\{\lambda, 0\},\{-\lambda, 0\}\}$ in $D$
- Cor. (not from above since $P$ has no need to be orth.) $A$ sym. $\Rightarrow A$ diag. 
### 14
#### 14.1 Sylvester
- Sylv is only on $Q(V)$, the quadratical forms
- .2.a number of pos. and neg. Eigenval.
- .2.c compute Cholesky and check the sign of elements in $D$ which are the $\lambda$.
- Mail Mario: if no Hauptmin. $= 0$, then Vorzeichnenwechsel of them is $r$, $(n-r,r)$.
#### 14.2 spd
- for $q \in Q(V)$ in an $\mathbb{R}$-VS, we say $spd(q) \Leftrightarrow \forall_{\bar{a} \in V} q(\bar{a})\ge 0$, $>$ for $pd(q)$.
- Cholesky only on $spd(A)$, with $p_{ii} = 1$ and $d_{ii} > 0$ .8
- $spd(q) \Leftrightarrow Sylv(q)=(r,0) \Leftrightarrow \exists_{l_1, ..., l_n \in V^*} q(v) = \sum_{i=1}^n l^2_i(v)$ .7
- $pd(q) \Leftrightarrow Sylv(q) = (n, 0)$ (n is the max) $\Leftrightarrow$ there's a basis of $V^*$, $l_1, ..., l_n$, $q(v) = \sum_{i =1}^n l_i^2(v)$ 
- $spd(A) \Leftrightarrow$ all real coef. of $\chi_A(-X)$ are $\ge 0$  (ez, not zerfallen) $\Leftrightarrow A = B^TB$ (in any way) $\Leftrightarrow \langle \cdot, \cdot \rangle$ 
- $pd(A) \Leftrightarrow$ all Leithau. $> 0 \Leftrightarrow$ has a Cholesky with $D >0$.
- $pd(q_1)$ then there's $\underline{v}$ s.t. $M(q_1, \underline{v}), M(q_2, \underline{v})$ are diagonal.
### 15
#### 15.1 Adjoint
- $\langle f(v), w \rangle = \langle  v, f^*(w) \rangle$, if $dim(V) \ge \omega$ see 15.1.1, else $f^*:W \rightarrow V$ for $f: V \rightarrow W$, *linear* 15.1.6
- if $f$ in $\mathbb{R}^n$ then $f^* = f^{ad}$, and $M(f^*, \underline{w}, \underline{v}) =M(f, \underline{w}, \underline{v})^*$, conj. trans. (hermitian don't change)
- For also inf. VS: $ker(f^*) = (im(f))^\bot$,  $f$ ismorphism $\Leftrightarrow f^* = f^{-1}$ 15.1.12
#### 15.2 Normal Functions
- $f$ normal $\Leftrightarrow f \circ f^* = f^* \circ f$, of $f$ and $f^*$ eigenvec. are the same and eigenval. are conj.
- Take an ONB of $V$ and let $f$ be the function with those eigenvec. then $f$ is normal .4
- There is a $\underline{v}$ ONB s.t. $M(f,\underline{v})$ is diag. $\Leftrightarrow f$ normal
- $A$ orth. $\Leftrightarrow$ exists $\underline{v}$ ONB s.t. $M(f, \underline{v})$ diagonal with every $|\lambda_i| = 1$.
- $f$ orth. is a VS with $\langle \cdot, \cdot \rangle$ isomorphism in $\mathbb{R}$ and $f$ unitary in $\mathbb{C}$, $\langle f(v), f(w) \rangle = \langle v, w \rangle$ 11.2.19
-  $R \in \mathbb{R}^{n \times n}$ is orth. $\Leftrightarrow$ $R^T = R^{-1}$; and $C \in \mathbb{C}^{n \times n}$ is unitary $\Leftrightarrow C^* = C^{-1}$ also: ([ext](https://en.wikipedia.org/wiki/Unitary_matrix), and [ext](https://en.wikipedia.org/wiki/Orthogonal_matrix))
- [ext](https://en.wikipedia.org/wiki/Matrix_similarity): for $C \in \mathbb{C}^{n \times n}$: $C$ normal $\Rightarrow C$ diag.; $(C^* = C^{-1}) \lor (C = C^*) \lor (C^* = -C) \Rightarrow C$ normal
- blue table:
	- $f$ orth. ($\Leftrightarrow \forall_{v \in V} ||f(v)|| = ||v||$) ONB with eigenval on the unit circle, $|\lambda_i| = 1$
	- $f$ selfadj. real eigenval, $\lambda_i = \lambda_i^*$
- $\sqrt{2}w = x + iy$, $(w, \bar{w})$ ONS $\Rightarrow (x,y) ONB$ of $span(w, \bar{w})$, useless? 15.2.9
- $f$ normal $\Leftrightarrow$ the matrix has $\lambda$s on the diagonal and weird $2 \times 2$ blocks, 15.2.10
- $f$ orthogonal $\Leftrightarrow$ weird matrix .11 $\Leftrightarrow$ $f$ is isom. $\Leftrightarrow \langle f(v) , f(w) \rangle = \langle v, w \rangle \Leftrightarrow ||f(v)|| = ||v||$ .6
### 16
#### 16.1 Teilbarkeit
- $a | b \Leftrightarrow \exists_{c} a \cdot c = b$, $a \widehat{=} b \Leftrightarrow a | b \land b|a \Leftrightarrow (a) = (b)$.
- We then define $\widehat{a} \preceq \widehat{b} \Leftrightarrow a | b \Leftrightarrow (a) \subseteq (b)$, $ggT$ and $kgV$ defined.
- $a$ is a $gT$ of $B$ $\Leftrightarrow B \subseteq (a)$. $a$ is $ggT(B)$ $\Leftarrow (a) = (B)$ if $B$ is Hauptid. then $\Rightarrow$.
#### 16.2 ID and PID
- in ID: $(ac = ab \land c \not = 0) \rightarrow a = b$, $ab = 0 \rightarrow (a = 0 \lor b = 0)$
- in a PID there is always a $ggT$ and a $kgV$ same holds in a FD (.4.23)
- in an ID: $a \widehat{=} b \Leftrightarrow \exists_{x \in A^\times} a = bc \Leftrightarrow (a) = (b)$ every princ. ideal is unique up to mult. with a unity.
#### 16.3 ggT
- $ggT(a,b)$ is the minimal ideal $(a, b) = (a, a-b)$ and also compute $mod.$ to simplify
- $ggT(a,b,c)$ where compute $d :=ggT(b,c)$ is easy, you can then just check if $a | d$
- in $\mathbb{Z}$ at least you can write $gcd(a,b) = \lambda_1 \cdot a  + \lambda_2 \cdot b$ to do that use the matrix as in .3
- in $\mathbb{K}[X]$ but also in $\mathbb{Z}$ for $gcd(a,b)$ you can compute $a =c\cdot b + d$ and then $gcd(a,b) = gcd(a,d)$.
#### 16.4 Factorial Rings
- Define $p$ is prime iff. $p | ab \rightarrow (p|a \lor p | b)$ and irr. if $p = ab \rightarrow a \in A^\times \lor b \in A^\times$.
- $0$ is prime $\Leftrightarrow A$ is ID; also in ID $p \not = 0$ and prime $\Rightarrow p$ is irr.
- Def $\alpha: \mathbb{P}_A \Rightarrow \mathbb{N}_0$ $supp(\alpha) := \{p \in \mathbb{P}_A| \alpha(p) \not = 0\}$. $\mathbb{P}_A^\alpha : = \prod_{p \in supp(\alpha)}p^{\alpha(p)}$, $fac(a) = (c, \alpha)$ s.t. $a = c\mathbb{P}^\alpha_A$
- in any ID the factorisation $(c, \alpha)$ is unique
- in an FD every $a \in A \setminus \{0\}$ has a $(c, \alpha) \in A^\times \times \mathbb{N}_0$.
- in a FD $c\mathbb{P}_A^\alpha | d\mathbb{P}_A^\beta \Leftrightarrow \alpha \preceq \beta$; PID $\Rightarrow$ FD
- $A$ FD $\Leftrightarrow$ irr. $\rightarrow$ prime $\land$ for every $(a_n)_{n \in \mathbb{N}}$ s.t. $(a_1) \subseteq (a_2) \subseteq ...$ then $k \in \mathbb{N}$ s.t. $(a_k) = (a_{k + 1}) = ...$ 
### 17
#### 17.1 Smith
- Define Spalten- Zeilenoperationen, add and sub. and mult. it by $\lambda \in A^\times$.
- $Z \cdot A \cdot S = B$ for inv. mat. $Z$ and $S$, $A \sim B$, $|det(A)|=|det(B)|$, $|det(Z)| = |det(S)| = 1$.
- We get a new $\sim$ and create new equivalence classes, rappresentative is Smith
- Smith: . $\lambda_1 |...|\lambda_l$ for $l =\min(m, n)$ (16.4.17), it always exists.
- 17.3.5
#### 17.2 Cauchy-Binet
- $A_{I, J}$ you forget useless rows and columns, it must not be square.
- $det(AB) = \sum_{J \subseteq \{1, ..., n\}, |J| = m}(det(A_{I, J})(det(B_{J, I}))$ for $AB \in \mathbb{K}^{n \times n}$; $m>n \Rightarrow det(AB) = 0$.
- $m>n \Leftrightarrow det(AB) = 0$, $m = n \Leftrightarrow det(A)det(B)$.
- Minoref.: for $|L| = |I|$, $det((AB)_{I, L}) = \sum_{J \subseteq \{1, ..., n\}, |J| = m}(det(A_{I, J})(det(B_{J, L}))$, $AB$ mustn't be $n \times n$
- *minor$_k$*, the ideal of every [minor](https://www.biancahoegel.de/mathe/algebra/minor.html) of order $k$, ideal are decreasing for "$\subseteq$" .13
#### 17.3
- $d_k(M)$ in the $gcd$ of all minors of order $k$, also $d_1(M)| ... |d_k(M)$, (Determinantenteiler) .3
- $d_k(M) = c_1, ..., c_k$, long way to get smith($M$), .4
- $c_j(M)$ is the $jj$th coeff. of $Smith(M)$; (Elementarteiler).
- $M \sim N \Leftrightarrow d(M) = d(N)$ .7.b, ez criterion for checking $\sim$.
#### 17.4 Cayley-Hamilton
- $A \approx B \Leftrightarrow B = P^{-1} A P$ where $P$ is a change of basis $\Rightarrow$ they share everything
- $P_iA =AP_i \Rightarrow (PQ)_A = P_A Q_A$
- ==17.4.8 $P_A = 0 \Leftrightarrow \exists_{Q \in K[X]^{n \times n}} P = (XI_n -A) Q$==
- ==$P\cdot ch(b) = ch(A) \cdot Q \Rightarrow AP_A = P_AB$, 17.4.9==
- $A \approx B \Leftrightarrow ch(A) \sim ch(B) \Leftrightarrow d(ch(A)) = d(ch(B)) \Leftrightarrow$ same Smith.
- [ext](https://en.wikipedia.org/wiki/Matrix_similarity): $A \approx B \Leftrightarrow B = P^{-1} A P$ where $P$ is a change of basis $\Rightarrow$ they share everything
- Algorithm .12
	1. Compute $Smith(ch(A)|I_n)$ which gives you $(S|L)$
	2. Compute $Smith(ch(B))=:T$ note the Zeilenoperationen.
	3. Now take $L$ and inverte the Zeilenoperationen noted before this gives you $P$
	4. Decompose $P \in K[X]^{n \times n}$ in $X^{n-1} P_{n-1} + ... + P_0$, for $P_{n-1}, ..., P_0 \in K^{n \times n}$
	5. Now evaluate $B$ in $P$ to get $R:=P_B$ and define $R^{-1} B R =A$.
- $A \approx_K B \Leftrightarrow A \approx_L B$, for $K \subset L$ fields .14
#### 17.5 Frobenius
- $Smith(ch(C_p))$ is easy $I_n$ con $p$ in fondo. $Frob(A)$ is like smith but with $C(p_1),...,C(p_m)$.
- Also $Smith(Ch(Frob(A)))$ is $I$ with $p_1, ..., p_m$ on the end of the diagonal; $A \approx Frob(A)$.
- $c(ch(A)) = (1, ..., 1, p_1, ..., p_m)$ then $c_m = \mu_A$ and $\chi_A = \prod c$.
- How to find$Frob(A)$: compute $Smith(ch(A))$, then read $p_1, ..., p_m$.
- For any quad. $A$, there's $(p_1, ..., p_n), p_1|...|p_n$ with Frob(A), $\mu_A = p_m, \chi_A=(-1)^np_1\cdot ... \cdot p_m$.
- To find $(p_1, ..., p_m)$, compute $Smith(ch(A))$, there you have $p_1, ..., p_m$.
#### 17.6 Weierstraß
- $Wei(A)$ eind. bis auf Reih. and $p_1, ..., p_m$ are powers of prime polyn. in $K[X]$; $A \approx Wei(A)$.
- How to compute: compute $Frob(A)$ then for every block ($> 1 \times 1$) split it in prime polyn .3.b
#### 17.7 Jordan
- $J(\lambda, n)$, $\chi_{J(\lambda, n)} = \mu_{J(\lambda, n)} = (x -\lambda)^n$. For any Eigenwert you build a block respecting the mult.
- If we are in no ACF and $\chi_A$ doesn't zerfällt, then the $Jord(A)$ is not defined.
### Arithmetic Tricks
- $xy = \frac{1}{4}((x + y)^2 - (x -y)^2)$, for Sylv. Sign and Cholesky
- $x^d - y^d = (x -y)(x^{d-1} +x^{d-2}y +...+y^{d-1})$
- $(AB)^T = B^T A^T$ 11.3.5
- for $V, W$ $F$-VS, $|V|=|W|>|F| \Rightarrow V \cong W$
- $deg(\chi_A) = n$ for $A \in K^{n \times n}$
- $I \cap J$ is an ideal


### To Memorise
- Gram-Schm. want $(w_i)_{i \in I}$ $w_1 = v_1$, $w_2 = v_2 - \frac{\langle v_2, w_1\rangle}{|w_1^2|}w_1$, $w_3 = v_3 - \frac{\langle v_3, w_1\rangle}{|w_1|^2}w_1 - \frac{\langle v_3, w_2 \rangle}{|w_2|^2}w_2$.
- $det(AB) = \sum_{J \subseteq \{1, ..., n\}, |J| = m}(det(A_{I, J})(det(B_{J, I}))$ for $AB \in \mathbb{K}^{n \times n}$; $m>n \Rightarrow det(AB) = 0$.
- Minoref.: for $|L| = |I|$, $det((AB)_{I, L}) = \sum_{J \subseteq \{1, ..., n\}, |J| = m}(det(A_{I, J})(det(B_{J, L}))$, $AB$ mustn't be $n \times n$