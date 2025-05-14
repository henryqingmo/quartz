### Idea
![[Assets/Pictures/12. Change of Variable - Annotated 7.png]]
[[12. Change of Variable - Annotated.pdf#page=2&rect=5,13,442,250|12. Change of Variable - Annotated, p.2]]

We can think of the mapping as changing the coordinate systems
![[Assets/Pictures/12. Change of Variable - Annotated 8.png]]
[[12. Change of Variable - Annotated.pdf#page=3&rect=6,28,448,249|12. Change of Variable - Annotated, p.3]]

Here each grid in the $(r,\theta)$ plane is scaled by a factor determined by the determinant of [[Jacobian matrix]]
![[Dr. Trefor Bazett - Change of Variables & The Jacobian Multi-variable Integration [wUF-lyyWpUc - 1047x589 - 4m51s].png]]
This is similar to the idea of [[Chain rules]] in 1D calculus
![[IMG_0416 1.jpeg]]
Here we expressed $dx$ and $dy$ in terms of their [[Differentials and best affine approximation]]. 

### Formally
The order of integration does matter and might change after a change of variable, which can be determined by their dependency.
![[Pasted image 20250405235702.png]]
### Example
![[Assets/Pictures/12. Change of Variable - Annotated 9.png]]
[[12. Change of Variable - Annotated.pdf#page=23&rect=3,11,450,246|12. Change of Variable - Annotated, p.22]]

![[Pasted image 20250405235851.png]]
```python
for θ in [0, 2π]:         // outer
    for r in [0, √a]:     // middle
        for z in [0, e^{-r²}]:  // inner (depends on r)
            volume += r * 1
```

#math #calculus 



