---
tags:
  - math/statistics/transformation
---
### Idea
![[Pasted image 20250724140503.png]]
> [!abstract] 
> We want to find the transformation of the [[Random Sampling|Sample Mean]],  First we use [[Taylor series]] to approximate it.  
> For large $n$, we can use [[Law of Large Number]], to see that $\bar X_{n} \rightarrow \mu$, 
> > [!note]
> > To approximate $\bar X_{n} - \mu$, we use the [[Central Limit Theorem]], to find out it's a [[Normal Distribution]], with fluctuation $\frac{1}{\sqrt(n)}$
> > ![[Pasted image 20250724150429.png]]
> > For the higher terms, since they are always positive, we measure their magnitude by their mean
> > ![[Pasted image 20250724151420.png]]

#### Visual Intuition
![[Pasted image 20250724151824.png]]
> [!note] 
> Since we have $X_n$ approaches $\mu$,  we can safely use [[Differentials and best affine approximation]] around $\mu$, which turns it into a linear transformation of the normal curve. 

![[Pasted image 20250724152627.png]]
> [!abstract]
> Basically follows from 
> $$
> \frac{g(\bar X_n) - g(\mu)}{\bar X_{n}- \mu} = g^{\prime}(\mu)
> $$
![[Pasted image 20250724153042.png]]
so we established that it's a linear transformation of a normal distribution, we can safely approximate $g(\bar X_n)$ by a shifted normal distribution.



