### Idea
![[Pasted image 20250511204710.png]]
![[Pasted image 20250511204746.png]]
A solution is to create several overloaded constructors, but now we have too many constructors
```java
new Car(id, brand, model);
new Car(id, screenType, weight, height);
new Car(id, brand, model, color, nbrDoors);
new Car(id, brand, screenType, weight, height);
```
![[Pasted image 20250511204838.png]]
We use a **Director** to orchestrate the construction of complex objects using a **Builder interface**,  
and delegate the actual build logic to **concrete builders** via **method chaining**.

The Director **"has-a" (composes)** a `Builder` (interface).
The **Builder interface** defines **chained methods** like `brand()`, `color()`, `height()`, etc.
**Concrete Builders** (e.g. `CarBuilder`) implement the `Builder` interface and return `this` to allow fluent chaining.
	The **Director** chooses which builder to use and defines construction routines (e.g. `buildBugatti()`).
The client invokes the Director’s method and calls `build()` at the end to get the product.
### Example 
![[Pasted image 20250511205531.png]]
![[Pasted image 20250511205754.png]]
![[Pasted image 20250511205808.png]]
##### Builder Interface
```java
public interface CarBuilderInterface {
    CarBuilderInterface brand(String brand);
    CarBuilderInterface color(String color);
    CarBuilderInterface nbrDoors(int doors);
    CarBuilderInterface engine(String engine);
    CarBuilderInterface height(int height);
    CarBuilderInterface reset();
    Car build();
}
```
##### Concrete Builders
```java
public class CarBuilder implements CarBuilderInterface {
    private Car car;

    public CarBuilder() {
        reset();
    }

    @Override
    public CarBuilderInterface reset() {
        car = new Car();
        return this;
    }

    @Override
    public CarBuilderInterface brand(String brand) {
        car.setBrand(brand);
        return this;
    }

    @Override
    public CarBuilderInterface color(String color) {
        car.setColor(color);
        return this;
    }

    @Override
    public CarBuilderInterface nbrDoors(int doors) {
        car.setDoors(doors);
        return this;
    }

    @Override
    public CarBuilderInterface engine(String engine) {
        car.setEngine(engine);
        return this;
    }

    @Override
    public CarBuilderInterface height(int height) {
        car.setHeight(height);
        return this;
    }

    @Override
    public Car build() {
        return car;
    }
}
```
##### Director
```java
public class Director {
    private CarBuilderInterface builder;

    public Director(CarBuilderInterface builder) {
        this.builder = builder;
    }

    public void setBuilder(CarBuilderInterface builder) {
        this.builder = builder;
    }

    public void buildBugatti() {
        builder.reset()
               .brand("Bugatti")
               .color("Blue")
               .nbrDoors(2)
               .engine("8L")
               .height(115);
    }

    public void buildSUV() {
        builder.reset()
               .brand("Range Rover")
               .color("Black")
               .nbrDoors(4)
               .engine("V6 Turbo")
               .height(180);
    }
}
```
##### Product & Usage
```java
public class Main {
    public static void main(String[] args) {
        CarBuilderInterface builder = new CarBuilder();
        Director director = new Director(builder);

        director.buildBugatti();
        Car bugatti = builder.build();
        System.out.println(bugatti);

        director.setBuilder(new CarBuilder());  // switch builder if needed
        director.buildSUV();
        Car suv = builder.build();
        System.out.println(suv);
    }
}
```

#coding #object-oriented




