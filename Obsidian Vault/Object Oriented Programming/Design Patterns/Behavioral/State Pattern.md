### Idea
![[Pasted image 20250511152405.png]]
![[Pasted image 20250511152433.png]]
So we basically refactor a switch statement on if state this do that, into having state as there own class, and each state have the ability to call next state on super.
### Example 
![[Pasted image 20250511152650.png]]
#### Refactor 
###### BEFORE: Using if Statements
```java
public class Context {
    private String state;

    public Context() {
        this.state = "STATE_A";
    }

    public void doThis() {
        if (state.equals("STATE_A")) {
            System.out.println("Doing THIS in State A");
            state = "STATE_B";
        } else if (state.equals("STATE_B")) {
            System.out.println("Doing THIS in State B");
        }
    }

    public void doThat() {
        if (state.equals("STATE_A")) {
            System.out.println("Doing THAT in State A");
        } else if (state.equals("STATE_B")) {
            System.out.println("Doing THAT in State B");
            state = "STATE_A";
        }
    }
}
```
##### Problems
- Hard-coded transitions
- Adding a new state means editing **every method**
- Violates [[Open-Closed Principle (OCP)]]

##### Solution
##### `State` Interface
```java
public interface State {
    void doThis();
    void doThat();
    void setContext(Context context);
}
```
##### Concrete States
```java
public class StateA implements State {
    private Context context;

    @Override
    public void setContext(Context context) {
        this.context = context;
    }

    @Override
    public void doThis() {
        System.out.println("StateA doing this");
        context.changeState(new StateB());  // transition to StateB
    }

    @Override
    public void doThat() {
        System.out.println("StateA doing that");
    }
}

public class StateB implements State {
    private Context context;

    @Override
    public void setContext(Context context) {
        this.context = context;
    }

    @Override
    public void doThis() {
        System.out.println("StateB doing this");
    }

    @Override
    public void doThat() {
        System.out.println("StateB doing that");
        context.changeState(new StateA());  // transition back to StateA
    }
}
```
Each state can call context for change state.
##### `Context` class
```java
public class Context {
    private State state;

    public Context(State state) {
        changeState(state);  // sets initial state
    }

    public void changeState(State newState) {
        this.state = newState;
        this.state.setContext(this);
    }

    public void doThis() {
        state.doThis();
    }

    public void doThat() {
        state.doThat();
    }
}
```
##### Usage (Client)
```java
public class Main {
    public static void main(String[] args) {
        State initialState = new StateA();
        Context context = new Context(initialState);

        context.doThis();  // StateA does this, switches to StateB
        context.doThat();  // StateB does that, switches back to StateA
    }
}
```
#coding #object-oriented 
