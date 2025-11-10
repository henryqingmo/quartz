---
tags:
  - coding/dsa
---
### Idea
#### Correctness
![[Pasted image 20251002163203.png]]
We define our set as $S$, $v$ being the vertex with shortest edge outside $S$ which we want to add, we have to prove the shortest path from the start $s$ to $v$ is only obtained using path in $S$

![[Pasted image 20251002163502.png]]
Let's suppose there's a better path that reaches $y$ (a point outside $S$) before reaching $v$.
![[Pasted image 20251002163634.png]]
![[Pasted image 20251002164358.png]]
So basically there's a contradiction because if v is the smallest d-value, then the weight to reach y would be larger, hence reaching from within S is closer.
#### Updates 
![[Pasted image 20251002170214.png]]
Here we are claiming that only the neighbours of the the added nodes get relaxed(checked) for new distance. 
![[Pasted image 20251002170231.png]]
![[Pasted image 20251002170251.png]]





