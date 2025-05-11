### Idea
![[Pasted image 20250511155958.png]]
![[Pasted image 20250511160240.png]]
![[Pasted image 20250511160254.png]]
### Example 
![[Pasted image 20250511163057.png]]
![[Pasted image 20250511163108.png]]
##### Component Interface
```java
public interface Expression {
    double compute();
}
```
##### Leaf Node
```java
public class Number implements Expression {
    private double value;

    public Number(double value) {
        this.value = value;
    }

    @Override
    public double compute() {
        return value;
    }
}
```
##### Composite Nodes
```java
public class Addition implements Expression {
    private Expression e1, e2;

    public Addition(Expression e1, Expression e2) {
        this.e1 = e1;
        this.e2 = e2;
    }

    @Override
    public double compute() {
        return e1.compute() + e2.compute();
    }
}

public class Subtraction implements Expression {
    private Expression e1, e2;

    public Subtraction(Expression e1, Expression e2) {
        this.e1 = e1;
        this.e2 = e2;
    }

    @Override
    public double compute() {
        return e1.compute() - e2.compute();
    }
}

// Similarly for Multiplication and Division
```
##### Calculator (Client)
```java
public class Calculator {
    private Expression expression;

    public Calculator(Expression expression) {
        this.expression = expression;
    }

    public double calculate() {
        return expression.compute();
    }
}
```
##### Usage
```java
public class Main {
    public static void main(String[] args) {
        Expression expr = new Addition(
            new Number(5),
            new Multiplication(
                new Number(2),
                new Number(3)
            )
        );

        Calculator calc = new Calculator(expr);
        System.out.println(calc.calculate());  // Outputs 11.0
    }
}
```
Follows [[Open-Closed Principle (OCP)]]

#coding #object-oriented 
