### Idea
![[Pasted image 20250511184227.png]]
[[Open-Closed Principle (OCP)]]
[[Single Responsibility Principle (SRP)]]
![[Pasted image 20250511184245.png]]
![[Pasted image 20250511184302.png]]
We want to add functionality to the `ConcreteElements`, so we have them implementing the `accept` method, that allows an instance of `visitor` to be passed in. 

Element will then call `visitor.visit(this)` which hands over it's entire instance to the visitor. 

The visitor can then call the element's method to perform extra logic, **without changing the element's class**.
### Example 
![[Pasted image 20250511185219.png]]
##### Element Interface
```java
public interface ComputerComponent {
    void accept(ComputerVisitor visitor);
}
```
##### Concrete Elements
```java
public class Mouse implements ComputerComponent {
    private String name;

    public Mouse(String name) {
        this.name = name;
    }

    @Override
    public void accept(ComputerVisitor visitor) {
        visitor.visit(this);
    }

    public String getName() { return name; }
}

public class Keyboard implements ComputerComponent {
    private String name;
    private int numKeys = 36;

    public Keyboard(String name) {
        this.name = name;
    }

    @Override
    public void accept(ComputerVisitor visitor) {
        visitor.visit(this);
    }

    public String getName() { return name; }
}

public class Computer implements ComputerComponent {
    private String name;
    private int memory;

    public Computer(String name, int memory) {
        this.name = name;
        this.memory = memory;
    }

    @Override
    public void accept(ComputerVisitor visitor) {
        if (visitor.isValidated()) {
            visitor.visit(this);
        }
    }

    public String getName() { return name; }
}
```
##### Visitor Interface
```java
public interface ComputerVisitor {
    void visit(Mouse m);
    void visit(Keyboard k);
    void visit(Computer c);
    boolean isValidated();
    void setIsValidated(boolean v);
}
```
##### Concrete Visitor
```java
public class ValidationVisitor implements ComputerVisitor {
    private boolean validated = false;

    @Override
    public boolean isValidated() {
        return validated;
    }

    @Override
    public void setIsValidated(boolean validated) {
        this.validated = validated;
    }

    @Override
    public void visit(Mouse m) {
        System.out.println("Validating mouse: " + m.getName());
    }

    @Override
    public void visit(Keyboard k) {
        System.out.println("Validating keyboard: " + k.getName());
    }

    @Override
    public void visit(Computer c) {
        System.out.println("Validating computer: " + c.getName());
    }
}
```
##### Usage
```java
public class Main {
    public static void main(String[] args) {
        ComputerComponent mouse = new Mouse("Logitech");
        ComputerComponent keyboard = new Keyboard("Corsair");
        ComputerComponent computer = new Computer("MacBook", 16);

        ComputerVisitor visitor = new ValidationVisitor();
        visitor.setIsValidated(true);

        mouse.accept(visitor); // logics inside visitors
        keyboard.accept(visitor);
        computer.accept(visitor);
    }
}
```

#coding #object-oriented 
