---
tags:
  - math/statistics/statistical_inference
---
### Idea
![[Pasted image 20250726122959.png]]
> [!note]
> Estimator is basically a function that acts on a sample taken from a distribution to predict some unknown constant such as the mean.  
> > [!tip]
> > Estimator is actually a random variable, where it's sample space is all of the possible sample with the same size, which maps to our estimation of the fix constant $\theta$. We can find probability density function of such mapping, as there's a probability of mapping to each possible estimation of $\theta$.

![[Pasted image 20250726123031.png]]

![[Pasted image 20250726210702.png]]
> [!abstract]
> We established that we can use the [[Sample Mean and Variance Estimator]] to estimate $E(X)$, and thereby $E(g(X))$ and be estimated by the sample mean of the random variable $g(X)$. We can apply this logic to get variance estimator and etc. 
#### Estimator bias
![[Pasted image 20250812160246.png]]
#### Estimator variance
![[Pasted image 20250812160345.png]]
#### Mean Square Error
![[Pasted image 20250812160508.png]]
### Property
![[Pasted image 20250812160618.png]]
[[Chebyshev Inequality]]
[[Convergence in Distribution and Probability]]

