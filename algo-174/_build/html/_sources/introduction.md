# Introduction to Algorithms

Informally, an <span style="background-color: #F9F9E0;">algorithm</span> is any well-defined computational procedure that takes some value, or set of values, as <span style="background-color: #F9F9E0;">input</span> and produces some value, or set of values, as <span style="background-color: #F9F9E0;">output</span>. An algorithm is thus a sequence of computational steps that transform input into the output.

An algorithm is considered **correct** if, for every input instance, it halts with the <span style="background-color: #F9F9E0;">correct</span> output. We say that a correct algorithm solves the given computational problem. Contrary to common belief, <span style="background-color: #F9F9E0;">incorrect</span> algorithms can sometimes be useful, if we can control their error rate.

> $\textcolor{#FF90BC}{\Longrightarrow}$ An algorithm can be viewed as a tool for solving a well-specified computational problem

## Efficiency

When assessing the efficiency of algorithms—comparing whether algorithm A is more efficient than algorithm B—we should focus on counting fundamental operations rather than measuring time. Performance is typically expected to vary based on the size of the input. As defined by {cite}`clrs` *"we are concerned with how the running time of an algorithm increases in the size of the input <span style="background-color: #F9F9E0;">in the limit</span>, as the size of the input increases without bound."*

> $\textcolor{#FF90BC}{\Longrightarrow}$ $O(\cdot)$ Upper bound $\quad | \quad \Omega(\cdot)$ Lower Bound $\quad | \quad \Theta(\cdot)$ Both

> $\textcolor{#FF90BC}{\Longrightarrow}$ $o(\cdot)$ Strict upper bound $\quad | \quad \omega(\cdot)$ Strict lower bound

Two primary measures determine algorithm efficiency: <span style="background-color: #F9F9E0;">time complexity</span> and <span style="background-color: #F9F9E0;">space complexity</span>.

### *Space Complexity*

The amount of <span style="background-color: #F9F9E0;">time</span> an algorithm takes to run as a function of the input size.

### *Time Complexity*

The amount of <span style="background-color: #F9F9E0;">memory</span> an algorithm requires to run as a function of the input size.

When evaluating either type of complexity—time or space—we utilize asymptotic notation, which we define briefly below:

- **$\Theta$-notation**: Represents the asymptotically tight bound of an algorithm's complexity. It defines functions that grow at the same rate asymptotically.
- **$O$-notation**: Denotes the upper bound of an algorithm's complexity. It signifies the worst-case scenario of the algorithm's growth rate.
- **$\Omega$-notation**: Indicates the lower bound of an algorithm's complexity. It defines the best-case scenario of the algorithm's growth rate.
- **$o$-notation**: Describes a stricter upper bound than $O$-notation. It denotes functions that grow faster than a given function but not asymptotically tight.
- **$\omega$-notation**: Denotes a stricter lower bound than $\Omega$-notation. It signifies functions that grow faster than a given function but not asymptotically tight.

For example, we represent notations such as $O(n)$, $O(2^n)$, $O(n \log n)$, $O(n^2)$, $O(\log n)$, and others. The distinctions between these functions can be visualized through plots, as illustrated in the figure below.

See {ref}`Figure <complexity_graph>` for a visual comparison of complexity graph curves.


:::{figure-md} complexity_graph
<img src="figures/complexity_graph.png" alt="Comparison of complexity graph curves" class="mb-1" width="500px" height="300px">

Comparison of complexity graph curves.
:::