### Idea
![[Pasted image 20250511201927.png]]
![[Pasted image 20250511202003.png]]
The **adapter** acts as a **bridge** between the **client** and the **adaptee (service)**.

The adapter implements the interface expected by the client.
The adapter "has-a" the adaptee (composition).
When the client calls a method on the adapter, the adapter:
- Optionally transforms the data or logic,
- Then delegates the call to the adaptee.
The client only talks to the adapter, never to the adaptee directly.

### Example
##### The Target Interface
```java
public interface ClientInterface {
    void method(String data);  // format expected by the client
}
```
##### The Adaptee (Service)
```java
public class Service {
    public void serviceMethod(byte[] specialData) {
        System.out.println("Service called with special data: " + Arrays.toString(specialData));
    }
}
```
##### The Adapter
```java
public class Adapter implements ClientInterface {
    private final Service adaptee;

    public Adapter(Service adaptee) {
        this.adaptee = adaptee;
    }

    @Override
    public void method(String data) {
        // Convert String to byte[] for the service
        byte[] specialData = data.getBytes();
        adaptee.serviceMethod(specialData);
    }
}
```
##### The Client
```java
public class Client {
    private final ClientInterface adapter;

    public Client(ClientInterface adapter) {
        this.adapter = adapter;
    }

    public void sendRequest(String data) {
        adapter.method(data);  // works seamlessly with adapter
    }
}
```
##### Usage
```java
public class Main {
    public static void main(String[] args) {
        Service legacyService = new Service();
        ClientInterface adapter = new Adapter(legacyService);
        Client client = new Client(adapter);

        client.sendRequest("Hello Adapter!");
    }
}
```

#coding #object-oriented 
