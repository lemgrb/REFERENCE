## Objects

- **Primitives** contain only a single thing; **objects** store keyed collections of various data and more complex entities.
- A JS **property** is a KVP pair where Key is String and Value _can be anything_.
- Di pareho sa variable names, ok ra ang reserved keywords (let, for) as property names

### Create

Create Empty object:

```Javascript
let user = new Object();
let user = {}; // object literal ni
```

Create Object with properties:

```Javascript
let user = {
  name: "Lemuel",
  age: 31,
  'multi word?': 'YES',
};
```

Notice the trailing comma sa taas.

### Read

- Dot notation: `console.log(user.name)`
- Bracket notation:
  - `console.log(user['name'])`
  - `console.log(user['multi word?'])`

### Update

```Javascript
user.isAdmin = false;
user['isActive'] = true;
```

### Delete

```Javascript
delete user.isAdmin;
delete user['isAdmin'];
```

### More on square brackets

Kung square brackets pwede gamiton ang result sa expression as key. Di ni mo work sa dot notation.

```javascript
let user = {};
let key = "customKey"; // or, prompt("Enter key?")

user[key] = "value"; // Computed property
user[key + '-guest'] = "value" // More complex computed property
user.key = "value"; // Di mo work sa dot notation


console.log(user); // { customKey: 'value', key: 'value', 'customKey-guest': 'val
ue' }
```

### Property Value Shorthand

```javascript
function makeUser(name, age) {
  return {
    name, // short ra sa name:name
    age: 30, // pwede sagol sa di shorthand
  };
}
```

#### Property existence with "in"

- Alternative sa simple test if property is undefined

```javascript
let user = {
  name: "Lemuel",
  age: 31,
  test: undefined, // rare ni kay dapat null ni or empty value
};

console.log("age" in user); // true
console.log("what" in user); // false
console.log(user.test); // undefined, because? 'test' property exists!
```

#### for...in

- Kung mag for..in ka, if integer (or nay integer property) ang keys order ascending, otherwise, by creation date lang.

```javascript
let user = {
  name: "Lemuel",
  age: 31,
  test: undefined,
};

for (let key in user) console.log(user[key]);
```
