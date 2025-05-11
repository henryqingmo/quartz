### Idea
![[Pasted image 20250511182741.png]]
![[Pasted image 20250511182753.png]]
We basically have a global instance for the class, and restricts initialisation using a **private constructor**, and allow a global access through a static method that returns the **singleton instance**, creating it **only once** if needed.
```java
public class Singleton {
    // Step 1: Private static instance
    private static Singleton instance;

    // Step 2: Private constructor (prevents instantiation)
    private Singleton() {}

    // Step 3: Public access method
    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();  // Lazy initialization
        }
        return instance;
    }

    public void doSomething() {
        System.out.println("Singleton is working!");
    }
}
```
##### Usage
```java
public class Main {
    public static void main(String[] args) {
        Singleton s1 = Singleton.getInstance();
        Singleton s2 = Singleton.getInstance();

        s1.doSomething();

        System.out.println(s1 == s2);  // true — same instance
    }
}
```
### Example 
![[Pasted image 20250511182841.png]]
![[Pasted image 20250511182855.png]]
![[Pasted image 20250511182907.png]]
[[Concurrency and Parallelism]]

#coding #object-oriented 
