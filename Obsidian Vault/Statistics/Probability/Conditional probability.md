### Idea
![[Pasted image 20250723152550.png]]
We define this function that takes in an event $A$ and spits out it's conditional probability.
![[Pasted image 20250723152916.png|300]]
We can represent $P(A\cap B)$ by this integral over $A$ with indicator to check if any of the outcome in $B$.
#### Intuition
![[Pasted image 20250626122135.png]]
We basically change the [[Sample Space]] to be of the condition.
![[Pasted image 20250626122248.png]]

![[Pasted image 20250626122453.png]]

![[Screen Shot 2024-08-09 at 3.09.02 pm.png]]
For the non-disjoint case, we have 
![[Pasted image 20250626121924.png]]
![[Screen Shot 2024-08-07 at 4.10.04 pm.png]]
![[Screen Shot 2024-08-09 at 3.09.37 pm.png]]
#### Proof
![[Pasted image 20250626122008.png]]
If A and B are independent, the definition is $P(A | B) = P(A)$ and $P(B|A) = P(B)$, which means that $P(A\cap B) = P(A)P(B)$. This is different to disjoint.

Discuss pre and post testing. 
#### Tree diagram
![[Pasted image 20241202212817.png]]
Probability under the same condition add up to 1 which explains the probability of the condition branch. [[Law of set algebra]]
![[Pasted image 20241202213225.png]]
The probability of the dependent variable. 
![[Pasted image 20241202213357.png]]
#math #statistics #probability



