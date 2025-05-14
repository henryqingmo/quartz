### Idea
# Composition vs Aggregation

## ✅ Summary Table

| Aspect                  | Composition (`◆`)                          | Aggregation (`◇`)                           |
|-------------------------|---------------------------------------------|----------------------------------------------|
| **Relationship Type**    | Strong "part-of" (ownership)               | Weak "has-a" (association)                  |
| **Lifetime Dependency**  | Part **cannot exist without** the whole    | Part **can exist independently**            |
| **Responsibility**       | Whole fully responsible for part's lifetime | Whole uses part but does not control its lifetime |
| **Example (Real Life)**  | `Car` owns `Engine` — engine dies with car | `University` has `Student` — students exist without university |
| **UML Notation**         | Solid diamond `◆`                          | Hollow diamond `◇`                          |
## ✅ Examples

### Composition (Strong ownership)
```java
public class BreakoutRoom {
    private String name;

    public BreakoutRoom(String name) {
        this.name = name;
    }
}

public class OnlineCall {
    private List<BreakoutRoom> breakoutRooms = new ArrayList<>();

    public OnlineCall() {
        // OnlineCall creates and owns its BreakoutRooms
        breakoutRooms.add(new BreakoutRoom("Room A"));
        breakoutRooms.add(new BreakoutRoom("Room B"));
    }
}
```
Here OnlineCall creates its own BreakoutRooms.
### Agreagation (Weak ownership)
```java
BreakoutRoom sharedRoom = new BreakoutRoom("Shared Room");

OnlineCall call1 = new OnlineCall(Arrays.asList(sharedRoom));
OnlineCall call2 = new OnlineCall(Arrays.asList(sharedRoom));
```
Here the BreakoutRoom is created externally.

	#coding #object-oriented 

