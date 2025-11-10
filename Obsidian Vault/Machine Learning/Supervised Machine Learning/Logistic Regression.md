---
tags:
  - machine_learning/supervised_learning
---
### Idea
![[Pasted image 20250930173905.png]]
If we use a [[Linear Regression]] model, we can define a rounding at $\frac{1}{2}$, however, this is easy to be messed up by outliers. 
![[Pasted image 20250930185414.png]]
So $z$ is basically the boundary that determines the classification.
![[Pasted image 20250930221613.png]]
####  Non-Linear Decision Boundaries
![[Pasted image 20250930222352.png]]


###  [[Cost Function]]  
![[Pasted image 20250930175651.png]]
### Formally
![[Pasted image 20250930181208.png]]
To maximise the [[Maximum Likelihood Estimator]], we use [[Gradient Descent]] but with addition.

In fact we cannot use [[Cost Function#Why Least Square|Least Squares]] , as there will be lots of local minima that our [[Gradient Descent]] might get stuck on.
![[Pasted image 20250930222745.png]]






