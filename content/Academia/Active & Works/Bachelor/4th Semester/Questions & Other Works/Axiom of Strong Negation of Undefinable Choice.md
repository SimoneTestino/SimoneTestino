The questions on this topic have been first exposed in: [Overleaf: Axiom of Strong Negation of Undefinable Choice](https://www.overleaf.com/read/cdjmtszyvqcv#476c02). 
## $ZF \vdash Finite$ $Choice$
In this section I resemble the proof of Finite Choice from the axioms of $ZF$ by following the [Discussion](https://mathoverflow.net/questions/32538/finite-axiom-of-choice-how-do-you-prove-it-from-just-zf).

Here I recap [Andreas Blass](https://mathoverflow.net/users/6794/andreas-blass)'s answer:
	We are given the existential statement, "There is an element in $x$." What should be noticed in addition is that what we want to prove is also an existential statement, "There is a choice function." We have an _explicit_ construction, which I'll call $C$, that will convert any element of $x$ into a choice function, namely sending any $y$ to $\{(x,y)\}$. **If we can't explicitly define any particular $y$**, then **we won't be able to define any particular choice function either**, but **the problem doesn't require us to explicitly define a choice function**; we need only prove that one exists. And that follows, thanks to $C$, from the existence of elements in $x$.

Then, I shall distinguish two axioms: Axiom of  Finite Choice ($AFC$) and Axiom of Finite Definable Choice ($AFDC$), and from the answer above I note $ZF \vdash AFC$. Now, meanwhile $AFC$ can clearly be written within the object language $\mathcal{L}_\epsilon$, it might not be the case with $AFDC$, in fact this axiom should entail the predicate "being $\mathcal{L}_\epsilon$-definable" which cannot clearly be written in the same language since it depends on it.

**Question**: Is there a way to express $AFDC$ in $\mathcal{L}_\epsilon$?
A candidate but possibly way to complex method would be to change the logic behind the existential quantifier "$\exists_x \varphi(x)$" might be true only if you can present an $x$ s.t. $\varphi(x)$, this would be a more radical version of _intuitionistic mathematics_ (here I mean the one excluding $AC$ and not necessarily $A \lor \lnot A$). In fact one would, in such a logic, not admit any proof of existence that cannot present a definable example, this can clearly be stated in the semantical definition of the quantifiers of a classical (or intuitionistic, in the sense that rejects $A \lor \lnot A$) logic.

Otherwise, one might simply add a predicate $\delta$ to $\mathcal{L}_\epsilon$, call it $\mathcal{L}_{\epsilon, \delta}$, s.t. $\delta(x)$ iff. there is a formula $\varphi \in \mathcal{L}_\epsilon$ s.t. $\forall_{y} \varphi(y) \leftrightarrow \varphi(x)$. Since there is an existential on formulae, this is a metalinguistic definition, which is not a problem since all syntax is traditionally defined metalinguistically (i.e. $a \land b$ iff $a$ and $b$). Note that the definition of $\delta$ is *not recursive* because it runs over formulae in the language without $\delta$ itself.

In $\mathcal{L}_{\epsilon, \delta}$ we can write $AFDC$ and consider both $ZF + AFDC$ and $ZF + \lnot AFDC$ which will both probably be consistent, since $ZF$ is written in $\mathcal{L}_\epsilon$ only. One might proceed by adding axioms to $ZF$ s.t. they result consistent with $SNUC$ as expressed in the $\LaTeX$ file above.

**Question**: Could we have an axiom $X$ in $\mathcal{L}_{\epsilon, \delta}$ s.t. $ZF + X \vdash ADC$, i.e. the Axiom of Definable Choice? Is $X$ needed?
That is an axiom that allows to pick definable elements. Perhaps this axiom might not even be needed if we are in $\mathcal{L}_{\epsilon, \delta}$.

**Question**: Can we finally prove $con(ZF) \Rightarrow con(ZF + AFDC) 