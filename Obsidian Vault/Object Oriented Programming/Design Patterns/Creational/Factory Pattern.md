	### Idea
![[Pasted image 20250511163647.png]]
![[Pasted image 20250511163802.png]]
![[Pasted image 20250511163852.png]]
![[Pasted image 20250511164106.png]]
✅ **We define a “creator” (abstract class)**  
✅ That creator has a **factory method**, like `createButton()`  
✅ **Concrete creators** (subclasses) **override** that method to return specific **product** objects  
✅ The **creator uses composition** to interact with the product — it does **not know the concrete type**
### Example 
![[Pasted image 20250511164345.png]]
##### Product Interface
``` java
public interface Button {
    void render();
    void onClick();
}
```
##### Concrete Products
```java
public class WindowsButton implements Button {
    @Override
    public void render() {
        System.out.println("Rendering Windows-style button");
    }

    @Override
    public void onClick() {
        System.out.println("Click handled by Windows button");
    }
}

public class HTMLButton implements Button {
    @Override
    public void render() {
        System.out.println("Rendering HTML button in browser");
    }

    @Override
    public void onClick() {
        System.out.println("Click handled by HTML button");
    }
}
```
##### Creator (Dialog)
```java
public abstract class Dialog {
    public void render() {
        Button okButton = createButton();
        okButton.onClick();
        okButton.render();
    }

    // Factory method
    public abstract Button createButton();
}
```
##### Concrete Creators
```java
public class WindowsDialog extends Dialog {
    @Override
    public Button createButton() {
        return new WindowsButton();
    }
}

public class WebDialog extends Dialog {
    @Override
    public Button createButton() {
        return new HTMLButton();
    }
}
```
##### Usage (Client Code)
```java
public class Main {
    public static void main(String[] args) {
        Dialog dialog;

        // Example decision logic
        String platform = System.getProperty("os.name");
        if (platform.contains("Windows")) {
            dialog = new WindowsDialog();
        } else {
            dialog = new WebDialog();
        }

        dialog.render();
    }
}
```

#coding #object-oriented 
