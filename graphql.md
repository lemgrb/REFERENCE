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
