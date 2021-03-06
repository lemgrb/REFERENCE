## Youtube videos
- https://www.youtube.com/watch?v=Ke90Tje7VS0

## Installation
1. Go to [](https://nodejs.org/en/) and download and install
2. Check versions: `$ npm -v && node-v`

## Setup
1. `npm install create-react-app`
2. `npx create-react-app <directory>`
3. cd `<directory>`
4. `npm start` | `npm run build` | `npm build` | `npm eject`
5. `$ serve -s <build_folder>`

## Resources
- [Commonly faced problems](https://jscomplete.com/learn/react-beyond-basics/react-cfp)
- [Css in js][https://github.com/michelebertoli/css-in-js]
- [Why react?](http://jscomplete.com/why-react)
- [Class Component](https://jscomplete.com/playground/rgs2.7)
- [Guide to configuring react locally](https://jscomplete.com/reactful)
    - Guide for font-awesome: https://github.com/FortAwesome/react-fontawesome
- [Entire game ba](http://github.com/jscomplete/rgs-star-match)

## VSCode plugins
- ESLint
- Prettier
- Simple React Snippets
- Live Server
- Bracket Pair Colorizer
- HTML CSS Support (Bootstrap 4)
- Live Sass Compiler
- Git lens
- Quokka
- Vim - Vim emulation for Visual Studio Code
- VS Color Picker
- Newton Next (Official) - Color Theme
- GraphQL for VSCode


## Checklist
- In useEffect, add '[]' if once lang eexecute, see https://jasonwatmore.com/post/2020/02/01/react-fetch-http-post-request-examples


## Examples

```javascript
ReactDOM.render(
  <App title="Github Cards app" />,
  document.getElementById("root")
);

```

Function component (Arrow function):
```javascript
const App = (props) => <div className="header">{props.title}</div>;
```

or with object destructuring (field=title)

```javascript
const App = ({ title }) => <div className="header">{title}</div>;
```

or with function component

```javascript
function App(props) {
  return <div className="header">{props.title}</div>;
}
```

