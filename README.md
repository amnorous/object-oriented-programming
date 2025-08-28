# 🦸‍♂️ Superhero Universe – OOP Class Design

## 📘 Overview

This project demonstrates foundational **Object-Oriented Programming (OOP)** principles in Python by modeling a **Superhero Universe**. It includes:

- A base `Character` class
- Subclasses `Superhero` and `Villain` implementing inheritance and polymorphism
- Encapsulation through protected attributes
- Realistic methods for interaction

---

## 🛠️ Features

### ✅ Object-Oriented Concepts Used:

| Concept         | Description |
|----------------|-------------|
| **Class**       | `Character`, `Superhero`, and `Villain` |
| **Constructor** | Initializes objects with custom attributes |
| **Inheritance** | `Superhero` and `Villain` inherit from `Character` |
| **Polymorphism**| Subclasses override the `introduce()` method |
| **Encapsulation** | `_power_level` is a protected attribute with getter/setter methods |

---

## 📦 Files

| File Name    | Description                                |
|--------------|--------------------------------------------|
| `main.py`    | Contains all class definitions and test code |
| `README.md`  | Project overview and documentation          |

---

## 🧪 Example Usage

```python
hero = Superhero("Photon", 85, "Light Beam")
villain = Villain("Darkthorn", 90, "Plunge world into darkness")

print(hero.introduce())         # Hero Photon here! Power: Light Beam, Level: 85
print(villain.execute_plan())   # Darkthorn executes the evil plan: Plunge world into darkness!

hero.set_power_level(95)
print(hero.get_power_level())   # 95
