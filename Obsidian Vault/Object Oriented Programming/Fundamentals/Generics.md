### Idea
![[Pasted image 20250512131148.png]]
```java
public class Box<T> {
    
    private T value; 
    
    public Box(T value) {
        this.value = value;
    }
    
    public void setValue(T value) {
        this.value = value;
    }
    
    public T getValue() {
        return value;
    }
}
```
For two variables
```java
public class Box<T, S> {
    
    private T value1; 
    private S value2; 
    
    public Box(T value1, S value2) {
        this.value1 = value1;
        this.value2 = value2;
    }
    
    public void setValue(T value1, S value2) {
        this.value1 = value1;
        this.value2 = value2;
    }
    
    public T getValue1() {
        return value1;
    }
    
    public S getValue2() {
        return value2;
    }
}
```

![[Pasted image 20250512131450.png]]
- Use **`?` when you only care about the upper or lower bounds and don’t need to know or use the actual type.
- Use **`T` when you need to refer to, return, or manipulate the actual type inside your method or class.**

#coding #object-oriented 
