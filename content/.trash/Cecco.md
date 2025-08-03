1.6 $A \cap B = A \Leftrightarrow A \subseteq B$
- $A \cap B = A \Rightarrow A \subseteq B$ 
	- Want to show $A \subseteq B$, which is proved $x \in A \Rightarrow x \in B$, so let $x \in A$ and want to prove $x \in B$. So for $x \in A$, since $A = A \cap B$, then $x \in A \cap B$, hence $x \in A \land x \in B$ hence $x \in B$.
- $A \subseteq B \Rightarrow A \cap B = A$ 
	- Assume $A \subset B$, want to show $A \cap B = A$. To prove the claim:
		- "$A \cap B \subseteq A$" to prove let $x \in A \cap B$ and want show $x \in A$, and we know that $x \in A \cap B \Rightarrow x \in A \land x \in B \Rightarrow B$.
		- "$A  \subseteq A \cap B$ " to prove let $x \in A$ and want show $x \in A \cap B$. So for $x \in A$, since $A \subseteq B$, hence $\forall_{x} x \in A \to x \in B$, hence $x \in B$. Since we know $x \in A \land x \in B$, we derive $x \in A \cap B$.
	