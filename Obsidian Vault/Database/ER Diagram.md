---
tags:
  - programming/database
---
### Idea

#### Regular mapping
![[Pasted image 20250620171810.png]]
##### Table
![[Pasted image 20250620171733.png|400]]
##### Code
```sql
CREATE TABLE Student (
    StuID INT PRIMARY KEY, 
    name VARCHAR(100),
    degree VARCHAR(50)
);
```
##### Crows
![[Pasted image 20250620171733.png|400]]
#### Weak entities mapping
![[Pasted image 20250620171900.png]]
##### Table
![[Pasted image 20250620174439.png]]
##### code
```sql
CREATE TABLE Employee (
    SSN CHAR(11) PRIMARY KEY,
    ename VARCHAR(100),
    salary DECIMAL(10,2)
);

CREATE TABLE Contact (
    SSN CHAR(11),
    name VARCHAR(100),
    phone VARCHAR(20),
    PRIMARY KEY (SSN, name),
    FOREIGN KEY (SSN) REFERENCES Employee(SSN)
);
```
![[Pasted image 20250620211301.png]]
> [!note]
>For N to M mapping, there is no way to store the foreign key in either of the entity, because each of them will have relation with many. This means if we put the foreign key on either side, we need to store a list of foreign keys.

#### one to many
![[Pasted image 20250620214910.png]]
Here we store the FK on the many side. 
#### one to one
![[Pasted image 20250620210420.png]]
> [!note]
>Imagine the case with person and passport. 
Each passport must be manged by one person, but there exist a person without a passport. So it make sense to store the foreign key in the passport, because if we instead store passport ID for each person, some of them is gonna be set to NULL.
Basically an Injective but not surjective function, and we should choose the domain.






