---
draft: false
date: 2025-03-07
---
For the [[Philosophy of Mathematics (Lecture)]] I wrote the following essay.

```LaTeX
\include{name}
\title{Applications and Limitations of Interpretations in Ontology}

\begin{document}

\maketitle

\begin{abstract}
    In this essay we focus on the ontological implications of the set theoretic result that adding urelements to pure set theory does not increase its expressibility. Two main elements are necessary for the argumentation: first, we introduce the concept of interpretation and, in particular, the result that \(ZF\) is definitionally equivalent to \(ZFU\); secondly, we show how a typical form of ontological argumentation relies on such interpretations. The core goal of the essay is to demonstrate, via examples and a review of broader ontological literature, the limitations of using interpretations in ontological debates.
\end{abstract}

\subsection*{Introduction}
To achieve the goal of this essay—namely, to present crucial limitations to the applicability of paraphrasing arguments in ontological debates—we begin by introducing the reader to set theory and the concept of urelements, emphasizing the natural emergence of urelements in the initial conception of sets. In order to reach the primary line of argumentation, we then introduce the definition of interpretation and of definitional equivalence as presented by \cite{visser}. With these definitions in hand, we present the result by \cite{lowe} on the similarity of pure set theory and set theory with urelements.

The second main element of the essay concerns the applicability of such set-theoretic results—which focus solely on the linguistic side of formal systems—to ontological debates. This is achieved by presenting parts of \cite{warren}, where a form of argumentation is set forth that can be very precisely defined. In this argument, a paraphrase (which is closely related to the concept of a relative interpretation as presented by \cite{visser}) is used to show how the existence of those elements that do not increase the expressive power of the language can be disregarded by committing only to the \q{smaller} language. We focus particularly on the limitations of this reasoning: as Warren himself notes, sets, by being abstract objects, cannot ontologically replace physical entities. We examine the reasons for this limitation further and address the question of exactly where the boundaries lie for this approach. We then present additional examples involving properties, considering a class of well-behaved properties that appear to best match sets, and question whether the paraphrasing succeeds in such a favourable environment. Finally, we discuss how, in general, there are two possible answers: either ontology is divided into distinct classes in which successful paraphrases can occur only within each class, or the boundaries between these classes are fuzzy, so that the composability of interpretations fails—thereby preventing the formation of a proper category as envisioned in \cite{visser}.

\section{Philosophy of Set Theory with and Without Urelements}
In this section, we provide a brief introduction to the philosophical significance of incorporating urelements into set theory. First, we explain how the role of urelements appears to be crucial for the most basic philosophical intuition of what a set is. Next, we discuss why urelements have recently come to be considered superfluous in contemporary mathematics, by briefly presenting the relevant mathematical results as outlined in \cite{lowe}. Finally, returning to the philosophical considerations, we discuss the rationale for including them in our philosophical frameworks. In particular, we outline the specific role that urelements play in ontological debates, and demonstrate how set theory can be employed—see \cite{warren}—to derive important conclusions in broader ontological discussions. We begin by considering urelements as introduced in \cite{yao}:

\begin{quote}
    Urelements are members of sets that are not themselves sets. 
\end{quote}

\subsection{The Intuition of Set}
For both mathematicians and philosophers, the idea of recasting all of mathematics in the language of set theory has always been highly appealing. This allure comes not only from set theory’s standing as a uniquely formal and well-structured framework – with its most popular version, $ZFC$, being remarkably simple – but also from the fact that sets are naturally intuitive and straightforward. The notion that complex results across algebra, analysis, and number theory can all be derived from the basic idea of a set is, without a doubt, very attractive.

Yet, within this vision two distinct ideas are often mixed up: the everyday, intuitive notion of a set and the rigorous mathematical construction of sets. For example, one could argue that the way we develop our understanding of arithmetic numbers – at least the finite ones, as discussed in \cite{carey} – closely mirrors the formal structure given by arithmetic axioms (like those in $PA$), so that the numbers we learn to count eventually resemble those defined by formal systems. Even this simple arithmetic case, however, encounters difficulties when the formalisation yields models that do not necessarily capture the \textit{intended} interpretation, such as the occurrence of non-standard models.

When we shift our focus back to set theory and compare our intuitive grasp of sets with the formal structures we ultimately construct, there are significant challenges to overcome before we can achieve a correspondence akin to that in arithmetic – and even then, with some limitations. First, when we think of sets as collections of objects in the physical world, this notion seems to arise in a much more instinctive manner and much earlier in our development compared with arithmetic. For instance, we naturally form the idea of a set when grouping items that share a common property, such as objects of the same colour. Nevertheless, this basic notion is still quite different from the formal concept of a set used in set theory. Moreover, a common initial confusion is that these everyday sets, as collections of objects, often include elements that are not themselves sets. In fact, the very first intuitive idea of a set that people use in daily life contains what we call urelements—objects that are not sets.

In the upcoming subsection, we introduce some mathematical results showing that it is possible to rephrase all those urelements in terms of sets while preserving the full meaning of our expressions. Initially, this should be regarded purely as a linguistic transformation—a rephrasing of our language into one that does not explicitly include urelements, yet conveys exactly the same ideas. The following subsection then explores how one can justify this transformation from an ontological perspective, ultimately reducing urelements to a smaller collection until only sets remain.

\subsection{Interpretations of Theories}
As we have seen, one primary goal of set theory, ever since it gained popularity in mathematical discourse, has been to recast mathematics in set‐theoretic terms. This approach offers the significant advantage that the language of set theory is remarkably simple, and once fully developed, the theory that defines sets turns out to be, in most of its axioms, straightforward. Conversely, if we were to choose between set theory with urelements and set theory without them, it is clearly more convenient to adopt the version without urelements. Urelements introduce additional complications in the language and require extra considerations when formulating the axioms, thereby making the overall system somewhat more complex.

This naturally raises the question: if we are to recast mathematics in set‐theoretic language, should urelements be included, and if so, which ones? A compelling argument against including urelements is to demonstrate that they are redundant. One way to do this is to prove that adding urelements to the language—and adopting the corresponding theory that reformulates the $ZF$ axioms so they retain an analogous meaning when quantifiers range over a larger domain that includes urelements—does not actually extend the expressive power of the language but instead leaves it unchanged.

Phrasing this claim in precise mathematical terms is challenging, as many details must be rigorously defined. To formalise the notion of redundancy in the expressive power of the language, we introduce two key concepts as presented in \cite{visser}. A \textit{relative translation} is a syntactic mapping between the language of set theory with urelements and that of pure set theory; it consists of a formula defining the domain of the translation together with a mapping that assigns to each predicate symbol a corresponding formula in the target language. A \textit{relative interpretation} is a relative translation that further preserves the logical structure of a theory—namely, it ensures that if a sentence is provable in the original theory, then its translation is provable in the target theory. In this way, by constructing a relative translation (and hence a relative interpretation) between the urelement theory and the pure set theory, we can rigorously demonstrate that adding urelements does not enrich the expressive power of the language. We see in more detail how this works in the upcoming subsection.

\subsubsection{Similarity of $ZF$ and $ZFU$}
Following \cite{visser}, we first present the formal definition of an interpretation and then introduce four conditions that can be used to consider two interpretations as identical. Understanding the identity criteria of an object is crucial because it provides us with the proper ontology of that object and allows us to understand its true nature. We begin by defining a relative translation as a tuple 
\[
\langle \delta, F \rangle,
\]
where \(\delta\) is a formula in the target language that determines the domain of the translation—that is, it specifies which elements of the target structure correspond to the elements in the source language—and \(F\) is a mapping that assigns to each predicate symbol \(R\) (of arity \(n\)) in the source language a corresponding formula \(F(R)\) in the target language with free variables among \(v_0,\dots,v_{n-1}\). A relative interpretation is then defined as a triple 
\[
\langle U, \tau, V \rangle,
\]
where \(U\) is a theory in the source language, \(V\) is a theory in the target language, and \(\tau = \langle \delta, F \rangle\) is a relative translation from the language of \(U\) to that of \(V\) such that for every sentence \(A\) of \(U\), if \(U \vdash A\) then \(V \vdash A^\tau\) (with \(A^\tau\) denoting the translation of \(A\) under \(\tau\)).

The framework presented in \cite{visser} distinguishes several levels of sameness between interpretations; however, here we focus on the strongest level, namely, \textit{synonymity} or \textit{definitional equivalence}. In our notation, the variables \(K, L, \dots\) always range over triples of the form \(\langle U, \tau, V \rangle\). The following are the detailed conditions that must be satisfied for two relative interpretations 
\(K = \langle U, \tau, V \rangle\) and \(K' = \langle U, \tau', V \rangle\) to be considered definitionally equivalent (i.e. equal$_0$ or =$_0$):

\begin{itemize}
    \item[(a)] \textit{Equivalence of Domain Formulas:} The domain formulas used in the translations must be provably equivalent in the target theory \(V\); that is,
    \[
    V \vdash \delta_\tau \leftrightarrow \delta_{\tau'},
    \]
    ensuring that both translations choose the same subset of \(V\) as the universe corresponding to the source theory.
    
    \item[(b)] \textit{Equivalence of Predicate Translations:} For every predicate symbol \(R\) in the source language, the formulas assigned by \(F_\tau\) and \(F_{\tau'}\) must be provably equivalent in \(V\):
    \[
    V \vdash F_\tau(R) \leftrightarrow F_{\tau'}(R).
    \]
    This guarantees that the relational structure is identically preserved by both translations.
    
    \item \textit{Equivalence on Formulas:} Consequently, for every sentence \(A\) in the source language, the translations \(A^\tau\) and \(A^{\tau'}\) must be provably equivalent in \(V\). This condition ensures that the entire deductive content of the source theory \(U\) is captured in the same manner by both interpretations.
\end{itemize}

What is the result of our main interest for this purpose is that $ZF$ and $ZFU$ are proved to be \textit{similar} or \textit{definitionally equivalent} in \cite{lowe}. This is a result that is achieved by constructing explicit translations between the two theories. In his proof, Löwe first defines a translation from $ZF$ to $ZFU$ by identifying each pure set in a model of $ZF$ with a corresponding set in a model of $ZFU$, effectively disregarding the urelements. Conversely, he shows that every model of $ZFU$ contains a canonical inner model of pure sets—its \textit{kernel}—which satisfies the axioms of $ZF$. By recursively translating sets in a $ZFU$ model into pure sets, one can demonstrate that the additional axioms governing urelements do not alter the structure of the pure sets. Consequently, every theorem concerning pure sets in $ZF$ remains valid in $ZFU$, and vice versa. Thus, Löwe's construction establishes that $ZFU$ is merely a conservative extension of $ZF$, showing that the expressive power of the language is unchanged even when urelements are present.

Before turning to the main claim of the essay, we examine the ontological consequences arising from this debate. In particular, we are interested in understanding how translations serve to diminish the role of urelements in our considerations, thereby providing a basis for more effective arguments in ontology. By showing that the addition of urelements does not extend the expressive power of our set‐theoretic language we are led to question whether urelements are ontologically indispensable.

\subsection{Urelements in Ontological Debates}
When one first realises that sets are tools that allow us to express all of the mathematics we discuss, a mathematical realist might then question whether it remains appropriate to assert that entities such as numbers or vector spaces exist independently, or whether it is more parsimonious to simply acknowledge the existence of sets—since all those other terms can be paraphrased in set-theoretic language. This straightforward yet informal argument implicitly bridges two distinct domains of philosophy. On one hand, we have results that are essentially linguistic, such as translations between different languages that speak of various objects; on the other hand, we derive conclusions about the ontology of the objects being discussed. Without a deeper explanation of this connection, however, the argument appears potentially fallacious—as, for instance, most would agree that the ontology of a \textit{chair} does not depend on the language used to describe it.

On this note, \cite{warren} argues that in ontological debates there is a frequently employed line of argumentation that uses interpretations\fn{the relation between paraphrases and interpretations is mentioned in \cite{warren}, p. 1245}:

\begin{quote}
    Adding ontological resources usually buys us some expressive power. This added expressive power is often offered as a reason for accepting the new ontology. But if a paraphrase is available, then the additional expressive power can be had without going in for the new ontology.
\end{quote}

The case of interest for applying the similarity between $ZF$ and $ZFU$ is one in which the resources accepted in the debate encompass the entirety of set theory, while some or every other object is disputed. In this scenario, we can successfully argue by considering $ZF$ as the nihilist theory—that is, a theory which accepts the resources provided by set theory but denies the existence of any other objects—while the anti-nihilist side supports some form of $ZFU$. In \cite{warren}, the author contends that the applicability of this ontological step depends on the subtleties of the specific debate in question and that this method has clear weaknesses when applied to a general claim such as this one.

In the upcoming section we aim to present one particular difficulty that arises both on the formal and informal level when working with translation in the attempt to conclude ontological claims. This issue has been only partially mentioned in \cite{warren}, and we show how the conclusions might be more dramatic for the argumentative line presented than they are regarded in that paper.

\section{Urelements and the Metalanguage}
In \cite{warren} before having the relative interpretations formally presented, we have the following concern: 
\begin{quote}
    The big picture point of interest is simple. When our RESOURCES are the resources of set theory, then OBJECTS + RESOURCES can be paraphrased using RESOURCES. Section 2's discussion took place in the informal language of set theory, in which we proved results about class models of $ZFU$. As we noted there, it simplified things to assume in the informal metalanguage that the disputed objects exist. But this is not an assumption that the anti-existence side in an ontological dispute can make. They deny the existence of the disputed objects. This is what the entire dispute is about! According to the anti-existence side, the supposed universe $V_{\text{Disp} \cup \text{Undisp}}$ simply is $V_{\text{Undisp}}$ - \q{$\text{Disp}(x)$} is empty, according to them.
\end{quote}
This fundamental issue is then resolved by constructing the relative interpretation in a language that takes as urelements only those objects on which both parties agree—the \(\text{Undisp}\)—it follows that such a result must be intelligible to both sides, and even the existence side will need to agree that all they can affirm about the disputed objects can be stated without assuming their existence.

What we argue for here is that an analogous problem arises even when we choose the smaller language. On one hand, anti-existence advocates reject any argument formulated in a metalanguage that includes the disputed objects; on the other, proponents of the existence of the disputed objects would object to restricting the language solely to a smaller subset comprising only the undisputed objects.

To simplify the context, we now consider the anti-existence side to claim that there are no urelements (i.e. \(\text{Undisp} = \emptyset\)), while the existence side asserts the existence of some finite set of urelements, \(\text{Disp} = \{u_1, u_2, ..., u_n\}\) denoting some physical objects. In order for the construction of the translation to be intelligible to the anti-existence side, the metalanguage in which it is developed must not include the disputed urelements; for the reasons Warren states above, this metalanguage would then be that of pure set theory. Such an argument would be entirely acceptable to the anti-existence side. What we question now, is whether the existence side would agree with the restriction of the metalanguage to a mathematical language that does not include physical entities.

On this point, Warren makes a straightforward note:
\begin{quote}
    Of course, the language of the pro-existence side (\(L_{\text{Disp} \cup \text{Undisp}}\)) can include these symbols, but nobody ever doubted that the \q{bigger} ontological language could paraphrase the \q{smaller} ontological language. They can do so quite simply by restricting quantifiers to exclude the disputed objects.
\end{quote}

In our simple example, this is equivalent to saying that the language of pure set theory is clearly intelligible also to someone whose language ranges over physical objects. What remains unclear—and precisely the passage that we claim to be failing—is whether the mere intelligibility of the language of pure set theory, for someone who claims the existence of urelements, implies that they would agree to limit the expressibility of their metalanguage to that fragment. Even though the construction of the relative interpretation is intelligible to the existence side, proponents of the existence of physical objects would object to the idea that such objects can be reduced to mere sets. The reason simply being that physical objects belong to another class of entities while sets are abstract objects and no collection of abstract objects makes up a physical one. This point partially also remarked by Warren, as he implicitly underlines some similar limitations, either considering debates that only concern abstract objects or by using the argument to reduce sets of physical entities to smaller sets of urelements that still contain physical entities (see \cite{warren}, p. 1246).

\subsection{Crossing an Ontological Class}

The question now arises whether this argument can be extended to certain classes of abstract objects that cannot be easily coded with sets. A notorious example is that of properties. The traditional comparison considers sets with physical objects as urelements, but a similar discussion applies when comparing properties and pure sets. The standard argument is that properties cannot be viewed purely extensionally because there exist distinct properties with the same extension—for example, the property of collecting entities with a heart versus those with a kidney, which may have the same extension yet are clearly different properties.

When we apply the previous discussion here, we are engaging in something more general than merely proposing an extensional treatment of properties. For instance, a mapping from a language that includes properties to a language of sets with urelements might fail in the given example by identifying two properties that are actually distinct. To facilitate the process, let us restrict our attention to well-behaved properties—that is, those whose extensions are sets, thereby excluding those whose extension we cannot prove to be a set. Now, suppose we were to establish a relative interpretation between the language of well-behaved properties and that of \(ZFU\), where the urelements are precisely the entities to which the properties apply. This could be achieved by, for example, distinguishing all properties with the same extension by indexing them by an ordinal.

Once we have demonstrated that this mapping is indeed a valid relative interpretation, the question remains: would this allow us to conclude that including properties in our ontology is unnecessary, as everything can be captured by the resources of sets? Similarly to the earlier debate in which physical objects were argued to belong to a different ontological branch, one might then claim that properties are fundamentally different from sets and that even these well-behaved properties cannot be fully rephrased in \(ZFU\)—and hence, by composition, in \(ZF\). This is traditionally done by claiming that the intensionality of properties cannot be well captured by set theoretic constructions. A similar discussion can also be done for possible worlds, where modally realists metaphysical frameworks would certainly disagree with their reduction to mere sets.

At first, it was clear that the gap between sets and physical objects was too wide to bridge; one could not convincingly argue that physical objects should be ontologically reduced to sets. A similar argument can be made with properties or possible worlds, since properties possess something fundamentally distinct from sets, and any rephrasing of them in set-theoretic terms would be merely a linguistic maneuver rather than an ontological reduction. The open question then is: what are the limits of these branches? In other words, which objects can we satisfactorily rephrase in terms of sets so that we might argue that an ontological commitment to those objects is unnecessary?

This question can be approached in two ways: in a fuzzy manner or in a determined manner. If answered in a determined way, ontologies would be split into distinct classes in which interpretations can be made, and within each of these classes an expressive language would exist that can phrase every term appropriately. For instance, one might have sets for mathematical entities and atomic particles for physical objects. However, what seems more plausible in a philosophical debate is that these classes have fuzzy boundaries. That is, there may be cases where some entities are close enough to be interpreted in a second class, and that second class is close enough to a third class for an interpretation to be established between them, yet we would not agree that the first class can be interpreted in the third one. This failure of composability of interpretation undermines the formation of a well-behaved category, as required by the framework presented in \cite{visser}.

\subsection*{Conclusion}
We have first seen that the argumentation presented by \cite{warren} is accompanied by certain difficulties, as he himself acknowledged, and that incorporating these issues into ontological debates raises questions that are not easily answered. In ontology, it is crucial that the objects whose existence is posited are organized into distinct classes. This classification emerges naturally from philosophical inquiry, and any attempt at generalization necessarily entails adopting a firm stance in various debates. Consequently, we are left with two alternatives, neither of which we definitively endorse, but both of which expose significant limitations. This concludes that the boundaries of the ontological classes in which successful paraphrases may be applied must be thoroughly examined before any paraphrase-based argumentation can be properly considered.


\newpage
\begin{thebibliography}{12}

\bibitem[Carey 2010]{carey} Carey, J. (2010). \textit{Foundations of Set Theory}. Cambridge: Cambridge University Press. 

\bibitem[Löwe 2006]{lowe} Löwe, B. (2006). Set Theory with and without Urelements and Categories of Interpretations. \textit{Notre Dame Journal of Formal Logic}, 47(1), 83--91.

\bibitem[Visser 2004]{visser} Visser, A. (2004). Categories of Interpretations in Logic. \textit{Journal of Symbolic Logic}, 69(2), 295--319.

\bibitem[Warren 2021]{warren} Warren, J. (2021). Ontology, Set Theory, and the Paraphrase Challenge. \textit{Journal of Philosophical Logic}, 50(6), 1231--1248.

\bibitem[Yao 2023]{yao} Yao, B. (2023). Set Theory with Urelements (Doctoral dissertation). University of Notre Dame.

\end{thebibliography}





\end{document}
```