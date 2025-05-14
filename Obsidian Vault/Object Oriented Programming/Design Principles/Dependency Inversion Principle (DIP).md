### Idea
	High-level modules should not depend on low-level modules. Both should depend on abstractions.

- Use **interfaces** or **abstract classes** to reduce tight coupling.

The abstraction allows us to add functionalities without modifying the high-level modules, which follows [[Open-Closed Principle (OCP)]].
### Example 
![[Pasted image 20250512153648.png]]
Here Calculator(High level) is not directly tied to the specific implementation
##### Without DIP but using separate classess
```java
public class AddOperation {
    public double operate(double a, double b) {
        return a + b;
    }
}

public class SubtractOperation {
    public double operate(double a, double b) {
        return a - b;
    }
}

public class Calculator {
    public double add(double a, double b) {
        AddOperation op = new AddOperation();
        return op.operate(a, b);
    }

    public double subtract(double a, double b) {
        SubtractOperation op = new SubtractOperation();
        return op.operate(a, b);
    }
}
```
##### With abstraction
```java
public interface ICalculatorOperation {
    double operate(double a, double b);
}

public class Calculator {
    private ICalculatorOperation operation;

    public Calculator(ICalculatorOperation operation) {
        this.operation = operation;
    }

    public double calculate(double a, double b) {
        return operation.operate(a, b);
    }
}
```

#coding #object-oriented
