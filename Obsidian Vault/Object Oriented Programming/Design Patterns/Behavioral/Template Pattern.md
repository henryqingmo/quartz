### Idea
![[Pasted image 20250511191840.png]]
![[Pasted image 20250511191851.png]]
We have a **common procedure** (algorithm) that applies to multiple tasks (e.g., making drinks, processing data),  
but **some steps differ** depending on the specific context.

So we define the **overall algorithmic structure** in an **abstract class**
using a `templateMethod()`. And the subclass(`concrete classess`) override only the steps they want to customise.

```java
public abstract class AbstractClass {
    // Template Method
    public final void executeAlgorithm() {
        step1();
        step2();
        step3();
    }

    // Abstract steps to be implemented by subclasses
	public abstract void step1();
    public abstract void step2();
    public abstract void step3();
}
```
##### Concrete Class
```java
public class ConcreteClass extends AbstractClass {
    @Override
    protected void step1() {
        // Custom implementation for step 1
    }

    @Override
    protected void step2() {
        // Custom implementation for step 2
    }

    @Override
    protected void step3() {
        // Custom implementation for step 3
    }
}
```

#coding #object-oriented 
