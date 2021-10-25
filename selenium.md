## Parallel runs
+ Use ThreadLocal to isolate variables per thread

## Page load strategy
[DOMContentLoaded vs normal "load"](https://youtu.be/8rc0zaTn2ew)


## By Xpath
- CONTAINS: `"//h4/a[contains(text()),"Log in"]`
- SIBLING: `//label/following-sibling::input`
- ANCESTOR: `//h1/ancestor::div`
- AND: `//*[@type='submit' OR @name='btnReset']`
- OR: `//input[@type='submit' and @name='btnLogin']`
- PARENT: `//*[@id='rt-feature']//parent::div`

## Grid
Grid maintenance (if not using i.e. Saucelabs):
+ Start/Stop EC2
+ Create scripts to start/stop hub
+ Enable warnings and logs
+ Explicitly kill browser after tests
+ Restart server after several test runs

## Upload APK to saucelabs
e.g. [Via curl](https://docs.saucelabs.com/mobile-apps/app-storage/)
