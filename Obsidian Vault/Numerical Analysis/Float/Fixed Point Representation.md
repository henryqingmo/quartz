### Idea
#### Convert from decimal to binary
We first split into whole number and fraction, since each part is different.

#### Whole number
![[Assets/Pictures/chap2_Float 1.png]]
![[IMG_0594.jpeg]]
We can continuously divide by 2 and note down the reminders and discards it, this is the same right shift by 1. 
```python
def decimal_to_binary_mod2(n):
    if n == 0:
        return '0'
    
    result = ''
    while n > 0:
        result = str(n % 2) + result  # prepend the remainder
        n = n // 2  # integer division by 2
    return result

# Example usage:
print(decimal_to_binary_mod2(50))  # '110010'
print(decimal_to_binary_mod2(0))   # '0'
```
[[chap2_Float.pdf#page=4&rect=62,637,527,739|chap2_Float, p.4]]

#### Fractions
![[Assets/Pictures/chap2_Float 2.png]]
[[chap2_Float.pdf#page=4&rect=68,494,528,600|chap2_Float, p.4]]
![[IMG_0595.jpeg]]
This time we continuously multiply by 2, and note down the integer bit and discards it.  
```python
import math

# Convert integer to binary
print(bin(50))  # '0b110010'

# Convert fraction to binary using custom logic
def float_to_binary(x, places=10):
    whole, frac = str(x).split(".")
    whole = int(whole)
    frac = float("0." + frac)
    
    # Convert whole part
    res = bin(whole).lstrip("0b") + "."
    
    # Convert fractional part
    while places:
        frac *= 2
        bit = int(frac)
        if bit == 1:
            frac -= bit
            res += "1"
        else:
            res += "0"
        places -= 1
    return res

print(float_to_binary(0.3125))  # '0.0101'
```

The problem with fixed-point approach is the number we represent cannot get as big. 
Thus we use [[Floating Point Representation]].

#math #coding 



