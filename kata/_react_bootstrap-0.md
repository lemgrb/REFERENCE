1.  [Create React App](_react-0.md)
2.  Install bootstrap and sass

    - `npm install --save bootstrap@next`
    - `npm install --save node-sass`

3.  Customize bootstrap default bg and color

        - Create file `src/scss/customs.scss`
        - Customize [theme](https://getbootstrap.com/docs/5.0/customize/sass/)
        - Compile: `$ sass scss/custom.scss:css/Custom.css`

4.  Create container>row with 8col+4col, verify bg and font color changed
5. Add new style with scss (new nested classes)
6. Use `<time>` tag and add 2 or more of the bootstrap classes below:
  - .text-muted
  - .fw-bold
  - .text-danger
  - .lead
  - .my-0
  - .list-unstyled
7. Install bootstrap icons: `npm i bootstrap-icons`
8. Use bootstrap icon as icon-font: `import "./../node_modules/bootstrap-icons/font/bootstrap-icons.css";`
