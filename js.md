## Objects

- Associative arrays
- While **Primitives** contain only a single thing; **objects** store keyed collections of various data and more complex entities.
- A JS **property** is a KVP pair where Key is String and Value _can be any type_.
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
user[key + "-guest"] = "value"; // More complex computed property
user.key = "value"; // Di mo work sa dot notation

console.log(user);
```

```bash
$ node main.js
{ customKey: 'value', 'customKey-guest': 'value', key: 'value' }
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

```bash
$ node main.js
Lemuel
31
undefined
```

#### Copy by reference, object comparisons

```javascript
let user = {
  name: "Lemuel",
};

let user2 = user; // copy by reference
let user3 = {};
let user4 = {};

user2.name = "Lemuel2";

console.log(user);
console.log(user2);
console.log(user == user2); // TRUE - if reference same object
console.log(user === user2); // TRUE - if references the same object;
console.log(user3 == user4); // FALSE - even if looks same
```

#### Cloning for simple objects

```javascript
let user = { name: "Lem" };

let permission1 = { canView: true };
let permission2 = { canEdit: true };

// Method 1
Object.assign(user, permission1, permission2);

// Method 2
let clone = Object.assign({}, user);

// Method 3 -- Spread operator
let clone2 = { ...clone };

// { name: 'Lem', canView: true, canEdit: true }
console.log(user);
console.log(clone);
console.log(clone2);
```

#### Cloning objects nga naa say object sulod (diba copy by reference)

- If eedit ang clone, ma edit sad original na nested object

```javascript
let user = {
  name: "Lem",
  permissions: {
    create: true,
    edit: true,
    read: true,
  },
};

let clone = Object.assign({}, user);
clone.permissions.edit = false; // Will affect user.permission.edit = false;

console.log(user);
console.log(clone);
```

```bash
{ name: 'Lem', permissions: { create: true, edit: false, re
ad: true } }
{ name: 'Lem', permissions: { create: true, edit: false, re
ad: true } }

```

Gamit lang sa \_.cloneDeep(obj) from the JavaScript library lodash. hehe

```javascript
// npm install --save lodash
var _ = require("lodash");

let user = {
  name: "Lem",
  permissions: {
    create: true,
    edit: true,
    read: true,
  },
};

let clone = _.cloneDeep(user);
clone.permissions.edit = false;
console.log(user);
console.log(clone);
```

```bash
$ node main.js
{ name: 'Lem', permissions: { create: true, edit: true, rea
d: true } }
{ name: 'Lem', permissions: { create: true, edit: false, re
ad: true } }

```

## this

Method shorthand:

```javascript
// Method shorthand
let user = {
  name: "Lem",
  age: 31,
  sayName() {
    console.log(this.name);
  },
};

user.sayName();
```

Result:

```bash
$ node main1.js
Lem
```

Methods not bound to object

```javascript
// Methods not bound to object

function greet() {
  console.log(this.name + " says " + this.hi);
}

let dog = { name: "Dog", hi: "Aww" };
let cat = { name: "Cat", hi: "Meow" };

dog.greet = greet;
cat.greet = greet;

dog.greet();
cat.greet();
```

Result:

```bash
$ node main2.js
Dog says Aww
Cat says Meow
```

#### Constructor functions (or object prototypes?)

Instead of creating multiple object literals:

```javascript
// Object literal 1
let user1 = {
  name: "User1",
  isAdmin: false,
};

// Object literal 2
let user2 = {
  name: "User2",
  isAdmin: false,
};

console.log(user1);
console.log(user2);
```

Use **constructor functions**:

```javascript
function User(name, isAdmin = false) {
  // this = {}; (implicitly)
  this.name = name;
  this.isAdmin = isAdmin;
  // Pwede methods pod diri (see Object literals sa taas)
  // return this; (implicitly)
}

let user1 = new User("User1");
let user2 = new User("User2");

console.log(user1);
console.log(user2);
```

#### Optional chaining with '?.'

- Can be used for function calls too.

```javascript
let user = {};
console.log(user.address && user.address.street);
// Is the same as..
console.log(user?.address?.street);
```

#### Symbols

See https://javascript.info/symbol

#### Object to primitive conversion
- Symbol.toPrimitive, toString, valueOf. For the subtle diff, see https://javascript.info/object-toprimitive

```javascript
let user31 = {
  name: 'Lemuel',
  age: 31,
  [Symbol.toPrimitive](hint) {
    console.log(`hint: ${hint}`);
    return hint == "string"? `{name: "${this.name}"}`: this.age;
  }
};

let userX = {};
userX[user31] = 1;
console.log(userX);
console.log(+user31);
console.log(user31+500);

```
Result:
```bash
$ node objtoprimitive.js
hint: string
{ '{name: "Lemuel"}': 1 }
hint: number
31
hint: default
531
```
