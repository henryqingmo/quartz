---
tags:
  - algorithm
---
### Idea
![[Pasted image 20251104155101.png|600]]
We are looking for the element thats greater than or equal to half of all the elements, which is the median. 
![[Pasted image 20251104163608.png]]
We first pick x, and partition the sets in to less than x and greater x. 
![[Pasted image 20251104163703.png]]
There are three cases, if B have exactly size $\lceil\frac{n + 1}{2}\rceil$, then $x$ is the median.
If less B has less, that means the median is in C, we needs to subtract the size of $B$ from the rank, indicating that we already have B on the left. 

>[!note]
>The worst case time complexity is $O(n^2)$, where we always choose the extreme like the right most element, that would means we recurse on T(n - 1) which recurse on T(n-2) etc, so the time complexity becomes arithmetic sequence.  

![[Pasted image 20251104165030.png]]
We divide the group of numbers into group size of 5, sorting them individually and 



