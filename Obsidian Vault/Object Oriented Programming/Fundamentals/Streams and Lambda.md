### Idea
![[Pasted image 20250512133832.png]]

![[Pasted image 20250512151503.png]]
### Example
```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");

List<String> filtered = names.stream()
    .filter(name -> name.startsWith("C"))
    .map(name -> name.toUpperCase())
    .collect(Collectors.toList());

filtered.forEach(System.out::println);
```
##### Comparison to traditional loops
```java
// Traditional
for (String name : names) {
    if (name.startsWith("C")) {
        result.add(name.toUpperCase());
    }
}

// Stream + Lambda
List<String> result = names.stream()
    .filter(name -> name.startsWith("C"))
    .map(String::toUpperCase)
    .collect(Collectors.toList());
```

#coding #object-oriented 
