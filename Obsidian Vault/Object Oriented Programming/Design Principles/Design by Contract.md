### Idea
![[Pasted image 20250510174029.png]]

### Example 
```java
public class Calculator {
    /**
     * @preconditions a, b != null
     * @postconditions a + b
     */
    public static Double add(Double a, Double b) {
        return a + b;
    }

    /**
     * @preconditions a, b != null, b != 0
     * @postconditions a / b
     */
    public static Double divide(Double a, Double b) {
        return a / b;
    }

    /**
     * @preconditions angle != null
     * @postconditions sin(angle)
     */
    public static Double sin(Double angle) {
        return Math.sin(angle);
    }

    /**
     * @preconditions angle != null, angle != Math.PI / 2
     * @postconditions tan(angle)
     */
    public static Double tan(Double angle) {
        return Math.tan(angle);
    }
}
```

#coding #object-oriented 
