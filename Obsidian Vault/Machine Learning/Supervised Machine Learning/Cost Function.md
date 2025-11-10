---
tags:
  - machine_learning/supervised_learning
---
### Idea
![[Pasted image 20250916154744.png]]
>[!note] 
>To minimise the cost functions, it's exactly the same as minimising the [[Estimator#Mean Square Error|Mean Square Error]]. 
>We append a $\frac{1}{2}$ in front to cancel out the extra 2 coming from the derivative. 

![[Pasted image 20250930222956.png]]
A single training sample is called the loss function.

![[Pasted image 20250916160838.png]]
![[Pasted image 20250916160451.png]]
>[!note]
> A surprising connection, the cost function is also the negative of  [[Maximum Likelihood Estimator]] in this case, therefore minimising the cost function is maximising the MLE.
> ![[Pasted image 20250930180918.png]]

![[Pasted image 20250916164056.png]]
>[!note] 
>On the left we have 3 different hypothesis, on the bottom we have a graph of the cost function of parameters $w$ and $b$, on the top right is the graph sliced at different levels, the contour doesn't look circular as it's in the space of (w, b) not (x, y).  

![[Pasted image 20251006012524.png]]
It turns out the least square error is equivalent to assuming that each data point was drawn from a [[Normal Distribution]] with the [[Mean]] lies on the regression line.

#### Test-Loss  
![[Pasted image 20250925120213.png]]
> [!note]
> Here we basically go through every sample in the test sample, and sum up the loss squared.
> 
![[Pasted image 20250925120800.png]]

#### Why Least Square
![[Pasted image 20250930164442.png]]



