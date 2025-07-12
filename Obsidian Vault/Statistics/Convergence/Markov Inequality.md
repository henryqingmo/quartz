---
tags:
  - math/statistics/Convergence
---
### Idea
![[Pasted image 20250625183704.png]]
> [!abstract]
> Markov inequality gives us an upper bound, It tells us that the larger the $x$ that's greater than $E(X)$ is more unlikely
> 
> And it tells us nothing about the X that's $\leq E(X)$, since the upper bound will be $\geq 1$, but we have [[Chebyshev Inequality]] to tell us the bound on both tails.

> [!note]
>We have the condition that $X \geq 0$, and $a \gt 0$, since $x \geq 0$, we have the first inequality.  Since $x$ ranges from $a$ to $\infty$, we have the second inequality. 


![[Pasted image 20250625184143.png]]
> [!note]
>Another proof involves defining a new [[Statistics/Random variable|Random variable]] $Y$, We see that if $0 \leq x < a$, $Y = 0$ and if $x \geq a$, $y = a$ ![[Pasted image 20250625191554.png]]
for each outcome, we have $Y \leq X$, since they are mapped by the same $\omega$, we conclude that holds for expected value.  
#### Intuition
![[Pasted image 20250626213626.png]]
We first partition $E(X)$ into two conditional expectation, using [[Expected Value#Total expectation theorem|total expectation]]. Now by fixing $P(X \lt t)$ and $P(X \geq t)$, we basically fix the amount of people in each category, we can freely move them inside their own category, changes the average of the category.
![[Pasted image 20250626213935.png|500]]
The Upper bound of $E(X)$ will have $E(X|X\lt t)$ be close to $t$, and $E(X|X\geq t)$ going to infinity.
![[Pasted image 20250626214208.png|500]]
The lower bound, on the other hand will have $E(X|X\lt t) = 0$  and $E(X|X\geq t) = t$. 
> [!abstract]
> In a nutshell, we are basically saying the absolute minimum of the average of the whole population related to a threshold, would have population below the threshold going to 0, thus no contribution to the mean, and the people above the threshold exactly at the threshold. The the mean is exactly at the threshold times the probability of above the threshold.





