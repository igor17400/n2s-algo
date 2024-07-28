# Mathematical Induction

Mathematical induction is a proof technique used to establish the truth of an infinite sequence of statements. It consists of two main steps:

- **Base Case:** Verify that the statement is true for the initial value, usually $n = 0$ or $n = 1$.
- **Inductive Step:** Assume that the statement is true for some arbitrary value $n = k$ (inductive hypothesis), and then prove that it is true for $n = k + 1$.

By completing these steps, one can conclude that the statement holds for all natural numbers $n$.

<u><i>Example:</i></u> Let's use mathematical induction to show that 

$$
1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}
$$

for all integers $n \geq 1$.

Our induction hypothesis claims that the equation holds for every $k$. That is,

$$
1 + 2 + 3 + \cdots + k = \frac{k(k+1)}{2}
$$

Then, we want to prove that the equation also holds for $k + 1$.

$$
1 + 2 + 3 + \cdots + (k + 1) = \frac{(k+1)(k + 2)}{2}
$$

From the above equations, let's take their left-hand side and compare them.

$$
\begin{aligned}
1 + 2 + 3 + \cdots + (k + 1) &= 1 + 2 + 3 + \cdots + (k + 1) \\
1 + 2 + 3 + \cdots + (k + 1) &= [1 + 2 + 3 + \cdots + k] + (k + 1)
\end{aligned}
$$

**Base Case:** let's verify the base case $n = 1$. Using the equation for this,

$$
n = 1, \quad 1 = \frac{1(1 + 1)}{2} \Rightarrow 1 = 1 \quad \text{(True)}
$$

**Inductive Step:** next, we need to verify that such equality also holds true for $n = k + 1$. By replacing the equations in the above comparison we have

$$
1 + 2 + 3 + \cdots + (k + 1) = [1 + 2 + 3 + \cdots + k] + (k + 1)
$$

$$
1 + 2 + 3 + \cdots + (k + 1) = \frac{k(k+1)}{2} + (k + 1)
$$

$$
1 + 2 + 3 + \cdots + (k + 1) = (k + 1)\left( \frac{k}{2} + 1 \right)
$$

Finally,

$$
1 + 2 + 3 + \cdots + (k + 1) = \frac{(k + 1)(k + 2)}{2}
$$

Which concludes our proof. We can see that our proof consisted of three main steps:

1. Verify that the base case (n = 1) holds true.
2. Assume by our induction hypothesis that the equation holds true for $n = k$.
3. From the equality where $n = k + 1$, our goal was to show that indeed the sequence $1 + 2 + 3 + \cdots + (k + 1)$ is equal to $\frac{(k + 1)(k + 2)}{2}$.
