---
draft: true
---
I began following this course at the [[LMU Munich]] for my [[B.Sc. Mathematics (LMU)]] but decide not to finish it, in order to prioritise the work for [[Bachelor Thesis]].
#### 1. Euclidian Geometry - Algebra
- instead of looking into euclidian geometry theory we look at a model, $\mathbb{R}^n$ and its subspaces $L:=b + v\mathbb{R}$.
- for $L \subsetneq \mathbb{R^2}$ str.lin., $p' \not \in L$ ex.uniq. $L'$ s.t. $p \in L' \land L \cap L = \emptyset$, 1.1
- $\langle \cdot, \cdot \rangle : \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}, (v, w) \mapsto \sum_{i \in n}v_iw_i$, for more see: [[Linear Algebra II (Lecture)#11.1 Scalar Produdct]]
- Length of a vector is defined $||v|| := \sqrt{\langle v , v \rangle}$, and distance $d_E(p, q) := ||p -q||$
- $\forall_{p, q,r \in \mathbb{R}} d(p, r) \le d(p,q) + d(q + r)$, more in [[Analysis II (Lecture)]].
- for $M$ a set, $d: M \times M \to \mathbb{R}$ os a dist. if (i) $\forall_{x, y \in M}d(x, y) \ge 0 \land (d(x, y) = 0 \to x = y)$, (ii) $\forall_{x, y \in M} d(x, y) = d(y, x)$, (iii) $\forall_{x, y, z \in M}d(x,z) \le d(x,y) + d(y,z)$, 1.3
- for any $p, q, r \in \mathbb{R}$ ex.uniq $L$ s.t. $p, q, r \in L$ iff $d(p, r) = d(p,q) + d(q, r)$
- $v, w$ perp. iff $\langle v, q \rangle = 0$, also recall: $\langle v, w \rangle = ||v|| \cdot ||w || cos(\angle(v,w))$
- sum of angles of a triangle is $\pi$, Pythagoras' theorem holds, 1.5-6
- for $L, L'$ str.lin., $p \in L \land p \in L'$ then $L \bot L':= \forall_{q \in L} \forall_{r \in L'}(( q \not =p \land r \not = p) d(q,r)^2 = d(p,q)^2 + d(q,r)^2$ 
- a lin.func. $f : \mathbb{R}^n \to \mathbb{R}^n$ is orth. if $\langle f(v), f(w) \rangle = \langle v, w \rangle$, see [[Linear Algebra II (Lecture)]]
- for $(X, d_x)$, $(T, d_Y)$ metr.sp., $\Phi$ isom. iff  $\Phi : X \to Y$ s.t. bij and $\forall_{x, x' \in X} d(\Phi(x), \Phi(x')) = d(x, x')$, 1.8
- for $L$ lin.func., $f$ aff.func. iff $f(x) = L(x) + b$
	- aff.func. on a set build a group under composition
- $R_\alpha$ rotation, $\tau_p := x + p$, $\tau_p \circ R_\alpha \circ \tau^{-1}_p$ is rot. of $\alpha$ centered in $p$
- $\forall_{v-1, v_2} (||v_1|| = ||v_2|| \to \exists_L L(v_1) = v_2)$, 1.10
- $\forall_{p_i, q_i}(d(p_1 q_1) = d(p_2, q_2)\to \exists_\Phi \Phi(p_1) = p_2 \land \Phi(q_1) = q_2)$, $\Phi$ is aff.isom., 1.11
	- $\forall_{v_i, w_i}((||v_1|| = ||v_2|| \land ||w_1 = w_2|| \land \angle (v_1, w_1) = \angle (v_2, w_2)) \to \exists_L L(v_1) = v_2 \land L(w_1) = w_2)$, $L$ is lin.isom., 1.11.b
- $\Phi$ isom. on $\mathbb{R}^n$, then $\Phi$ aff.isom., 1.12
- each lin.isom. is a rot. or a mirroring
#### 2. Euclidian Geometry - Analysis
- $\gamma: [a, b] \to \mathbb{R}^n$ is a path, if $\gamma$ is cont., 2.1
- for $\gamma:[a,b] \to \mathbb{R}^n$ path, $(t_i)_I$ a division of $[a, b]$, 2.2
- $\gamma$ is rec. iff $l(\gamma):= \sup \{\sum^n_{1= 0} d(\gamma(t_i) , \gamma(t_{i -1})) : (t_i)_I$ div. of $[a,b]\} < \infty$, 2.2
- $l(\gamma) \ge d(\gamma(a), \gamma(b))$ 
- for $\gamma$ cont.diff. then $\gamma$ rect. and $l(\gamma) = \int^b_a||\gamma'(t)||dt$, 2.3
- $\gamma(t) = \left(\begin{smallmatrix} cos(t)\\ sin(t) \end{smallmatrix}\right)$, then $\gamma$ rec. and $l(\gamma|_{[a, b]}) = b-a$, 2.4
- for $\gamma: [a,b] \to \mathbb{R}^n$ rec. never const., then exists a cont str.mon.func. $f:[0, l(\gamma)] \to [a,b]$ s.t. $\gamma \circ f$ is a param., 2.5
#### 3. Pathmetric
- $X$ is a (rec.)conn.set if each two points can be connected by a (rec.) path, see [[Analysis II (Lecture)]]
- $X \subsetneq \mathbb{R}^n$ conn.set, then $d_X (p, q) := inf\{l(\gamma) : \gamma(a) = p \land \gamma(b) = q \land im(\gamma) \subseteq X\}$, 3.1-2
- $X \subsetneq \mathbb{R}^n$ conn.set, a path $\gamma: [a, b]$ is geod. if $d(\gamma(a), \gamma(b)) = l(\gamma)$
#### 4. Spheric Geometry I - Geodatics
- consider $S^2 = \{(x, y, z) \in \mathbb{R}^3 : x^2 + y^2 + z^2 = 1\}$, param. as $\gamma(t) = \cos(t)p + \sin(t)v$
- for $\Phi$ isom. $\forall_{\text{rec. }\gamma} l(\Phi \circ \gamma) = l(\gamma)$, each lin.isom. $L$ def. an isom. on $d_{S^2}$.
	- $R_{p, \alpha}$ is the clockwise rot. through $p$ and $0$ of $\alpha$
- for $p, q \in S^2$ s.t. $q \not = -p$, then (i) $\forall_{u \in U}d(u, p) < d_{S^2}(p, q)$, (ii) $\forall_{v \in V} d(v, p) >d_{S^2}(p, q)$, (iii) $C(p, q) = \{c \in S^2 : d(c,p) = d_{S^2}(p, q)\}$, 4.2
	- $C(p, q) := \{R_{p, \alpha}q:\alpha \in [0, 2\pi]\}$ divides the sphere in two (call them $U$, $V$)
- for $p, q \in S^2$ s.t. $q \not = -p$ and $l(C(p, q)) < \pi$, then $\forall_{z \in C(p, q)} C(p, z) \cap C(q,z) = \{z\}$, also $U(p, z) \cap U(q, z) = \emptyset$, 4.3
- for $p, q \in S^2$ s.t. $q \not = -p$ and $l(C(p, q)) < \pi$, then $C(p, q)$ is unique, each path has length $\ge \angle(q, p)$, 4.4
- $d_{S^2}(p, q) = \angle p, q$ and the geod.path are exactly the bows of lenght $\le \pi$, 4.5
- $d_{S^2}$ is cont. (for the top. of $\mathbb{R}^3$), 4.6
- for $p \in S^2$, $0 < r < \pi$, $C_r(p) := \{q \in S^2 :d(p,q) = r\}$, then $l(C_r(p)) = 2 \pi \sin (r)$
#### 5. Spheric Geometry II - Triangles
- a geo.tr. is $(\gamma_1, \gamma_2, \gamma_3)$ that connect $(p_1, p_2, p_3)$.
- $Z(\alpha) \subsetneq S^2$ is a biangle of angle $\alpha$, $area(Z(\alpha)) = 2 \alpha$, 5.2
- $\Delta$ a geo.tr., then $area(\Delta) = \gamma_1 + \gamma_2 + \gamma_3 - \pi$
#### 6. Cylindric Geometry
- consider $C = \{(x, y, z) : x^2 + y^2 = 1\}$
- $U \subseteq \mathbb{R}^n$ op., $f: U \to \mathbb{R}^m$ cont.diff.func. s.t. $\forall_{u \in U}\forall_v \in \mathbb{R}^n ||D_uf(v)|| = ||v||$, then $\forall_{\gamma} \gamma \text{ rec. }\Leftrightarrow  l(f \circ \gamma) = l(\gamma)$, 6.1
- $\Psi: \mathbb{R}^2 \to C$ is a loc.isom. if $\forall_{(a, h)}\exists_{U \supset (a, h)} \Psi|_U : U \to isom(\Psi(U))$, 6.2
	- $\exists_{\varepsilon > 0} isom(\Psi|_{B_\varepsilon(x)})$, 6.3
	- for $\gamma: [0, L] \to C$, then $\exists_{\rho: [0, L] \to \mathbb{R}^2} \gamma = \Psi \circ \rho$, 6.4
- $\forall_{y_1, y_2} d_C(y_1, y_2) = min\{||x_1 - x_2||, \Psi(x_i) = y_i\}$, 6.5
	- loc.geod. on $C$ are exactly images of $\Psi$ of str.lin.

- $\Gamma < \mathbb{R}^2$ disj. subgr., then $\Gamma = \{0\}$ or $\Gamma = \{n \cdot v : n \in \mathbb{Z}\}$ for some $v \in \mathbb{R}^2$ or $\Gamma = \{n \cdot v + m \cdot w : n, m \in \mathbb{Z}\}$ for $v, w \in \mathbb{R}^2$ basis.
- If $G < isom(\mathbb{R}^2)$ s.t. $\Gamma_G = \{0\}$, $L_G$ fin., then $G$ fin. and $\exists_{p \in \mathbb{R}^2}\forall_{g \in G}g(p) = p$. then for $G$: (i) $G = \{id\}$, (ii) $G \cong \mathbb{Z}/2\mathbb{Z}$, (iii) $G \cong \mathbb{Z}/n \mathbb{Z}$, (iv) $G \cong $D_n$.
	- see [[Algebra (Lecture)]].