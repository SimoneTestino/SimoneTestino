This writing are unfinished notes on formalisation of different possible theories of causality and reality. I am not currently working anymore on those notes, written during the #2nd_Semester but, in case I would come back reasoning to connected themes, I will consider rewriting some of these notes in an essay form.
### Realism Defined
Given:
- $\sim_C$ a causality relation 
- $E$ a set of events
- $\phi$ a predicate individuating physical events
- $\psi$ a predicate individuating mental events
- $\mathcal{L}_\epsilon := \langle \land, \lnot, \in, T \rangle$ the language of set theory as usually defined
I define the language of realism by expanding the language of set theory to $\mathcal{L}_r:= \mathcal{L}_\epsilon \langle E, \sim_C, \psi, \phi \rangle$, where $\phi: E \rightarrow \{T, F\}$, $\psi: E \rightarrow \{T, F\}$, $\sim_C: E\times E \rightarrow \{T, F\}$. 

Then I define the following theories:

**Theory of Dualism** $T_d := \{\forall_x(\psi(x) \lor \phi(x))$, $\forall_x(\lnot (\psi(x) \land \phi(x)), \exists_x\phi(x), \exists_x\psi(x)\}$

**Theory of Causality** $T_c := \{\forall_x\forall_y((x \sim_C y)\rightarrow \lnot(y \sim_C x)), \forall_x(x \sim_C x),$ $\forall_x\forall_y\forall_z(((x \sim_C y) \land (y \sim_C z) \rightarrow (x \sim_C z))\}$

So $(E, \sim_C)$ is a partial ordering.

**Theory of Realism** $T_r := T_d \cup T_c \cup \{\forall_{x}\forall_{y}((\psi(x) \land \phi(y))\rightarrow \lnot(x \sim_C y))\}$

#### Cubic Variant
Extend $\mathcal{L}_r$ to $\mathcal{L}_r^R := \mathcal{L}_r \cup \langle \chi_s, \chi_t \rangle$, $\chi_s: E \rightarrow \mathcal{P}(\mathbb{R}^3)$, $\chi_t: E \rightarrow \mathcal{P}(\mathbb{R})$, namely the functions that give the spatio-temporal cordinates of an event. Now define:

$\chi(x) := \chi_s(x)\cup \chi_t(x)$,

$x=_\chi y:= (\chi_s(x) = \chi_s(y)) \land (\chi_t(x) = \chi_t(y))$

$x =_e y := x =_\chi y \land ((\phi(x) \land \phi(y)) \lor (\psi(x) \land (\psi(y)))$

$x \sim_C^0 y := x \sim_C y \land \forall_{i \in [1,4]}(max(\chi(x)_i) = min(\chi(y)_i)$, for $min$ and $max$ as usually defined, 

**Theory of Cubic Events**: $T_e^C:= \{\forall_x\exists_{r_1, ..., r_8 \in \mathbb{R}}(\chi(x)=([r_1, r_2], [r_3, r_4], [r_5, r_6],[r_7, r_8]),$ $\forall_x\forall_y((\phi(x) \land \phi(y) \land \lnot(x =_e y)) \rightarrow \lnot(\chi(x) = \chi(y))\}$

Given the usual set theoretic definition of $\mathbb{R}$ and of closed set $[\cdot, \cdot]$, I define for $r_1, ..., r_{16} \in \mathbb{R}$ and $x, y \in E$ s.t. $\chi(x)=([r_1, r_2], [r_3, r_4], [r_5, r_6],[r_7, r_8])$ and $\chi(y)=([r_9, r_{10}], [r_{11}, r_{12}], [r_{13}, r_{14}],[r_{15}, r_{16}])$:
$x \cup_\chi y := z$ s.t. $\chi(z)=([r_1, r_{10}], [r_3, r_{12}], [r_5, r_{14}],[r_7, r_{16}])$,

I define $E^\chi := \{\chi(x)| x \in E\}$, every $x \in E$ has its equivalence class $x^\chi := \overline{x}^{=_\chi}$ and it holds that $E/=_\chi \cong E^\chi$, also notice that given $E^\chi_\phi := \{\chi(x) | x\in E \land \phi(x)\}$ and $E_\phi := \{x | x\in E \land \phi(x)\}$, then $\chi\restriction_{E^\chi_\phi}$ is injective and $\chi(E_\phi)=E_\phi^\chi$; I then define $\chi^{-1}_\phi: E_\phi^\chi \rightarrow E_\phi$ which is bijective.

Then given $x, y \in E$ and $x \sim_C^0 y$, I define $\overline{x \sim_C^0 y}:= \chi(z) := \chi(x) \cup_\chi \chi(y)$ and $\chi(z) \in E^\chi$ and $\chi(z)$.

**Theory of Cubic Causation**: $T_c^C:= T_c \cup T_e^C \cup \{\forall_x\forall_y((x \sim_C y) \rightarrow max(\chi_t(x)) \le min(\chi_t(y)),$ $\forall_x\forall_y((x \sim_C y)\rightarrow \exists_z(x \sim_C^0 z \land z \sim_C^0 y)), \forall_x\forall_y((x \sim_C^0 y) \rightarrow \exists_z(\chi(z) = \chi(x) \cup_\chi \chi(y) = \overline{x \sim_C^0 y}))\}$. 

**Theory of Cubic Dualism**: $T_d^C:= T_c^C \cup \{\forall_x\forall_y ((\phi(x) \land \psi(y) \land x \sim_C^0 y)\rightarrow \chi(x) =_\chi \chi(y)\}$

**Theory of Cubic Weak Realism**: $T_r^{Cw} := T_d^C \cup T_r$

**Theory of Cubic Strong Realism**: $T_r^{Cs} := T_r^{Cw} \cup \{\forall_x(\psi(x) \rightarrow \exists_y(\phi(y) \land (y \sim_C x)))\}$
##### Notes:
This variant begins by considering events as fractions of the space-time which was the Russelian definition, I don't attribute to B. Russel any of the other definitions. This is a theory that starts by the definition of events as cubic pieces of the space-time, I made them cubic for semplicity. The assumptions I made in defining causation are: one says that cause comes before of the effect, the second that if cause and effect are far apart in space and time there must be a continous chain of causations that connects the cause with its effect and the third claims that causation is an event itself (which is needed for realism to be stated).
The main problem one gets with such a definition of event is to give enough space to mental events. It makes sense to speak about realism when we have the a theory of dualism, at least as presented in $T_d$. When we have no mental events or physical events then realism becomes a trivial matter. Here, where dualism seems to not well fit the context, there are a couple of options: one could see mental events as fractions of space and time where those coordinates are the same as their closest cause ($\sim_C^0$), e.g. when a certain chemical activity takes place in the brain, call it $x$, and it causes a certain feeling, call it $y$, then it might be that $\phi(x) \land \psi(y) \land \chi(x)=\chi(y)$ so we could say that $x =_\chi y$ even though $x$ and $y$ are two distinct events. Then in the theory of strong realism I say that any mental event (call it $y$) must have a physical event and therefore there will be one (call it $z$ s.t.$z \sim_C^0 y$) will determine its coordinates ($\chi(z) = \chi(y)$). Though in the theory of weak realism it is possible that there are some mental events that are competely disconnected, with no physical cause, though might create a causal net in the same coordinates of some other physical event even if they're causally disconnected from it.
#### Statistical Correlation Variant
Extend $\mathcal{L}_r$ to $\mathcal{L}_r^S := \mathcal{L}_r \cup \langle \tau, \sim_\rho \rangle$, where $\tau: E \rightarrow \mathcal{P}(E), e \mapsto e^\tau$ where $e^\tau$ is called the *type* of $e$ and $\sim_\rho: \mathcal{P}(E) \times \mathcal{P}(E) \rightarrow \{T, F\}$, if $x^\tau \sim_\rho y^\tau$ we saywe say that $x^\tau$ and $y^\tau$ are statistically correlated.

**Theory of Statistical Causation**: $T_c^S:= T_c \cup \{\forall_x\forall_y((\tau(x)\sim_\rho\tau(y))\rightarrow((x \sim_C y)\lor(y \sim_C x)\lor(\exists_z(z \sim_C x \land z \sim_C y))))\}$

By extending $\mathcal{L}_r^S$ to $\mathcal{L}_r^{SC} := \mathcal{L}_r^S \cup \mathcal{L}_r^R$, I can define:

**Theory of Cubic Statistical Dualism**: $T_d^{SC} := T_d^C \cup T_c^S$

One may do similarly for **Weak** and 

**Theory of Cubic Statistical Strong Realism**: $T_r^{CsS}:= T_r^{Cs} \cup T_r^S$
##### Notes:
This is simply a characterisation of causation which, on a theoretical level at least, doesn't particularly enrich the discussion, since there is not much I can *a priori* state on statistical correlation. Though I think that the **Theory of Statistical Cubic Strong Realism** is a rapresentative theory of the usual scientific praxis (one should first quickly fix the approximation of cubic to any shape on $\mathbb{R}^3$ and an interval on $\mathbb{R}$ for time). What is probably still missing in order to get to the actual practical notion of cause we have is the possibility to distinguish two events happening at the same time, e.g a ball spinning and heating up; those two events have different causal networks and can't be distinguished in the Russelian way, for more see [SEP](https://plato.stanford.edu/entries/causation-metaphysics/)

#### D. Lewi' Variant
Extend $\mathcal{L}_r$ to $\mathcal{L}_r^L:= \mathcal{L}_r \cup \langle W, \sim_S, \square \rightarrow \rangle$, where $\sim_S: W \times W \rightarrow \{T, F, P\}$, where $T$ and $F$ denote the usual *True* and *False* as in the domain classical connectives, though $P$ denotes tie. In order to use only two-valued relations, for any $w_1, w_2 \in W$, I define:

$w_1 \vartriangle w_2 := (w_1 \sim_S w_2) = P$

$w_1 \vartriangleright w_2 := (w_1 \sim_S w_2) = T$

$w_1 \vartriangleleft w_2 := (w_1 \sim_S w_2)=F$

$\square \rightarrow: \mathcal{P}(W) \times \mathcal{P}(W) \rightarrow \{T, F\}$, notice that an $A \subset W$ is called a *proposition*, $A$ is the set of worlds where it holds.

**Theory of Determinism**: $T_{det}^L:= T_c \cup \{\forall_{x \in E}\exists_{y \in E}(x \sim_C y)\}$ 

**Theory of Possible Worlds**: $T_w^L:= T_{det}^L \cup \{idk\}$ 

**Theory of Comparative Similarity**: $T_s^L := T_w^L \cup \{\forall_{w_1,w_2 \in W}((w_1 \vartriangleright w_2)\lor (w_1 \vartriangleleft w_2)\lor (w_1 \vartriangle w_2)),$ $\exists_{a \in W}\forall_{w \in W}(a \vartriangleright w), \forall_{w \in W} (w \vartriangle w), \forall_{w_1, w_2 \in W}((w_1 \vartriangle w_2) \leftrightarrow (w_2 \vartriangle w_1)),$ $\forall_{w_1, w_2, w_3 \in W} (((w_1 \vartriangleright w_2) \land (w_2 \vartriangleright w_3)) \rightarrow w_1 \vartriangleright w_2), \forall_{w_1, w_2, w_3 \in W} (((w_1 \vartriangleleft w_2) \land (w_2 \vartriangleleft w_3)) \rightarrow w_1 \vartriangleleft w_2)\}$

So $(W, \vartriangleright)$ and $(W, \vartriangleleft)$ are strict partial orderings and $\vartriangle$ is an equivalence relation on $W$.
Lewis underlines "we do *not* impose the further constraint that for any set $A$ of worlds there is a unique closest $A$-world, or even a set of $A$-worlds tied for closest." immediatly after he suggests: "Why not an infinite sequence of closer and closer $A$-worlds, but no closest?". Let's define such structure: Let $A \subset W$ and state $\lnot (\exists_{\alpha \in A}\forall_{a \in A}(\alpha \vartriangleright a \lor \alpha \vartriangle a))$ then there is a $(a_i)_{i \in \mathbb{N}} \subseteq A$, s.t. $a_i \vartriangleleft a_{i+1}$. Now if $A$ is bounded under $\vartriangleright$ then $(a_i)_{i \in \mathbb{N}}$ must be converging by Bolzano-Weierstrass-Theorem, therefore we might consider simply the closure of $A$, $\bar{A}$ and it will contain such a maximal $\alpha$. For finite clsoed sets the "constrain" is a theorem in $Th(T_s^L)$, otherwise not.

**Theory of Counterfactual**: $T_{con}^L := T_s^L \cup \{\}$
##### Notes:
###### Theory of Determinism
I regard this point as coming from p. 559 where D. Lewis writes "the prevailing laws of nature are such that there do not exists any two possible worlds which are exactly alike up to some time, which differ tehreafter, and in which those laws are never violated." I considered it to be equivalnt to affirm that every event must be causated since all such natural laws are causal laws (laws stating that all events of a sort cause events of another sort); therefore clearly if there are no uncaused events then two alike worlds will still be alike and if we assume he's statement it follows that there cannot be any uncaused event (or it will definetely excape the causal laws).