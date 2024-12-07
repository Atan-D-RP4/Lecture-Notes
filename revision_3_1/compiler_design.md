# Syllabus
## UNIT-I:
Programs related to compilers.
Translation process.
Major data structures.
Other issues in compiler structure.
Boot strapping and porting.
Lexical analysis:
* The role of Lexical Analyzer
* Input Buffering
* Specification of Tokens
* Recognition of Tokens
* The Lexical-Analyzer Generator Lex.

## UNIT-II:
Design of Parsers:
* Top-down Parsers
* Backtracking
* Recursive Descent Parser
* Left recursion
* Left factoring Ambiguity
* LL (1) grammar,
* Non-recursive descent parser (Predictive Parser).

## UNIT-III:
Bottom-up parser:
* Introduction to LR Parsing
* Shift Reduce parser
* Operator Precedence Parser
LR parser:
* LR (0)
* SLR
* CLR parsers
* LALR parsers
* Parser Generator - YACC.

## UNIT-IV:
Syntax Directed Translation:
* Syntax Directed Definitions and Translation.
* Intermediate code generation
* Three-Address Code
* DAG, Types and Declarations,
* Translation of Expressions
* Type Checking, Control Flow.
Machine Independent Optimizations:
* The Principal Sources of Optimizations
* Introduction to data flow analysis
* Foundation of data flow analysis.

## UNIT-V:
Code Generation:
* Problems
* Machine model
* A simple code generator
* Machine dependent code Optimization
* Register allocation and assignment
* Code generation from DAG
* Peephole optimization.
Storage Organization and Error Recovery:
* Symbol tables
* Run-time storage administration
* Stack
* Heap Management
* Garbage Collection
* Error detecting and Reporting in various Phases.



# Questions and Answers
## Unit - I
### Question
Define compiler? Explain Phases of compilation with examples?

### Answer
A Compiler is a program that takes a source language and through the use
of the languages syntax and semantic specification, translates it into equivalent
target language.

Phases of Compilation are:
* Lexical Analysis:
    The first phase of a compiler is lexical analysis, also known as scanning. This
    phase reads the source code and breaks it into a stream of tokens, which are
    the basic units of the programming language. The tokens are then passed on to
    the next phase for further processing. For example, in the following C code;
    "int main() { return 0; }", the tokens are "int", "main", "(", ")", "{",
    "return", "0", ";", and "}".

* Syntax Analysis:
    The second phase of a compiler is syntax analysis, also known as parsing. This
    phase takes the stream of tokens generated by the lexical analysis phase and
    checks whether they conform to the grammar of the programming language. The
    output of this phase is usually an Abstract Syntax Tree (AST).

* Semantic Analysis:
    The third phase of a compiler is semantic analysis. This phase checks
    whether the code is semantically correct, i.e., whether it conforms to the
    language’s type system and other semantic rules. In this stage, the compiler
    checks the meaning of the source code to ensure that it makes sense. The
    compiler performs type checking, which ensures that variables are used
    correctly and that operations are performed on compatible data types. The
    compiler also checks for other semantic errors, such as undeclared variables
    and incorrect function calls.

* Intermediate Code Generation:
    The fourth phase of
    a compiler is intermediate code generation. This phase generates an
    intermediate representation of the source code that can be easily translated
    into machine code. Optimization: The fifth phase of a compiler is optimization.
    This phase applies various optimization techniques to the intermediate code to
    improve the performance of the generated machine code. Code Generation: The
    final phase of a compiler is code generation. This phase takes the optimized
    intermediate code and generates the actual machine code that can be executed by
    the target hardware.

### Question
Identify the Lexemes, Tokens and write the number of tokens in a given program.
```c
int main() { int *a,b; b=10; a=&b; printf(“%d%d”,b,*a); b=*/*pointer*/b; }
```

### Answer
Lexemes are the smallest units of a program that the compiler can recognize. Tokens are the
group of characters that are meaningful to the compiler. The number of tokens in the given program
are 20. The tokens are:
```table
    Lexemes         | Tokens
    1. int          | Keyword
    2. main         | Identifier
    3. (            | Special Symbol
    4. )            | Special Symbol
    5. {            | Special Symbol
    6. int          | Keyword
    7. *            | Operator
    8. a            | Identifier
    9. ,            | Special Symbol
    10. b           | Identifier
    11. ;           | Special Symbol
    12. b           | Identifier
    13. =           | Operator
    14. 10          | Constant (Integer)
    15. ;           | Special Symbol
    16. a           | Identifier
    17. =           | Operator
    18. &           | Special Symbol
    19. b           | Identifier
    20. ;           | Special Symbol
    21. printf      | Identifier
    22. (           | Special Symbol
    23. "%d%d"      | String Literal
    24. ,           | Special Symbol
    25. b           | Identifier
    26. ,           | Special Symbol
    27. *a          | Identifier
    28. )           | Special Symbol
    29. ;           | Special Symbol
    30. b           | Identifier
    31. =           | Operator
    32. *           | Operator
    34. /*pointer*/ | Comment
    35. b           | Identifier
    36. ;           | Special Symbol
    37. }           | Special Symbol
```

```c
int main() {
    // comment
    int a,b;
    a = 10;
    b = 20;
    return;
}
```
For the above program, the tokens are:

```table
Lexemes         | Tokens
1. int          | Keyword
2. main         | Identifier
3. (            | Special Symbol
4. )            | Special Symbol
5. {            | Special Symbol
6. // comment   | Comment
7. int          | Keyword
8. a            | Identifier
9. ,            | Special Symbol
10. b           | Identifier
11. ;           | Special Symbol
12. a           | Identifier
13. =           | Operator
14. 10          | Constant (Integer)
15. ;           | Special Symbol
16. b           | Identifier
17. =           | Operator
18. 20          | Constant (Integer)
19. ;           | Special Symbol
20. return      | Keyword
21. ;           | Special Symbol
22. }           | Special Symbol
```

### Question
Explain the key elements in the lex program?

### Answer
The key elements in the lex program are:
* Regular Expressions:
    Regular expressions are used to define the patterns of tokens in the input
    stream. Lex uses regular expressions to match the input stream with the
    patterns defined in the lex program.

* Actions:
    Actions are the code snippets that are executed when a pattern is matched.
    Actions can be used to perform various tasks, such as updating variables,
    printing output, or calling functions.

* Macros:
    Macros are used to define reusable code snippets that can be used in the lex
    program. Macros can be used to define regular expressions, actions, or other
    elements of the lex program.

* Rules:
    Rules are the basic building blocks of the lex program. A rule consists of a
    regular expression pattern followed by an action. When the input stream
    matches the pattern, the action associated with the rule is executed

### Question
Explain about input buffering and its types.

### Answer
Input buffering is the process of reading characters from the input stream and
storing them in a buffer before processing them. Input buffering is used to
improve the efficiency of the lexical analysis phase by reducing the number of
system calls required to read characters from the input stream and by allowing
the lexer to process characters in batches.

Types of input buffering are:
* Line buffering:
    In line buffering, the input stream is read one line at a time. The lexer
    processes each line of input separately, which can be useful for processing
    text files or other input streams that are organized into lines.

* Block buffering:
    In block buffering, the input stream is read in blocks of characters. The
    lexer processes each block of characters as a single unit, which can be
    useful for processing binary files or other input streams that are not
    organized into lines.

* Token buffering:
    In token buffering, the input stream is read one token at a time. The lexer
    processes each token separately, which can be useful for processing
    programming languages or other input streams that are organized into
    tokens.

### Question
Demonstrate the phases of compiler for the following
assignment statement: a = (b+c)+12.

### Answer
The phases of the compiler for the assignment statement "a = (b+c)+12" are:
* Lexical Analysis:
    The lexical analysis phase reads the input stream and breaks it into tokens.
    The tokens for the assignment statement are:
    "a", "=", "(", "b", "+", "c", ")", "+", "12".

* Syntax Analysis:
    The syntax analysis phase checks whether the tokens conform to the grammar
    of the programming language. The syntax tree for the assignment statement is:
    ```
    =
    / \
    a  +
       / \
      +   12
     / \
    a   +
       / \
      b   c
    ```

* Semantic Analysis:
    The semantic analysis phase checks whether the code is semantically correct.
    The compiler checks the meaning of the source code to ensure that it makes
    sense. The compiler performs type checking, which ensures that variables are
    used correctly and that operations are performed on compatible data types.

* Intermediate Code Generation:
    The intermediate code generation phase generates an intermediate representation
    of the source code that can be easily translated into machine code. The
    intermediate code for the assignment statement is:
    ```
    t1 = b + c
    t2 = t1 + 12
    a = t2
    ```

* Optimization:
    The optimization phase applies various optimization techniques to the intermediate
    code to improve the performance of the generated machine code.

* Code Generation:
    The code generation phase takes the optimized intermediate code and generates
    the actual machine code that can be executed by the target hardware.

### Question
Compare PASS and PHASE with examples?

##
PASS:
* A pass is a complete traversal of the entire program or data structure
  during compilation, typically performing a specific transformation or analysis.
* Characteristics of a PASS:
    - Operates on the entire input
    - Completes a specific analysis or transformation
    - May modify or analyze the program representation
    - Can be single or multiple times through the code
* Example:
    - Lexical Pass: Reads the input stream and breaks it into tokens.
    ```c
    Input: int x = 10 + 20;
    First Pass: Tokenization
    Tokens: [INT] [IDENTIFIER:x] [ASSIGNMENT] [CONSTANT:10] [PLUS] [CONSTANT:20]
    ```
    - Type Checking Pass: Checks whether the types of operands in an expression are compatible.
    ```c
    Input: float x = 10; int y = 20.5;
    Second Pass: Type Checking
    Error: Incompatible types in assignment: float to int
    ```
PHASE:
* A phase is a specific stage in the compilation process that performs a
  particular task or analysis on the input program or data structure.
* Characteristics of a PHASE:
    - Focuses on a specific task or analysis
    - May operate on a subset of the input
    - Typically part of a larger compilation process
    - May be composed of multiple passes
* Example:
    - Lexical Analysis Phase: Breaks the input stream into tokens.
    ```c
    Input: int x = 10 + 20;
    Lexical Analysis Phase
    Tokens: [INT] [IDENTIFIER:x] [ASSIGNMENT] [CONSTANT:10] [PLUS] [CONSTANT:20]
    ```
    - Syntax Analysis Phase: Checks whether the tokens conform to the grammar of the programming language.
    ```c
    Tokens: Parse and create Abstract Syntax Tree (AST)
         =
        / \
       a   +
          / \
         b   c
    ```

### Question
Explain Bootstrap technique with example?

### Answer
Bootstrapping is the process of writing a compiler for a programming language
using the language itself. In other words, it is the process of using a
compiler written in a particular programming language to compile a new version
of the compiler written in the same language.

Let's consider a simple example of bootstrapping using the new Rust programming
language. The Rust compiler is written in Rust itself, which means that the
Rust compiler is used to compile a new version of the Rust compiler.

The process of bootstrapping involves the following steps:
1. Write an initial version of the Rust compiler in another language, such as C.
2. Rewrite the Rust compiler in Rust itself using the initial version of the compiler.
3. Compile the new version of the Rust compiler using the initial version of the compiler.
4. Use the new version of the compiler written in Rus to compile another new version of the compiler.
5. Repeat the process until the compiler reaches a stable state or ad infinitum.

Advantages of bootstrapping:
* Self-hosting: The compiler can compile itself, which ensures that the compiler is self-consistent.
* Language evolution: The compiler can be easily updated to support new language features.
* Portability: The compiler can be easily ported to different platforms.
Disadvantages of bootstrapping:
* Complexity: Bootstrapping can be complex and time-consuming.
* Maintenance: The compiler must be maintained to ensure that it remains self-consistent.
* Debugging: Debugging a bootstrapped compiler can be challenging. Since
  errors/idiosyncrasies in an earlier compiler can effect the results of later
  versions.

### Question
What kind of errors can be detected during lexical
analysis? Explain.

### Answer
The following types of errors can be detected during lexical analysis:
* Illegal characters: The lexer can detect characters that are not part of the programming language's character set.
* Invalid tokens: The lexer can detect tokens that do not conform to the language's syntax rules.
* Unmatched quotes: The lexer can detect strings that are not properly terminated with matching quotes.
* Unmatched braces: The lexer can detect unbalanced braces, parentheses, or brackets.
* Invalid identifiers: The lexer can detect identifiers that do not conform to the language's naming rules.
* Reserved words: The lexer can detect reserved words that are used as identifiers.
* Comments: The lexer can detect comments that are not properly terminated.
* Whitespace: The lexer can detect excessive whitespace or tabs that are not part of the language's syntax.
* Line breaks: The lexer can detect line breaks that are not properly terminated.

### Question
Describe the need and Functionality of linker, assembler
and loader.

### Answer
Linker:
* Need: The linker is needed to combine multiple object files generated by
  the compiler into a single executable file.
* Functionality: The linker resolves external references between object files,
  combines them into a single executable file, and assigns memory addresses to
  the code and data sections.
Assembler:
* Need: The assembler is needed to translate assembly language code into machine code.
* Functionality: The assembler reads the assembly language code, translates
  it into machine code, and generates an object file that can be linked with
  other object files.
Loader:
* Need: The loader is needed to load the executable file into memory and start the execution of the program.
* Functionality: The loader reads the executable file, allocates memory for
  the program, loads the program into memory, and starts the execution of the
  program.

## Unit - II

### Question
Check whether the following grammar is LL(1) or not
```
S->iEtSS’|a
S’->eS|€
E->b
```

### Answer
To check whether the given grammar is LL(1), we need to construct the
FIRST and FOLLOW sets for each non-terminal symbol and check for any conflicts.

Given Grammar:
```
S -> aBDh
B -> cC
C -> bC / ∈
D -> EF
E -> g / ∈
F -> f / ∈
```

Rules for calculating First Function:
- For a production rule X -> ∈, First(X) = {∈}
- For any terminal symbol ‘a’, First(a) = { a }
- For a production rule X -> Y1Y2Y3,
    * Calculating First(X)
        - If ∈ ∉ First(Y1), then First(X) = First(Y1)
        - If ∈ ∈ First(Y1), then First(X) = { First(Y1) – ∈ } ∪ First(Y2Y3)
    * Calculating First(Y2Y3)
        - If ∈ ∉ First(Y2), then First(Y2Y3) = First(Y2)
        - If ∈ ∈ First(Y2), then First(Y2Y3) = { First(Y2) – ∈ } ∪ First(Y3)
    * Similarly, we can make expansion for any production rule X -> Y1Y2Y3…..Yn.

Rules for calculating Follow Function:
- For the start symbol S, Follow(S) = { $ }
- For a production rule A -> αB, Follow(B) = Follow(A)
- For any production rule A -> αBβ, where β is a string of grammar symbols,
    * If ∈ ∈ First(β), then Follow(B) = Follow(A) ∪ { First(β) - ∈ }
    * If ∈ ∉ First(β), then Follow(B) = Follow(A)

```sets
FIRST(S) = {a}
FIRST(B) = {c}
FIRST(C) = {b, ∈}
FIRST(D) = {First(E) - {∈}} U {First(F)} = {g, f, ∈}
FIRST(E) = {g, ∈}
FIRST(F) = {f, ∈}

FOLLOW(S) = {$}
FOLLOW(B) = { First(D) - {∈} } U { First(h) } = {g, f, h}
FOLLOW(C) = Follow(B) = {g, f, h}
FOLLOW(D) = First((h) = {h}
FOLLOW(E) = First(F) U Follow(D) = {f, h}
FOLLOW(F) = Follow(D) = {h}
```

The given grammar is LL(1) because there are no conflicts in the FIRST and FOLLOW sets.

### Question
Compare Top Down Parsing and Bottom up parsing with
examples?

### Answer
Top-Down Parsing:
* In top-down parsing, the parser starts from the root of the parse tree and
  works its way down to the leaves. The parser uses a set of production rules
  to match the input string with the grammar of the programming language.
* Characteristics of Top-Down Parsing:
    - The parser starts from the start symbol and tries to match the input string.
    - The parser uses a set of production rules to generate the parse tree.
    - The parser uses a recursive descent or predictive parsing technique.
    - The parser may backtrack if it encounters a conflict in the grammar.
* Example of Top-Down Parsing:
    Consider the following grammar.
    ```
    S -> aAB
    A -> b / ∈
    B -> c / d
    ```
    Input: abd
    Parse Tree:
    ```
      S
     / \
    a   AB
       /  \
      b    d
    ```

Bottom-Up Parsing:
* In bottom-up parsing, the parser starts from the leaves of the parse tree
 and works its way up to the root. The parser uses a set of production rules
 to match the input string with the grammar of the programming language.
* Characteristics of Bottom-Up Parsing:
   - The parser starts from the input string and tries to generate the start symbol.
   - The parser uses a set of production rules to generate the parse tree.
   - The parser uses a shift-reduce or LR parsing technique.
   - The parser may reduce the input string to the start symbol.
* Example of Bottom-Up Parsing:
   Consider the following grammar:
   ```
   S -> aAB
   A -> b / ∈
   B -> c / d
   ```
   Input: abd
   Parse Tree:
   ```
     S
    / \
   a   AB
      /  \
     A    d
    / \
   b   B
      / \
     c   d
   ```




### Question
Explain Left Recursion and Left Factoring with an examples?

### Answer
Left Recursion:
* Left recursion occurs when a non-terminal symbol can directly or indirectly
  produce a production rule that starts with itself.
* Example of Left Recursion:
- Consider the following grammar:
  ```
  A -> Aa / b
  ```
  The production rule A -> Aa is left-recursive because A can directly produce
  a production rule that starts with itself.
* Left recursion can cause infinite loops in the parser and lead to non-termination.
* To eliminate left recursion, we can rewrite the grammar as follows:
  ```
  A -> bA’
  A’ -> aA’ / ∈
  ```

Left Factoring:
* LeftLeft factoring is a technique used to transform a grammar to make it
  suitable for predictive parsing. It involves factoring out the common prefixes
  of the alternatives in a production.
* Example of Left Factoring:
  Consider the following grammar:
  ```
  A -> ab / ac
  ```
  The production rules ab and ac share a common prefix a.
* To eliminate left factoring, we can rewrite the grammar as follows:
  ```
  A -> aB
  B -> b / c
  ```

### Question
Explain Recursive Descent parser with an examples?

### Answer
Recursive Descent Parser:
* A recursive descent parser is a type of top-down parser that uses a set of
  recursive procedures to parse the input string. Each non-terminal symbol in
  the grammar is associated with a procedure that implements the production
  rules for that symbol.
* Characteristics of Recursive Descent Parsing:
  - The parser starts from the start symbol and recursively applies the
    production rules to match the input string.
  - The parser uses a set of recursive procedures to generate the parse tree.
  - The parser uses a predictive parsing technique to choose the correct
    production rule based on the next input symbol.
  - The parser may backtrack if it encounters a conflict in the grammar.
* Example of Recursive Descent Parsing:
  Consider the following grammar:
  ```
  S -> aAB
  A -> b / ∈
  B -> c / d
  ```
  Input: abd
  Parse Tree:
  ```
    S
   / \
  a   AB
     /  \
    b    d
  ```
* Recursive Descent Parsing Procedure:
  - For each non-terminal symbol in the grammar, define a recursive procedure
    that implements the production rules for that symbol.
  - Start the parsing process by calling the procedure associated with the
    start symbol.
  - The procedure reads the next input symbol and chooses the correct production
    rule based on the input symbol.
  - If the procedure encounters a non-terminal symbol, it recursively calls
    the procedure associated with that symbol.
  - The parsing process continues until the entire input string is matched
    with the grammar.
* Recursive Descent Parsing Algorithm for he above grammar:
  ```
  Procedure S:
      Read next input symbol
      If input symbol = a:
          Call procedure A
          Call procedure B
      Else:
          Error
  Procedure A:
      Read next input symbol
      If input symbol = b:
          Accept
      Else:
          Accept
  Procedure B:
      Read next input symbol
      If input symbol = d:
          Accept
      Else if input symbol = c:
          Accept
      Else:
          Error
  ```

### Question
Eliminate the left recursion for the grammar.
```
A -> ABd | Aa | a
B -> Be | b
```

### Answer
Rules for Eliminating Left Recursion:
* Given Grammar:
    ```
    A -> ABd | Aa | a
        |  Aα    |

    B -> Be | b
    ```
* For a production rule A -> Aα|β, where α and β are strings of grammar symbols,
  Eliminate left recursion by replacing A with A’:
  ```
  A -> βA’
  A’ -> αA’ | ∈
  ```

Therefore the grammar after eliminating left recursion is:
```
A -> aA’
A’ -> BdA’ | aA’ | ∈
B -> bB’
B’ -> eB’ | ∈
```

### Question
Check whether the following grammar is ambiguous or not.
```
S-> aS | Sa | Є
```

### Answer
A grammar is ambiguous if it has more than one parse tree for a given input string.
To check whether the given grammar is ambiguous, we need to construct the
parse tree for a given input string and check if there are multiple parse trees.

Given Grammar:
```
S -> aS | Sa | ∈
```
Let's consider the input string 'aaa':
Parse Tree 1:
```
    S
   / \
  a   S
     / \
    a   S
       / \
      a   ∈
```
Parse Tree 2:
```
        S
       / \
      S   a
     / \
    a   S
       / \
      a   ∈
```
Since there are multiple parse trees for the input string "aaa", the given grammar is ambiguous.

### Question
Show that following Grammar is LL(1)
```
S->AaAb |BbBa
A->€
B->€
```

### Answer
To check whether the given grammar is LL(1), we need to construct the
FIRST and FOLLOW sets for each non-terminal symbol and check for any conflicts.

Given Grammar:
```
S -> AaAb | BbBa
A -> €
B -> €
```

First Set:
```
FIRST(S) = {€, a, b}
FIRST(A) = {€}
FIRST(B) = {€}
```

Follow set:
```
FOLLOW(S) = { $ }
FOLLOW(A) = { a, b }
FOLLOW(B) = { b, a }
```

The given grammar is not LL(1) because there multiple possible derivations for
'a' and 'b'. The epsilon productions can cause conflicts in parsing table and
thus a deterministic LL(1) parsing table cannot be constructed

### Question
Construct Right most derivation for the grammar:
```
E->E+T/T
T->T*F/F
F->(E)/id
for w= id+id*id.
```

### Answer
Given Grammar:
```
E -> E + T / T
T -> T * F / F
F -> ( E ) / id
```
Input String: id + id * id

Rightmost Derivation:
```
E -> E + T
  -> E + T * F
  -> E + F * F
  -> E + id * F
  -> E + id * id
  -> T + id * id
  -> F + id * id
  -> id + id * id
```

### Question
Construct predictive parsing table for the grammar:
```
E->E+T/T
T->T*F/F
F->(E)/id
```

### Answer
Given Grammar:
```
E -> E + T / T
T -> T * F / F
F -> ( E ) / id
```

Modified Grammar after removing Left Recursion:
```
E -> T E'
E' -> + T E' / €
T -> F T'
T' -> * F T' / €
F -> ( E ) / id
```

First and Follow Sets:
```
FIRST(E) = First(T) = First(F) = { (, id }
FIRST(E') = { +, € }
FIRST(T) = First(F) = { (, id }
FIRST(T') = { *, € }
FIRST(F) = { (, id }

FOLLOW(E) = { $, ) }
FOLLOW(E') = { $, ) }
FOLLOW(T) = { +, $, ) }
FOLLOW(T') = { +, $, ) }
FOLLOW(F) = { *, +, $, ) }
```
Parsing Table:
```table
+-------+------------+-------------------+--------------+--------------+------------+-------------+
|       |   id       |   +               |   *          |   (          |   )        |   $         |
+-------+------------+-------------------+--------------+--------------+------------+-------------+
|  E    |  E -> T E'  |                   |              |  E -> T E'    |            |             |
|  E'   |            |  E' -> + T E'      |              |              |  E' -> €    |  E' -> €     |
|  T    |  T -> F T'  |                   |              |  T -> F T'    |            |             |
|  T'   |            |  T' -> €           |  T' -> * F T' |              |  T' -> €    |  T' -> €     |
|  F    |  F -> id    |                   |              |  F -> ( E )   |            |             |
+-------+------------+-------------------+--------------+--------------+------------+-------------+
```


## Unit - III

### Question
Explain LR parsing with an example?

### Answer
LR Parsing:
* LR parsing is a type of bottom-up parsing that uses a deterministic pushdown
  automaton to parse the input string. The LR parser reads the input string from
  left to right and constructs a reversed rightmost derivation of the input string.
* Characteristics of LR Parsing:
    - The parser starts from the input string and works its way up to the start symbol.
    - The parser uses a deterministic pushdown automaton to generate the parse tree.
    - The parser uses a shift-reduce technique to reduce the input string to the start symbol.
    - The parser may use LR(0), SLR, LALR, or CLR parsing techniques.
* Example of LR Parsing:
    Consider the following grammar:
    ```
    E -> E + T / T
    T -> T * F / F
    F -> ( E ) / id
    ```
    Input: id + id * id

    Parse Steps:
    ```table
    Stack        | Input          | Action
    -------------+----------------+----------------
    0            | id + id * id $ | Shift
    0 id         | + id * id $    | Reduce F -> id
    0 F          | + id * id $    | Shift
    0 F +        | id * id $      | Shift
    0 F + id     | * id $         | Reduce F -> id
    0 F + F      | * id $         | Shift
    0 F + F *    | id $           | Shift
    0 F + F * id | $              | Reduce F -> id
    0 F + F      | $              | Reduce T -> F
    0 F          | $              | Reduce T -> T * F
    0 T          | $              | Reduce E -> T
    0 E          | $              | Accept
    ```

### Question
Show that the following grammar:
```
S -> Aa | bAc | Bc
A -> d
B -> d
```
... is LR(1) but not LALR(1).

### Answer
To show that the given grammar is LR(1) but not LALR(1), we need to construct
the LR(1) and LALR(1) parsing tables and check for any conflicts.

Given Grammar:
```
S -> Aa | bAc | Bc
A -> d
B -> d
```

LR(1) Parsing Table:
```table
+-------+------------+------------+------------+------------+
|       |   a        |   b        |   c        |   $        |
+-------+------------+------------+------------+------------+
|  S    |  S -> Aa   |  S -> bAc  |  S -> Bc   |            |
|  A    |  A -> d    |            |            |            |
|  B    |            |            |  B -> d    |            |
+-------+------------+------------+------------+------------+
```

LALR(1) Parsing Table:
```table
+-------+------------+------------+------------+------------+
|       |   a        |   b        |   c        |   $        |
+-------+------------+------------+------------+------------+
|  S    |  S -> Aa   |  S -> bAc  |  S -> Bc   |            |
|  A    |  A -> d    |            |            |            |
|  B    |            |            |  B -> d    |            |
+-------+------------+------------+------------+------------+
```

### Note
Steps of Construction for LR(1) and LALR(1) Parsing Tables:
1. Construct the LR(0) items for the given grammar. The LR(0) items are the
   sets of items that represent the possible configurations of the LR(0) parser.
2. Construct the LR(1) items by augmenting the LR(0) items with the look-ahead
   symbols. The look-ahead symbols are used to resolve shift-reduce and reduce-reduce conflicts.
3. Construct the LR(1) parsing table by filling in the action and go-to entries for each LR(1) item.
4. Construct the LALR(1) parsing table by merging the states of the LR(1) parsing table that have the same core items.

Augmented Form of given grammar:
```
S' -> S
S -> Aa | bAc | Bc
A -> d
B -> d
```
For production of the form [A -> α.Xβ, a], if there exists a production [X -> γ]
and a state [X -> .γ, b] in the LR(1) items, then add [A -> αX.β, a] to the LR(1)
items. [Closure]

Canonical LR(1) Items:
```
I0:
S' -> .S, $
S -> .Aa, a
S -> .bAc, c
S -> .Bc, c
A -> .d, a
B -> .d, c

I1:
S' -> S., $

I2:
S -> A.a, a

I3:
S -> b.Ac, c
A -> .d, a

I4:
S -> B.c, c

I5:
A -> d., a

I6:
B -> d., c
```

## UNIT-IV
### Question
Explain about YACC?

### Answer
YACC (Yet Another Compiler Compiler) is a tool that generates parsers for
programming languages. YACC is a parser generator that takes a grammar as input
and generates a parser that can parse the input according to the grammar.

Features of YACC:
* YACC uses a context-free grammar to specify the syntax of the programming language.
* It supports LALR(1) grammars (Look-Ahead Left-to-Right parsing with 1 token of look-ahead).
* Grammar rules are defined with production rules that describe how input strings can be derived.
* YACC generates a C program that implements a parser for the given grammar.
* The parser processes input text and validates whether it conforms to the specified grammar.
* YACC is often used alongside a lexical analyzer generator like Lex.
* Lex generates the tokenizer, which divides input into tokens, and YACC uses these tokens to build the syntax tree.
* Grammar rules in YACC can have actions, written in C, which are executed when the rule is matched.
* These actions are commonly used to build abstract syntax trees (ASTs) or perform semantic checks.
* YACC resolves shift/reduce and reduce/reduce conflicts using predefined rules (e.g., favoring shifts for shift/reduce conflicts).

### Question
Differentiate between LL and LR Parsers.

### Answer
LL Parser:
* LL parsers are top-down parsers that read input from left to right and construct a leftmost derivation of the input string.
* Characteristics of LL Parser:
    - The parser starts from the start symbol and works its way down to the input string.
    - The parser uses a set of production rules to generate the parse tree.
    - The parser uses a recursive descent or predictive parsing technique.
    - The parser may backtrack if it encounters a conflict in the grammar.
* Advantages of LL Parser:
    - Easy to implement and debug.
    - Suitable for LL(1) grammars.
    - Can be used for syntax-directed translation.
* Disadvantages of LL Parser:
    - Cannot handle left-recursive grammars.
    - May require backtracking for ambiguous grammars.
    - Limited lookahead may lead to conflicts.

LR Parser:
* LR parsers are bottom-up parsers that read input from left to right and construct a rightmost derivation of the input string.
* Characteristics of LR Parser:
    - The parser starts from the input string and works its way up to the start symbol.
    - The parser uses a deterministic pushdown automaton to generate the parse tree.
    - The parser uses a shift-reduce technique to reduce the input string to the start symbol.
    - The parser may use LR(0), SLR, LALR, or CLR parsing techniques.
* Advantages of LR Parser:
    - Can handle left-recursive grammars.
    - Suitable for a wide range of grammars.
    - Can handle a larger class of languages.

### Question
What is meant by three address code? Different types of three
address code techniques with examples?

### Answer
Three-address code is an intermediate representation of code that uses at most
three operands per instruction. Each instruction in a three-address code performs
a single operation on two or three operands and produces a result.

Types of Three-Address Code Techniques:
1. Quadruples:
    Quadruples are a simple form of three-address code that uses four fields
    to represent an instruction. The fields are:
    - Operator: The operation to be performed.
    - Operand1: The first operand.
    - Operand2: The second operand.
    - Result: The result of the operation.
    Example:
    ```
    +, a, b, t1
    *, t1, c, t2
    =, t2, _, x
    ```
2. Triples:
    Triples are a more compact form of three-address code that uses three fields
    to represent an instruction. The fields are:
    - Operator: The operation to be performed.
    - Operand1: The first operand.
    - Operand2: The second operand.
    Example:
    ```
    +, a, b
    *, t1, c
    =, x, t2
    ```
3. Indirect Triples:
    Indirect triples are a form of three-address code that uses three fields
    to represent an instruction. The fields are:
    - Operator: The operation to be performed.
    - Operand1: The first operand.
    - Operand2: The second operand.
    Here, references to the instructions instead of the stored values
    Example:
    ```
    +, t1,t2
    *, t1, c
    =, x, t2
    ```

### Question
Explain synthesized and inherited attributes with an example?

### Answer
Synthesized Attributes:
Synthesized attributes are attributes that are computed bottom-up. They are
computed from the values of the attributes of the child nodes in the parse
tree. These attributes are passed from the leaves of the tree to the root.
* Purpose: They are typically used to represent information that is derived
  from the children of a node in the syntax tree.
* Computation: Synthesized attributes are computed by the semantic rules
  associated with the grammar's production rules.
* Example:
  Consider the following grammar:
  ```
  E -> E + T | T
  T -> T * F | F
  F -> ( E ) | id
  ```
  Synthesized attributes can be used to compute the value of an expression.
  ```
  E -> E1 + T2 { E.val = E1.val + T2.val }
  E -> T1 { E.val = T1.val }
  T -> T1 * F2 { T.val = T1.val * F2.val }
  T -> F1 { T.val = F1.val }
  F -> ( E1 ) { F.val = E1.val }
  F -> id { F.val = id.val }
  ```

Inherited Attributes:
Inherited attributes are attributes that are computed top-down. They are passed
from the parent node to the child nodes in the syntax tree. These attributes
carry information that needs to be passed down from the root of the tree to its
subtrees.

* Purpose: They are used to represent information that needs to be passed from
  the parent to the children, such as context-sensitive information.
* Computation: Inherited attributes are computed based on the values of the
  parent node or neighboring nodes.
* Example:
  Consider the following grammar:
  ```
  E -> E + T | T
  T -> T * F
  F -> ( E ) | id
  ```
  Inherited attributes can be used to pass context information from the parent
  to the children.
  ```
  E -> E1 + T2 { E.type = E1.type; T1.type = T2.type }
  E -> T1 { E.type = T1.type }
  T -> T1 * F2 { T.type = T1.type; F2.type = F2.type }
  F -> ( E1 ) { F.type = E1.type }
  F -> id { F.type = id.type }
  ```