# Selenium 4
- Why 4?
  - W3C WebDriver Protocol over JSON Wire protocol
  - Chrome debugging platform
  - Relative locators: "near", "above", "below", "left of", "right of"
  - Pluggable locators

## Grid 4
1. Router - Directs request to the Grid
2. Distributor - Determines where to run the session
3. Session map - Maps session ids to where the session is
4. Node - Actually hosts the session

- Modes:
  1. Standalone
  2. Hub and Node
  3. Fully distributed (Used by saucelabs, browerstack, ...)

## Puppeteer
## Cypress

## Distributed Tracing
- Jaeger, Splunk, Kibana
- Opentelemetry
