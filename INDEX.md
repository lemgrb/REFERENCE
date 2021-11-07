# BIG INDEX

NOTE: Using the term framework loosely (might also include libraries)

_italicized_ items are TODOs.

See [TESTING](TESTING.md) for testing.


## PROTOTYPES
- [Prototyping tools 2021](https://miro.com/app/board/o9J_kxk7mGU=/)
  - Webflow
  - Adobe XD
  - Supernova Studio
  - Axure
  - Sketch
  - Invision
  - [Figma](https://www.figma.com/)
### Free assets
- Openmoji
- [Undraw](https://undraw.co/)
### UI/UX
+ [Tailwind](https://tailwindcss.com/)
+ [Bootstrap](https://getbootstrap.com/docs)
    - [react-bootstrap](https://react-bootstrap.netlify.app/)
+ [Chakra-ui](https://chakra-ui.com/)
---------------------------------------------------------------------------------
## WEB STANDARDS
+ Web Dev Specialization, Coursera:
  + [Intro to HTML5, University of Michigan](https://www.coursera.org/learn/html)
  + [Intro to CSS3, University of Michigan](https://www.coursera.org/learn/introcss)
  + [Interactivity with Javascript, University of Michigan](https://www.coursera.org/learn/javascript)
  + [Advanced Styling with Responsive Design, University of Michigan](https://www.coursera.org/learn/responsivedesign)
+ [Javascript.info](https://javascript.info/) - Vanilla JS
+ [A re-introduction to Javascript(JS Tutorial), MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/
A_re-introduction_to_JavaScript)
+ [typescript-cheatsheets/react](https://github.com/typescript-cheatsheets/react)
+ [The State of Javascript Survey](https://stateofjs.com/)

### Javascript Frameworks
+ [Unified.js](https://unifiedjs.com/) - For processing content e.g. Markdown to HTML
+ [lodash](https://lodash.com/docs/)

--------------------------------------------------------------------------------
## FRONTEND
### React
+ [React Developer Roadmap](https://roadmap.sh/react)
+ [React Environment Setup, Jscomplete.com](https://jscomplete.com/reactful) | Not using create-react-app
+ [How to Set Up React.JS Without create-react-app](https://www.youtube.com/watch?v=ddUqNwTpFyM)
+ [_Learn React by Building an eCommerce Site_](https://www.freecodecamp.org/news/learn-react-by-building-an-ecommerce-site/)
+ [React JS - React Tutorial for Beginners, Programming with Mosh](https://www.youtube.com/watch?v=Ke90Tje7VS0)
+ [React: Getting Started by Samer Buna, Pluralsight](https://www.pluralsight.com/courses/react-js-getting-started)
+ [Setting up ENV Variables Without create-react-app](https://stackoverflow.com/questions/59243719/setting-up-env-variables-without-create-react-app)
Storybook setup
```bash
$ npx sb init
$ npm i @storybook/addon-postcss
# See https://github.com/storybookjs/storybook/blob/next/MIGRATION.md#deprecated-implicit-postcss-loader
$ npm install @storybook/builder-webpack5 @storybook/manager-webpack5 --save-dev
# See https://github.com/storybookjs/storybook/blob/next/MIGRATION.md#webpack-5
# import "../src/index.css" in .storybook/preview.js
# import PropTypes from 'prop-types';
```

### React State Management - Shared state by components
  - [Redux](https://redux.js.org/) - Redux is a predictable state container for JavaScript apps.
  - [React Context](https://reactjs.org/docs/context.html) Context provides a way to pass data through the component tree without having to pass props down manually at every level.
  - [Unstated](https://github.com/jamiebuilds/unstated) Unstated is designed to build on top of the patterns already set out by React components and context.

### React REST
  - [Redux Saga](https://redux-saga.js.org/) An intuitive Redux side effect manager.

### GraphQL
  - [The Apollo Data Graph Platform](https://www.apollographql.com/) - 
Apollo is the industry-standard GraphQL implementation, providing the data graph layer that connects modern apps to the cloud.
  - AWS' GraphQL (#tbd)

### React Forms
  - [React Final Form](https://final-form.org/react/) High performance subscription-based form state management for React
  - [Formik](https://formik.org/docs/overview)

### Other react libraries
- "CSS-in-JS"
  - [styled-jsx](https://github.com/vercel/styled-jsx)
  - [styled-components](https://styled-components.com/)
  - [emotion/react](npmjs.com/package/@emotion/react)
- CSS
  - [classnames](https://github.com/JedWatson/classnames)
  - [clsx](https://www.npmjs.com/package/clsx)

### Static-Site Generators (SSG)
+ [Gatsby](https://www.gatsbyjs.com/)
+ HUGO (Go lang)

### React-based Frameworks
+ [Next.js Docs](https://nextjs.org/docs) - Supports SSR/SSG/CSR. SSG good for SEO requirement
+ [Next.js Crash Course 2021, Traversy Media^](https://www.youtube.com/watch?v=mTz0GXj8NN0)

### Headless CMS
- [MachAlliance](https://machalliance.org/) - Microservices based, API-first, Cloud-native SaaS and Headless
- [The state of headless landscape 2021](https://media-exp1.licdn.com/dms/image/sync/C4D27AQGzTFwoAUR6CA/articleshare-shrink_800/0/1613587038813?e=2159024400&v=beta&t=mXpMzWEWsmhpLNbo1lipX0WuAowC86Cbg0si677ZddU)
+ Headless Drupal
+ Headless Laravel
+ [Strapi](https://strapi.io/)
  + [strapi starters](http://strapi.io/starters) backend (rest and graphql) + nextjs frontend
+ Other solutions (!ssg): Joomla/WP/Drupal + Caching/CDN

### Other frameworks/library
+ [_commerceJS](https://commercejs.com/) - Headless eCommerce
+ [Algolia](https://www.algolia.com/) - AI-powered search and discovery platform
+ [threejs](https://threejs.org) - Javascript 3d library
- [NestjS](https://nestjs.com/) 
+ [Yotpo](https://www.yotpo.com/) eCommerce marketing, avalara, simplr, klaviyo, ckustomer
+ [Avalara: Tax compliance software and automated solutions](https://www.avalara.com/us/en/index.html)
+ [Simplr: 24/7 US-Based Customer Service Outsourcing](https://www.simplr.ai/)
+ [Klaviyo offers an sms + email marketing automation software for campaigns driven by a customer data platform with reporting, visualization and analysis.](https://www.klaviyo.com/)
+ [Kustomer: The Customer Service CRM Platform Built for Today](https://www.kustomer.com/)

--------------------------------------------------------------------------------
## BACKEND

### Backend-as-a-service (Baas)
+ [NextJS Firebase Auth Crash Course by James Perkins^](https://www.youtube.com/watch?v=qBGAdenirbs) - Firebase Authentication (Email/Password), nookies, chakra-ui
+ [How To Set Up React With Firebase/Firestore | Get & Realtime | Part 1^](https://www.youtube.com/watch?v=3ZEz-iposj8)
+ [Add Google Analytics And Google AdSense To NextJS!^](https://www.youtube.com/watch?v=I9KJ_rVkmxk)
+ [_Supabase: The Open Source Firebase Alternative_](https://supabase.io/)

--------------------------------------------------------------------------------
## Other frameworks
- Wordpress + Woocommerce
- Shopify
- Magento
- Wix
--------------------------------------------------------------------------------
## No-code
- builder.io
--------------------------------------------------------------------------------
## Optimization
- [https://web.dev/measure/](https://web.dev/measure/)
- [GtMetrix](https://www.gtmetrix.com)
--------------------------------------------------------------------------------
## Data Science
- Machine Learning
- Deep Learning
- Bots

## Data visualization
- [d3](https://d3js.org) - Data driven documents
- [Vizhub Data Visualization Platform](https://vizhub.com)
- [DataTables](https://datatables.net/)
- [React Table: A complete tutorial with examples](https://blog.logrocket.com/complete-guide-building-smart-data-table-react/)
- [GoodData.UI](https://sdk.gooddata.com/gooddata-ui/docs/why_gdui.html) - GoodData.UI is a TypeScript framework for building analytical applications on top of the GoodData platform or GoodData.CN.
- [Google charts](https://developers.google.com/chart/glossary)
--------------------------------------------------------------------------------
## Blockchain/NFT
--------------------------------------------------------------------------------
## Database
- NoSQL
  - [MongoDB](https://www.mongodb.com/)
    - [Mongoose](https://mongoosejs.com/) elegant mongodb object modeling for node.js
  - [Firebase by Google](https://firebase.google.com/)
  - [Cloud Firestore by Google](https://firebase.google.com/docs/firestore)
- Relational
  - MySQL
  - Oracle
  - Postgres
- Graph database
  - [Neo4j](https://neo4j.brand.live/c/2021nodes-homepage)
--------------------------------------------------------------------------------
## DEV-OPS
### Deployment options
+ [Vercel](https://vercel.com/)
+ [Netlify](https://www.netlify.com/)
+ [AWS](https://aws.amazon.com/)
+ [AWS Amplify](https://aws.amazon.com/amplify/)
+ [Firebase console](https://console.firebase.google.com/)
+ [Cloud Firestore Documentation](https://firebase.google.com/docs/firestore)
+ [Github pages](https://pages.github.com/)
+ [GCP]()
+ [Azure]()
+ [Serverless on AWS](https://aws.amazon.com/serverless/)
--------------------------------------------------------------------------------
## Mobile
+ [Flutter](https://flutter.dev/) Flutter is Google's UI toolkit for building beautiful, natively compiled applications for mobile, web, desktop, and embedded devices from a single codebase.
+ [Android](https://developer.android.com/docs)
+ [React Native](https://reactnative.dev/)
+ [_Android App Development for Beginners_](https://www.freecodecamp.org/news/android-app-development-for-beginners/)
--------------------------------------------------------------------------------
## API gateway
+ [Apigee](https://docs.apigee.com/)
+ [Zuul](https://github.com/Netflix/zuul)
+ [WSO2](https://wso2.com/api-manager/)
--------------------------------------------------------------------------------
## Data Structures and Algorithms
## Design Patterns
- Builder
- Singleton
--------------------------------------------------------------------------------
## Digital marketing
- hootsuite
- buffer
- globe MyBusiness AMBER SMS Blaster
- https://www.globe.com.ph/business/sme/shop/gallery.html
--------------------------------------------------------------------------------
## Startups
- [Techcrunch](https://techcrunch.com/)
+ [upscale.upd.edu.ph](upscale.upd.edu.ph)
+ [godigitalasean.ph]
+ [itstartshere.ph]
+ [spri.ng]
+ [indiehackers](https://www.indiehackers.com/)
+ [8.ventures](https://8.ventures/)
--------------------------------------------------------------------------------
## Streaming
- [OBS](https://obsproject.com/)
--------------------------------------------------------------------------------
## Some inspirations
- herdimmunity.ph
- sakay.ph
- coderanch - Kinaraan na style but unique
--------------------------------------------------------------------------------
## Other languages
+ [Svelte](https://svelte.dev/)
+ [Rust](https://www.rust-lang.org/)
+ [Kotlin](https://kotlinlang.org/)
--------------------------------------------------------------------------------
## Agile
+ [Agile manifesto](https://agilemanifesto.org/)
--------------------------------------------------------------------------------
## Data Sources
- data.gov.ph
- efoi
- namria
