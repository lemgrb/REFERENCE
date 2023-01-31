Test automation:

1. Need to be written
2. Monitored / Who executes?
3. Maintained / Updated

Test Automation project is NOT A SIDE PROJECT. It is a software-development project!

1. Which tests should we automate?
2. What's the scenario? (Gherkin scenario, test cases)

Develop standards and conventions.

Who executes? (local, separate build, developer build)

## Tools
1. Consider, who will be using the tools? How easy it is to hire someone who can code in i.e. Java? Manual testers will automate? = training.
2. Minimum: Interaction tool and validation tool
	1. UI (Interact: Navigation library, Validate: TestNG)
		1. Browser and device you need to run your automation against. e.g. Cypress (runs directly on the browser, running e2e tests combining multiple platforms is not possible)
	2. Service (Interaction: HTTP service calls, Validation: Python smart_assertion)
	3. Unit (Interaction: Unit level call to functions using programming language, Validate: JUnit)
4. Optional tools: Reporting, Specification-driven, CI tools.

## Future-proofing your test automation efforts

Design considerations:
1. Running in parallel. Tests have to be designed to run this way. No test dependencies. 
	1. **Any test that needs to change test data should be the only test using that data!**
2. Objects and variables used by multiple tests should be Thread-safe (not global, or static).
3. Clean code
	1. Avoid code duplicates for maintenability
	2. Design patterns
		1. Page object model
		2. Fluent
		3. Builder
		4. Screenplay
		5. Singleton
		6. Factory
		7. Facade

## Scaling

Tests should support:

1. Multiple environments (use properties files!)
2. Multiple browsers (use saucelabs?)
3. Multiple devices (i.e. responsive layout! native mobile (android/ios))

## Measuring the value of your test automation

Benefits:

1. Shortened Regression Testing Time! (e.g. VALIDATION regression!)
	1. Defect on response json changed
2. Frequent feedback
3. Trustworthiness
4. Scalability


