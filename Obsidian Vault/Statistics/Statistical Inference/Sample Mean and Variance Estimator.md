---
tags:
  - math/statistics/statistical_inference
  - "#status/todo"
---
### Idea
![[Pasted image 20250725180356.png]]


![[Pasted image 20250725174105.png]]
> [!note] 
> The bottom distribution is the sample mean distribution.
> 
> The blue line indicates the average of the current sample, the entire distribution is plotted by infinite sampling of size 5, with varying average of their sample. 
> > [!tip]
>> If our sample size is 1, we will obtain the same curve as the population.
> 
> On the left, we can see the average of all samples, equivalent to the grand average of the average of each individual sample, will approach the mean of the curve, because the mean of the curve is exactly that but of infinite samples.

![[Pasted image 20250725174924.png]]
> [!note] 
> As we increase our sample size, we will get a much narrower curve, which means the possible averages of each sample gets squished. 

> [!abstract]
> So basically for a good estimator, we can take small sample size, which has large variations, but we can compute average of many samples, and this will approach the mean.
> ![[Pasted image 20250725175834.png]]
> Second way, we can take a very large sample, so that the variation is very small 
![[Pasted image 20250725175911.png]]
So the two ways are mathematically equivalent.

#### Sample Variance Estimator
![[Pasted image 20250812185554.png]]
>[!note]
> We have $n-1$ instead of $n$ to account for 1 less [[Degree of Freedom]] because the sample mean used it up. 
>![[Pasted image 20250812185522.png|400]]
>Here we can see if we if we took $\frac{1}{n}$ it would be a biased estimator.

![[Pasted image 20250812190012.png]]
[[]]

