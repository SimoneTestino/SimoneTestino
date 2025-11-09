Why is this not true? (So they say in [mathoverflow](https://mathoverflow.net/questions/111283/number-of-linear-orders)).
```LaTeX
\begin{Proposition}[Completeness Results]
\label{Completenes Results}
    Let $T_\preceq$ be the set of formulae (i) - (iv) defining Total Orders \ref{Total Order} and consider the classes of structures of $T_\preceq$, $(X, \preceq)$ in the first order signature $\langle \preceq \rangle$ such that $|X| = k$, then note that $T_\preceq \cup \{\vf\}$ there are at maximum eight isomorphism classes such that precisely those three formulae are either theorems or their negation is:
    \begin{itemize}
        \item[($d$)] $\forall_{x, y} \exists_z x \preceq z \preceq y$
        \item[($b^*$)] $\exists_x \forall_y y \preceq x$
        \item[($b_*$)] $\exists_x \forall_y x \preceq y$
    \end{itemize}
\end{Proposition}
```

I believe that what I wrote is correct but that what they claim is different. What they claim is for a signature $\langle N, \preceq \rangle$ where $N$ is a name for each of the objects in the domain (i.e. $|N| = k$), which is certainly not the case what I am arguing for.

I work for a prove of this result whose validity I seem to remember from [[Model Theory (Lecture)]] in the project [[Ontic Structuralism of Concepts]]. The Proposition is in fact almost true, see [StackExchange](https://math.stackexchange.com/questions/3470132/about-infinite-discrete-linear-orders-theory), the result for DLO is also widely known. The proposition is completely true for Elementary Equivalence instead of Isomorphsm, for instance take $(\mathbb{Z}, \leq) \not \simeq (\mathbb{Z},  \leq)$, or is it?