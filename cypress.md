Install with `npm install cypress` on a node project.

See [DOCUMENTATION](https://docs.cypress.io/)

### Basics
+ Open cypress `$ npx cypress open`

### Assertions
+ [Chai Assertions](https://docs.cypress.io/guides/references/assertions#Chai)


## Filter, Not, Special characters
+ [Filter](https://docs.cypress.io/api/commands/filter)
+ [Not](https://docs.cypress.io/api/commands/not)
+ Special chars : `.type('{Enter}')`

### Environment variables
+ Specify environment variable via CLI argument: `$ npx cypress open --env MY_VARIABLE=Lem` then access via `Cypress.env('MY_VARIABLE')`.
+ Specify environment variable via System, add prefix `CYPRESS`: `$ export CYPRESS_MY_VARIABLE=Lem` (Unix-like)
+ Via cypress.json

```json
{
	"baseUrl":"localhost:3000",
	"env": {
		"MY_VARIABLE":"hellow
	}
}
```


+ Via cypress.env.json
```json
{
	"MY_VARIABLE":"hello"
}
```

> Be sure to add .env files in .gitignore


## Mocking, and Stubs

See [Stubs, Spies, and Clocks](https://docs.cypress.io/guides/guides/stubs-spies-and-clocks#Libraries-and-Tools)


## Autocompletes
Add at the top:

```javascript
/// <reference types="Cypress" />
```

or in `jsconfig.json`
```jsconfig.json
{
  "include": [
    "./node_modules/cypress",
    "cypress/**/*.js"
  ]
}
```
