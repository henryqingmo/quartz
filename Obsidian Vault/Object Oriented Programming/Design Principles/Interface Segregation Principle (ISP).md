### Idea
	Clients should not be forced to depend on interfaces they do not use.
- Split large interfaces into smaller, more specific ones.

### Example 
```java
interface Printer {
    void print();
}

interface Scanner {
    void scan();
}

// Instead of:
interface MultiFunctionMachine extends Printer, Scanner {}
```

#coding #object-oriented  
