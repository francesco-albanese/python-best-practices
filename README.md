# python-best-practices

This repo includes 8 Python designs principle to write better Python production code.

1. Cohesion & Single responsibility principle
- each class should have only one reason to change
- high cohesion = related functionality grouped together
- Example: separate UserRepository, EmailService, Validator Classes

2. Encapsulation & Abstraction
- Keep internal state private
- expose behaviour, not data
- use properties/getters for controlled access
- abstract away complexity

3. Loose Coupling & Modularity
- use interfaces / abstract base classes
- inject dependencies
- components should be swappable
- minimize inter-module dependencies
