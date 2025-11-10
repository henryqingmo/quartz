---
tags:
  - machine_learning/supervised_learning
---
### Idea
![[Pasted image 20250930234815.png]]
One way to address [[Overfit]] is by changing the parameters of the features, thus decreasing minimizing the effects on some feature.

Here the higher the $\lambda$, the more lower the feature will get reduce in order to minimize the cost.

![[Pasted image 20250930234730.png]]

>[!warning]
>Simultaneous update means $b$ and $w$ has to both use values before the update.

### Formally
![[Pasted image 20250930235314.png]]
We can observed that we actually shrinks $w_j$ first before gradient descent.

![[Pasted image 20250930235548.png]]




