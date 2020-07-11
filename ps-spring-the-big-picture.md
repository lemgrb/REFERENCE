# Spring: The Big Picture 
- @schultzdustin (Pluralsight)

## Spring boot features
- Auto-configuration (context-aware to best guess how app is setup)
  - Just enable by adding: `@EnableAutoConfiguration`
- Standalone
  - > java -jar application.jar
- Opinionated (sensible defaults)
  - "Soft-opinion" cause it's easy to override

## The Spring Framework
- Is a 'Software Framework'

### Six Key Areas:
1. Core
    - **Dependency Injection**
        - (a) Object fulfill its own dependencies = tightly coupled*
        - (b) Object relies on something else. Just declare dependencies = "Loosely coupled" => Dependency Injection. Spring core is a *dependency injection container* / the "glue" of the application.
    - i18n support
    - Validation
    - Data binding
    - Type conversion
2. Web
    - Spring Web MVC
        - Started w/ (Java) Servlet API : Low-level API
        - Provides higher level API
    - Spring WebFlux
        - Define Reactive Programming - TBD
        - Asynchronous, no block-and-wait
3. AOP
    - Define **AOP (Aspect-oriented Programming)**: A programming paradigm that aims to increase modularity by separation of cross-cutting concerns (e.g. SECURITY, AUDIT can be found in various area of the application)
4. Data Access
    - Helps in transactions
    - Helps in Exceptions translation (thrown by different DBMS w/ diff. err codes)
    - Helps in testing 
5. Integration
    - Make diff. systems and apps work together
    - How to expose: RMI, Messaging, Web Services
    - How to invoke: ..Web Services
    - Helps to programmatically invoke web service via `RestTemplate`
        - > restTemplate.getForObject("https://the.end/point", Account.class);
6. Testing
    - Unit testing - smallest testable part are testing
        - When code has no dependencies = OK
        - When code has dependencies, use DI and replace w/ mocks.
    - Integration testing - indiv modules are combined and tested as a group.
        - Spring helps in testing with data
        - Web app testing
        - Clean up after tests

## Other Spring projects
1. Spring Data
    - Extends 'Data Access' (w/c is relational)
    - Adds new ways for Relational
    - Then add some more type of data stores that are !relational
2. Spring Cloud
    - For distributed systems e.g. **Microservices architecture**
    - Helps in **Service Discovery**
3. Spring Security
    - Handles both Authorization and Authentication
    - Protect against common attack e.g. XSS

## Links
- https://start.spring.io
- https://spring.io/projects

## What's next? (for deep dive)
- Creating Your First Spring Boot Application
- Spring Boot: Efficient Development, Configuration, and Deployment
- Introduction to Spring MVC 4 by Bryan Hansen
- Spring WebFlux: Getting Started by Esteban Herrera
- Aspect Oriented Programming (AOP) using Spring AOP and Aspect J - Eberhard Wolff
- Getting Started with Spring Data JPA by Dan Bunker
- Getting Started with Spring Data REST by Dan Bunker
- Spring Cloud Fundamentals by Dustin Schultz
- Spring Security Fundamentals by Bryan Hansen

## Terms
- Boilerplate code
