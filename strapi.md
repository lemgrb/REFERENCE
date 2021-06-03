## Installing Next.js E-commerce Starter w/ STRAP

Source: [https://strapi.io/starters](https://strapi.io/starters/strapi-starter-next-js-ecommerce)


```bash
$ npx create-strapi-starter my-project next-ecommerce
```

### Setup:
- Ubuntu 20.04

### Error 1: spawn yarn ENOENT

```bash
tawing@DESKTOP-LGHDCI9:~/strapi-starters$ npx create-strapi-starter commerce-be next-ecommerce
Creating Strapi starter frontend at /home/tawing/strapi-starters/commerce-be/frontend.
Installing strapi/strapi-starter-next-ecommerce starter
⠋ Installing dependencies:Command failed with ENOENT: yarn install
spawn yarn ENOENT
```

Solution: Install yarn from PPA

```bash
$ sudo apt remove cmdtest
$ sudo apt remove yarn
$ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
$ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
$ sudo apt update
$ sudo apt install yarn
```

### Error 2: Found incompatible module
```bash
error backend@0.1.0: The engine "node" is incompatible with this module. Expected version ">=10.16.0 <=14.x.x". Got "16.2.0"
error Found incompatible module.
```
Solution: Swith to v14 with nvm
```bash
$ nvm install v14.17
$ nvm use v14.17
```