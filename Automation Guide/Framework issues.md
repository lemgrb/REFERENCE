Avoid the ff. issues:

+ Slow to execute! Automation tests should be fast. Make use of parallel runs
+ Too generic framework. e.g. Gherkin steps tells how test not what to test (behavior) e.g. "When user clicks the "Login" button" -> field level. 
+ FLAKY TESTS. Failing tests due to failing labels. The locator should be same regardless of language (localization/internationalization)
+ NOT REPEATABLE. e.g. need manual test data setup
+ Page objects that contains assertions? "Page objects themselves should never make verifications or assertions." (https://www.selenium.dev/documentation/guidelines/page_object_models/). Unless there's a case for it like Business people wants to see friendlier messages. (Note to self: need to read more)