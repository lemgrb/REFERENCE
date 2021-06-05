# Cucumber.io
- [DOCS](https://cucumber.io/docs/cucumber/)
- Recommended to choose an implementation for the same platform language as the production code.

## BDD
- "Living documentation" - can be auto-validated against the app it describes and tell you when it's out of date
- BDD is an approach that **collaboratively** specifies the system's desired behaviour. Each time a piece of behaviour is agreed, we use that specification to "drive" the development of the code that will implement that behaviour.
- Discovery -> Formulation -> Automation
  - Discovery: Discuss user story from 3 perspectives: test, dev, product owner. For tester, determine what to test.
  - Formulation: Translate **examples** into e.g. Gherkin
- BDD complements Agile process
- BDD is collaborative. Output of collab is the "living documentation"

## Scenario
- Scenario (Gherkin) are Examples
- `Scenario` describes an Example we can exec
- When writing scenario, focus on observable, testable behaviour of the system, not on business goals (we can document this later also using Gherkin)
- `Given`, `When`, `Then` are *STEPS* we can exec
  - `Given` ang *context* kung aha ni-occur ang scenario, and unsa na ang nahitabo (pre-req)
  - `When` ang *actions* na makausab sa state sa system
  - `Then` what should happen at the end of scenario
- **Step definitions** are java methods that does what's described in each step in Gherkin scenario. Cucumber will do pattern-matching.
- BDD is similar to TDD uses red-green-refactor
  - red : a scenario that fails
  - green: make it pass as simply as possible
  - refactor: improve code while keeping all tests green
- ![](https://marcabraham.files.wordpress.com/2012/04/06_red_green_refactor.jpg)

## Cucumber expressions
- Subset of RegEx. Can still use RegEx 

## Cleaning up
- Cucumber bridget the comms gap betw. business domain experts and dev team
- *Cucumber scenario do act as tests when automated, but ITS PRIMARY PURPOSE IS TO PROVIDE A SINGLE, SHARED SPECIFICATION, written in domain language of business. Otoh, primary purpose of automated test is to check that the software behave as expected.*
- Steps should be independent and composable.
- `Background` are like pre-requisites
