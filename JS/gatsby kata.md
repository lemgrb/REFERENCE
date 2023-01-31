1. `npm install -g gatsby-cli`
2. `gatsby --version`
3. Create starter : `gatsby new [rootPath] [starter]` e.g. `gatsby new riderph.com https://github.com/gatsbyjs/gatsby-starter-blog.git
4. Create global stylesheet in `src/styles/global.css` and import in `gatsby-browser.js`
5. npm install for sass: `npm install sass gatsby-plugin-sass`
6. Source plugin: `npm install --save gatsby-source-filesystem`
7. Install transformer plugin: `npm install --save gatsby-transformer-remark`

### GraphQL

Retrieve markdown files without transformation
```graphql
{
  allFile {
    edges {
      node {
        id
        name
        ext
        size
      }
    }
  }
}
```

Retrieve markdown files after transformation

```graphql
{
  allMarkdownRemark(sort: {frontmatter: {date: ASC}}) {
    totalCount
    edges {
      node {
        id
        html
        frontmatter {
          title
          image
          date(formatString: "MMM YYYY")
        }
        excerpt
      }
    }
  }
}
```


## Deployment to AWS (S3 and Cloudfront)