### Idea
	High-level modules should not depend on low-level modules. Both should depend on abstractions.

- Use **interfaces** or **abstract classes** to reduce tight coupling.
### Example 
```java
interface Database {
    void save(User u);
}

class UserService {
    private Database db;
    UserService(Database db) { this.db = db; }
}
```

#coding #object-oriented
