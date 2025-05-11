### Idea
[[Strategy Pattern]]
[[Observer Pattern]]
[[State Pattern]]
[[Template Pattern]]
[[Visitor Pattern]]

##### ✅ Common Structure
- Each pattern involves an **interface** defining common behaviour.
- One or more **concrete classes implement** the interface.
- The **context/subject** class **has-a** relationship with the interface (composition).
- Behavior is **delegated**, not hardcoded.

---

##### 🔄 Pattern Comparison

| Pattern      | Interface Role               | Composition Style         | Behavior Delegation                               |
| ------------ | ---------------------------- | ------------------------- | ------------------------------------------------- |
| **Strategy** | Defines algorithm variants   | `has-a` (1 strategy)      | Context calls strategy method (e.g., `execute()`) |
| **Observer** | Defines subscriber callback  | `has-many` observers      | Subject calls `update()` on each subscriber       |
| **State**    | Defines state-specific logic | `has-a` (1 current state) | State handles method & may change context state   |
#coding #object-oriented 