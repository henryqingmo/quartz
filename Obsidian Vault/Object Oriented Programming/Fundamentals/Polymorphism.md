### Idea

- The ability of an object to take on many forms
- Any object that can pass more than one IS-A test is considered to be polymorphic

```java
public interface Vegetarian {}
public class Animal {}

// Polymorphic since a Deer IS-A Animal, IS-A Vegetarian, IS-A Deer, IS-A Object
public class Deer extends Animal implements Vegetarian {}
```

### Formally

#coding #object-oriented



