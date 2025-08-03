This writing was a part of [[What a Logic Could not Be]] which I decided to cut after changing course to the essay. It gives a decently precise definition of _choice_, possibly different from the familiar one used in mathematical praxis. The formalisation uses theory presented in [[Model Theory (Lecture)]].

``` LaTeX
\section{The \enquote{Choice}}
What we naturally mean when we say that we have a choice, is that we are given with the to pick one of some options we are given, these choice are supposed to be, on one hand all different, or it wouldn't be much of a choice, but on the other hand, they should all have some common features for a certain aim we are making the choice for. Similarly, in mathematics a choice is made between options that are, in some respects, equivalent but in some other equivalent: for instance, it often happens to be the choice of an element in some equivalence class.  What is crucial here, is that the chosen element has no distinguished feature, i.e. there is no definable property in the language that is true only for that object. That is to say that all options we have are equivalent, there is nothing that we can say for a distinguished object among our options. In set theory, we say that, if the set of choices we are given is infinite, then we require the Axiom of Choice; in the definition I gave above though, there is no need for it to be infinite.

\subsubsection*{Formalisation}
In order to get to a more precise definition of a choice, I need first to define what a complete type is. The following formalisations are not necessary for a satisfactory understanding of the essay. To have a better grasp of the distinction of object and metalanguage, the reader is suggested to read the first section of \href{https://plato.stanford.edu/entries/tarski-truth/#ObjLanMet}{SEP: Tarski's Truth Definitions}.

\begin{Definition}[Complete Type]
    Given a model $\mathcal{M}$ (with domain $M$) in a language $\mathcal{L}$ and an object $\alpha \in M$, define the complete type $tp^\mathcal{M}(\alpha) = \{\varphi(\cdot) \in \mathcal{L}: \mathcal{M} \models \varphi(\alpha)\}$ where $\varphi(\cdot)$ denotes formulae with one free variables.
\end{Definition}

\begin{Definition}[Choice]
    Given a theory $T$, a set $S$ s.t. for each $\mathcal{M} \models T$ it holds $\forall_{s, s' \in S} tp^\mathcal{M}(s) = tp^\mathcal{M}(s')$ (definitional equivalence of $S$ with respect to $T$) and a function $f: S \to \{0, 1\}$ s.t. there is a unique element with $f(s) = 1$, then $s$ is called a choice of $f$ in $S$ with respect to $T$.
\end{Definition}

\begin{Remark}
    Existence of a choice $s$ in a set $S$ with respect to $T$ for $|S|$ infinite requires the axiom of choice in the metatheory.
\end{Remark}

\subsection{\enquote{Canon} and \enquote{Abstraction}}
In this essay I denote with the term \enquote{Abstraction} some object previous to a choice, like an equivalence class previous to the choice of a single element; that is, I believe, a more strict denotation of the natural one for abstraction, it is also a more precise one and the one I need in the scope of this essay. Also, with the word \enquote{Canonical Choice} I denote an object that has some metalinguistic feature that is, indeed, distinguished among the other options, and which allows to bypass the \emph{definitional equivalence} of all properties. For instance, a Canonical Choice might be one referring to the syntax, i.e. take the object whose name comes first in the alphabetical order, features of this kind, are not accessible within the language and are therefore not definable even though metalinguistically, we can clearly define those.

\subsubsection*{Formalisation}

\begin{Definition}[Abstraction]
    For a choice $s$ in a set $S$, call $S$ (one of) the abstraction(s) of $s$.
\end{Definition}

\begin{Definition}
    In a set $S$ with a choice $s$ a canon $\kappa$ is a metalinguistic formula with one free variable s.t. $\kappa(s)$ and $\forall_{s' \in S \setminus \{s\}} \lnot \kappa(s')$.
\end{Definition}

\subsection{The Problem of Choice}

Given a definitionally equivalent set $S$, the logician is can choose one of the three following paths

\paragraph{I. Abstract} If the logician refuses to pick an element, they can decide to stick with the set $S$. This allows them to do not loose information but may not allow them to make any considerations or computations that can be made only on elements of $s$ and not on sets of them, some examples are present in the upcoming sections.

\paragraph{II. Choose} In order to make some of the named computations, the logician may choose one object, this though requires them, if $|S|$ is infinite, to assume the axiom of choice in their metatheory.

\paragraph{III. Canonical Choice} Some of the named computations may come out easier if one knows already, metalinguistically, what to expect from the choice, therefore one often looks for some form of canonical choice. This option also prevents us to assume metatheoretically the axiom of choice.

These paths are best understood via examples, I present in the next sections how one can apply this concepts in a complete conception of pluralism.
```