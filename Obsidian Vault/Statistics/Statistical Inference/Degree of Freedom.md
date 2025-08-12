---
tags:
  - math/statistics/statistical_inference
---
	### Idea
![[Pasted image 20250812102057.png|400]]
We can decompose our vector of [[Random Sampling|observations]] into [[Sample Mean and Variance Estimator|sample mean]].
The degrees of freedom exactly corresponds to the [[Basis and Dimension]] of where the vector can lands.
![[Pasted image 20250812102134.png|400]]
Since the component of the residual vector adds to 0, it's dot product with vector of all 1s will be 0, but then the sample mean is a scaling factor of all 1s. Therefore they are [[Orthogonal]] complement.
![[Pasted image 20250812103245.png|400]]
In 3d, the sample mean is exactly a normal to the plane of residuals.

#### Sample Mean Estimator
![[Pasted image 20250812121804.png|400]]
We want to estimate $\mu$ base on the observations, for most distributions like [[Normal Distribution]] will have mode at $\mu$, therefore we expect $X$ to be close to $\mu$. 
![[Pasted image 20250812122754.png|400]]
![[Pasted image 20250812122855.png|400]]
By Minimising the squared distance, we find $\mu$ to be exactly the [[Sample Mean and Variance Estimator]].
#### Sample Variance
![[Pasted image 20250812122955.png|400]]
The [[Expected Value|Expectation]] of the length of the yellow vector is an unbiased estimator of the true variance
![[Pasted image 20250812123323.png|400]]
The expectation of the length of the purple vector is also an unbiased estimator, the sum cancels out the n. This has one degree of freedom. 
![[Pasted image 20250812123505.png|400]]
We can then use the Pythagorean theorem to find the expectation of the length of the red vector.
![[Pasted image 20250812123818.png]]
The result is an unbiased estimator.
![[Pasted image 20250812123856.png|300]]





