### Idea
![[Pasted image 20250510164158.png]]
![[Pasted image 20250510174147.png]]
[[Design by Contract]]
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
