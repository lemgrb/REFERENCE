> Treat test code as production code

1. Browser tests are expensive to run. **Browser test only what's necessary**. e.g. "Set up test data" portion can be via API call.
2. Tests should **use DSL**, not low-level operations like "Click button", "Select x from dropdown"
3. When not to automate
	1. When UI is not stable yet
	2. On tight deadline, in the short term don't automate
4. Use **Page Object Model** to separate test codes from page codes
5. Use **domain-specific language**
6. Don't use selenium to generate application state e.g. State=Logged in. Use API call?
7. ISOLATED TESTS **DO NOT SHARE STATE** (e.g. Test data, WebDriver) Ensure tests are isolated from one another. 
	1. Create new WebDriver instance per test. Use "ThreadLocal"
8.** INDEPENDENT TESTS.**
9. Consider **fluent API**
10. Fresh browser per test

Source: https://www.selenium.dev/documentation/guidelines/