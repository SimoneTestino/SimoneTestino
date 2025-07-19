This page is about a field of mathematics which _should exist_ but which I did not hear about yet, if anyone reading this page has ever heard about literature in a field that has even some similarities with this, please contact me, [[Contacts]].

For now I limit myself to write no more than [[Closure Theory#The Intuition]] in the hope that I will encounter literature directly facing these issues soon; if that will turn out not to be the case, I will then provide some formalisms to the intuition.
#### The Intuition
A closure is a function that takes as input a structure and an operation on a subset of the underlying set of the structure and outputs what is commonly known as the closure of that structure under the given operation.

Examples of such closures are numerous in mathematical practice, very often one is explicitly required to close graphs and algebraic structures under some given operations. Often this turns out to be trivial but many cases, especially in those involving more closures in a row, this may get tricky.

In particular, there are some operations and classes of structures that always admit a closure, like transitivity and graphs. There are some closures which _open_ the set under other operations, for instance, if we take a graph and close it first under transitivity and then close it under symmetry, we may have _opened_ it again under the transitivity operation. This shows that sometimes the order in which one closes a structure could make a difference and that, sometimes, only repetitions allow for an actual closure under multiple operations. It is admissible, that there are some operations whose closure is incompatible, i.e. there is no order nor (finite?) repetitions of closures such that the underlying set is closed under all operations.

From this handful of imprecise observations, the reader should only share with me the feeling that if some mysterious dynamics in history of mathematics prevented this field to see the light, then it certainly should now!
## Some Definitions
Before getting to the definition of a Closure, I need to have some structures. I conceive in fact the to be a function on structures. There may be technique to generalise a closure to broader classes of structures, for now, I take some specific kinds of structures.

A closable structure $\mathfrak{C} = (C, \circ)$ is tuple of $C$ a set and $\circ$ an operation.

#### List of Potentially Related Fields
- [Magma Algebra](https://en.wikipedia.org/wiki/Magma_(algebra)#:~:text=à%203%2C%201970.-,Definition,for%20a%20properly%20defined%20operation.)
- Fixed Points