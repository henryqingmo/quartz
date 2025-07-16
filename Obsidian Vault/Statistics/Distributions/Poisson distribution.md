---
tags:
  - math/statistics/distribution
---
### Idea
#### Poisson Distribution
![[Screenshot_2025-07-16-13-01-26_23173.jpg|400]]
> [!abstract]
>We want to see the number of emails received before time t. Assuming that the rate of email received per unit time is $\lambda$, then the expected number of emails will be $\lambda t$
>
>We can define a sample space of all possible outcomes of email coming in before $t$, it can be at **different times or different number of emails**. Regardless, we will map them onto the number of emails which arrived.
>
>We now define the [[Probability Mass Function]] as each number of email arriving.

![[Screenshot_2025-07-16-13-23-43_.jpg|400]]
> [!abstract]
>Now we define a new [[Statistics/Random variable|Random variable]] $y_1$, it looks at the time interval $[0, t]$ as a whole, and **maps to 0 if no emails received before t**, and **1 if at least 1 email received before t**, this is exactly a [[Bernoulli Distribution]].  
>>[!note]
>>Notice that there is 1 case for no emails but infinite cases of getting 1 or more emails, that doesn't mean the probability of getting no email is 0, in measure theory, we assigned it some probability.
>
>>[!warning]
>> Even if we cap $0 \leq \lambda t \leq t$, the expected number of arrival $\lambda t$ will not entirely be the expectation of the Bernoulli, 
>
>
>So we can define $y_2$ by dividing the the interval into 2 pieces, and each piece is a [[Bernoulli Distribution]], and we add up the values in each sub_intervals.

![[Pasted image 20250708182622.png]]

>[!abstract]
> We basically have to take $n\rightarrow \infty$ , that would mean the arrival in each sub-interval can only be 0 or 1, hence it's **expected arrival will exactly match that of a Bernoulli.**  And so the number of arrivals follows a [[Binomial Distribution]].
> ![[Pasted image 20250716153356.png]]
> $\tau$ is the interval length, $\lambda \tau$ is the number of arrivals per $\tau$ duration, $k$ is the number of arrivals.
>>[!note]
>> 1. We have to assume the occurrence of one event doesn't affect the other.
>> 2. The number of events depend only on the length of the interval, not it's position in time, and the expected rate of the event remains constant (This means we can linearly scale the expected rate with time). 
>>3. We must assume that no two event can occur simultaneously
#### Mean and Variance
![[Pasted image 20250716154336.png]]




![[Pasted image 20250708174843.png]]
![[Pasted image 20250716121730.png]]
> [!note]
> The whole distribution is discrete, represented with a [[Probability Mass Function]]. X is the number of occurrences, and $\lambda$ represents the rate of the event in a fixed interval.

![[Pasted image 20250708181227.png]]





