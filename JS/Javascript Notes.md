+ Is dynamically-typed
+ C-like
	+ Compile just-in-time
+ DOM : The functions and objects that JS has access to in a browser (client)
+ import package: `to be determined`
+ VSCode extensions: eslint, prettier, javascript (es6) code snippets
+ NodeJS for JS outside the browser (https://nodejs.org)
+ Use NVM (http://nvm.sh/) to manage NodeJS versions
+ Setup Node JS development environment using [Install WSL | Microsoft Learn](https://learn.microsoft.com/en-us/windows/wsl/install)
+ Setup VSCode with WSL: [Set up a WSL development environment | Microsoft Learn](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password)
+ Single quote, double quotes, template literals using `${variable}`
+ Single line comment //, multi-line comments /** Hello **/. CTRL + /
+ Make code "self-documenting"!

### Variables

+ var : Don't use anymore!
	+ Function scoped
	+ Can be changed in scope (mutable)
	+ Available before declaration
+ let
	+ Block scoped
	+ Can be changed in scope (mutable)
	+ Only available after declaration
+ const
	+ Block scoped
	+ Cannot be changed ("immutable")
	+ Only available after declaration

Recommendation: **const by default, let in loops**


### Strings
+ Concatenate variables/string literals with `+`
+ "1" + 1 = 2
+ 1 + "1" = 11
+ Template literals: ${expression or variables} and ``  --> respects line breaks!

### Data Types

+ Simple Type System - Number (float), String, Boolean, Date, Function, Array, Object
+ Special Types = **NaN, null, undefined**
+ `typeof arraySample` -> Object
+ `instanceof` -> false if primitive used instead of constructor
+ type coercion e.g. `1 == false`
	+ type respected e.g. `1 === false`

### Math
```txt
+
-
/
*
%
++
--
```

Use Math object for more advanced Math functions.

### Converting Strings to Numbers
+ `parseInt(string)` - Numbers after special characters are ignored e.g. `parseInt('1 + 1')` -> 1
+ `parseFloat(string)`
+ `parseString(Number)`

### Error-handling

```js
throw 'myException';
throw true;

try {
	someCode();
} catch (ex) {
	console.log("Some error");
	logError(ex)
} finally {
	console.log("Will run all the time");
}
```

### Dates
+ Internally, the number of milliseconds since EPOCH
+ Contains both date and time.
```js
const now = new Date();
// month starts with 0
const randomDate = new Date(2015,3,12,6,25,58);
```

### Equality

> ALWAYS USE CONST AND ===

### if-else, switch, other syntax

When writing code, you typically want to look for positive rather than negative.

+ & is short-circuit vs && 
+ | is short-circuit vs ||

> ALWAYS USE && and ||

### STRINGS are case sensitive!

### forEach, forIn, forOf, for loops

What is the difference?

### Functions
+ Are objects. See `functionName.name`
+ There are also anonymous functions.
+ If param has no argument, then it will be undefined! So pede nimo sya e-call maski 2 function parameters sya pero 1 argument imong gi pass!
+ If no return statement, value is undefined (dili Null)

### Arrow functions and anonymous functions
```js
const add = (a,b) => a + b;

```

**Arrow functions:**

1. Must be assigned to a variable OR immediately used
2. Implicit return statement
3. `this` is inherited from parent scope!
	1. Cannot be changed
	2. Maintained when function is passed as reference (sticky ba di mag matter kung kinsay caller)

### JSON
+ Only 2 data structures: key-value pair and ordered list of values (arrays)
+ Use `JSON.stringify(obj)` to convert JS object into JSON string.
+ Json string to object use `JSON.parse(str)`

### Objects in JS
+ This `this` keyword kay mo refer sa object at run time (method) OR global object if dili within sa object gi declare ang function! If browser, global is Window. Pede sad nimo erefer as globalThis

### Promises

```js
function promiseTimeout(ms) {
  return new Promise((resolve, reject)=> {
    setTimeout(resolve, ms);
  })
}


promiseTimeout(3000)
  .then(()=> {
    console.log("Done!")
    return promiseTimeout(1000);
  }).then(() => {
    console.log("Second promise 1s done!")
    return Promise.resolve("The message")
  }).then((result) => {
    console.log(result);
  }).catch(() => {
    console.log("Error man!")
  })
```


### async await
Di ko na gets!

### Package management

### Question
1. Why in MDS, `Date.prototype.getFullYear()` nganong `.prototype` pa?

### Decisions to use...
1. Object constructor or literal?
2. Array constructor or literal?
3. Number constructor or literal?
4. Which function expression to use?
5. Which loop construct to use?
6. if-else or switch?


### Tips
1. Array.isArray(obj)

### Automation problem
+ Dynamically create JSON object: CSV / MD table -> JSON object -> JSON string  <--- All JSON schema!
+ Lesson learned: Did not use functions and objects! and other design patterns

TODO:
1. MDN
2. Consolidate with REFERENCE

### TODO

+ Classes
+ Async await promise
+ this!
+ require vs import
+ prototypical inheritance
+ apply
+ Performance and thread 