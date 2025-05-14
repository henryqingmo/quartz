### Idea

- The ability of an object to take on many forms
- Any object that can pass more than one IS-A test is considered to be polymorphic

```java
public interface Vegetarian {}
public class Animal {}

// Polymorphic since a Deer IS-A Animal, IS-A Vegetarian, IS-A Deer, IS-A Object
public class Deer extends Animal implements Vegetarian {}
```

##### dynamic polymorphism
```java
class Animal {
    public String noise() {
        return "I make a noise";
    }
}
class Dog extends Animal {
    @Override
    public String noise() {
        return "Woof woof";
    }
}
class App {
    public static void main(String[] args) {
        Dog dog = new Dog();
        Animal animal = dog;
        System.out.println(animal.noise());
    }
}
```
The above program will print `Woof woof!`. This is due to the way dynamic polymorphism works. Dynamic polymorphism ensures that when you run a method on an object, the implementation that gets run depends on the runtime type (i.e. the type the object was instantiated as) rather than the compile-time time. In this case, even though the compile-time type of animal is the `Animal` class, the runtime type is Dog so the implementation of `noise()` that will be run is the overridden method inside the `Dog` class.

### Formally

#coding #object-oriented



