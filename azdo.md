# Azure Dev Ops

## Creating build pipeline

## Creating release pipeline
1. Go to Pipelines > Releases
2. Create a new pipeline
3. Choose classic
4. Choose artifact
5. Define 1..* Stages

## Pipeline templates
## Pipelines > Library
For new variable group.
## Pipelines > Task Group

## Continuous-testing challenges
1. Scalability
2. Test Data management
3. Test scope

## Checklist
1. Never publish secrets!
2. How to update config (local, dev, tst, acc)?

## Pre-defined variables
- `$(System.DefaultWorkingDirectory`/a/b/c
  - Scope: Agent

## Parameters
- `${{ parameters.url }}`

## Resources

- [Use predefined variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml)
- [TestAutomationU Azure Dev Ops Tutorial](https://testautomationu.applitools.com/azure-devops-tutorial/)
