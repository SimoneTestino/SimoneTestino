---
draft: false
date: 2024-09-02
---
I followed this course by, Prof. Ronald de Haan during my [[5th Semester]] at the [[ILLC Amsterdam]] for my [[M.Sc. Logic (UvA)]].
#### Assignments
- [Overleaf: KRR, 1](https://www.overleaf.com/read/bfjnnbqgwpwy#69388b)
- [Overleaf: KRR, 2](https://www.overleaf.com/read/bfdnbszxcptq#930549)
- [Overleaf: KRR, 3](https://www.overleaf.com/read/pvwshhgkvbdw#77491b)
## Lecture Notes
Here I summarise the material and, in particular, write in a very schematic manner, all that is needed for passing the exam.
#### 09.09, III. DPLL & CDCL
- SAT is _NP-complete_
- a _CNF formula_, is a conjunction of _clauses_, which are disjunctions of possibly negated _literals_ (at.form.)
	- every $\varphi \in \mathcal{L}_{PL}$ is logically equivalent to a CNF-formula
		- _Tseytin transformation_ solves the problem in P-time.
	- for $\varphi \in CNF$, for $\mathcal{l}$ literal, then $\varphi|_\mathcal{l}$ is $\varphi$ given $\mathcal{l}$
-  _Backtracking search_: is a brute force algorithm on truth-assignments
	- it can easily represented through a tree-graph
	- _Propagation_: 
		- _Unit Propagation_: if $\varphi$ contains a unit clause, satisfy it (DPLL)
			- repeat until there is no unit clause
			- _unit clauses_ are those whose all literals other than one have already been set false \[s.15\]
		- _Conflict Analysis_: (CDCL) \[[lec.](https://hva-uva.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=067a60ea-d9f3-4477-9f84-b11000bc7f79), 1:12\]
			1. Build the conflict graph 
				- arrows from literals to literals that indicate what forced propagation
			2. Draw cuts, each corresponds to a clause
				- the clause is the negation of provenience of the cut arrows
			3. _Theorem_: if you add these clauses to the formula, the result does not change
				- to avoid this situation again, you can add these clauses
				- these clauses are logically entailed in the initial formula
			4. Adding all makes the algorithm slower, take the 1UIP \[1:24\]
				- 1UIP is the rightmost _asserting_ clause \[1:27\]
					- a clause is asserting if it contains (the neg. of) exac. one literal of the maximal _decision level_
						- the decision level of a literal is when it got chosen, if it derived from propagation, take the highest literal that forced propagation.
					- _precise method_: once drawn the graph, proceed by define the cut $(L, R)$,
						1. all $p$ with not max.dec.lev. in $L$
						2. $l_d$ is the dec.lit. of max.dec.lev.
						3. $l_1$ is lit. closest to $\bot$ s.t. lies on all path $l_d \rightsquigarrow \bot$
						4. put the path $l_d \rightsquigarrow l_1$ in $L$, & all lit. with max.dec.lev.
						5. the rest (and $\bot$) in $R$
						6. 1UIP is the disj. of the neg. of the antecedents of the arrows crossing
			1. Jump back the second highest decision level of the 1UIP and use it to propagation
		- if a literal appears and never its negation, assume it (PL) \[1:46\]
		- pick the literal that satisfies as many clauses as possible
		- a random restart makes the algorithm sometimes quicker
		- Give each literal a score, at each conflict decrease the score of all literals involved, always chose the one with the least score (VSIDS)
#### 13.09, IV. ASP
-  Similar to Prolog (idk)
- Introduction to Syntax
	1. rules: `a :- b, c, d, ..., z
		- meaning $(b \land c \land d \land ... \land z) \to a$
	2. facts: formula that are true
		- `a` meaning $\vdash a$
	- Examples:
		1. Universally quantifiers:
```ASP
rainy(amsterdam).
rainy(vienna).
wet(X) :- rainy(X).
```
- Semantic Rules:
	1.  _Domain Closure_: the objects mentioned are the only objects
	2.  _Unique-names Assumption_: objects with different names are different objects
	3. _Closed-world Assumption_: what is not proved true is false
	- _Herbrand Interpretation_: ? \[S. 10\]
	- _Minimal Model_ is a model s.t. any subset of it is not a model
		- for positive programs there is one unique minimal model.
	- _Supported Model_: for each $a \in M$, there is a rule $a \leftarrow \beta$ in $P$ s.t. $M$ makes $\beta$ true
- _Normal Logic Programs_ (NLP)
	- `not` means $\lnot$
	- `a :- b_1, ..., b_n, not c_1, ..., not c_n` is allowed
	- we lose the unique-minimal-model property
- Simpler: _Stratified Negation_
	1. draw the dependency graph \[S. 16\]
	2. check that there is no cycle of negative arrows
#### 16.09, V. ASP & VI. 
- For a NLP $P$ and an interpretation $M$, then $P^M$ s.t. 
	1. remove rules with `not a` in the body if $a \in M$
	2. remove literals `not b` from all rules if $b \not \in M$
- An _Answer Set_ (AS) of $P$ is a minimal model of $P^M$
- **Lego Approach**: learn some pieces that improve ASP vocabulary
```ASP
num(1)
left(X) :- not right(X), num(X)
right(X) :- not left(X), num(X)
```
has as a AS the binary combinations of $1$ to right and left, can be expanded by adding `num(2)`.
You can add then `left(1)` or `right(1)` then you can narrow the AS.
- if a command starts with a `#` is a meta-command
	- `#show left/1` only show the predicates you are interested in (e.g. hide `num()`)
		- `#show predicate/arity`
``` ASP
#const k = 2 %generate a constant
num(a;b) %all letters in between
num(1..2) %all nums in between
```
- Given a formula $\varphi$ in CNF, then:
	1. take `var(1..n)` for $n$ number of prop.var.
	2. set `true(X) :- not false(X), var(X)` and `false(X) :- not true(X), var(X)`
	3. set to false (no head) the formulae that falsify each clause of $\varphi$
- _Choice rule_ `{ a; b }` (as a fact or as a head of a rule)
	- Cardinality constrain: `1 { a; b; c } 2` (take only solutions with at least 1 true variables and maximally 2).
- `s :- p(X) : q(X)` stands for ``s :- p(1), p(2)`` \[V. S. 32\]
- one-to-one mappings \[V. S. 33\]
#### 23.09, VI. Games with ASP
- we use `T = #sum {C, X, Y, Z : P(X), P(Y)}` sums only `C`s but allows the sum of two equal `C`s if the `X, Y, Z` are different.
- `D = #count { M : edge(N, M, C)}` workds similarly, or also `#max`
#### 18.10, Summary
- **Syntax**
	- _normal logic programs_
		- containing only rules of the form: `a :- g, c, d, not e, not f`
	- _extensions_:
		- include variables `X, Y
		- choice rules (with cardinality constrains)
		- aggregates (`#sum, #count`)
- **Semantic**
	- _Interpretations_ $M \subseteq Atom(P)$ 
	- _Models_ $M$ are interpretations that make all rules of the program true
	- _Supported Models_ $M$ are models where each atom $a \in M$ is supported
	- _Answer Sets_ $M$ are minimal models of the riduct $P^M$
- **More Theory**
	- ==_Clark Completion_==: translate the program
		- Exam: not going to make us write the clark completion of a program down
	- ==_Unfounded Sets_==: 
	- 