## Variables

- Robot Framework has its own variables that can be used as scalars, lists or dictionaries using syntax ${SCALAR}, @{LIST} and &{DICT}, respectively. In addition to this, environment variables can be used directly with syntax %{ENV_VAR}.
- Use 'Create list' for list variables. `@{list} =    Create List    foo    baz`
- Precedence of global variables: `CMD > Script > Keyword`
