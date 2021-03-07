# Mocha, Chai testing

See [https://mochajs.org/](https://mochajs.org/)

## Method 1 (Server side testing)

1. Install mocha: `npm install --dev-save mocha`
2. Create `test/test.js`
3. Example test:

```js
describe("Custom Math Functions", function () {
  describe("pow", function () {
    it("should raises to nth power", function () {
      assert.equal(pow(2, 3), 8);
    });

    it("should raises to nth power", function () {
      assert.equal(pow(2, 4), 16);
    });
  });
});
```

4. Example src:

```js
function pow(x, n) {
  return 8;
}
```

## Method 2 (Client side testing)

1. Import Mocha css: `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/mocha/3.2.0/mocha.css" />`
2. Import Mocha js: `<script src="https://cdnjs.cloudflare.com/ajax/libs/mocha/3.2.0/mocha.js"></script>`
3. Import Chai assertion library: `<script src="https://cdnjs.cloudflare.com/ajax/libs/chai/3.5.0/chai.js"></script>`
4. Initialize: `mocha.setup("bdd");`
5. Initialize `assert` to use chai assert: `let assert = chai.assert;`
6. Create `div#mocha` kay diri ang output
7. Import scripts
8. Import tests
9. `mocha.run();`
