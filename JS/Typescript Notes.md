+ Free functions don't need Class
+ Functions are first-class citizens! can be passed around as arguments!
+ Singleton and static classes are NOT NECCESSARY
+ "Structural types" / types as sets
+ Static typechecker -> A code that runs before your code runs.
+ tsconfig.json
+ Install using NPM or marketplace
+ Autocomplete and inline documentation! haha kay na static naman...


## tsconfig

+ noEmit -> Ayaw output og JS
+ 
```json
{
        "compilerOptions": {
	        "allowJs": false,
	        "checkJs": false,
	        "outDir": "build",
	        "target": "esnext",
	        "noEmit": true
        },
        "include": ["src/**/*"]
}
```


https://github.com/definitelytyped/definitelytyped

## Interface
+ Interface exists to provide type information in TYPESCRIPT never appears in JS!
+ extend using `Interface1 extends Interface2`
```js
interface Exam {
    id: number;
    title: string;
    description: string;
    questions: Question[];
}

interface Question {
    id: number;
    // optional field
    title?: string;
    description: string;
    type: "text" | "choice";
    choices: null | string[];
}

let ltoExam : Exam = {
    id: 1,
    title: "LTO Sample Set 1",
    description: "This is a sample exam. All questions were taken from LTO reviewer.",
    questions: [
        {
            id: 1,
            description:"When the green signal is ON, what does it mean?",
            type: "choice",
            choices: [
                "You must go",
                "You must stop",
                "You must wait"
            ]
        }
    ]
}
```

+ type alias using `type ContactName = string`
+ Enums using: 
+ keyof
+ Use type instead of enums
+ indexed access type
+ Utility types
+ decorators