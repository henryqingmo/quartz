---
tags:
  - math/statistics/statistical_inference
---
### Idea
![[Pasted image 20250726133649.png]]

![[Pasted image 20250726133702.png]]
#### Confidence Interval
![[Pasted image 20250726123603.png]]
After we obtain our sample, we want to find the interval of every possible sample such that 95% of the time the true population mean lies within the interval. 
So we are basically looking for $P(? \lt \bar X \lt ?) = 0.95$, Since the sample mean is a normal distribution, we can [[Normal Distribution#Standardise|Standardise]] it to see that  $P\left(? \lt \frac{\bar X - \mu}{\frac{\sigma}{\sqrt(n)}} \lt ? \right)= 0.95$, so we can choose $Z_{0.025}, Z_{0.975}$ or even $Z_{0}, Z_{0.95}$.

#### Confidence interval with known variance
![[Pasted image 20250812160758.png]]
#### Unknown Variance
![[Pasted image 20250812162611.png]]
We replaced standard deviation with [[Sample Mean and Variance Estimator#Sample Variance Estimator|Sample standard deviation]], which changes the distribution to [[Student's t-distribution]]

#### Example
![[Pasted image 20250813124547.png]]
![[Pasted image 20250813125652.png]]
We need one-sided CI in this case as the alternatives is one sided.

> [!note]
>Using confidence interval for this question,  we first find the confidence interval using $\bar x + t_{0.95}\frac{s}{\sqrt{n}}$, because the hypothesis is $\mu$ less than the upper bound, so we only want 5% of the time we have $\mu$ greater than the upper bound.  We see the upper bound is 63.47%, which is well below 78.1%, **95% of intervals constructed this way will contain $\mu$** , therefore $\mu$ must lie below 63.47% and hence reject the hypothesis.