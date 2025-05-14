### Idea
![[Pasted image 20250510164158.png]]
![[Pasted image 20250510174147.png]]
[[Design by Contract]]

In a mathematical view, think of

f(x) is the superclass function, where:
	Domain (input space) = Pre_A
	Codomain (output space) = Post_A

g(x) is the subclass function, substituting f(x):
	Domain = Pre_B
	Codomain = Post_B

### To **preserve substitutability (LSP)**:

#### ✅ Preconditions (Inputs):

We need to **weaken preconditions**:
- The subclass **must accept all inputs that the superclass accepts**, or **more**
$$
Pre_A ⊆ Pre_B

$$
#### ✅ Postconditions (Outputs):

We need to **strengthen postconditions**:
- The subclass **must guarantee at least what the superclass promised, or more strict guarantees (subset of possible outcomes)**.

$$
Post_B ⊆ Post_A
$$
### Example 
![[Pasted image 20250510174236.png]]
##### In `OnlineSeminar`
```java
/**
 * An online seminar is a video that can
 * be viewed at any time by employees. 
 * A record is kept of which employees
 * have watched the seminar.
 */
public class OnlineSeminar extends Seminar {
    private String videoURL;
    private List<String> watched;
}
```
Here `OnlineSeminar` violates LSP because it does not need the to make booking like it's parent class `Seminar`.

#### How to refactor
#####  Option 1: Use a shared **interface**, not inheritance
```java
public interface Seminar {
    void attend(String employee);
}

public class InPersonSeminar implements Seminar {
    public void attend(String employee) {
        // booking logic
    }
}

public class OnlineSeminar implements Seminar {
    public void attend(String employee) {
        // add to watched list
    }
}
```
Now both implements the interface Seminar.
[[Polymorphism]]
##### Option 2:  Use **Composition Instead of Inheritance**
```java
public class OnlineSeminar {
    private SeminarMetadata metadata;
    private String videoURL;
    private List<String> watched;

    public void watch(String employee) { /* watch logic */ }
}
```
So basically we make a helper class `SeminarMetadata` to store all the common methods and attribute, and use a composition in each of the class. 
##### Option 3:  Abstract Class with Shared Data & Abstract Behaviour
```java
public abstract class Seminar {
    protected String title;
    protected String speaker;
    protected LocalDate date;

    public String getSummary() {
        return title + " by " + speaker + " on " + date;
    }

    public abstract void attend(String employee);
}
```

#coding #object-oriented 
