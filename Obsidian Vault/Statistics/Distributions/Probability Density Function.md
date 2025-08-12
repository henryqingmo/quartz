---
tags:
  - math/statistics/random_variable
---
### Idea
![[Pasted image 20250701120423.png]]
> [!note]
> Unlike [[Probability Mass Function|PMF]], PDF has continuous [[Statistics/Random variable|Random variable]].
![[Pasted image 20250714192445.png]]
Here we can only defined the height as some probability per unit, and let the area under the curve represent probability.
![[Pasted image 20250714193100.png]]
Intuitively, it's better to think of possibility as the probability density. 

![[Pasted image 20250701120506.png]]
> [!note] 
> We can only define probability of X at a range, This will corresponds to the area under the curve.

#### Conditional PDF
![[Pasted image 20250701121718.png]]
Exactly the same as [[Probability Mass Function#Conditional PMF|Conditional PMF]]

![[Pasted image 20250701122724.png]]
> [!note]
>This is exactly the definition of probability when $\delta \rightarrow 0$ ,
>Which we think of as the smallest partition.
>
 Here we get the same for conditional, which would be the red curve for $x \in A$, and 0 everywhere else, but scaled to have area sum up to 1. 
#### Conditional Expectation
![[Pasted image 20250701124017.png]]
#### Joint PDF
![[Assets/Pictures/MATH2801_2901_Revision_Sheet___3_ 1.png|500]]
[[MATH2801_2901_Revision_Sheet___3_.pdf#page=8&rect=46,551,293,718|MATH2801_2901_Revision_Sheet___3_, p.8]]
![[Pasted image 20250701131743.png]]
A valid joint pdf requires every single point to be positive.

![[Pasted image 20250701131821.png]]
[[Double integral]]

![[Pasted image 20250701132310.png]]
> [!note]
> Here we partition the probability into each unit area, as defined by the area $\delta^{2}$
> The joint distribution has to be jointly continueous, which is stricter than both random variables continueous.

#### Marginal Joint
![[Pasted image 20250701132728.png]]
The marginal can be thought of as the area of each thin slices that's being cut by out axis. [[Fubini's Theorem]]

#### Independence
![[Pasted image 20250705190135.png]]
We require a rectangular domain for independent $X,Y$, for example
$0 < x < y < 1$ is triangular therefore dependent, you can tell since the value of x and y are dependent. 








