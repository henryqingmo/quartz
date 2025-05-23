### Idea
![[Assets/Pictures/chap3_LinSys.png]]
[[chap3_LinSys.pdf#page=3&rect=59,62,520,412|chap3_LinSys, p.3]]

All norms induces a [[Metric]], the $L^{1}$ norm induces **Manhattan distance**.
![[Pasted image 20250516164513.png]]
$L^{2}$ norm induces the Euclidean [[Metric]]
![[Pasted image 20250516164530.png]]
The $\infty$ norm is exactly the max component of a vector
![[Pasted image 20250516164750.png]]
From the graph we can see that some points on the `small p-norm` is inside the large `p-norm`, which means for the same point, the distance on the small p-norm is **larger**

#### Norm Inequaltiy

This gives us the following inequality
![[Pasted image 20250517182703.png]]
[[Cauchy-Schwarz inequality]]

For inequality 2, we can square both side and the RHS becomes
![[Pasted image 20250517232731.png]]

![[Pasted image 20250517230858.png]]
#### Summary 
![[Pasted image 20250517233049.png]]

#### Induced Matrix Norm
![[Assets/Pictures/chap3_LinSys 1.png]]
[[chap3_LinSys.pdf#page=4&rect=67,351,534,697|chap3_LinSys, p.4]]

$$
\begin{align*}
\vec w &= \frac{\vec{v}}{||\vec{v}||} \\
||\frac{1}{||\vec{v}||}A\vec{v}|| &= |\frac{1}{||\vec v||}||A\vec{v}|| \;\; \text{norm of vector and scalar} \\
&= \frac{||A\vec{v}||}{||\vec{v}||}
 \end{align*}
$$
$C$ is greater all $A\vec{v}$, and $||A||$ is the least upper bound [[Hasse diagram]]. 

Hence $||A||$ represents the furthest distance(defined by p-norm) from the origin, by applying $A$ to every point on a unit circle(if p = 2).
#### Matrix Norm
![[Assets/Pictures/chap3_LinSys 2.png]]
[[chap3_LinSys.pdf#page=4&rect=70,60,534,348|chap3_LinSys, p.4]]

This is basically the same as the vector norm.
#### Proof
![[Assets/Pictures/chap3_LinSys 3.png]]
[[chap3_LinSys.pdf#page=5&rect=65,201,563,694|chap3_LinSys, p.5]]
### Example 
![[Assets/Pictures/chap3_LinSys 4.png]]
[[chap3_LinSys.pdf#page=5&rect=69,49,449,200|chap3_LinSys, p.5]]

```python
from scipy import linalg  
import numpy as np

A = np.array([[1, -3, 4], [2, 0, 1], [-6, 8, 1]])
print("Matrix 1-norm (max column sum):", linalg.norm(A, 1))    # 11.0  
print("Matrix 2-norm (spectral norm):", linalg.norm(A))        # ~11.489 (approximate)  
print("Matrix ∞-norm (max row sum):", linalg.norm(A, np.inf))  
# 15.0
```


#coding #math 
