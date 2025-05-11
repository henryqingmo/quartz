### Idea
![[Pasted image 20250511175443.png]]
![[Pasted image 20250511175519.png]]
![[Pasted image 20250511175549.png]]
✅ Both the **decorator** and the **concrete component** implement the **same interface** (`Component`).

✅ Instead of calling the component’s methods **directly**,  
we **wrap** the component with one or more decorators,  
and call the methods of the component using the **outermost decorator**.

### Example 
![[Pasted image 20250511175856.png]]
Here is an example where we can wrap multiple layers of decorators.
![[Pasted image 20250511175906.png]]
```java
Character troll = new Troll(10, 10); // Base component
Character armoredTroll = new Helmet(new ChestPlate(new ChainMail(troll)));

// All behavior is dynamically layered
armoredTroll.attack(enemy);
armoredTroll.damage(15);
```

#coding #object-oriented 
