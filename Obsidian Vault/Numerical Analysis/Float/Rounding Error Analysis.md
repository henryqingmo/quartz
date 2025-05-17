### Idea
![[Assets/Pictures/chap2_Float 6.png]]
[[chap2_Float.pdf#page=9&rect=67,468,530,695|chap2_Float, p.9]]

For round down we basically chop all the digits after the mantissa. 

For round up we add the smallest increment [[The Machine Epsilon]] multiplied by the exponent $2^{e}$ because we are use [[Floating Point Representation]].

![[Pasted image 20250515134233.png]]
#### IEEE standard

![[Assets/Pictures/chap2_Float 7.png]]
[[chap2_Float.pdf#page=9&rect=70,99,570,455|chap2_Float, p.9]]
#### Round to nearest
![[Floating Point Representation and Rounding Error - YouTube - 0-10-46.jpeg]]
![[IMG_0597.jpeg]]
We basically look at if the digits after the mantissa pass the half way point of the smallest increment(machine epsilon).

The special case being we have trailing 1 follow by all 0s, which is exactly the half way point. 

 Then we look at the last bit of the Mantissa, if 0 then round down, if 1 we round up.

#### Error
![[Assets/Pictures/chap2_Float 8.png]]
[[chap2_Float.pdf#page=10&rect=65,261,538,524|chap2_Float, p.10]]

The absolute error is the difference between the rounding and the actual value.

Relative error tells us what fraction of the true number is the error.

![[Assets/Pictures/chap2_Float 9.png]]
[[chap2_Float.pdf#page=10&rect=64,51,436,152|chap2_Float, p.10]]
This is pretty obvious, because the way our number is rounded.

![[Assets/Pictures/chap2_Float 10.png]]
[[chap2_Float.pdf#page=11&rect=71,298,530,696|chap2_Float, p.11]]

#coding #math 
