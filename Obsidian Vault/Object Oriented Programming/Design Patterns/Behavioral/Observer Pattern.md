### Idea
![[Pasted image 20250511143059.png]]
##### Subject
Maintains a list of observers and notifies them of state changes. During this notification, they are passing data (push/pull)
```java
public void registerObserver(Observer o);
public void removeObserver(Observer o);
public void notifyObservers(data);	// Calls update() of observers
```
##### Observer
Register (and unregister) themselves on a subject and to update their state when they are notified.
```java
// Two possible options for update()
public void update(Subject obj);	// PULL data from subject
public void update(data);	// PUSH data to observers
```
### Example 
![[Pasted image 20250511143845.png]]
##### The Subscriber Interface
```java
public interface Subscriber {
    void update(Publisher context);
}
```
##### Concrete Subscribers
```java
public class EmailSubscriber implements Subscriber {
    public void update(Publisher context) {
        System.out.println("EmailSubscriber received update: " + context.getState());
    }
}

public class SMSSubscriber implements Subscriber {
    public void update(Publisher context) {
        System.out.println("SMSSubscriber received update: " + context.getState());
    }
}
```
##### The Publisher (Subject)
```java
import java.util.ArrayList;
import java.util.List;

public class Publisher {
    private List<Subscriber> subscribers = new ArrayList<>();
    private String mainState;

    public void subscribe(Subscriber s) {
        subscribers.add(s);
    }

    public void unsubscribe(Subscriber s) {
        subscribers.remove(s);
    }

    public void setState(String newState) {
        this.mainState = newState;
        notifySubscribers();
    }

    public String getState() {
        return mainState;
    }

    private void notifySubscribers() {
        for (Subscriber s : subscribers) {
            s.update(this);
        }
    }

    public void mainBusinessLogic() {
        // Example state change
        this.setState("Important update!");
    }
}
```
The `subject` stores a list of subscribers, where it can notify changes through their common method `update`. 
##### Usage (Client)
```java
public class Main {
    public static void main(String[] args) {
        Publisher publisher = new Publisher();

        Subscriber email = new EmailSubscriber();
        Subscriber sms = new SMSSubscriber();

        publisher.subscribe(email);
        publisher.subscribe(sms);

        publisher.mainBusinessLogic();
    }
}
```

#coding #object-oriented 
