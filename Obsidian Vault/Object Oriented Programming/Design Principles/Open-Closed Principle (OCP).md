### Idea
	Software entities should be open for extension, but closed for modification

- Add new behaviour via **inheritance** or **composition**, not by modifying existing code.

### Example 
```java
abstract class Shape {
    abstract double area();
}

class Circle extends Shape {
    double area() { return Math.PI * r * r; }
}
```
#### violation
```java
public class NotificationService {
    public void send(String type, String message) {
        if (type.equals("email")) {
            // send email
        } else if (type.equals("sms")) {
            // send SMS
        } else if (type.equals("push")) {
            // send push notification
        }
    }
}
```
Every time a new notification type is added, we **modify** `send()`.  This violates OCP — we keep changing existing logic.

```java
// Abstraction
public interface Notification {
    void send(String message);
}

// Concrete implementations
public class EmailNotification implements Notification {
    public void send(String message) {
        // send email
    }
}

public class SMSNotification implements Notification {
    public void send(String message) {
        // send SMS
    }
}

public class PushNotification implements Notification {
    public void send(String message) {
        // send push notification
    }
}

// Open/Closed class
public class NotificationService {
    private List<Notification> notifiers;

    public NotificationService(List<Notification> notifiers) {
        this.notifiers = notifiers;
    }

    public void sendAll(String message) {
        for (Notification n : notifiers) {
            n.send(message);
        }
    }
}
```

#coding #object-oriented 
