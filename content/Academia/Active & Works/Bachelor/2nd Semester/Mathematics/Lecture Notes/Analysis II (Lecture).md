Hold by Prof. Reinhard Racke at the #UniKonstanz during the #2nd_Semester. Here follows a recap of all chapters relevant for the exam.
## Recap
### 9
#### 9.3 Taylorreihen
- $f :[a,b] \rightarrow \mathbb{R}$, there is a $c \in (a,b)$ s.t. $f(b) = \sum_{j =0}^n \frac{f^{(j)}(a)}{j!}(b-a)^j+\frac{f^{(n+1)}(c)}{(n+1)!}(b-a)^{n+1}$ .12
- ==.13==
- $f \in C^\infty([a, b], \mathbb{R})$ s.t. $\exists_{c >0}\forall_{n \in \mathbb{N}}\forall_{c \in [a, b]} |f^{(n)}(x)| \le c^n$ $\Rightarrow \sup_{x \in [a, b)} \sup_{|h| \le h_0, x \pm h \in[a,b]}|R_n(x,h)| \rightarrow 0 \textit{ for }n \rightarrow \infty$.
-  for $f \in C^\infty(U(x), \mathbb{R})$: $f(x+h) = \sum_{j =0}^\infty \frac{f^{(j)}(x)}{j!}(h)^j$ .16 such func. are called analytisch .18
#### 9.4 Weierstraßsche Approximation
- for $f\in C([a,b], \mathbb{R})$: ex. $P_n$ s.t. $|f(x) - P_n(x)| < \epsilon$, coeff. $a_j^{(n)}$ dep. on $n$ which dep. on $\epsilon$ .21
- ==.22==
- $(P_nf)(x):= \sum_{j=0}^n \left(\begin{smallmatrix}n\\j\end{smallmatrix}\right)x^j (1-x)^{n-j}f(\frac{j}{n})$ is the formula to find each $a_j^{(n)}$ given $n$ .23
- Cor: the system of Polynomials is dense in $C(J, \mathbb{R})$ respect to $||\cdot||_\infty$ .23
- Also: $T_n(x) = a_0 + \sum_{j=1}^n (a_j \cos(jx) + b_j \sin(jx))$, the trig. sum is dense in $C(J, \mathbb{R})$ res. $||\cdot||_\infty$ .24
#### 9.5 ONS
- Let $\delta_{mn} := \langle v_n, v_m \rangle$ s.t. $n \not = m \rightarrow \delta_{mn} =0$, exam. at the beginning, ONB of $C(\mathbb{R}, \mathbb{R})$ if $2 \pi$-periodic
- Note: in $C(\mathbb{R}, \mathbb{R})$ is $\langle f, g \rangle:=\int^\pi_{-\pi}f(x)g(x)dx$. ==Q:? see script, p.119==.
- def. OS if $\langle u_n, u_m \rangle = c_n\delta_{nm}$, ONS if $c_n = 1$ i.e. $||u_n||_2:=\sqrt{\langle u_n, u_n \rangle} = 1$ .25
- Gram-Schm. want $(w_i)_{i \in I}$ $w_1 = v_1$, $w_2 = v_2 - \frac{\langle v_2, w_1\rangle}{|w_1^2|}w_1$, $w_3 = v_3 - \frac{\langle v_3, w_1\rangle}{|w_1|^2}w_1 - \frac{\langle v_3, w_2 \rangle}{|w_2|^2}w_2$.
- $L^2 := \{C(\bar{I}, \mathbb{R}), ||\cdot ||_2\}$ _closed under convergence_ (vervollständigt)
- $\{u_n\}_{n \in \mathbb{N}} \subset L^2$ an ONS: $f_n := \langle f, u_n \rangle \in \mathbb{R}$ and $s_n [f](x):= \sum^n_{j = i} f_ju_j(x)$, so: $s_n \rightarrow f$ .26
- $\sum_{j=1}^m |\int_a^bf(x)u_j(x) dx|= \sum_{j = 1}^n |f_j|^2 \le ||f||_2^2 = \int_a^b f^2(x) dx$
- $||s_n[f]||_2 \le ||f||_2$, we are approaching from below since we sum pos elements.
- $\sum^\infty_{j= 1}|f_j|^2 = ||f||_2^2 \Leftrightarrow||f - s_n||_2 \rightarrow 0$ , ==boh== & $(s_n)_n$ conv.
- $\{u_m\}_{n \in \mathbb{N}} \subset L^2(I, \mathbb{C})$ ONVS $\Leftrightarrow \forall_{f \in L^2(I\mathbb{C})} \sum^\infty_{j =1} = ||f||^2_2$ (.28) $\Leftrightarrow \forall_{f \in L(I, \mathbb{C})}\forall_{n \in \mathbb{N}} f_n = 0 \rightarrow f = 0$ .30
- ==but .29?==
- The Fourier Serie is the best ==.32==
#### 9.6
- for $\mathbb{R}$: $f(x) = a_0 + \sum_{j=1}^\infty (a_j \cos(jx) + b_j \sin(jx))$: $a_0 = \frac{1}{2\pi} \int_{-\pi}^\pi f(x)dx$; $a_j = \frac{1}{\pi}\int^\pi_{-\pi}f(x) \cos(jx)dx$; $b_j = \frac{1}{\pi}\int^\pi_{-\pi}f(x)\sin(jx)dx$ 
- for $\mathbb{C}$: $f_n := \langle f, u_n \rangle = \frac{1}{\sqrt{2 \pi}} \int^\pi_{-\pi}f(x)e^{-inx}dx$; $a_0 = \frac{1}{\sqrt{2 \pi}} f_0$; $a_n = \frac{1}{\sqrt{2 \pi}}(f_n + f_{-n})$; $b_n  = \frac{-i}{\sqrt{2 \pi}}(f_n - f_{-n})$
- $||f - \sum_{j = -n}^n f_ju_j||_\infty \le \frac{1}{\sqrt{\pi n}}||f'||_2$ .33 ==make Bsp. .34==
### 10
#### 10.1 Normed VS
- Normed spaces examples
	- $(C(\bar{I}, \mathbb{R}), ||\cdot||_p)$, $||f||_p := (\int_I |f|^p)^{\frac{1}{p}}$ is normed space
	- The space of sequences $(l_p, ||\cdot ||_p)$ s.t. $|| \cdot ||_p: x \mapsto (\sum^\infty_{j=1}|\xi|^p)^{\frac{1}{p}}$ & infinite vectors in $\mathbb{C}$, $l_p := \{x = (\xi_n)_{n \in \mathbb{N}}|\forall_{j \in \mathbb{N}} \xi_j \in \mathbb{C}, \sum^\infty_{j = 1} |\xi_j|^p < \infty\}$, bounded seq. in $\mathbb{C}$, similarly for $p \rightarrow \infty$
- $\frac{1}{p} + \frac{1}{q}  =1$ then ([watch](https://youtu.be/yIXahhfRbTc))
	- Young: $\forall_{a, b > 0 (\in \mathbb{R})} a \cdot b \le \frac{a^p}{p} + \frac{b^q}{q}$
	- Hölder: $\sum_{ i = 1}^\infty |\xi_i \cdot \eta_i| \le ||x||_p \cdot ||y||_q$ ($\Leftrightarrow ||xy||_1 \le ||x||_p \cdot ||y||_q$)
	- Mikowski: $||x + y||_p \le ||x||_p + ||y||_p$ 
#### 10.2 Stetigkeit und Kompaktheit
- Bolzano-Weierstraß: $(x_k)_{k \in \mathbb{N}} \subset \mathbb{R}^n$ bounded $\Rightarrow$ there is a converging sequence in $(x_k)_{k \in \mathbb{N}}$.
- $K \subset \mathbb{R}^n$ clos. and boun. $\Leftrightarrow K$ is compact $\Leftrightarrow$ every $(x_k)_{k \in \mathbb{N}}$ has $(x_{k_j})_{j \in \mathbb{N}}$ s.t. $\lim_{j \rightarrow \infty} x_{k_j} \in K$ .5
- $f$ cont. $\Leftrightarrow f:$ op/cl comes from op/cl $\Leftrightarrow \forall_{(x_k)_{k \in \mathbb{N}} \subset X}, x_k \rightarrow x, f(x_k) \rightarrow f(x)$ .6
- $f: X \rightarrow Y$ cont., $K \subset X$ compact $\Rightarrow f(K)$ compact & $f|_K$ glm. stet.
- Nichtzus. $\Leftrightarrow \exists_{A, B \not = \emptyset} A \cap B = \emptyset \land X = A \cup B$ ($A, B$ both open or both closed) .11
- Zwischenwe.: $X$ zusam., $f: X \rightarrow Y$ cont. $R(f)$ ($=Im(f)$ as a space) is zusam. .12
- a cont. fun $\gamma: [a, b] \rightarrow \mathbb{R}^n$ is a _Weg_; for all $m_1, m_2$ then $\gamma: [a, b] \rightarrow M$ s.t. $\gamma(a) = m_1 \land \gamma(b) = m_2$ 
- wegzusamm $\Rightarrow$ zusamm. .15; a lin. func. is cont. iff it is bounded
- $L(X, Y)$ lin. bound. cont. func.; $||\cdot ||: L(X, Y) \rightarrow \mathbb{R}^+_0, A \mapsto \sup_{||x|| = 1}||Ax||$($=\sup_{x \not =0}\frac{||Ax||}{||x||} = \sup_{||x||\le 1}||Ax||$)
- For $A$ lin.: $A$ stet. $\Leftrightarrow A$ stet. in $0 \Leftrightarrow \sup_{||x||_X =1} ||Ax||_Y < \infty \Leftrightarrow \exists_{c \in \mathbb{K}}\forall_{x \in X} ||Ax||_Y\le c||x||_X$ (Blatt 3.)
### 11
#### 11.1 Diff. Func.
- $(f_k)_{k \in \mathbb{N}}$ glm con. iff $\lim_{k \rightarrow \infty}||f_k - f||_\infty = 0$ 
- Sequences of continuous functions glm. converge to continuous functions .2
- $f$ is diff. if there is such $A(x), r(x, \cdot)$ s.t. $f(x + h) = f(x) + A(x)h + r(x,h)|h|$ ==.3==
- For $im(f) \subset \mathbb{R}$ but also $im(f) \subset \mathbb{R}^m$ if $f$ always part. diff $\Rightarrow$ f diff.
- Note: $A(x)$ is unique and $r(x, 0)=0$ stet. in $0$ $\Rightarrow f^{-1}$ is defined
- For $im(f) \subset \mathbb{R}$ but also $im(f) \subset \mathbb{R}^m$ if $f$ always part. diff $\Rightarrow$ f diff.
- ext. all $\partial_i$ are stetig $\Rightarrow f$ diff. ($A(x) = \nabla f(x) \Rightarrow f'(x, h) \not = \langle \nabla f(x) , h \rangle$ ==why??==)
- $f$ diff in $x \Rightarrow f$ cont. in $x$
- ext: $\lim_{t \rightarrow 0}\frac{f(x + t) - f(x)}{t}$ der. in $\mathbb{R}$ in $x$, in $\mathbb{R}^n$, $h \in \mathbb{R}^n$ s.t. $|h| = 1$, $D_y(h):= \lim_{t \rightarrow 0} \frac{f( y + th)- f(y)}{t}$, $f$ diff. $\Rightarrow \forall_{h \in \mathbb{R}^n}D_y(h) = \langle \nabla f (t), h \rangle$ 
- $f: U(\subset \mathbb{R}) \rightarrow \mathbb{R}$, $\frac{\partial f(x)}{\partial x_i}:=\lim_{h \rightarrow 0}\frac{f(x+he_i) - f(x)}{h}$  .6
- $\nabla f(x) := (\frac{\partial f(x)}{\partial x_1}, ..., \frac{\partial f(x)}{\partial x_n})^T =: (\partial_1 f(x), ..., \partial_n f(x))^T$
- Note: $f'(x) = (\nabla f(x))^T$ if $f: U(\subset \mathbb{R}^n) \rightarrow \mathbb{R}$ so $f'(x)$ is an orisontal vector.7
- $$J_f(x):= \begin{pmatrix}  \partial_1 f_1(x) & ... & \partial_n f_1(x)\\  \vdots & & \vdots \\ \partial_1 f_m(x) & ... & \partial_nf_m(x)  \end{pmatrix} =: (\partial_1 f, ..., \partial_n f)(x) =: \frac{\partial f(x)}{\partial x}$$for $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$, it is a gen. of the $\nabla$-operator .8, 
- also $f': U \rightarrow L(\mathbb{R}^n, \mathbb{R}^m), x \mapsto f'(x)$, or similarly $f': (x,h) \mapsto f'(x)\cdot h$ (matr. mult) .10
- $f: U (\subset \mathbb{R}^n) \rightarrow \mathbb{R}: (fg)' = gf' + fg'  \land (g \circ f)' = (g' \circ f) \cdot f' \land (f + g)' = f' + g' \land (\alpha f)' = \alpha f'$ .11
- $\nabla f(x_0) \cdot h_0$ for $|h_0|$ is the _Richtungsableitung von $f$  in Richtung $h_0$ an der Stelle $x_0$_ .12
	- To Compute: $D_x(h) = \lim_{t \rightarrow 0} \frac{f(x  + th) - f(x)}{t}$, $f$ diff in $x$, $\forall_{h \in \mathbb{R}^n} D_x(h) = \langle \nabla f(x), h \rangle$ 
- _Höhelinien_: $N_f(c) := \{x \in U | f(x) = c\}$ clear, $U$ is the domain of $f: \mathbb{R}^2 \rightarrow \mathbb{R}$
- _Falllinien_: for $\beta: \mathbb{R} \rightarrow \mathbb{R}^2$ s.t. $\beta'(t) = \nabla f(\beta(t))$ ==uhm==
- $div f : \mathbb{R}^n \rightarrow \mathbb{R}, x \mapsto div f(x) := \sum_{i = 1}^n \partial_i f_i (x)$; $rot f: \mathbb{R}^3 \rightarrow \mathbb{R}^3, x \mapsto (\partial_2f_3(x)-\partial_3f_2(x),  \partial_3f_1(x) - \partial_1f_3(x),  \partial_1f_2(x) - \partial_2f_1(x))^T$; $\Delta: C^2(\mathbb{R}^n, \mathbb{R}) \rightarrow C(\mathbb{R}^n, \mathbb{R}), f \mapsto \sum_{i = 1}^n \partial_i^2 f_i$, $\Delta(f) = div(\nabla(f))$, called _Laplace-Operator_ .14
- $f: U (\subset \mathbb{R}^n) \rightarrow \mathbb{R}^n$ inj. diff in $a$ s.t. $\det f'(a) \not = 0$ (so that $f'(a)$ is an inv. matrix), for $b := f(a)$ for $f(a)$ is an inner point of $f(U)$ (or you can't derivate) def. $g: = f^{-1}:f(U) \rightarrow \mathbb{R}^n$. then $g'(b) = (f'(a))^{-1}$, see those as matrices. Maybe it is to say when $\cdot^{-1}$ and  $\cdot '$ commute .16
- Actually you need only $\det f'(a) \not = 0$ .17
- ==Q! dom(g) wtf? .18==
- $f \in C^1(U, \mathbb{R}^n)$, inv., $f(U)$ open, $f^{-1} \in C^1$ then $f$ is a Diffeomorphismus on $U$. .19
#### 11.2 Mittelwertsatz
 - for $a, b \in \mathbb{R}^n, t \in (0, 1)$: $\gamma_{ab}(t) := a + t(b-a)$; $\Gamma_{ab} := \{x \in \mathbb{R}^n| \exists_{t \in (0, 1)} x = \gamma_{ab}(t)\}$
 - Mittelwertsatz: $\exists_{c \in \Gamma_{ab}} f(b) = f(a) + f'(c)(b-a)$, $\Gamma_{ab}$ is a the Gerade from $a$ to $b$, for $Im(f) \subseteq \mathbb{R}$ 
 - It's ok $\gamma: [0,1] \rightarrow U$ s.t. $\gamma(0) = a \land \gamma(1) = b$ with $\gamma$ diff. so $f(b) = f(a) + f'(\gamma(\theta))\gamma'(\theta)$, $\theta \in (0, 1)$
 - for $f: U \rightarrow \mathbb{R}^n$, $f' = 0 \Leftrightarrow f = k$ for $k \in \mathbb{R}$
 - $\partial_1 f, ..., \partial_n f$ cont. around $a$ $\Rightarrow f$ diff. .23, comp both lim. $\partial_i f(a)$, for $Im(f) \subset \mathbb{R}^n$ 
#### 11.3 Höhere Ableitungen
- $f''': U \rightarrow L(\mathbb{R}^n , L(\mathbb{R}^n, L(\mathbb{R}^n, \mathbb{R}^m)))$ or $f'': U \times \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}^m, (x, h, k) \mapsto f''(x, h, k) = (f''(x)h)k$
- In general $f^{(p)}: U \times (\mathbb{R}^n)^p \rightarrow \mathbb{R}^m, (x, h_1, ..., h_p) \mapsto f^{(p)}(x, h_1, ..., h_p)$
- also remember: $\partial_j\partial_i f(x) = f''(x, e_i, e_j)$ .24
- Schwarz: if $f \in C^2(\mathbb{R}^n, \mathbb{R}^m) \land U$ open $\Rightarrow \forall_{i, j \in \{1, ..., n\}} \partial_i \partial_j f(x) = \partial_j \partial_i f(x)$ .25
- ==check .26==
- Taylor: $f(x + h) = f(x) + f^{(1)}(x, h) + ... + \frac{1}{p!}f^{(p)}(x, h, ..., h) + R_p(x, h)$, .27 where $R_p(x, h) = \frac{1}{(p+ 1)!}f^{(p +1)}(x +\theta h, h, ...,h )$ for $\theta \in (0, 1)$; $Im(f) \subset \mathbb{R}$ and $f^{(n)} = $ $f(x +h) = \sum^p_{|\alpha| = 0, \alpha \in \mathbb{N}_0^n}\frac{1}{\alpha!} \partial^\alpha f(x)h^\alpha + R_p(x, h)$ where: $h^\alpha := h_1^{\alpha_1} \cdot ... \cdot h_n^{\alpha_n}$ same for the others
	- e.g. $f(x, y) = f(a, b) + f_x(a, b)(x -a) + f_y(a, b)(y -b) + \frac{1}{2}f_{xx}(a, b)(x -a)^2$ $+ \frac{1}{2}f_{yy}(a, b)(y -b)^2 + f_{xy}(a,b)(x-a)(y-b)+R_2(x, h)$ for $R_2 (x, y) = \frac{1}{6} f''' (x + \theta h, h, h, h)$ for $\theta \in (0, 1)$.
- $Im(f) \subset \mathbb{R}$: $a$ critical point of $f$ $\Leftrightarrow \nabla f(a) = 0 \Leftrightarrow \forall_{h \in \mathbb{R}^n}f'(a, h) = 0$
- If $a$ extremstelle of $f \Rightarrow a$ critical point of $f$ .29
	- for $f \in C^2(\mathbb{R}^n, \mathbb{R})$ then $Hess_f(x) := (\partial_i\partial_jf(x))_{i, j \in \{1, ..., n\}}$ .31, .32, ==.34==
	- $pd(Hess_f(a)) \Rightarrow a$ minimum; $nd(Hess_f(a)) \Rightarrow a$ maximum; $Hess_f(a)$ indef. $\Rightarrow a$ not an extr.
- $M$ convex if the line between any two $m_1, m_2$ is in $M$ .35
- $im(f) \subset \mathbb{R}$ op, conv: $f$ conv. $\Leftrightarrow \forall_{x_1, x_2, x_1 \not = x_2} \forall_{t \in (0, 1)} f(x_1 +t(x_2 - x_1)) \le f(x_1) + t(f(x_2)- f(x_1))$
- if only $<$ it is streng convec, also $f$ conv. $\Rightarrow$ $f$ cont. .37
- $f$ convex $\Leftrightarrow \forall_{x_1, x_2 \in U} f(x_1 + t(x_2 - x_1)) \le f(x_1) + t(f(x_2)-f(x_1))$, with $>$ for streng convex .36
- .38 if $f$ diff.
- if $pd(Hess_f) \Rightarrow f$ streng conv.; $spd(Hess_f) \Rightarrow f$ conv.
#### 11.4 Extrema mit Nebenbedingungen
- ext: Berechnung der Extrema von $f: \mathbb{R}^n \rightarrow \mathbb{R}$ ($n = 2$ in the Klausur)
	1. $\nabla f(x) =^! 0$ and get the points, $P_i$
	2. Compute $Hess_f(x)$ and insert $P_i$
		1. $pd(Hess_f(P_i))\Rightarrow P_i$ is a min.
		2. $nd(Hess_f(P_i)) \Rightarrow P_i$ is a max.
		3. if $Hess_f(P_i)$ is indef: $P_i$ is Sattelpunkt
		4. else: we can't say (for $spd$ and $snd$)
- $im(f) \subset \mathbb{R}$, else there can't be an exercise but to compute the Jacobi.
	1. Checks:
		1. Check if $\wedge_{i = 1}^n (g_1 = 0, ..., g_m = 0)$ (for $m < n$) holds for the extrema of $f$.
		2. Check that $M = \{ x \in \mathbb{R}^n | g(x) =0\}$ is compact (necess. to use this method).
			1. Remember $M = g^{-1}(\{0\}) \land g$ stet $\land$ ($\{0\}$ abg.) $\Rightarrow M$ abg. 
	2. Solve $\sum_{i = 1}^n (\nabla f(x))_i + \lambda_i (\nabla g(x))_i =^! 0 \land g_1 =^! 0 \land ... \land g_m =^! 0$, and get $P_i$ for some $\lambda_i$ 
	3. Compute $f(P_i)$ and compare them, they are extrema (not rel.), check if minima or maxima
- If we have $n-m = 1$ then $h: \mathbb{R} \rightarrow \mathbb{R}$
	1. notice $h = f(\phi(t), \psi(t))$ for some $\phi$ and $\psi$ then see simply ==.41 write alg.== 
- Define $F: \mathbb{R}^n \times \mathbb{R}^m \rightarrow \mathbb{R}, (x, \lambda) \mapsto f(x) + \sum_{i = 1}^m \lambda_i g_i(x)$ and then ($\lambda$ is Lagrange Moltiplikator) $\nabla F(x, \lambda) = (\nabla f(x) + \sum_{i = 1}^m \lambda_i g_i(x), g_1(x), ..., g_n(x) )^T$ set all to $0$, .42 is an ez application. ==.43==
- $spd(Hess_F(x_0, \lambda_0)) \lor snd(Hess_F(x_0, \lambda_0)) \Rightarrow x_0$ is extr. of $f|_M$ for $M:=\{x \in U| g_j(0) \forall_{j \in \{1, ..., m\}}\}$ 
	1. compute $\nabla F(x, \lambda) = 0$ and get $x_0$ and $\lambda_0$, then compute $Hess_F(x_0, \lambda_0)$ check if definit.
### 12
#### 12.1 Weglängen
- $\gamma: [a,b] \rightarrow \mathbb{R}^n$, if $\gamma$ stetig diff. and $\forall_{s \in (a, b)}\gamma'(s) \not = 0$ then $\gamma$ is glatt; def. $t = s \mapsto \frac{\gamma'(s)}{|\gamma'(s)|}$
- $L(\gamma): = \int_a^b |\gamma'(s)| ds$; additiv, $\lim_{n \rightarrow \infty} L(\gamma_n) =L(\gamma)$
- $dom(\gamma)= [a,b] \sim dom(\tilde{\gamma})= [c,d]$ if ex. $\phi: [a,b] \rightarrow [c,d]$ s.t. stetig diff. and bij with $\forall_{s \in [c, d]}\phi'(s) > 0$, $\tilde{\gamma}(\tilde{s}) = \gamma(\phi(\tilde{s}))$; the equivalence classes on $\sim$ are a _orientierte stückwise glatte Kurve_.
- Every class has rapresentatvie a $\gamma$ s.t. $|\gamma'(s)| =1$. The _Bogenlänge_ of $\gamma$ is $\int_0^s|\gamma'(t)|dt$ .6 .7
- $k(s):=|\gamma''(s)|$ is called _Krümmung_, $\langle \gamma'(s), \gamma''(s) \rangle = 0$ direction of $k$ and $t$ are $\bot$ .7
#### 12.2 Kurve in der Ebene und im Raum
- for $|\gamma'(s)| =1$, (set speed to 1) we have $t(s) = \left(\begin{smallmatrix} x'(s)\\ y'(s) \end{smallmatrix}\right)$; $n(s) = \left(\begin{smallmatrix} -y'(s)\\ x'(s) \end{smallmatrix}\right)$, now define $\alpha, \beta, \delta, \epsilon$ s.t. $t'(s) =\alpha(s)t(s) + \beta(s)n(s)$; $n'(s) =\delta(s)t(s) + \epsilon(s)n(s)$ like if they were funcitons. But $\alpha = \epsilon = 0$ and $\beta = -\delta$ called ==Frenetsche Gleichungen==
- $a \times b = \left(\begin{smallmatrix} a_2b_3 - a_3b_2\\ a_3b_1 - a_1b_3 \\ a_1b_2 - a_2b_1 \end{smallmatrix}\right)$, def. $b(s) := t(s) \times n(s)$, $b \bot t \land b \bot n \land det(t(s), n(s), b(s)) = 1 \land |b(s)| = 1$
- def. $\tau(s) : = \langle n'(s), b(s) \rangle = \langle -b'(s), n(s) \rangle$ called _Torsion_.
#### 12.3 $m$-dimensionale Flächen im $\mathbb{R}$
- $\gamma: U (\subset \mathbb{R}^m) \rightarrow \mathbb{R}^n$, $m<n$ so $\gamma': U \rightarrow L(\mathbb{R}^m, \mathbb{R}^n)$. $\tau:= \gamma(u) + \gamma'(u, h)$, so $\tau$ is aff. subsp. in $\mathbb{R}^n$
- $\gamma(u, v) = \left(\begin{smallmatrix} f(u) \cos(v) \\ f(u) \sin(u) \\ g(u) \end{smallmatrix}\right)$ _Rotationsfläche_, check $\gamma'(u, v)$ is full rank then $\gamma(u, v)$ is a $2$-Fläche
- $dom(\gamma) = U$ & $dom(\tilde{\gamma}) = \tilde{U}$ then $\gamma \sim \tilde{\gamma} \Leftrightarrow \exists \Phi: \tilde{U} \rightarrow U$ s.t. $\tilde{\gamma} = \Phi(\gamma)$ and $\Phi$ is a diffeomorph. .12 then the class is called $m$-Fläche with the _gleiche Orientierung_ if $det(\Phi')>0$. ==uhm what?==
- ==.13==
### 13
#### 13.1 Measure Theory
- $\mathcal{A} \subseteq \mathcal{P}(X)$ is a $\sigma$-algebra if: (i) $\emptyset \in \mathcal{A}$, (ii) $A \in \mathcal{A} \rightarrow A^c \in \mathcal{A}$, (iii) $(\forall_{n \in \mathbb{N}} A_n \in \mathcal{A}) \rightarrow \bigcup_{n \in \mathbb{N}} A_n \in \mathcal{A}$ .1
- char. of $\sigma$-al., (i) $X \in \mathcal{A}$ (ii) $B \subseteq A \rightarrow A \setminus B \in \mathcal{A}$ (iii) $A \cap B \in \mathcal{A}$ (iv) $\bigcup_{n \in \mathbb{N}} A_n \in \mathcal{A}$ Blatt 9.4
- ==see blatt other rules== & given a fixed $X$ $\bigcap_{i \in I} \mathcal{A}_i$ is a $\sigma$-algebra, so $\sigma(\mathcal{E}) := \bigcap\{\mathcal{A}| \mathcal{E} \subset \mathcal{A} \}$ is the smallest $\sigma$-algebra containing $\mathcal{E}$.
- $\mu: \mathcal{A} \rightarrow [0, \infty]$ a measure on $\mathcal{A}$ if (i) $\mu(\emptyset) = 0$, (ii) $\mu(\bigcup^\cdot_{n \in \mathbb{N}}A_n) = \sum_{n \in \mathbb{N}}\mu(A_n)$
- $\mu$ is said $\sigma$-endlich if ex. $(A_n)_{n \in \mathbb{N}}\subset \mathcal{A}$ s.t. $\bigcup_{n \in \mathcal{N}} A_n = X$ and $\forall_{n \in \mathbb{N}} \mu(A_n) < \infty$ .3
- $\mu(\{x \in X| \lnot M(x)\}) = 0$ : $M(x)$ is true _fast überall_.
- $\delta_x(A) = \chi_A(x) = 1$ if $x \in A$, $0$ if $x \not \in A$; $\zeta(A) := |A|$ if $|A| < \aleph_0$ , $\infty$ if $|A| \ge \aleph_0$ .5
- $\mathcal{A}_E := \{A \cap E| A \in \mathcal{A}\}$ is a $\sigma$-al. $\mu|_E := \mu|_{\mathcal{A}_E}$ then $(E, \mathcal{A}_E, \mu|_E)$ is a measure space
- $\sigma(f):=\{f^{-1}(B)|B \in \mathcal{B}\}$ for $f:X \rightarrow Y$ and $(Y, \mathcal{B})$, $(X, \mathcal{A})$ is the $\sigma$-al. generated by $f$.
- 1. $\Leftrightarrow$ 2. $\Rightarrow$ 3. (3. $\Rightarrow$ 2. if $\mu$ endlich, i.e. $\mu(x)<\infty$)
	1. $\mu$ is $\sigma$-additiv
	2. $(\forall_{n \in \mathbb{N}} A_n \subset A_{n +1})$, so $\bigcup_{n \in \mathbb{N}} A_n =: A(\in \mathcal{A})$: $\lim_{n \rightarrow \infty} \mu(A_n) = \mu(A)$
	3.  $(\forall_{n \in \mathbb{N}} A_{n +1} \subset A_n)$,  $\bigcap_{n \in \mathbb{N}} A_n = \emptyset$ and $\mu(A_1) < \infty$ $\lim_{n \rightarrow \infty} \mu(A_n) = 0$
- (Borel-$\sigma$-algebra) $\mathcal{B}(\mathbb{R}^n) := \sigma(\{(a,b]|a,b \in \mathbb{R}^n \land a<b\})$, all open and closed sets are $\mathcal{B}$-mess. .9
- _Lebesgue-Maß_: $\lambda_n: \mathcal{B}(\mathbb{R}^n) \rightarrow [0, \infty]$ s.t. $\lambda(\prod_{j = 1}^n (a_j , b_j]) = \prod_{j = 1}^n(b_j - a_j)$
- (i) $\lambda(\{x\}) = 0$ (ii) if $\exists_{j \in \{1, .., n\}} a_j b_j \rightarrow \lambda (\prod_{j = 1}^n [a_j , b_j])$ (iii) $\lambda((a,b)) = \lambda([a,b)) = ...$ ez (iv) $\lambda(\mathbb{Q})=0$ (v) $\lambda$ is $\sigma$-end., since $\mathbb{R}^n = \bigcup_{N \in \mathbb{N}} \prod_{j=1}^n [-N, N]$.
- $\lambda(C) = 1 - \frac{1}{3} \cdot \sum_{n = 0}^\infty (\frac{2}{3})^n = 0$ but $|C| = |\mathbb{R}| \Rightarrow \lambda(C) \not = 0$
- $f: X \rightarrow S$, $(X, \mathcal{A})$, $(S, \mathcal{S})$ $f$ $\mathcal{A}$-$\mathcal{S}$-meas. $\Leftrightarrow f^{-1}(\mathcal{S}) \subset \mathcal{A}$ i.e. for all $B \in \mathcal{S}$: $f^{-1}(B) \in \mathcal{A}$, $\mathcal{A}$-meas.: $(S, \mathcal{S}) = (\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$; Borel-Meas if also $(X, \mathcal{A}) = (\mathbb{R}^m, \mathcal{B}(\mathbb{R}^m))$. Meas. comes from meas.
- ext. for $f$ meas. $f: \mathbb{R}^n  \rightarrow \mathbb{R}^n$ and $M \in \mathcal{B}(\mathbb{R}^n) \Rightarrow f^{-1}(M) \in \mathcal{B}(\mathbb{R}^n)$ 
- contant func. are always meas.; $f, g$ meas $\Rightarrow$ $g \circ f$ meas.
- for $(X, \mathcal{A})$, $(S, \sigma(\mathcal{E}))$: $f: X \rightarrow S$ $\mathcal{A}$-$\sigma(\mathcal{E})$meas. $\Leftrightarrow f^{-1}(\mathcal{E}) \subset \mathcal{A}$ .15
- How to find $\mathcal{E}$ of $\mathcal{B}$? Check if with the rules of a $\sigma$-al. you get $(a, b]$ like in .16.(ii)$\Rightarrow$(i)
- For $im(f) \subset \mathbb{R}$: $f$ Borel-meas. $\Leftrightarrow$ $\forall_{a \in \mathbb{R}}\{x \in X| f(x) > a \} \in \mathcal{B}(\mathbb{R}^n) \Leftrightarrow ...$ .16
- $f$ stetig $\Rightarrow f$ Borel-meas.; $(f_k)_{k \in \mathbb{N}}$ Borel-meas $\Rightarrow f$ Borel meas.; $f, g$ meas. $\Rightarrow f\cdot g, f + g, max\{f, g\},$ for $r>0$: $|f|^r$ and for $k \in \mathbb{N}$: $f^k$ are all meas. .18
#### 13.2 Lebesgue Integral
- $f = \sum_{i=1}^k{c_i}\chi_{A_i}$ for $\chi_{A_i} (x) :=$ $1$ if $x \in A_i$, $0$ if $x \not \in A_i$, is a _Stufenf._, $B(X, \mathcal{A}; \mathbb{R})$ meas. bound func.
- like in 1-dim: $(s_k)_{k \in \mathbb{N}} \rightarrow f$. if $f \in B(X, \mathcal{A}; \mathbb{R})$ then a $(s_k)_{k \in \mathbb{N}}$ conv. glm. so the space of the $s_k$ is dense in $B(X, \mathcal{A}; \mathbb{R})$ respect to the $||\cdot ||_\infty$; $f_+ := \max\{f, 0\}$, $f_- := \min\{0, f\}$; $f = f_+ - f_-$ .20
- $\int sd\mu := \sum_{j=1}^k c_j \mu(A_j)$  $(\in [0, \infty])$, $\int f_+d\mu:=\sup\{\int sd\mu| 0 \le s \le f_+\}$; $\int fd\mu := \int f_+d \mu - \int f_- d\mu$ 
- all int. func: $\mathcal{L}^1$ or $\mathcal{L}_1$, in $\int fd\mu$ for $\mu = \lambda$ becomes $\int f(x) dx$, $\int_A fd\mu := \int \chi_Af\mu$ 
- $\{f \in B(X, \mathcal{A}; \mathbb{R})| \mu(dom(f)) < \infty\} \subset \mathcal{L}^1$; $f, g \in \mathcal{L}^1 \land f \le g \Rightarrow \int f d\mu \le \int gd\mu$
- $\mu(A) = 0 \Rightarrow \int_A fd\mu = 0$; $\int_{A \cup^\cdot B} fd\mu = \int_A fd\mu = \int_Bfd\mu$
- $f \ge 0 \land \int f d \mu = 0 \rightarrow f=0$; $|\int f d\mu| \le \int |f| d\mu$; $g \in \mathcal{L}^1(\mu) \land |f| \le g$ respect to $\mu$ $\Rightarrow f \in \mathcal{L}^1(\mu)$ .23
- "$\int$" is _linear_, on limits also for sequences s.t. $0 \le f_n \le f_{n+1}$, lin on $\sum^\infty_{n=1}$ too .24 .25. 26
- Fatou: linear on $\lim \inf_{n \rightarrow \infty}$ .27;
- $(f_n)_{n \in \mathbb{N}}$ meas. $f \in \bar{\mathbb{R}}$ $\mu$-f.ü., $g \in \mathcal{L}^1(\mu)$: $|f_n(x)| \le g(x) \mu$-f.ü. $\Rightarrow f \in \mathcal{L}^1(\mu) \land lim_{n \rightarrow \infty} \int f_n d \mu = \int f d \mu$
- normally $A_i$ macchie di mucca for Riemann $A_i = (a_i, b_i]$, call those $s^{(r)}$ 
- Maj. Krit.: $|f_n|$ s.t. f.ü. $f(x) =f_n(x) \in \overline{\mathbb{R}}$ and ex. $g$ s.t. f.ü. $\forall_{n \in \mathbb{N}}|g(x)| \ge |f_n(x)|$ then $\lim$ com. $\int$.
- for $supp(f):= \overline{\{x \in \mathbb{R}^n| f(x) \not = 0\}}$: call $\overline{\int}f(x)dx:=\inf\{\int s^{(r)}(x) dx| s^{(r)} \ge f\}$ & $\underline{\int}f(x)dx:=\sup\{\int s^{(r)}(x) dx| s^{(r)} \le f\}$; $f$ Riem. int. $\Leftrightarrow \overline{\int}f(x)dx = \underline{\int}f(x)dx := \int f(x)dx$ .29
- $f$ stetig $\Rightarrow f$ Riem. int.; $f$ Riem. int $\Rightarrow f$ Les. int $\land \int f(x) dx = \int f d\lambda$ .30
#### 13.3 Iterierte Integrale (The Italians)
- Tonelli: $f: \mathbb{R}^2 \rightarrow [0,\infty]$ meas.,$\int_{\mathbb{R}^2}f(x, y)d(x, y) = \int_{\mathbb{R}}(\int_{\mathbb{R}} f(x, y) dx) dy = \int_{\mathbb{R}}(\int_{\mathbb{R}} f(x, y) dy) dx$ .32
- Fubini: $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ Les. int. then the same above holds, Fubini holds for $\mathbb{R}^n$.
- Cavalieri: $A \in \mathcal{B}(\mathbb{R})$, $A^t := \{(x_1, ..., x_{n-1}) \in \mathbb{R}^{n-1}|(x_1, ..., x_{n-1}, t) \in A\}$ $\Rightarrow A_t \in \mathcal{B}(\mathbb{R}^{n-1}) \land \lambda_n(A) = \int_\mathbb{R} \lambda_{n-1}(A_t) dt$.
	- compute: prove $A_t$ is meas., compute $\lambda(A_t)$ then integrate $\int_I \lambda_{n-1} (A_t) dt$ for $t \in I$
#### 13.4 Transformationssatz
- $U \subset \mathbb{R}^n$, $\mathcal{B}(U):= \{B \cap U | B \in \mathcal{B}\}$, $\Phi: U \rightarrow \mathbb{R}^n$ meas. $\Rightarrow \mu \circ \Phi^{-1} : \mathcal{B}(\mathbb{R}^n) \rightarrow [0, \infty], A \mapsto \mu (\Phi^{-1}(A))$
- $\mu$ translationsinvariant if $\mu \circ \Phi^{-1} = \mu$ for all translation of the form $\Phi: x \mapsto x + c$ 
- $\mu$ bewegungsinvariant if $\mu \circ \Phi^{-1} = \mu$ for all bewegungen of the form $\Phi: x \mapsto Sx + c$ for $S$ orth.
- $\mu$ translat. on $(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$ s.t. $\mu(W) < \infty$ for $W$ an Einheitswürfel then $\mu = \mu(W)\lambda$.
- $\lambda$ is bewegungs.;
- $T$ sq. inv. matrix $\lambda(T(B)) = |det(T)| \cdot \lambda(B)$ .42
- $U, V \subset \mathbb{R}^n$  op. $\Phi: U \rightarrow V$ a $C^1$-Diffeo, let $f: V \rightarrow  \mathbb{R}$ meas:$f$ int. on $V = \Phi(U) \Leftrightarrow (f \circ \Phi) \cdot |det\Phi'|$ integr. $\Rightarrow \int_{\Phi(U)} f(x) dx = \int_U f(\Phi(z)) \cdot |det\Phi'(z)| dz$ .43
- ==.44==
#### 13.5 Kurven- und Flächenintegrale 
- Vector Field: $v: D (\subset \mathbb{R}^n) \rightarrow \mathbb{R}^n$; $\Gamma \subset \mathbb{R}^n = im(\gamma)$ and $\omega: \Gamma \times \mathbb{R}^n \rightarrow \mathbb{R}^n$ stet. linear in the second argument, then $\omega$ is an $1$-Form in $\Gamma$. Similarly for any $U \subset \mathbb{R}^n$ instead of $\Gamma$ we call $\omega$ an $1$-Form. 
- for $\omega(x, h) = \langle \omega(x), h \rangle$, $\omega(x) = (\omega_1(x), ..., \omega_n(x))^T$ for $\omega_i := \omega(x, e_i)$ 
- ext: example: for any $f$ diff. then $(x, h) \mapsto \langle \nabla f(x), h \rangle$ is an $1$-Form
- call $\int_\Gamma \omega := \int_b^a \omega(\gamma(t), \gamma'(t)) dt$ _Kurvenintegral_; then lin. and for $\Gamma = \Gamma_1 + \Gamma_2$: $\int_\Gamma \omega = \int_{\Gamma_1} \omega + \int_{\Gamma_2} \omega$
	1. Compute: $\int_\Gamma \Omega = \int_\Gamma \langle \omega(\gamma(t)), \gamma'(t) \rangle dt$, like a vectorfield $\cdot$ the directon of $\gamma$. For $\Omega: \Gamma \times \mathbb{R}^2 \rightarrow \mathbb{R}$ and $\omega: \mathbb{R}^2 \rightarrow \mathbb{R}^2$, so $\omega$ is like $v$ and $\Omega$ must give us something in one dimension so that we are allowed to integrate.
- for $\Gamma_1, \Gamma_2$ have the same starting and ending point, and $\int_{\Gamma_1} \omega = \int_{\Gamma_2} \omega$ then $\omega$ is wegunabhängig
- $U$ sternförmig to $p$ $\Leftrightarrow \forall_{x \in U} \overline{px} \subset U$.
- Exakt, How to prove: 
	1. if you have a $f$ s.t. $\omega(x) = \nabla f(x)$, call $f$ Stammfunktion and $\omega$ exakt. .49
		1. ext: e.g. for $U$ sternf. find$f$ s.t. $f(x) = \int_{\Gamma(x_0, x)}\omega$, for $\gamma: t \mapsto x_0 + t(x - x_0)$ ==uhm==
		2. ext: e.g. for all $i$ find: $f = \int \omega_i dt_i + c(x_1, ..., x_{i-1}, x_{i+1}, ..., x_n)$ ==uhm== 
	2. $\omega$ has $U$ open and zusamm.: $\omega$ exakt $\Leftrightarrow \omega$ wegunabähngig .50
	3. for $\omega_i = \partial_i f$:  $\omega$ exakt $\Rightarrow \partial_j \omega_i = \partial_j \partial_i f = \partial_i \partial_j f = \partial_i \omega_j$, conver. holds if $U$ sternfö. for one $p$
		- Then thanks to Schwarz if $f \in C^2(U, \mathbb{R}^n)$ and $U$ sternf. then $f$ is exakt.
- $\gamma$ Par. von $m$-Fl. $g: u \mapsto \gamma'(u)^T\gamma'(u) = (\langle \partial_i \gamma (u), \partial_j \gamma(u)\rangle)_{i, j =1, ..., m}$ .55.i
- $A(\Gamma):= \int_U \sqrt{det(g(u))} du = \int_U \sqrt{det(\gamma'(u)^T \gamma'(u))} du$ .55.ii
	- Compute: the volume of $\Gamma$, say $\lambda(\Gamma)$ is $A(\Gamma) = \int_U \sqrt{|det(g(u))|}du$ .58.iv
	- ext: But also if $\gamma'(u)$ is square, then just compute $\int_U det(\gamma'(u)) du$, no need of $g(u)$.
- $A$ ist bewegungsinvariant; $A(\Gamma)$ independent form $\gamma$
- if $u\mapsto f(\gamma(u))\sqrt{det(g(u))}$ int., then:$\int_\Gamma fdA:= \int_\Gamma f(x) d A(x) := \int_U f(\gamma(u)) \sqrt{det(g(u))} du$, _Surf. Int._
	- ext: But also if $\gamma'(u)$ is square, then just compute $\int_U f(\gamma(u)) det(\gamma'(u))du$, no need of $g(u)$.
- a set $M$ is int. if $\chi_M$ int., so $A(M) := \int_\Gamma \chi_M dA$ (useful?)
- $\gamma: I \times (0, 2\pi) \rightarrow \mathbb{R}^3, (t, \phi) \mapsto \left(\begin{smallmatrix} f(t) \cos(\phi)\\ f(t) \sin(\phi) \\ t \end{smallmatrix}\right)$ _Rotationsfläche_, $A(\Gamma) = 2\pi \int_I f(t) \sqrt{f'(t)^2+1}dt$ .59
- $A($graph$F) = \int_U \sqrt{1 + |\nabla F(u)|^2}du$, gr. $F :=$ a $(n-)1$-dim Flä. par: $\gamma:(U) \rightarrow \mathbb{R}^n, u \mapsto (u, F(u))^T$
- Compute volume integrals on circles: $\int_{\mathbb{R}^n}f(x)dx = \int^\infty_0(\int_{|x| =r} f(x)dA(x))dr$ .61
- $\int_{\mathbb{R}^n}f(|x|)dx = A(S^{n-1}) \int^\infty_0 f(r)r^{n-1}dr$ ==practice==
#### 13.6 Gauß and Stokes
 $\int_G div V(x) dx = \int_{\partial G} \langle V(x), \mathcal{v}(x) \rangle dA(x)$ for $V: \bar{G} \rightarrow \mathbb{R}^n$ a glatt VF., $v: \partial G \rightarrow \mathbb{R}^n$ die äuß. normale
1. For a $\int_{\partial G} f(x) dA(x)$ find a $\psi(x)$ s.t. $\{x \in \mathbb{R}^n|\psi(x) = 0\} = \partial G$ and $\psi \in C^1(\mathbb{R}^n, \mathbb{R})$ 
2. Compute $v(x) := \frac{\nabla \psi(x)}{||\nabla \psi(x)||}$
3. Show that $G^\circ := G \setminus \partial G = \{x \in \mathbb{R}^n| \psi(x) < 0\}$ is bounded and that $\partial G$ is glatt
4. Define $V : G \rightarrow \mathbb{R}^n$ s.t. , $\int_{\partial G}f(x) dA(x) = \int_{\partial G} \langle V(x), v(x)\rangle d A(x)$ now use Gauß and compute:
5. $\int_G div V(x) dx = \int_G \partial_1 V_1(x) + ... + \partial_n V_n(x) dx = \int_U (\partial_1 V_1(\gamma(u)) + ... + \partial_n V_n(\gamma(u))) \sqrt{|\det g(u)|} du$
- Stokes in $\mathbb{R}^2$: $G$ bounded, $\partial G$ glatt, $V \in C^1(\bar{G}, \mathbb{R}^2)$ then: $\int_G rot (V(x))dx = \int_{\partial G} \langle V (x), dx \rangle$
	- $rot(V) := \partial_1 V_2 - \partial_2 V_1$ in $\mathbb{R}^2$ 
- In $\mathbb{R}^3$: $M \subset \mathbb{R}^3$ a $2$-Fl., $G$ b., $\partial G$ gl., $V \in C^1 (\overline{G}, \mathbb{R}^3)$: $\int_G \langle rot(v(x)), v(x) \rangle dA(x) = \int_{\partial G} \langle V(x), dx \rangle ds$
	- $rot(V):= \nabla \times V: = \left(\begin{smallmatrix} \partial_2V_3 - \partial_3V_2\\ \partial_3V_1 - \partial_1V_3 \\ \partial_1V_2 - \partial_2V_1 \end{smallmatrix}\right)$ 
### To memorise
- Taylor: $f(x+h) = \sum_{j =0}^\infty \frac{f^{(j)}(x)}{j!}(h)^j$ 9.18
- Weier.: $(P_nf)(x):= \sum_{j=0}^n \left(\begin{smallmatrix}n\\j\end{smallmatrix}\right)x^j (1-x)^{n-j}f(\frac{j}{n})$ 9.23
- Fourier: for $\mathbb{R}$: $f(x) = a_0 + \sum_{j=1}^\infty (a_j \cos(jx) + b_j \sin(jx))$: $a_0 = \frac{1}{2\pi} \int_{-\pi}^\pi f(x)dx$; $a_j = \frac{1}{\pi}\int^\pi_{-\pi}f(x) \cos(jx)dx$; $b_j = \frac{1}{\pi}\int^\pi_{-\pi}f(x)\sin(jx)dx$  9.32
- Young: $\forall_{a, b > 0 (\in \mathbb{R})} a \cdot b \le \frac{a^p}{p} + \frac{b^q}{q}$
- Hölder: $\sum_{ i = 1}^\infty |\xi_i \cdot \eta_i| \le ||x||_p \cdot ||y||_q$ ($\Leftrightarrow ||xy||_1 \le ||x||_p \cdot ||y||_q$)
- Mikowski: $||x + y||_p \le ||x||_p + ||y||_p$
- Nichtzus. $\Leftrightarrow \exists_{A, B \not = \emptyset} A \cap B = \emptyset \land X = A \cup B$ ($A, B$ both open or both closed) 10.11
- Gram-Schm. want $(w_i)_{i \in I}$ $w_1 = v_1$, $w_2 = v_2 - \frac{\langle v_2, w_1\rangle}{|w_1^2|}w_1$, $w_3 = v_3 - \frac{\langle v_3, w_1\rangle}{|w_1|^2}w_1 - \frac{\langle v_3, w_2 \rangle}{|w_2|^2}w_2$.
- $div f : \mathbb{R}^n \rightarrow \mathbb{R}, x \mapsto div f(x) := \sum_{i = 1}^n \partial_i f_i (x)$
- $rot f: \mathbb{R}^3 \rightarrow \mathbb{R}^3, x \mapsto (\partial_2f_3(x)-\partial_3f_2(x),  \partial_3f_1(x) - \partial_1f_3(x),  \partial_1f_2(x) - \partial_2f_1(x))^T$
- $\Delta: C^2(\mathbb{R}^n, \mathbb{R}) \rightarrow C(\mathbb{R}^n, \mathbb{R}), f \mapsto \sum_{i = 1}^n \partial_i^2 f$, $\Delta(f) = div(\nabla(f))$, called _Laplace-Operator_ 11.14
- ext: $D_y(h):= \lim_{t \rightarrow 0} \frac{f( y + th)- f(y)}{t}$,
- Mittelwertsatz: $\exists_{c \in \Gamma_{ab}} f(b) = f(a) + f'(c)(b-a)$, $\Gamma_{ab}$ is a the Gerade from $a$ to $b$, for $Im(f) \subseteq \mathbb{R}$
- Taylor in $\mathbb{R}^n$: $f(x, y) = f(a, b) + f_x(a, b)(x -a) + f_y(a, b)(y -b) + \frac{1}{2}f_{xx}(a, b)(x -a)^2$ $+ \frac{1}{2}f_{yy}(a, b)(y -b)^2 + f_{xy}(a,b)(x-a)(y-b)+R_2(x, h)$ for $R_2 (x, y) = \frac{1}{6} f''' (x + \theta h, h, h, h)$ for $\theta \in (0, 1)$. 11.27
-  $f$ convex $\Leftrightarrow \forall_{x_1, x_2 \in U} f(x_1 + t(x_2 - x_1)) \le f(x_1) + t(f(x_2)-f(x_1))$, with $<$ for streng conv. 11.36
- Solve $\sum_{i = 1}^n (\nabla f(x))_i + \lambda_i (\nabla g(x))_i =^! 0 \land g_1 =^! 0 \land ... \land g_m =^! 0$, and get $P_i$ for some $\lambda_i$
- $t = s \mapsto \frac{\gamma'(s)}{|\gamma'(s)|}$, $k(s):=|\gamma''(s)|$, $\langle \gamma'(s), \gamma''(s) \rangle = 0$ 
- For  $|\gamma'(s)| =1$, $t(s) = \left(\begin{smallmatrix} x'(s)\\ y'(s) \end{smallmatrix}\right)$; $n(s) = \left(\begin{smallmatrix} -y'(s)\\ x'(s) \end{smallmatrix}\right)$, ==Frenetsche Gleichungen==, $a \times b = \left(\begin{smallmatrix} a_2b_3 - a_3b_2\\ a_3b_1 - a_1b_3 \\ a_1b_2 - a_2b_1 \end{smallmatrix}\right)$, def. torsion as $\tau(s) : = \langle n'(s), b(s) \rangle = \langle -b'(s), n(s) \rangle$
- $\mathcal{A} \subseteq \mathcal{P}(X)$ is a $\sigma$-algebra if: (i) $\emptyset \in \mathcal{A}$, (ii) $A \in \mathcal{A} \rightarrow A^c \in \mathcal{A}$, (iii) $(\forall_{n \in \mathbb{N}} A_n \in \mathcal{A}) \rightarrow \bigcup_{n \in \mathbb{N}} A_n \in \mathcal{A}$ .1
-  $\sigma(\mathcal{E}) := \bigcap\{\mathcal{A}| \mathcal{E} \subset \mathcal{A} \}$
-  $\mu: \mathcal{A} \rightarrow [0, \infty]$ a measure on $\mathcal{A}$ if (i) $\mu(\emptyset) = 0$, (ii) $\mu(\bigcup^\cdot_{n \in \mathbb{N}}A_n) = \sum_{n \in \mathbb{N}}\mu(A_n)$
-  $\mathcal{B}(\mathbb{R}^n) := \sigma(\{(a,b]|a,b \in \mathbb{R}^n \land a<b\})$
- $f: X \rightarrow S$, $(X, \mathcal{A})$, $(S, \mathcal{S})$ $f$ $\mathcal{A}$-$\mathcal{S}$-meas. $\Leftrightarrow f^{-1}(\mathcal{S}) \subset \mathcal{A}$ i.e. for all $B \in \mathcal{S}$: $f^{-1}(B) \in \mathcal{A}$, $\mathcal{A}$-meas.: $(S, \mathcal{S}) = (\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$; Borel-Meas if also $(X, \mathcal{A}) = (\mathbb{R}^m, \mathcal{B}(\mathbb{R}^m))$
- Tonelli if $f > 0$ and meas., Fubini if $f$ Les. Int.
-  $A(\Gamma):= \int_U \sqrt{det(g(u))} du$, and$\int_\Gamma fdA:= \int_U f(\gamma(u)) \sqrt{det(g(u))} du$ Surf. Int.
- $\gamma: I \times (0, 2\pi) \rightarrow \mathbb{R}^3, (t, \phi) \mapsto \left(\begin{smallmatrix} f(t) \cos(\phi)\\ f(t) \sin(\phi) \\ t \end{smallmatrix}\right)$ _Rotationsfläche_, $A(\Gamma) = 2\pi \int_I f(t) \sqrt{f'(t)^2+1}dt$ .59
- Gauß, 5 steps
	1.  For a $\int_{\partial G} f(x) dA(x)$ find a $\psi(x)$ s.t. $\{x \in \mathbb{R}^n|\psi(x) = 0\} = \partial G$ and $\psi \in C^1(\mathbb{R}^n, \mathbb{R})$ 
	2. Compute $v(x) := \frac{\nabla \psi(x)}{||\nabla \psi(x)||}$
	3. Show that $G^\circ := G \setminus \partial G = \{x \in \mathbb{R}^n| \psi(x) < 0\}$ is bounded and that $\partial G$ is glatt
	4. Define $V : G \rightarrow \mathbb{R}^n$ s.t. , $\int_{\partial G}f(x) dA(x) = \int_{\partial G} \langle V(x), v(x)\rangle d A(x)$ now use Gauß and
	5. compute $\int_G div V(x) dx$.