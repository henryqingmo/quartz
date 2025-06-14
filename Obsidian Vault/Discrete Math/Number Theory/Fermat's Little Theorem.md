### Idea
![[Assets/Pictures/Topic 2 Lecture Notes (Gardiner) 4.png]]
[[Topic 2 Lecture Notes (Gardiner).pdf#page=32&rect=5,11,347,269|Topic 2 Lecture Notes (Gardiner), p.32]]

![[Pasted image 20250604220221.png|300]]
$$
\begin{align*}
a^{p-1} \equiv 1 (mod\;p) \\ 
a^{p}a^{-1} \equiv 1(mod\;p) \\
a^{p} \equiv a (mod\;p)
\end{align*}
$$
![[Pasted image 20250604220150.png|300]]

#### Proof
![[Pasted image 20250604013007.png|100]]
First consider all the possible combinations of $3$ beads with $2$ colours, which equates to $2^{3}= 8$.
We first **Remove** the mono-coloured ones.
![[Pasted image 20250604012931.png]]
Connecting the beads to make a ring, those beads have $3$ rotations, which exactly corresponds to $3$ combinations.

We can observe that each rotation is equivalent to moving the beads at the **end to the top**.$

Important thing to notice is we can split into $2$ groups of $3$ , so the total combinations without the mono-coloured ones is $6$, which is divisible by $3$. 
![[Pasted image 20250604013835.png]]
By doing the same steps for $4$ beads $2$ colours, we see that the [[Groups]] doesn't have the same numbers. 

This problem raised because of repeated pattern, when we have repeated patterns.
![[Pasted image 20250604014439.png|400]]
When we have n repeats of m beads in each pattern, the total number of beads is $n \times m$, a **composite number** (though each pattern can be further break down into smaller patterns). 

for the m beads, we only need to rotate m times to get to the same pattern, which means it would have only have m combination for that group.

![[Pasted image 20250604015013.png|200]]
So if the number of beads is prime, $m, n$ has to be $1$ and the number of beads, therefore each group will have exactly the number of beads of combinations.

Also modulo prime without 0 satisfy the property of a group.

![[Pasted image 20250604015320.png|200]]

![[Pasted image 20250604015342.png|300]]

![[Pasted image 20250604015414.png|300]]

#math #discrete #number_theory  



