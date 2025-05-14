### Idea

	A class should have only one reason to change.
- Each class should only do one thing and do it well.
- Promotes **high [[Coupling and Cohesion|cohesion]]** (related functionality grouped together).

### Example 
```java
class InvoicePrinter {
    void print(Invoice invoice) { /* printing logic */ }
}

class InvoiceSaver {
    void save(Invoice invoice) { /* saving logic */ }
}
```
#### Example of violation
```java
public class Invoice {
    private List<Item> items;

    public double calculateTotal() {
        // Business logic
    }

    public void saveToDatabase() {
        // Database persistence logic
    }

    public void printInvoice() {
        // Printing logic
    }
}
```
#### Problems:
- If business rules change → modify `calculateTotal()`
- If DB schema changes → modify `saveToDatabase()`
- If printing format changes → modify `printInvoice()`

#coding #object-oriented  



