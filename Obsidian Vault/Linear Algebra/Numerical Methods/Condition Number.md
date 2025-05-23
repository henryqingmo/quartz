### Idea
![[Assets/Pictures/chap3_LinSys 5.png]]
[[chap3_LinSys.pdf#page=7&rect=65,58,526,346|chap3_LinSys, p.7]]

[[Singular Matrix]]

![[Assets/Pictures/chap3_LinSys 6.png]]
[[chap3_LinSys.pdf#page=8&rect=67,456,534,696|chap3_LinSys, p.8]]
Here we used inequality of [[Norm]]
![[Assets/Pictures/chap3_LinSys 8.png]]
[[chap3_LinSys.pdf#page=8&rect=68,280,546,456|chap3_LinSys, p.8]]
[[Inverse Matrix]]
#### Proof
1. 
![[Pasted image 20250517235633.png]]
Notice we dropped the max because it applied only to $\frac{||A(Bx)||}{||x||}$, so that each of the product might not be maximised.
![[Pasted image 20250518000036.png]]
Part 2 follows from there.

![[Assets/Pictures/chap3_LinSys 9.png]]
[[chap3_LinSys.pdf#page=8&rect=68,48,530,175|chap3_LinSys, p.8]]

[[Eigenvalues and eigenvectors]]
[[Symmetric Matrix]]
![[Assets/Pictures/chap3_LinSys 11.png]]
[[chap3_LinSys.pdf#page=9&rect=71,488,586,697|chap3_LinSys, p.9]]
Here we use [[Spectral Theorem]] which allows us to choose P as orthogonal. 

From the Inequality we deduce
![[Pasted image 20250518161522.png]]
Now we choose $w = \vec{e_1}$.
![[Pasted image 20250518161545.png]]
#### Stability
![[Assets/Pictures/chap3_LinSys 12.png]]
[[chap3_LinSys.pdf#page=9&rect=71,300,549,485|chap3_LinSys, p.9]]

![[Assets/Pictures/chap3_LinSys 13.png]]
[[chap3_LinSys.pdf#page=9&rect=72,62,549,299|chap3_LinSys, p.9]]

##### Proving Invertible
![[Pasted image 20250518170118.png]]
Using [[Neumann series]]
![[Pasted image 20250518170254.png]]
#### Proof 
![[Pasted image 20250518171826.png]]
![[Pasted image 20250518171851.png]]
![[Pasted image 20250518171902.png]]

#### Example
![[Assets/Pictures/chap3_LinSys 14.png]]
[[chap3_LinSys.pdf#page=10&rect=51,368,519,696|chap3_LinSys, p.10]]
Now we can investigate when $\mu= 0.1$, which means $\kappa{(A)} = 183$
![[Assets/Pictures/chap3_LinSys 15.png]]
[[chap3_LinSys.pdf#page=10&rect=51,61,521,370|chap3_LinSys, p.10]]
![[Pasted image 20250519131744.png]]
![[Assets/Pictures/chap3_LinSys 16.png]]
[[chap3_LinSys.pdf#page=11&rect=69,500,523,695|chap3_LinSys, p.11]]

We can see the relative change is **huge** compared to the relative perturbation.

```python
mu = 0.1  
A = np.array([[2, 1], [4, 2.1]])  
b = np.array([1, 1])  
deltaA = np.array([[0, 0], [0, 0.1]])  
deltaB = np.array([0, 0.1])

x1 = linalg.solve(A, b)  
x2 = linalg.solve(A + deltaA, b)  
x3 = linalg.solve(A + deltaA, b + deltaB)  
print("x1:", x1) # x1: [  5.5 -10. ] 
print("x2:", x2) # x2: [ 3. -5.]
print("x3:", x3) # x3: [ 2.75 -4.5 ]

relativeErrorX2 = linalg.norm(x1 - x2, 1) / linalg.norm(x1, 1)  
relativeErrorX3 = linalg.norm(x1 - x3, 1) / linalg.norm(x1, 1)  
pertubationA = linalg.norm(deltaA, 1) / linalg.norm(A, 1)  
pertubationB = linalg.norm(deltaB, 1) / linalg.norm(b, 1)  
  
print(relativeErrorX2 / pertubationA) # 29.032258064516128 
print(relativeErrorX3 / (pertubationA + pertubationB)) # 7.983870967741937
```



#coding #math 
