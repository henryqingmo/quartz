---
tags:
  - machine_learning/supervised_learning
---

### Idea
K-Fold 
![[Pasted image 20250925113427.png]]
> [!abstract]
> The k basically represents the number of splits, here the fold is 4. 
> We basically cycle our choice of test and training, and then sum up and average the loss function of all.

![[Pasted image 20250925113938.png]]

![[Pasted image 20250925113952.png]]

![[Pasted image 20250925114051.png]]

![[Pasted image 20250925114107.png]]
>[!note]
>For each fold, we basically we have a  [[Cost Function#Test-Loss| Test Loss]], that have sample $x_i$ in  test sample $C_k$, and $n_k$ of them

![[Pasted image 20250925114134.png]]
>[!abstract]
>So since we are summing up all the loss function for each test sample, and each test sample sum up the loss for each data point within the sample, it's like summing up all of the n points in the sample.

![[Pasted image 20250925113645.png]]





