## How many for each type of tests?
```txt
  /\   --> UI (Slow, integrated)
 /  \  --> Integration
/    \ --> Unit (Fast, isolated)
------
```

See https://martinfowler.com/articles/practical-test-pyramid.html

> Write the **smallest number** of tests possible to reach the **required** level of **quality** or **confidence** in the system being developed.

## Testing trophy (another way)

See [The Testing Trophy and Testing Classifications](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)

## WHAT scenario to automate?
Not all!!!! Identify scenarios to automated based on:
1. Value : Importance of feature, probability feature would be fixed if broken, distinctness
2. Risk: Impact to cx, Probability of use
3. Cost: Ease of writing, How quick to write

