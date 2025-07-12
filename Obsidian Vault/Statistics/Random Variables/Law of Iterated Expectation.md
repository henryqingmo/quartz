---
tags:
  - math/statistics/random_variable
---
### Idea
![[Pasted image 20250708124526.png]]
> [!note]
The [[Expected Value|Expectation]] is a function that acts on a [[Statistics/Random variable|Random variable]], and outputs a number. But If we impose a condition on a value $Y=y$, we obtain a function.  We can also instead condition on a RV, which creates a new RV.

![[Pasted image 20250708125150.png]]
We can utilise this fact, and apply expectation on that RV,  Using [[Expected Value#Total expectation theorem|Total Expectation Theorem]], to find out that's exactly the same as no condition applied.
#### Example
![[Pasted image 20250708132555.png]]
> [!note]
> Here we can observe that $E(E(X|Y))$ is exactly [[Expected Value#Total expectation theorem|Total Expectation Theorem]], as $E(X|Y)$ has probability $P(Y=y_i)$ that's associated with outcome $E(X|Y=y_i)$

#### Application
![[Pasted image 20250708140303.png]]



