### Idea
![[Pasted image 20250510153911.png]]
#### Purpose
![[Pasted image 20250510154214.png]]
[[Coupling and Cohesion]]
### Example
```java
public class TrainingSystem {
    private List<Trainer> trainers;
	
public LocalDate bookTraining(String employee, List<LocalDate> availability) {
        for (Trainer trainer : trainers) {
            for (Seminar seminar : trainer.getSeminars()) {
                for (LocalDate available : availability) {
                    if (seminar.getStart().equals(available) &&
                            seminar.getAttendees().size() < 10) {
                        seminar.getAttendees().add(employee);
                        return available;
                    }
                }
            }
        }
        return null;
    }
```
Here are the offending lines 
```java
for (Seminar seminar : trainer.getSeminars()) {     // trainer → seminars
    if (seminar.getStart().equals(available) &&     // seminar → start
        seminar.getAttendees().size() < 10) { // seminar → attendees → size
        seminar.getAttendees().add(employee); // seminar → attendees → add

```
![[Pasted image 20250510160230.png]]

#### How to refactor
##### In `seminar`
```java
public boolean isAvailableOn(LocalDate date) {
    return start.equals(date) && attendees.size() < 10;
}

public void addAttendee(String employee) {
    attendees.add(employee);
}
```
##### In **Trainer**
```java
public boolean tryBook(String employee, LocalDate date) {
    for (Seminar s : seminars) {
        if (s.isAvailableOn(date)) {
            s.addAttendee(employee);
            return true;
        }
    }
    return false;
}
```
##### In `TrainingSystem`
```java
public LocalDate bookTraining(String employee, List<LocalDate> availability) {
    for (Trainer trainer : trainers) {
        for (LocalDate date : availability) {
            if (trainer.tryBook(employee, date)) {
                return date;
            }
        }
    }
    return null;
}
```

After refactoring we achieved
![[Pasted image 20250510163910.png]]
[[Single Responsibility Principle (SRP)]]
![[Pasted image 20250510163932.png]]

#coding #object-oriented 
