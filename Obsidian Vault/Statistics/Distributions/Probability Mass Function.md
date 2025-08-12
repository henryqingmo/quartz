---
tags:
  - math/statistics/random_variable
---
### Idea
#### Discrete
![[Pasted image 20250614173355.png]]
PMF is basically an function that maps the output of [[Statistics/Random Variables/Random Variable|Random Variable]] to the probability of their preimage.
 
 $X = x$ is the preimage of an element $x$ in the range produced by the function of $X$. [[Statistics/Random variable|Random variable]], so it's an event (subset of $\Omega$).

Preimage of different $x$ is disjoint, 
> [!note]
>This is because if there is overlapping preimage, the overlapped element would have been mapped to more than one $x$, which is impossible for a function.

So the union of all possible event $X = x$ is $\Omega$, which would have probability of $1$.
#### Example
![[Pasted image 20250614175335.png]]
Here $\Omega = X \times Y$, the Cartesian product $(x, y)$

#### Conditional PMF
![[Pasted image 20250615185008.png]]
![[Pasted image 20250621213916.png]]
> [!note]
> Think of basically replaced the sample space with the $P(A\cap x)$

Basically the rule for [[Expected Value]] and [[Variance and Standard Deviation]] still applies. 
![[Pasted image 20250615185258.png]]
##### Multi-variable condition.
![[Pasted image 20250622160947.png]]
Here we replaced the $A$ from above to the event $Y = y$
![[Pasted image 20250622161038.png]]
##### Joint PMF
![[Pasted image 20250621220937.png]]
> [!note]
>For looking at the marginal PMF $P_X(x)$ for some $x$, we fix $x$ and loop through all the possible $y$ for that $x$.

![[Pasted image 20250621221531.png|400]]

![[Pasted image 20250621221803.png]]





