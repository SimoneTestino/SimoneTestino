The PDF of the paper can be found [here](https://philsci-archive.pitt.edu/8940/1/semantic-defect-revised2.pdf). My comment and understanding of the paper can be found in the essay [[Structure on Models]] and what follows are some other, mostly related, remarks.

---
Here I collect brief notes on particular topics connected or of particular interest for my [[First Bachelor Thesis Concept]]. On the same topic, see [[Halvorson, H. (2013), The semantic view, if plausible, is syntactic]]. For other papers by the same author, visit [[Hans Halvorson]]
### Identity Crisis for Theories
In this part of the paper Halvorson presents three possible identity criteria for theories in the semantic view: for $mod(T) := \{\mathcal{M}$ is a model $: T \models \mathcal{M}\}$.
- $T \sim_E T' :=$  exists $f: mod(T) \to mod(T')$ s.t. $f$ is bij.
- $T \sim_P T' :=$ exists $f: mod(T) \to mod(T')$ s.t. $f$ is bij. and $\forall_{\mathcal{M} \in mod(T)} \mathcal{M} \cong f(\mathcal{M})$.
- $T \sim_ I T' := mod(T) = mod(T')$
These criteria, I believe, assume an intuition on $mod(T)$, namely that it is no more than a set. For instance, if $mod(T)$ had some structure, like a partial order or the one of a group, one would define some equivalence relation as isomorphisms of such structures. For this reason I am interested in finding some further structure to $mod(T)$ so that some alternative equivalence relation as an isomorphism of such structures can be defined.
##### Partial Order
Following the usual construction of a maximally order set through the procedure of the Lindenbaum's Lemma (see [[Modal Logic (Lecture)#7. Soundness and Completeness I]], whose proof gives a practical grasp to the algorithm), one notices that for  $\mathcal{P}_T:= \{A \subseteq \mathcal{L} : T \subseteq A \land A \not \models \bot \}$, $(\mathcal{P}_T, \subseteq)$ is a partial order whose minimal element is $T$ and maximal elements of each chain are in $mod(T)$. Following the previous reasonings one could now consider two other identity criteria for theories:
- $T \sim_{PO_1} T' \Leftrightarrow (\mathcal{P}_T, \subseteq) \cong (\mathcal{P}_{T'}, \subseteq)$
- $T \sim_{PO_2} T' \Leftrightarrow (\mathcal{P}_T, \subseteq) \cong (\mathcal{P}_{T'}, \subseteq)$ for $f$ isom., $\forall_{\mathcal{M} \in mod(T)} \mathcal{M} \cong f(\mathcal{M})$

One might also consider: $(\mathcal{P}_T, \subseteq) \cong (\mathcal{P}_{T'}, \subseteq)$ for $f$ isom., $\forall_{A \in \mathcal{P}_T} A \cong f(A)$. Though clearly $A \cong A'$ for $A, A' \in \mathcal{P}$ is not defined since $A, A'$ are only consistent sets, i.e. theories, but not structures. One could instead define:
- $T \sim_{PO_3} T' \Leftrightarrow (\mathcal{P}_T, \subseteq) \cong (\mathcal{P}_{T'}, \subseteq)$ for $f$ isom., $\forall_{A \in mod(T)} A \sim_{PO_2} f(A)$
It might be the case though that $T \sim_{PO_3} T' \Leftrightarrow T \sim_{PO_2} T'$.

It would be then interesting to see whether $\sim_{PO_1}$, $\sim_{PO_2}$ and $\sim_{PO_3}$ are equivalent to one of the previously mentioned relation or if they are subject to the same critique. 
##### Special Identities
Halvorson considers only those identity criteria that can be applied on all theories in full generality, just like the method I described above. Though, one might be willing, for some other reason, to consider only some theories in particular and define some equivalence relation not subject to Halvorson's critique. I do not dive into the numerous possibilities here but want instead consider one precise method that goes in this direction which is strictly related to my [[First Bachelor Thesis Concept]] in particular to: [[Algebra on Worlds]].

The thesis I want to argue for in part of my thesis is that, thanks to some structure on generators of ultrafilters, I am able to transfer such a structure up to ultraproducts (i.e. some models). For the sake of this comment, I will assume that there is some algebra $\mathcal{A}$ on ultraproducts of $(A_n)_{n\in \mathbb{N}}$ a sequence of structures. More precisely I assume that there are some operations (of any arity) $R_1, ..., R_n$ on $\mathcal{X} := \{\prod_{\mathcal{U}} A_n : \mathcal{U}$ is ultrafil.$\}$ s.t. for any $X, Y \in \mathcal{X}$ we have $X R_i Y \in \mathcal{X}$.

Now, in case $mod(T) = \mathcal{X}$,
- $T \sim_{\Pi_1} T' \Leftrightarrow mod(T) \cong mod(T')$ for $mod(T) = \{\prod_{\mathcal{U}} A_n : \mathcal{U}$ is ultrafil.$\}$ and operations $R_1, ..., R_n$.

The case $mod(T) = \mathcal{X}$ rightfully seems not to be a probable one, though, since in $\mathcal{X}$ we range on all $\mathcal{U}$ and keep $A_n$ fixed, we might set $A_n := mod(T)$, hence consider: $\mathcal{X}_T := \{\prod_{\mathcal{U}} mod(T) : \mathcal{U}$ is ultrafil.$\}$ and $\mathcal{A}_T$ its algebra. A relevant question here is: does $mod(T) \subseteq \mathcal{X}_T$ hold for any theory?

If we have $mod(T) \subseteq \mathcal{X}_T$ we can then define:
- $T \sim_{\Pi_2} T' \Leftrightarrow \mathcal{A}_T \cong \mathcal{A}_{T'}$ for  is ultrafil..

Now back to the question, does $mod(T) \subseteq \mathcal{X}_T$ hold for any theory? By Łos Theorem, for $\mathcal{U}$ ultrafil. and $A \equiv A' := \forall_{\varphi \in \mathcal{L}} A \models \varphi \Leftrightarrow A' \models \varphi$, we have $\forall_{u \in \mathcal{U}} n \in u \Rightarrow \prod_\mathcal{U} A_n \equiv A_n$ and since $\forall_{n \in \mathbb{N}} \exists_{\mathcal{U} \subseteq \mathcal{P}(\omega)}(\mathcal{U}$ is ultrafil. $\land \forall_{u \in \mathcal{U}} n \in u)$, then $\forall_{n \in \mathbb{N}} \exists_{X \in \mathcal{X}} A_n \equiv X$ hence, up to elem. equivalence, $(A_n)_{n \in \mathbb{N}} \subseteq \{\prod_\mathcal{U}A_n : \mathcal{U}$ is ultrafil.$\}$. To get to a formal proof I should prove: (i) $\forall_{n \in \mathbb{N}} \exists_{\mathcal{U} \subseteq \mathcal{P}(\omega)}(\mathcal{U}$ is ultrafil. $\land \forall_{u \in \mathcal{U}} n \in u)$ and (ii) $\forall_{u \in \mathcal{U}} n \in u \Rightarrow \prod_\mathcal{U} A_n \equiv A_n$.
## Technical Part
Here I summarise some of the results and definition that Halvorson states from page 191. $\mathcal{L}(T)$ is the language of the theory $T$.
- for $T$, $T'$ theories, $F: \mathcal{L}(T) \to \mathcal{L}(T')$ preserving var. and arity of constants s.t. for each $\varphi, \psi \in T$, $\varphi \vdash \psi \Rightarrow F(\varphi) \vdash F(\psi)$ p. 191 (Interpretation)
- $F: T \to T’$, $G: T’ \to T$ interpretations s.t. $\forall_{\varphi \in \mathcal{L}(T)}(T \vdash G \circ F (\varphi) \leftrightarrow \varphi)\land \forall_{\psi \in \mathcal{L}(T')}(T') \vdash F \circ G(\psi) \leftrightarrow \psi)$, ($G$ is weak inverse)
	- ==I don't see how concatenation of the functions can work here== 
- $F, G$ interp. s.t. $G$ weak inv. of $F$ ($T$, $T'$ definitionally equivalent)
- $T = \{\exists_{= 1} x ( x = x)\}$, $T' = T \cup \{i \in \mathbb{N} : Q_0 (x) \vdash Q_i(x)\}$
	- |$mod(T)| = |mod(T')|$
	- there is a bij. $f : mod(T) \to mod(T')$ s.t. $f(m) \cong m$. (p. 192bottom)
- $F, F^*$ interp. s.t. $F^*$ weak inv. of $F$, $\exists_{m' \in mod(T')}|m'| \not = |F^*(m')|$.
	- hence def.equiv. theories don't have isom. models. (?)