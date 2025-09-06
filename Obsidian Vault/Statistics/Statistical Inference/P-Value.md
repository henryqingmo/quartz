---
tags:
  - math/statistics/statistical_inference
---
### Idea
![[Pasted image 20250813131425.png]]
P value is the probability of 
$P(T \leq \frac{\bar x - \mu}{\frac{s}{\sqrt(n)}})$, so under the hypothesis is true, we must have it following a t distribution, which means that the test statistics must follows a t distribution.
![[Pasted image 20250813150216.png]]
Assuming $H_0$ is true, which forms a [[Student's t-distribution]]. 
We expect for this t distributions, $P(T \leq t_{0.05}) = 0.05$, so only 5% of the t-value will fall below $t_{0.05}$, we expect our t-value to be among these 95% most of the time.
![[Pasted image 20250813150848.png]]
	So if the $t_{obs}$ fall below $t_{0.05}$ or equivalently $P(T \leq t_{obs}) \leq 0.05$, it's unlikely for the hypothesis to be true.

![[Pasted image 20250813131404.png]]

### Formally




