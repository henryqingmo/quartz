---
tags:
  - math/statistics/random_variable
---
### Idea
![[Pasted image 20250614210622.png]]
[[Mean]]
> [!note]
>
>![[IMG_0689 1.jpeg]]
>We can think of the expected value as the balance point of the distribution, Hence if the distribution is symmetric, the expected value will fall in the middle. 

![[Pasted image 20250614212858.png]]
By Frequentest approach, we can conduct n experiments and the average result is exactly the expected value
#### Alternative definition
![[Pasted image 20250701161836.png]]
> [!note]
> Here we define $X$ as the sum of all of the indicator function with all possible $x$.
> for eg. If we take $X = 1$, the only indicator function evaluates to 1 is $\mathbb{1}_{x=0}$, with all other giving us 0.
#### Elementary property
![[Pasted image 20250615124738.png]]
#### The Expected Value Rule
![[L05.10 The Expected Value Rule - YouTube - 0-9-57.jpeg]]
There are two ways of thinking about this.
##### Using composite function
> [!abstract] 
 >we can apply $g \circ X$, so we basically look at the all the possible $y$ that's being mapped to, and multiply that y by the probability of arrow reaching it $P_Y(y)$. 
 >
 >So basically we look at the possible output of $y$ and  find it's probability
 
##### Apply two times 
> [!abstract] 
> We can Apply $X$ to get $P_{X}(x)$ associated with each x, 
> Since $g$ will map all $x$ to some $y$, we can mutiply $P_{X}(x)$ by whatever $g(x)$  maps to.  
> 
> So basically we look at the possible X and look at what it maps to 

#### Change of Variables
![[Pasted image 20250723151223.png]]
> [!note] 
> Here we basically define the expected value as the sum of $X(w)P(w)$ over all the $\omega$ in A, here we can do a substitution letting $x = X(\omega)$

#### Linearity of expectation
![[Pasted image 20250615133112.png]]
#### Total expectation theorem 
![[Pasted image 20250621214609.png]]
Here we replaced $B$ with $X = x$ from [[Total probability rule]], Since $X = x$ is the whole sample space.  
#### Conditional Expectation
![[Pasted image 20250723152018.png]]
>[!abstract]
>$A$ is some subset of outcomes in $\Omega$, that we can assign with 
>probability measure $\mathbb{P}$.
>>[!note]
>> With conditional probability, we basically reassigned our probability measure by [[Conditional probability]] function.
>> ![[Pasted image 20250723153318.png]]
>> Now we can substitute the definition of conditional probability.


![[Pasted image 20250622161222.png]]
Here we replace $A$ with $Y = y$
> [!tip]
> We think of expected value as the sum of outcome multiplied by their probability, the outcome doesn't change in conditional, but the probability of each outcome has to be adjusted.

![[Pasted image 20250622161257.png]]
This is exactly [[Law of Iterated Expectation]]
### Example
![[Pasted image 20250621214904.png]]
#### Multi-variable
![[Pasted image 20250702174202.png]]
> [!note]
>We can basically use the conclusion from single variable, and define a multivarable function.
>![[Pasted image 20250702184046.png]]
##### Linearity of expectation
![[Pasted image 20250622081518.png]]
This [[Double integral#Double sum|Double Sum]], sums up all the possible $(x, y)$
Here we basically get Marginal PMF.
![[Pasted image 20250622081901.png]]
 
#### Independent Expectation
![[Pasted image 20250622162914.png]]
[[Independent Event]]
