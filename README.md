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

4. Reusability & Extensibility

- Using composition over inheritance
- strategy pattern for variation
- plugin architectures
- don't hardcode behaviour

5. Portability

- use cross-platform libraries (pathlib, not os.path)
- env variables for configuration
- avoid platform specific assumptions
- abstract environment dependencies

6. Defensibility

- Fail-fast, validate input immediately
- store/log only what is necessary
- use safe defaults

7. Maintainability and Testability

- write clear, self-documenting code
- pure functions where possible
- separate business logic from I/O
- write tests

8. Simplicity (KISS, DRY, YAGNI (you ain't gonna need it))

- prefer simple solutions
- avoid unnecessary abstractions
- if it's hard to explain it's too complex
- extract common logic into functions
- don't build for hypothetical future needs
- don't over engineer solutions

No specific code to show for the 8th principle!
