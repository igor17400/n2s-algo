# Computing Time Complexity

Computing the time complexity of algorithms can be challenging. Understanding and analyzing the time complexity is crucial for evaluating the efficiency of algorithms. Several methods are available to compute and solve recurrences, which help in determining the time complexity of recursive algorithms. In this section, we will briefly explain some commonly used methods and give some examples to sharpen our intuition.

Let's focus on some examples and rules that can help determine the running time of an algorithm.

<u><i>Examples:</i></u>

- **Loops**: The total running time is the product of the running time of the statements inside the loop and the number of iterations. In general, this results in $O(n)$.

- **Nested Loops**: The total running time is the product of the sizes of all the loops. For two nested loops, $T(n) = c \cdot n \cdot n = cn^2 = O(n^2)$.

- **Consecutive Statements**: Add the time complexity of each statement. Look at the pseudocode in Algorithm, we have $T(n) = c + cn + cn^2 = O(n^2)$.

- **If-Then-Else**: The total running time will be based on the test plus the larger of either part of the if/else. Look at Algorithm. We can see that $T(n) = c + cn = O(n)$.

```{prf:algorithm} Ford–Fulkerson
:label: my-algorithm

**Inputs** Given a Network $G=(V,E)$ with flow capacity $c$, a source node $s$, and a sink node $t$

**Output** Compute a flow $f$ from $s$ to $t$ of maximum value

1. $f(u, v) \leftarrow 0$ for all edges $(u,v)$
2. While there is a path $p$ from $s$ to $t$ in $G_{f}$ such that $c_{f}(u,v)>0$
	for all edges $(u,v) \in p$:

	1. Find $c_{f}(p)= \min \{c_{f}(u,v):(u,v)\in p\}$
	2. For each edge $(u,v) \in p$

		1. $f(u,v) \leftarrow f(u,v) + c_{f}(p)$ *(Send flow along the path)*
		2. $f(u,v) \leftarrow f(u,v) - c_{f}(p)$ *(The flow might be "returned" later)*
```