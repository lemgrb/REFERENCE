## Resources
- [](https://dev.to/dabit3/data-modeling-in-depth-with-graphql-aws-amplify-17-data-access-patterns-4meh)

## Mutation

````Graphql
mutation updateSts($input: ChangeUserStatusInput!) {
  changeUserStatus(input: $input) {
    clientMutationId
    status {
      message
    }
  }
}

query viewUserInfo {
  viewer {
    login
    name
    status {
      id
      message
    }
  }
}
## Query variables

{
	"input": {
    "clientMutationId": "121121212",
    "message": "Updated via GraphQL"
  } 
}
````

## Another example
# Create a post and associate it with the blog via the "postBlogId" input field.
# Provide the returned id as the "postId" variable.
````Graphql
query list {
  listPropertys(filter: {
    permalink: {
      contains: "TEST"
    }
  }) {
    items {
      name
      permalink
    }
  }
}

mutation create {
  createProperty(input: {
    name: "TEST"
		description:"TEST"
    banner: "TEST"
    permalink: "TEST"
  }) {
    id name description banner permalink
  }
}
  ````
}
