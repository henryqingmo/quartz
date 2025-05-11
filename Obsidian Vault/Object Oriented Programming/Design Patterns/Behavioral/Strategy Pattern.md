### Idea
![[Pasted image 20250511141859.png]]
![[Pasted image 20250511141928.png]]

### Example 
![[Pasted image 20250511143209.png]]
##### Strategy Interface
```java
public interface RouteStrategy {
    String buildRoute(String A, String B);
}
```
##### Concrete Strategies
```java
public class RoadStrategy implements RouteStrategy {
    @Override
    public String buildRoute(String A, String B) {
        return "Driving from " + A + " to " + B;
    }
}

public class WalkingStrategy implements RouteStrategy {
    @Override
    public String buildRoute(String A, String B) {
        return "Walking from " + A + " to " + B;
    }
}

public class PublicTransportStrategy implements RouteStrategy {
    @Override
    public String buildRoute(String A, String B) {
        return "Taking public transport from " + A + " to " + B;
    }
}
```
All of the concrete strategies inherits from the strategy interface.
##### Navigator
```java
public class Navigator {
    private RouteStrategy routeStrategy;

    public Navigator(RouteStrategy strategy) {
        this.routeStrategy = strategy;
    }

    public void setRouteStrategy(RouteStrategy strategy) {
        this.routeStrategy = strategy;
    }

    public void buildRoute(String A, String B) {
        String route = routeStrategy.buildRoute(A, B);
        System.out.println(route);
    }
}
```
The navigator has-a strategy(composition)
##### Usage
```java
public class Main {
    public static void main(String[] args) {
        Navigator navigator = new Navigator(new RoadStrategy());
        navigator.buildRoute("Home", "Work");

        navigator.setRouteStrategy(new WalkingStrategy());
        navigator.buildRoute("Park", "Library");

        navigator.setRouteStrategy(new PublicTransportStrategy());
        navigator.buildRoute("Station", "University");
    }
}
```


#coding #object-oriented 
