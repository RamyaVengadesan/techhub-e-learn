"""JavaScript module lessons for TechHub. Same schema as the other modules:
slug, title, group, intro, sections[{h, p, code?}], example, tip (optional), exercise[{q, options, answer}].

Examples run live in a sandboxed iframe (scripts allowed) with a console shim, so they use
console.log and DOM output only: no alert/prompt, no storage, no network.
"""

GROUPS = ["Getting Started", "Control Flow", "Functions", "Strings & Numbers", "Arrays & Objects",
          "The DOM", "Events & Timers", "Asynchronous JavaScript", "Modern JavaScript", "Best Practices"]


def L(slug, title, group, intro, sections, example, tip=None, exercise=()):
    d = dict(slug=slug, title=title, group=group, intro=intro,
             sections=[dict(h=s[0], p=s[1], **({"code": s[2]} if len(s) > 2 else {})) for s in sections],
             example=example)
    if tip:
        d["tip"] = tip
    d["exercise"] = [dict(q=q, options=o, answer=a) for q, o, a in exercise]
    return d


LESSONS = [
# ============================================================ Getting Started
L("js-intro", "JavaScript Introduction", "Getting Started",
  "JavaScript is the programming language of the web. It makes pages react to clicks, update content and talk to servers.",
  [("What is JavaScript?", "JavaScript is a programming language that runs in every web browser. HTML gives a page structure, CSS styles it, and JavaScript adds behaviour such as menus, form checks, animations and live updates."),
   ("Where does it run?", "Browsers have a built-in JavaScript engine. The same language also runs outside the browser, for example on servers with Node.js. In this course every example runs right here in your browser."),
   ("Your first script", "A script is plain text placed inside a `<script>` element. The browser runs it from top to bottom.",
    '<p id="out"></p>\n<script>\n  document.getElementById("out").textContent = "Hello from JavaScript!";\n</script>')],
  '''<h2 id="title">Waiting...</h2>
<script>
  document.getElementById("title").textContent = "Hello from JavaScript!";
  console.log("The script ran successfully");
</script>''',
  "JavaScript and Java are different languages. The similar name is a historical accident.",
  [("Which language adds behaviour such as clicks and live updates to a web page?", ["JavaScript", "CSS", "HTML", "Markdown"], 0),
   ("Which element holds JavaScript code inside an HTML page?", ["<script>", "<js>", "<code>", "<style>"], 0)]),

L("js-where-to", "JavaScript Where To", "Getting Started",
  "You can put JavaScript inside the page or in a separate file. Where you place it affects when it runs.",
  [("Internal script", "Put code between `<script>` and `</script>` in the HTML. It can go in the head or the body.",
    '<script>\n  console.log("Internal script");\n</script>'),
   ("External script", "Save code in a `.js` file and load it with the `src` attribute. One file can be shared by many pages and the browser can cache it.",
    '<script src="app.js"></script>'),
   ("Placement matters", "A script runs as soon as the browser reaches it. If it needs elements that come later in the page, put it at the end of `<body>`, or add the `defer` attribute so it waits until the HTML is parsed.",
    '<script src="app.js" defer></script>')],
  '''<p id="msg">Before the script</p>
<script>
  // This script is after the paragraph, so the paragraph already exists.
  var p = document.getElementById("msg");
  p.textContent = "The script found this paragraph because it runs after it.";
</script>''',
  "Prefer external files with `defer` for real projects. They keep HTML tidy and scripts cacheable.",
  [("Which attribute loads an external JavaScript file?", ["src", "href", "link", "file"], 0),
   ("What does the defer attribute do on a script?", ["Runs it after the HTML has been parsed", "Stops it from running", "Runs it twice", "Makes it load from the server only"], 0),
   ("Why do scripts often go at the end of the body?", ["The elements they use already exist", "Browsers ignore scripts in the head", "It makes the code shorter", "It is required by the language"], 0)]),

L("js-output", "JavaScript Output", "Getting Started",
  "JavaScript can show results in several ways. Knowing which to use makes your code easier to test and safer.",
  [("console.log()", "Writes a message to the browser console. It is the main tool for testing and debugging. In this tutorial the console output appears under the result.",
    'console.log("Hello", 42, [1, 2, 3]);'),
   ("Changing the page", "Use `textContent` to put plain text into an element, or `innerHTML` to put HTML. Prefer `textContent` when the text may come from a user, because `innerHTML` can run unwanted markup.",
    'document.getElementById("out").textContent = "Done";'),
   ("document.write()", "`document.write()` writes into the page while it loads. After the page has loaded it erases everything. Avoid it in real code.")],
  '''<div id="box"></div>
<script>
  console.log("1. Written to the console");
  console.log("Numbers and arrays:", 7, [1, 2, 3]);
  document.getElementById("box").textContent = "2. Written into the page with textContent";
</script>''',
  "Alerts and prompts are blocked in this tutorial's preview, so use `console.log` or the page itself to show results.",
  [("Which method writes a message to the browser console?", ["console.log()", "window.print()", "document.say()", "page.write()"], 0),
   ("Which property is safest for inserting plain text into an element?", ["textContent", "innerHTML", "outerHTML", "document.write"], 0)]),

L("js-syntax", "JavaScript Syntax", "Getting Started",
  "Syntax is the set of rules for writing valid JavaScript. A few basics cover most of what you will read and write.",
  [("Statements", "A program is a list of statements. Each statement is an instruction, and statements are normally ended with a semicolon.",
    'let a = 5;\nlet b = 6;\nlet c = a + b;'),
   ("Case sensitive", "JavaScript treats upper and lower case as different. `myVar`, `myvar` and `MyVar` are three different names."),
   ("Identifiers and naming", "Names can contain letters, digits, `_` and `$`, and cannot start with a digit. The common style is camelCase, such as `firstName`."),
   ("Whitespace", "Extra spaces and blank lines are ignored. Use them to make code readable.")],
  '''<pre id="out"></pre>
<script>
  let firstName = "Asha";
  let FirstName = "Ravi";   // a different variable
  let total = 4 + 6;
  document.getElementById("out").textContent =
    firstName + " and " + FirstName + " are different.\\nTotal: " + total;
</script>''',
  "Pick one style, such as camelCase for variables and functions, and use it everywhere.",
  [("Are `score` and `Score` the same variable in JavaScript?", ["No, JavaScript is case sensitive", "Yes, case is ignored", "Only inside functions", "Only with let"], 0),
   ("Which of these is a valid variable name?", ["total_2", "2total", "my-total", "my total"], 0)]),

L("js-comments", "JavaScript Comments", "Getting Started",
  "Comments are notes for people. The browser ignores them, so you can explain code or switch lines off temporarily.",
  [("Single-line comments", "Everything after two slashes on a line is a comment.", '// This is a comment\nlet x = 5; // so is this'),
   ("Multi-line comments", "Everything between `/*` and `*/` is a comment, even across many lines.", '/* This comment\n   spans two lines */'),
   ("Disabling code", "Putting `//` in front of a line stops it running without deleting it. This is handy while testing.")],
  '''<script>
  // console.log("This line is switched off");
  console.log("Only this line runs");
  /* Multi-line
     comment: ignored too */
</script>''',
  "Good comments explain why the code does something, not what it obviously does.",
  [("Which symbol starts a single-line comment in JavaScript?", ["//", "<!--", "#", "--"], 0),
   ("What do multi-line comments start and end with?", ["/* and */", "// and //", "<!-- and -->", "## and ##"], 0)]),

L("js-variables", "JavaScript Variables", "Getting Started",
  "Variables are named containers for values. Modern JavaScript has three ways to declare them: `let`, `const` and `var`.",
  [("let", "Use `let` for a value that will change later. It is limited to the block where it is declared.", 'let score = 0;\nscore = score + 10;'),
   ("const", "Use `const` for a value that will not be reassigned. You must give it a value when you declare it. Objects and arrays declared with `const` can still have their contents changed.", 'const pi = 3.14159;\n// pi = 3; would throw an error'),
   ("var", "`var` is the old way. It ignores block scope and is hoisted, which causes surprises. Prefer `let` and `const` in new code."),
   ("Default to const", "A good habit: start with `const`, and switch to `let` only when you need to reassign.")],
  '''<pre id="out"></pre>
<script>
  let score = 0;
  score = score + 10;
  const player = "Asha";
  let text = player + " has " + score + " points";
  console.log(text);
  try {
    player = "Ravi";
  } catch (e) {
    console.log("Cannot reassign a const: " + e.name);
  }
  document.getElementById("out").textContent = text;
</script>''',
  "If you never reassign a variable, `const` tells readers (and tools) that it will not change.",
  [("Which keyword declares a variable that cannot be reassigned?", ["const", "let", "var", "static"], 0),
   ("Which keyword should you generally avoid in new code?", ["var", "let", "const", "function"], 0),
   ("What happens if you assign a new value to a const variable?", ["A TypeError is thrown", "The value changes silently", "The old value is kept without error", "The page reloads"], 0)]),

L("js-data-types", "JavaScript Data Types", "Getting Started",
  "Every value has a type. Knowing the types helps you predict how operators and functions behave.",
  [("Primitive types", "The primitives are string, number, bigint, boolean, undefined, null and symbol. They hold a single simple value.",
    'let name = "Asha";   // string\nlet age = 21;        // number\nlet ok = true;       // boolean\nlet nothing = null;  // null\nlet notSet;          // undefined'),
   ("Objects", "Everything else is an object: plain objects, arrays, functions, dates and more. Objects hold collections of values.",
    'let person = { name: "Asha", age: 21 };\nlet list = [1, 2, 3];'),
   ("typeof", "The `typeof` operator tells you the type of a value as a string. Note that `typeof null` returns `object`, which is a long-standing quirk.")],
  '''<script>
  const values = ["text", 42, true, undefined, null, [1, 2], { a: 1 }, function () {}];
  values.forEach(function (v) {
    console.log(String(typeof v).padEnd(10), "->", Array.isArray(v) ? "array" : JSON.stringify(v));
  });
</script>''',
  "Use `Array.isArray(value)` to test for arrays, since `typeof` reports arrays as `object`.",
  [("What does typeof 42 return?", ["number", "integer", "numeric", "digit"], 0),
   ("Which value does typeof report as object even though it is not one?", ["null", "undefined", "true", "NaN"], 0),
   ("Which of these is a primitive type?", ["string", "array", "function", "date"], 0)]),

L("js-operators", "JavaScript Operators", "Getting Started",
  "Operators perform actions on values: arithmetic, assignment, comparison and logic.",
  [("Arithmetic", "`+`, `-`, `*`, `/` work as expected. `%` gives the remainder and `**` raises to a power. `++` and `--` add or subtract one.",
    'let a = 10, b = 3;\nconsole.log(a + b, a % b, a ** b);'),
   ("Assignment", "`=` stores a value. Shortcuts such as `+=`, `-=` and `*=` update a variable in one step.", 'let n = 5;\nn += 2; // 7'),
   ("Logical", "`&&` means and, `||` means or, `!` means not. They are used to combine conditions."),
   ("String joining", "The `+` operator joins strings. If one side is a string, the other side is converted to text.")],
  '''<script>
  let a = 10, b = 3;
  console.log("a + b =", a + b);
  console.log("a % b =", a % b);
  console.log("a ** b =", a ** b);
  let n = 5;
  n += 2;
  console.log("n after += 2:", n);
  console.log("true && false =", true && false);
  console.log("true || false =", true || false);
  console.log("Joined:", "Java" + "Script");
</script>''',
  "`%` is handy for even/odd checks: `n % 2 === 0` is true when `n` is even.",
  [("Which operator returns the remainder of a division?", ["%", "/", "**", "&&"], 0),
   ("What does the ** operator do?", ["Raises a number to a power", "Multiplies twice", "Divides twice", "Joins two strings"], 0)]),

L("js-type-conversion", "JavaScript Type Conversion", "Getting Started",
  "JavaScript converts between types, sometimes automatically. Converting on purpose avoids surprises.",
  [("Explicit conversion", "Use `Number()`, `String()` and `Boolean()` to convert on purpose. `parseInt()` and `parseFloat()` read numbers from the start of a string.",
    'Number("42");      // 42\nString(42);        // "42"\nparseInt("10px");  // 10'),
   ("Automatic conversion", "Operators convert types when needed. `+` with a string joins text, but `-`, `*` and `/` turn strings into numbers.",
    '"5" + 2;  // "52"\n"5" - 2;  // 3'),
   ("Truthy and falsy", "In a condition, these values count as false: `false`, `0`, `\"\"`, `null`, `undefined` and `NaN`. Everything else is true.")],
  '''<script>
  console.log('"5" + 2  =', "5" + 2);
  console.log('"5" - 2  =', "5" - 2);
  console.log("Number('42') =", Number("42"));
  console.log("Number('abc') =", Number("abc"));
  console.log("parseInt('10px') =", parseInt("10px"));
  console.log("Boolean('') =", Boolean(""));
  console.log("Boolean('hi') =", Boolean("hi"));
</script>''',
  "Form fields always give you strings. Convert with `Number()` before doing maths.",
  [("What does the expression \"5\" + 2 produce?", ["\"52\"", "7", "\"7\"", "NaN"], 0),
   ("Which value is falsy?", ["0", "\"0\"", "[]", "\"false\""], 0)]),

L("js-comparison", "JavaScript Comparison", "Getting Started",
  "Comparison operators produce true or false. The difference between `==` and `===` is one of the most important rules in JavaScript.",
  [("Strict equality", "`===` compares value and type. `5 === \"5\"` is false. Use it almost always.", 'console.log(5 === "5"); // false'),
   ("Loose equality", "`==` converts types before comparing, so `5 == \"5\"` is true. The conversion rules are surprising, so avoid `==` in most code.", 'console.log(5 == "5"); // true'),
   ("Other operators", "`!==` means not strictly equal. `>`, `<`, `>=` and `<=` compare order.")],
  '''<script>
  console.log("5 === '5'  ->", 5 === "5");
  console.log("5 == '5'   ->", 5 == "5");
  console.log("5 !== '5'  ->", 5 !== "5");
  console.log("10 > 9     ->", 10 > 9);
  console.log("'10' > '9' ->", "10" > "9", "(text compares letter by letter)");
  console.log("NaN === NaN ->", NaN === NaN);
  console.log("Number.isNaN(NaN) ->", Number.isNaN(NaN));
</script>''',
  "NaN is never equal to anything, even itself. Test for it with `Number.isNaN()`.",
  [("What does 5 === \"5\" evaluate to?", ["false", "true", "undefined", "an error"], 0),
   ("Which operator compares both value and type?", ["===", "==", "=", "=>"], 0),
   ("How do you reliably test whether a value is NaN?", ["Number.isNaN(value)", "value === NaN", "value == NaN", "typeof value === \"nan\""], 0)]),

# ============================================================ Control Flow
L("js-if-else", "JavaScript If...Else", "Control Flow",
  "Conditions let your program make decisions. The `if` statement runs code only when a condition is true.",
  [("if, else if, else", "Test conditions in order. The first one that is true runs, and the rest are skipped.",
    'if (score >= 90) {\n  grade = "A";\n} else if (score >= 80) {\n  grade = "B";\n} else {\n  grade = "C";\n}'),
   ("Ternary operator", "A short form for a simple choice: `condition ? valueIfTrue : valueIfFalse`.", 'let label = age >= 18 ? "Adult" : "Minor";'),
   ("Combining conditions", "Use `&&` (and) and `||` (or) to test more than one thing at once.")],
  '''<script>
  function grade(score) {
    if (score >= 90) return "A";
    else if (score >= 80) return "B";
    else if (score >= 70) return "C";
    return "Needs work";
  }
  [95, 84, 72, 40].forEach(function (s) {
    console.log(s + " -> " + grade(s));
  });
  const age = 20;
  console.log(age >= 18 ? "Adult" : "Minor");
</script>''',
  "Always use curly braces, even for one-line bodies. It prevents mistakes when you add a second line later.",
  [("Which keyword runs code when the first condition is false?", ["else", "then", "otherwise", "elif"], 0),
   ("What is the ternary operator form?", ["condition ? a : b", "condition then a else b", "if condition a b", "condition => a : b"], 0)]),

L("js-switch", "JavaScript Switch", "Control Flow",
  "A `switch` statement compares one value against many cases. It is tidier than a long chain of `else if`.",
  [("How it works", "The value is compared with each `case` using strict equality. When one matches, its code runs.",
    'switch (day) {\n  case 0:\n    name = "Sunday";\n    break;\n  case 6:\n    name = "Saturday";\n    break;\n  default:\n    name = "Weekday";\n}'),
   ("break", "Without `break`, execution falls through into the next case. Add `break` at the end of each case unless you want that."),
   ("default", "The `default` block runs when no case matches.")],
  '''<script>
  function dayType(day) {
    switch (day) {
      case 0:
      case 6:
        return "Weekend";
      case 5:
        return "Almost weekend";
      default:
        return "Weekday";
    }
  }
  [0, 3, 5, 6].forEach(function (d) { console.log("Day " + d + ": " + dayType(d)); });
</script>''',
  "Stacking cases with no code between them, like `case 0:` and `case 6:` above, lets several values share one result.",
  [("What happens if a switch case has no break?", ["Execution continues into the next case", "The switch stops with an error", "The default block runs first", "The case is skipped"], 0),
   ("Which block of a switch runs when no case matches?", ["default", "else", "otherwise", "finally"], 0)]),

L("js-loops", "JavaScript Loops", "Control Flow",
  "Loops repeat code. Pick the loop that matches what you are doing.",
  [("for loop", "Best when you know how many times to repeat. It has an initialiser, a condition and an update.",
    'for (let i = 0; i < 3; i++) {\n  console.log(i);\n}'),
   ("while and do...while", "`while` repeats as long as a condition is true. `do...while` always runs the body once before checking.",
    'let n = 3;\nwhile (n > 0) {\n  n--;\n}'),
   ("for...of", "Loops over the values of an array, string, Set or Map.", 'for (const fruit of ["apple", "pear"]) {\n  console.log(fruit);\n}'),
   ("for...in", "Loops over the property names of an object.", 'for (const key in { a: 1, b: 2 }) {\n  console.log(key);\n}')],
  '''<script>
  for (let i = 1; i <= 3; i++) console.log("for: " + i);

  let n = 3;
  while (n > 0) { console.log("while: " + n); n--; }

  for (const fruit of ["apple", "pear", "plum"]) console.log("for...of: " + fruit);

  const user = { name: "Asha", age: 21 };
  for (const key in user) console.log("for...in: " + key + " = " + user[key]);
</script>''',
  "Use `for...of` for arrays and `for...in` for object keys. Avoid `for...in` on arrays.",
  [("Which loop iterates over the values of an array?", ["for...of", "for...in", "while", "do...while"], 0),
   ("Which loop always runs its body at least once?", ["do...while", "while", "for...of", "for...in"], 0),
   ("What does for...in loop over?", ["Property names of an object", "Values of a Set", "Characters of a number", "Lines of a file"], 0)]),

L("js-break-continue", "JavaScript Break and Continue", "Control Flow",
  "`break` and `continue` give you finer control inside loops.",
  [("break", "Stops the loop completely and continues with the code after it.", 'for (let i = 0; i < 10; i++) {\n  if (i === 3) break;\n}'),
   ("continue", "Skips the rest of the current pass and jumps to the next one.", 'for (let i = 0; i < 5; i++) {\n  if (i === 2) continue;\n  console.log(i);\n}'),
   ("Labels", "A label lets you break out of an outer loop from inside an inner one. It is rarely needed.")],
  '''<script>
  for (let i = 0; i < 10; i++) {
    if (i === 2) continue;   // skip 2
    if (i === 5) break;      // stop at 5
    console.log("i = " + i);
  }
  console.log("Loop finished");
</script>''',
  None,
  [("Which statement skips the current loop iteration and moves to the next?", ["continue", "break", "skip", "next"], 0),
   ("Which statement ends a loop immediately?", ["break", "continue", "return false", "stop"], 0)]),

# ============================================================ Functions
L("js-functions", "JavaScript Functions", "Functions",
  "A function is a reusable block of code. You define it once and call it as many times as you like.",
  [("Declaring a function", "Use the `function` keyword, a name, parameters in parentheses and a body in braces.",
    'function greet(name) {\n  return "Hello, " + name + "!";\n}'),
   ("Calling it", "Write the name followed by parentheses. The `return` statement sends a value back. A function without `return` gives back `undefined`.", 'greet("Asha"); // "Hello, Asha!"'),
   ("Function expressions", "A function can also be stored in a variable. It is not available before the line that defines it.", 'const square = function (n) {\n  return n * n;\n};')],
  '''<script>
  function greet(name) {
    return "Hello, " + name + "!";
  }
  const square = function (n) { return n * n; };

  console.log(greet("Asha"));
  console.log(greet("Ravi"));
  console.log("5 squared is", square(5));
</script>''',
  "Give functions verb names such as `calculateTotal` so calls read like sentences.",
  [("Which keyword sends a value back from a function?", ["return", "send", "yield", "output"], 0),
   ("What does a function return if it has no return statement?", ["undefined", "null", "0", "an empty string"], 0)]),

L("js-arrow-functions", "JavaScript Arrow Functions", "Functions",
  "Arrow functions are a shorter way to write functions, introduced in ES6.",
  [("Syntax", "Write the parameters, then `=>`, then the body. If the body is a single expression it is returned automatically.",
    'const add = (a, b) => a + b;\nconst double = n => n * 2;'),
   ("Block bodies", "Use braces for several statements. Then you need an explicit `return`.", 'const area = (w, h) => {\n  const result = w * h;\n  return result;\n};'),
   ("Where they shine", "Arrow functions are ideal for short callbacks such as `map` and `filter`. They also do not have their own `this`, which is covered in the `this` lesson.")],
  '''<script>
  const add = (a, b) => a + b;
  const double = n => n * 2;
  const area = (w, h) => {
    const result = w * h;
    return result;
  };
  console.log("add(2, 3) =", add(2, 3));
  console.log("double(8) =", double(8));
  console.log("area(4, 5) =", area(4, 5));
  console.log([1, 2, 3].map(n => n * 10));
</script>''',
  None,
  [("What does the arrow function n => n * 2 return for n = 4?", ["8", "6", "4", "undefined"], 0),
   ("When must an arrow function use an explicit return?", ["When its body is wrapped in braces", "When it has one parameter", "When it is used in map", "Always"], 0)]),

L("js-parameters", "JavaScript Function Parameters", "Functions",
  "Parameters make functions flexible. JavaScript lets you set defaults and gather extra arguments.",
  [("Default values", "A parameter can have a default that is used when the argument is missing or `undefined`.", 'function greet(name = "friend") {\n  return "Hi " + name;\n}'),
   ("Rest parameters", "`...args` collects any number of extra arguments into a real array.", 'function sum(...nums) {\n  return nums.reduce((a, b) => a + b, 0);\n}'),
   ("Arguments are copied", "Numbers and strings are passed by value. Objects and arrays are passed by reference, so a function can change their contents.")],
  '''<script>
  function greet(name = "friend") { return "Hi " + name; }
  function sum(...nums) { return nums.reduce((a, b) => a + b, 0); }
  function addItem(list) { list.push("new"); }

  console.log(greet());
  console.log(greet("Asha"));
  console.log("sum =", sum(1, 2, 3, 4));
  const items = ["a"];
  addItem(items);
  console.log("array changed by function:", items);
</script>''',
  None,
  [("What do rest parameters (...args) collect arguments into?", ["An array", "A string", "An object", "A number"], 0),
   ("When is a default parameter value used?", ["When the argument is undefined", "Only when the argument is null", "Always", "Only for numbers"], 0)]),

L("js-scope", "JavaScript Scope", "Functions",
  "Scope decides where a variable can be used. Understanding it prevents many bugs.",
  [("Global scope", "A variable declared outside any function or block is global and can be used anywhere. Too many globals make code hard to manage."),
   ("Function and block scope", "Variables declared inside a function are local to it. `let` and `const` are also limited to the block `{ }` they are written in; `var` is not.",
    'if (true) {\n  let inside = 1;\n  var leaky = 2;\n}\n// inside is not defined here\n// leaky is still available'),
   ("Scope chain", "When you use a name, JavaScript looks in the current scope, then in the outer scopes, until it finds it.")],
  '''<script>
  const outer = "I am global";
  function show() {
    const inner = "I am local";
    console.log(outer, "|", inner);
  }
  show();

  if (true) {
    let blockLet = 1;
    var blockVar = 2;
  }
  console.log("var leaks out of the block:", blockVar);
  console.log("let does not:", typeof blockLet);
</script>''',
  "Declare variables in the smallest scope that works.",
  [("Where is a variable declared with let inside curly braces available?", ["Only inside that block", "Everywhere in the page", "Only in the next function", "Only after the block ends"], 0),
   ("Which keyword does not respect block scope?", ["var", "let", "const", "class"], 0)]),

L("js-hoisting", "JavaScript Hoisting", "Functions",
  "Hoisting is JavaScript moving declarations to the top of their scope before the code runs.",
  [("Function declarations", "Function declarations are hoisted completely, so you can call them before they appear in the file.", 'sayHi();\nfunction sayHi() { console.log("Hi"); }'),
   ("var is hoisted", "A `var` variable is hoisted but its value is not. Before the assignment it is `undefined`.", 'console.log(a); // undefined\nvar a = 5;'),
   ("let and const", "`let` and `const` are hoisted too, but cannot be used before their declaration. Doing so throws a ReferenceError (the temporal dead zone).")],
  '''<script>
  sayHi();                       // works: function declaration is hoisted
  function sayHi() { console.log("Hi from a hoisted function"); }

  console.log("var before assignment:", typeof a, a);
  var a = 5;

  try {
    console.log(b);
    let b = 1;
  } catch (e) {
    console.log("let before declaration:", e.name);
  }
</script>''',
  "Hoisting is a good reason to declare variables at the top and use `let` and `const`.",
  [("What value does a var variable have before its assignment line runs?", ["undefined", "null", "0", "It throws an error"], 0),
   ("Which declarations can be called before they appear in the code?", ["Function declarations", "let variables", "const variables", "Arrow functions in variables"], 0)]),

L("js-closures", "JavaScript Closures", "Functions",
  "A closure is a function that remembers the variables from where it was created, even after that outer function has finished.",
  [("A counter example", "The inner function keeps access to `count`, but nothing outside can touch it directly.",
    'function makeCounter() {\n  let count = 0;\n  return function () {\n    count++;\n    return count;\n  };\n}'),
   ("Why they matter", "Closures give you private data, factory functions and the memory that makes callbacks and event handlers work."),
   ("Separate copies", "Each call to the outer function creates a new, independent set of variables.")],
  '''<script>
  function makeCounter() {
    let count = 0;
    return function () {
      count++;
      return count;
    };
  }
  const a = makeCounter();
  const b = makeCounter();
  console.log("a:", a(), a(), a());
  console.log("b:", b());
</script>''',
  "If you can write a counter with a closure, you understand closures.",
  [("What does a closure remember?", ["Variables from the scope where it was created", "Every global variable ever used", "Only its parameters", "The HTML of the page"], 0),
   ("Do two counters made by calling makeCounter twice share one count?", ["No, each has its own", "Yes, they share it", "Only inside loops", "Only if declared with var"], 0)]),

L("js-callbacks", "JavaScript Callbacks", "Functions",
  "A callback is a function passed to another function so that it can be called later.",
  [("Functions are values", "In JavaScript a function can be stored in a variable, passed as an argument and returned from another function."),
   ("A simple callback", "The function `repeat` below calls whatever function it is given.",
    'function repeat(times, action) {\n  for (let i = 0; i < times; i++) action(i);\n}\nrepeat(3, i => console.log(i));'),
   ("Everywhere in JS", "Array methods like `forEach` and `map`, event handlers and timers all take callbacks.")],
  '''<script>
  function repeat(times, action) {
    for (let i = 0; i < times; i++) action(i);
  }
  repeat(3, function (i) { console.log("Callback called with " + i); });

  [10, 20].forEach(n => console.log("forEach got " + n));
</script>''',
  None,
  [("What is a callback function?", ["A function passed to another function to be called later", "A function that calls itself", "A function with no parameters", "A function stored in a file"], 0),
   ("Which of these takes a callback?", ["Array.forEach", "Math.PI", "typeof", "String.length"], 0)]),

L("js-recursion", "JavaScript Recursion", "Functions",
  "A recursive function calls itself. It needs a base case so that it eventually stops.",
  [("Base case and recursive case", "The base case returns without calling itself. The recursive case calls the function again on a smaller problem.",
    'function factorial(n) {\n  if (n <= 1) return 1;\n  return n * factorial(n - 1);\n}'),
   ("When to use it", "Recursion suits problems that repeat on smaller parts, such as trees and nested data. A loop is often simpler for plain counting."),
   ("Stack limit", "Every call uses memory. Recursion without a base case runs until the browser throws a RangeError.")],
  '''<script>
  function factorial(n) {
    if (n <= 1) return 1;      // base case
    return n * factorial(n - 1);
  }
  function countdown(n) {
    if (n === 0) { console.log("Liftoff!"); return; }
    console.log(n);
    countdown(n - 1);
  }
  console.log("5! =", factorial(5));
  countdown(3);
</script>''',
  "Always write the base case first.",
  [("What stops a recursive function from running forever?", ["A base case", "The return keyword alone", "A global variable", "A semicolon"], 0),
   ("What is 4 factorial?", ["24", "10", "16", "12"], 0)]),

L("js-this", "JavaScript this Keyword", "Functions",
  "`this` refers to the object that is using the function. Its value depends on how the function is called.",
  [("In an object method", "When a function is called as `object.method()`, `this` is that object.", 'const user = {\n  name: "Asha",\n  hi() { return "Hi " + this.name; }\n};'),
   ("Arrow functions", "Arrow functions do not have their own `this`. They use the `this` of the surrounding code, which makes them good for callbacks inside methods."),
   ("Losing this", "If you pull a method out and call it alone, `this` is no longer the object. Use `bind` or an arrow function to fix it.")],
  '''<script>
  const user = {
    name: "Asha",
    hi() { return "Hi " + this.name; }
  };
  console.log(user.hi());

  const loose = user.hi;
  console.log("Detached:", loose.call({ name: "Someone else" }));

  const bound = user.hi.bind(user);
  console.log("Bound:", bound());
</script>''',
  "If `this` is `undefined` or wrong, check how the function was called, not where it was written.",
  [("In obj.method(), what does this refer to inside the method?", ["obj", "window always", "The method itself", "undefined always"], 0),
   ("Which kind of function does not have its own this?", ["Arrow function", "Function declaration", "Method", "Constructor"], 0)]),

# ============================================================ Strings & Numbers
L("js-strings", "JavaScript Strings", "Strings & Numbers",
  "Strings hold text. They are written in single quotes, double quotes or backticks.",
  [("Creating strings", "Single and double quotes work the same. Use a backslash to include special characters such as a quote or a new line (`\\n`).",
    'let a = "Hello";\nlet b = \'World\';\nlet c = "She said \\"hi\\"";'),
   ("Length and characters", "`length` gives the number of characters. Square brackets read one character by its position, starting at 0.", 'let s = "Code";\ns.length; // 4\ns[0];     // "C"'),
   ("Strings are immutable", "You cannot change a character in place. String methods return a new string and leave the original unchanged.")],
  '''<script>
  const s = "JavaScript";
  console.log("length:", s.length);
  console.log("first letter:", s[0]);
  console.log("last letter:", s[s.length - 1]);
  console.log("quotes:", "She said \\"hi\\"", 'It\\'s fine');
  console.log("joined:", "Java" + "Script");
  s[0] = "X";            // silently ignored
  console.log("unchanged:", s);
</script>''',
  "The first character is at index 0, so the last is at `length - 1`.",
  [("What is the index of the first character in a string?", ["0", "1", "-1", "It depends on the string"], 0),
   ("Can you change one character of a string in place with s[0] = \"X\"?", ["No, strings are immutable", "Yes, always", "Only with var", "Only for short strings"], 0)]),

L("js-string-methods", "JavaScript String Methods", "Strings & Numbers",
  "Strings come with many built-in methods for searching, slicing and transforming text.",
  [("Changing case and trimming", "`toUpperCase()`, `toLowerCase()` and `trim()` each return a new string.", '"  Hi ".trim().toUpperCase(); // "HI"'),
   ("Searching", "`includes()`, `startsWith()` and `endsWith()` return true or false. `indexOf()` returns the position, or -1 if not found.", '"banana".indexOf("na"); // 2'),
   ("Extracting and replacing", "`slice(start, end)` takes part of a string. `replace()` swaps the first match and `replaceAll()` swaps all of them.", '"banana".slice(0, 3); // "ban"'),
   ("Splitting and repeating", "`split()` turns a string into an array. `repeat()` repeats it. `padStart()` pads to a length.", '"a,b,c".split(","); // ["a","b","c"]')],
  '''<script>
  const text = "  Learn JavaScript Fast  ";
  console.log(text.trim());
  console.log(text.trim().toUpperCase());
  console.log(text.includes("Java"));
  console.log("banana".indexOf("na"), "banana".lastIndexOf("na"));
  console.log("banana".slice(1, 4));
  console.log("banana".replaceAll("a", "o"));
  console.log("a,b,c".split(","));
  console.log("ha".repeat(3));
  console.log("7".padStart(3, "0"));
</script>''',
  "Methods do not change the original string. Store the result in a variable.",
  [("Which method removes spaces from both ends of a string?", ["trim()", "strip()", "cut()", "clean()"], 0),
   ("What does indexOf return when the text is not found?", ["-1", "0", "undefined", "null"], 0),
   ("Which method turns a string into an array?", ["split()", "slice()", "join()", "repeat()"], 0)]),

L("js-template-literals", "JavaScript Template Literals", "Strings & Numbers",
  "Template literals use backticks. They make it easy to build strings from variables and to write several lines.",
  [("Embedding values", "Put any expression inside a dollar sign and curly braces. It is converted to text and inserted.",
    'const name = "Asha";\nconst msg = `Hello, ${name}! 2 + 3 = ${2 + 3}`;'),
   ("Multi-line strings", "A template literal can span several lines, and the line breaks are kept.",
    'const poem = `Roses are red,\nViolets are blue`;'),
   ("Compared with +", "Template literals are easier to read than joining many pieces with `+`.")],
  '''<script>
  const name = "Asha";
  const items = 3;
  const price = 4.5;
  console.log(`Hello, ${name}!`);
  console.log(`Total: ${items * price} for ${items} items`);
  console.log(`Line one
Line two`);
</script>''',
  "Use backticks whenever you need to mix text and variables.",
  [("Which characters create a template literal?", ["Backticks", "Single quotes", "Double quotes", "Square brackets"], 0),
   ("How do you insert a variable into a template literal?", ["${variable}", "#{variable}", "{{variable}}", "%variable%"], 0)]),

L("js-numbers", "JavaScript Numbers", "Strings & Numbers",
  "JavaScript has one main number type for both whole numbers and decimals.",
  [("Integers and decimals", "`42` and `3.14` are both numbers. Very large or small values can be written in scientific notation such as `1e6`."),
   ("Floating point surprises", "Numbers are stored in binary, so some decimals are not exact. `0.1 + 0.2` is `0.30000000000000004`. For money, work in whole cents or round the result.",
    'console.log(0.1 + 0.2);'),
   ("Useful methods", "`toFixed(2)` formats to two decimals (as a string). `Number.isInteger()` and `Number.isNaN()` test values. `Number.MAX_SAFE_INTEGER` is the largest integer that is always exact."),
   ("Special values", "`NaN` means not a number, and `Infinity` appears when you divide by zero.")],
  '''<script>
  console.log("0.1 + 0.2 =", 0.1 + 0.2);
  console.log("rounded:", (0.1 + 0.2).toFixed(2));
  console.log("1e3 =", 1e3);
  console.log("10 / 0 =", 10 / 0);
  console.log("'abc' * 2 =", "abc" * 2);
  console.log("isInteger(5.0):", Number.isInteger(5.0));
  console.log("isInteger(5.5):", Number.isInteger(5.5));
  console.log("max safe integer:", Number.MAX_SAFE_INTEGER);
</script>''',
  "`toFixed()` returns a string. Wrap it in `Number()` if you need a number again.",
  [("What does 10 / 0 give in JavaScript?", ["Infinity", "An error", "0", "NaN"], 0),
   ("What does the toFixed(2) method return?", ["A string", "A boolean", "An array", "An integer"], 0)]),

L("js-math", "JavaScript Math", "Strings & Numbers",
  "The built-in `Math` object has constants and functions for common calculations.",
  [("Rounding", "`Math.round()` rounds to the nearest whole number, `Math.floor()` rounds down, `Math.ceil()` rounds up and `Math.trunc()` removes the decimals."),
   ("Min, max and power", "`Math.min()` and `Math.max()` take any number of values. `Math.pow(2, 3)` or `2 ** 3` gives 8. `Math.sqrt()` gives the square root."),
   ("Random numbers", "`Math.random()` returns a decimal from 0 up to (but not including) 1. Scale and floor it to get a whole number in a range.",
    'Math.floor(Math.random() * 6) + 1; // dice roll 1-6')],
  '''<script>
  console.log("round(4.6):", Math.round(4.6));
  console.log("floor(4.9):", Math.floor(4.9));
  console.log("ceil(4.1):", Math.ceil(4.1));
  console.log("trunc(-4.9):", Math.trunc(-4.9));
  console.log("max:", Math.max(3, 9, 5), " min:", Math.min(3, 9, 5));
  console.log("sqrt(81):", Math.sqrt(81), " 2 ** 10:", 2 ** 10);
  console.log("PI:", Math.PI);
  const roll = Math.floor(Math.random() * 6) + 1;
  console.log("A dice roll is between 1 and 6:", roll >= 1 && roll <= 6);
</script>''',
  "`Math.random()` never returns exactly 1, which is why `floor(random * 6) + 1` gives 1 to 6.",
  [("Which method rounds a number down to the nearest integer?", ["Math.floor()", "Math.ceil()", "Math.round()", "Math.abs()"], 0),
   ("What range does Math.random() return?", ["From 0 up to but not including 1", "From 1 to 10", "From 0 to 100", "From -1 to 1"], 0)]),

L("js-dates", "JavaScript Dates", "Strings & Numbers",
  "The `Date` object works with dates and times. Months are numbered from 0, which catches many beginners out.",
  [("Creating dates", "`new Date()` is the current moment. You can also give a date string or separate numbers (year, month, day).", 'const d = new Date(2026, 0, 15); // 15 January 2026'),
   ("Getting parts", "`getFullYear()`, `getMonth()` (0 to 11), `getDate()`, `getDay()` (0 is Sunday), `getHours()` and similar methods read each part."),
   ("Formatting", "`toISOString()` gives a standard text form. `toLocaleDateString()` formats for a language and region."),
   ("Differences", "Subtracting two dates gives milliseconds. Divide by 86,400,000 to get days.")],
  '''<script>
  const d = new Date(2026, 0, 15);            // 15 January 2026 (month 0 = January)
  console.log("year:", d.getFullYear());
  console.log("month index:", d.getMonth());
  console.log("day of month:", d.getDate());
  console.log("day of week (0 = Sunday):", d.getDay());
  const start = new Date(2026, 0, 1);
  const end = new Date(2026, 0, 31);
  console.log("days between:", (end - start) / 86400000);
  console.log(new Date("2026-03-05T00:00:00Z").toISOString());
</script>''',
  "To avoid time zone confusion, store and compare dates using `toISOString()` or timestamps from `Date.now()`.",
  [("What number does getMonth() return for January?", ["0", "1", "12", "-1"], 0),
   ("What does subtracting one Date from another give?", ["Milliseconds", "Days", "Seconds", "A new Date"], 0)]),

L("js-regexp", "JavaScript Regular Expressions", "Strings & Numbers",
  "A regular expression (regex) describes a pattern of text. It is used to search, test and replace.",
  [("Writing a pattern", "A regex literal sits between slashes. Flags follow the closing slash: `i` ignores case and `g` finds every match.", 'const pattern = /cat/i;'),
   ("Testing and matching", "`pattern.test(text)` returns true or false. `text.match(pattern)` returns the matches. `text.replace(pattern, newText)` swaps them.", '/\\d+/.test("Room 42"); // true'),
   ("Common symbols", "`\\d` is a digit, `\\w` is a word character, `.` is any character, `+` means one or more, `*` means zero or more, `^` is the start and `$` is the end.")],
  '''<script>
  console.log(/cat/i.test("A Cat sat"));
  console.log("Room 42, floor 7".match(/\\d+/g));
  console.log("2026-03-05".replace(/-/g, "/"));
  const email = /^[\\w.]+@[\\w.]+\\.\\w+$/;
  console.log("asha@example.com valid?", email.test("asha@example.com"));
  console.log("not an email valid?", email.test("not an email"));
</script>''',
  "Regex is powerful but hard to read. Add a short comment explaining what each pattern is for.",
  [("Which regex flag makes a pattern ignore upper and lower case?", ["i", "g", "m", "s"], 0),
   ("Which regex method returns true or false?", ["test()", "match()", "replace()", "split()"], 0)]),

# ============================================================ Arrays & Objects
L("js-arrays", "JavaScript Arrays", "Arrays & Objects",
  "An array is an ordered list of values. Each value has a position (index) starting at 0.",
  [("Creating and reading", "Use square brackets. `length` is the number of items.", 'const fruits = ["apple", "pear", "plum"];\nfruits[0];      // "apple"\nfruits.length;  // 3'),
   ("Changing items", "You can assign to an index, even for a `const` array, because the array itself is not replaced.", 'fruits[1] = "mango";'),
   ("Mixed content", "Arrays can hold any types, including other arrays. Use `Array.isArray()` to check whether a value is an array.")],
  '''<script>
  const fruits = ["apple", "pear", "plum"];
  console.log(fruits[0], "|", fruits.length);
  fruits[1] = "mango";
  console.log(fruits);
  console.log("last:", fruits[fruits.length - 1], "| at(-1):", fruits.at(-1));
  console.log("isArray:", Array.isArray(fruits), "| typeof:", typeof fruits);
  const grid = [[1, 2], [3, 4]];
  console.log("grid[1][0] =", grid[1][0]);
</script>''',
  "`at(-1)` is a neat way to read the last item.",
  [("What is the index of the last item in an array of 5 items?", ["4", "5", "6", "1"], 0),
   ("Which function checks whether a value is an array?", ["Array.isArray()", "typeof", "isArray()", "value.isArray"], 0)]),

L("js-array-methods", "JavaScript Array Methods", "Arrays & Objects",
  "Arrays have many methods to add, remove, find and rearrange items.",
  [("Adding and removing", "`push()` adds to the end, `pop()` removes from the end, `unshift()` adds to the start and `shift()` removes from the start.", 'const a = [1, 2];\na.push(3);   // [1, 2, 3]\na.shift();   // [2, 3]'),
   ("Slicing and splicing", "`slice(start, end)` returns a copy of part of an array and leaves the original alone. `splice(start, count)` removes items and changes the original."),
   ("Searching and joining", "`indexOf()` and `includes()` find items. `join()` turns an array into a string. `concat()` joins arrays."),
   ("Sorting", "`sort()` sorts as text by default, so numbers need a compare function: `sort((a, b) => a - b)`. `reverse()` flips the order.")],
  '''<script>
  const a = [3, 1, 2];
  a.push(4);\n  console.log("push:", a);
  a.pop();\n  console.log("pop:", a);
  a.unshift(0);\n  console.log("unshift:", a);
  console.log("slice(1, 3):", a.slice(1, 3), "original:", a);
  a.splice(1, 1);\n  console.log("splice(1, 1):", a);
  console.log("includes(2):", a.includes(2), "| join:", a.join(" - "));
  console.log("default sort:", [10, 9, 1].sort());
  console.log("numeric sort:", [10, 9, 1].sort((x, y) => x - y));
</script>''',
  "`push`, `pop`, `shift`, `unshift`, `splice` and `sort` change the original array. `slice` and `concat` do not.",
  [("Which method adds an item to the end of an array?", ["push()", "pop()", "shift()", "slice()"], 0),
   ("Why does [10, 9, 1].sort() give [1, 10, 9]?", ["It sorts values as text by default", "It sorts in reverse", "It ignores numbers", "It only sorts strings"], 0),
   ("Which method returns a copy of part of an array without changing it?", ["slice()", "splice()", "pop()", "reverse()"], 0)]),

L("js-array-iteration", "JavaScript Array Iteration", "Arrays & Objects",
  "Array iteration methods run a function on every item. They make loops shorter and clearer.",
  [("forEach and map", "`forEach()` runs a function for each item. `map()` returns a new array with each item transformed.", '[1, 2, 3].map(n => n * 2); // [2, 4, 6]'),
   ("filter, find and findIndex", "`filter()` keeps items that pass a test. `find()` returns the first matching item and `findIndex()` returns its position.", '[1, 2, 3, 4].filter(n => n % 2 === 0); // [2, 4]'),
   ("reduce", "`reduce()` combines all items into one value, such as a total.", '[1, 2, 3].reduce((sum, n) => sum + n, 0); // 6'),
   ("some and every", "`some()` is true if at least one item passes. `every()` is true only if all items pass.")],
  '''<script>
  const nums = [1, 2, 3, 4, 5];
  console.log("map:", nums.map(n => n * 2));
  console.log("filter:", nums.filter(n => n % 2 === 0));
  console.log("find:", nums.find(n => n > 3));
  console.log("findIndex:", nums.findIndex(n => n > 3));
  console.log("reduce:", nums.reduce((sum, n) => sum + n, 0));
  console.log("some > 4:", nums.some(n => n > 4));
  console.log("every > 0:", nums.every(n => n > 0));
  nums.forEach((n, i) => { if (i < 2) console.log("forEach item", i, "=", n); });
</script>''',
  "`map`, `filter` and `reduce` return new values and leave the original array alone, so they can be chained.",
  [("Which method builds a new array by transforming every item?", ["map()", "filter()", "forEach()", "find()"], 0),
   ("Which method combines all items of an array into a single value?", ["reduce()", "map()", "some()", "slice()"], 0),
   ("What does every() return when all items pass the test?", ["true", "The first item", "An array", "undefined"], 0)]),

L("js-objects", "JavaScript Objects", "Arrays & Objects",
  "An object groups related values as named properties. It is how JavaScript models real things such as a user or a product.",
  [("Creating an object", "Use curly braces with `key: value` pairs separated by commas.", 'const user = {\n  name: "Asha",\n  age: 21\n};'),
   ("Reading and changing", "Use dot notation (`user.name`) or bracket notation (`user[\"name\"]`). Brackets are needed when the key is in a variable or has special characters.", 'user.age = 22;\nuser.city = "Chennai";'),
   ("Methods", "A property can hold a function. It is then called a method.", 'const dog = {\n  name: "Rex",\n  speak() { return this.name + " says woof"; }\n};'),
   ("Deleting", "The `delete` operator removes a property.")],
  '''<script>
  const user = { name: "Asha", age: 21 };
  user.age = 22;
  user.city = "Chennai";
  const key = "name";
  console.log(user.name, "|", user["age"], "|", user[key]);
  console.log(user);
  const dog = { name: "Rex", speak() { return this.name + " says woof"; } };
  console.log(dog.speak());
  delete user.city;
  console.log("city after delete:", user.city);
</script>''',
  "Use bracket notation when the property name is stored in a variable.",
  [("Which notation reads a property whose name is stored in a variable?", ["obj[key]", "obj.key", "obj->key", "obj::key"], 0),
   ("What is a function stored as an object property called?", ["A method", "A class", "A closure", "A literal"], 0)]),

L("js-object-methods", "JavaScript Object Methods", "Arrays & Objects",
  "The built-in `Object` helpers let you list, copy and merge objects.",
  [("Keys, values and entries", "`Object.keys(obj)` gives the property names, `Object.values(obj)` the values and `Object.entries(obj)` pairs of `[key, value]`.", 'Object.keys({ a: 1, b: 2 }); // ["a", "b"]'),
   ("Copying and merging", "`Object.assign(target, source)` copies properties. The spread syntax `{ ...a, ...b }` creates a new merged object.", 'const merged = { ...a, ...b };'),
   ("Freezing", "`Object.freeze(obj)` stops further changes to an object. It only protects the first level."),
   ("Checking", "`\"name\" in obj` and `obj.hasOwnProperty(\"name\")` test whether a property exists.")],
  '''<script>
  const user = { name: "Asha", age: 21 };
  console.log("keys:", Object.keys(user));
  console.log("values:", Object.values(user));
  console.log("entries:", Object.entries(user));
  for (const [k, v] of Object.entries(user)) console.log(k + " => " + v);

  const merged = { ...user, city: "Chennai", age: 22 };
  console.log("merged:", merged);

  const frozen = Object.freeze({ x: 1 });
  frozen.x = 99;
  console.log("frozen x:", frozen.x);
  console.log("has name:", "name" in user);
</script>''',
  None,
  [("Which method returns an array of an object's property names?", ["Object.keys()", "Object.values()", "Object.assign()", "Object.freeze()"], 0),
   ("What does the spread syntax in { ...a, ...b } create?", ["A new merged object", "A new array", "A string", "A function"], 0)]),

L("js-destructuring", "JavaScript Destructuring", "Arrays & Objects",
  "Destructuring unpacks values from arrays or properties from objects into separate variables.",
  [("Array destructuring", "Variables are matched by position.", 'const [first, second] = ["a", "b", "c"];'),
   ("Object destructuring", "Variables are matched by property name. You can rename or give defaults.", 'const { name, age = 18 } = user;\nconst { name: userName } = user;'),
   ("In parameters", "You can destructure directly in a function's parameters, which makes functions easy to call with an options object.", 'function show({ name, age }) {\n  return name + " is " + age;\n}')],
  '''<script>
  const [first, second, ...others] = ["a", "b", "c", "d"];
  console.log(first, second, others);

  const user = { name: "Asha", age: 21, city: "Chennai" };
  const { name, age: years, country = "India" } = user;
  console.log(name, years, country);

  function show({ name, city }) { return name + " lives in " + city; }
  console.log(show(user));

  let a = 1, b = 2;
  [a, b] = [b, a];
  console.log("swapped:", a, b);
</script>''',
  "Swapping two variables is a one-liner with array destructuring: `[a, b] = [b, a]`.",
  [("Which syntax unpacks the first two items of an array into variables?", ["const [x, y] = list", "const {x, y} = list", "const (x, y) = list", "const <x, y> = list"], 0),
   ("In const { name, age = 18 } = user, what is age if user has no age?", ["18", "undefined", "null", "An error is thrown"], 0)]),

L("js-spread-rest", "JavaScript Spread and Rest", "Arrays & Objects",
  "The three dots `...` do two related jobs: spread values out, or gather them in.",
  [("Spread", "In a call, array or object literal, `...` expands an iterable into separate items.", 'const all = [...a, ...b];\nMath.max(...[3, 7, 5]); // 7'),
   ("Rest", "In a parameter list or destructuring pattern, `...` collects the remaining items into an array or object.", 'function sum(first, ...others) {}'),
   ("Copies", "Spread makes a shallow copy. Nested objects and arrays are still shared between the copy and the original.")],
  '''<script>
  const a = [1, 2], b = [3, 4];
  const all = [...a, ...b, 5];
  console.log("combined:", all);
  console.log("max:", Math.max(...all));

  const copy = [...a];
  copy.push(99);
  console.log("original:", a, "copy:", copy);

  const base = { color: "blue", size: 2 };
  const custom = { ...base, size: 5 };
  console.log(custom);

  const [head, ...rest] = all;
  console.log("head:", head, "rest:", rest);
</script>''',
  None,
  [("What does Math.max(...[3, 7, 5]) return?", ["7", "3", "5", "NaN"], 0),
   ("Is the spread copy [...arr] a deep copy?", ["No, it is a shallow copy", "Yes, always deep", "Only for numbers", "Only for strings"], 0)]),

L("js-set-map", "JavaScript Set and Map", "Arrays & Objects",
  "`Set` stores unique values. `Map` stores key-value pairs where keys can be any type.",
  [("Set", "A Set keeps each value only once. It is the easiest way to remove duplicates.", 'const unique = [...new Set([1, 2, 2, 3])]; // [1, 2, 3]'),
   ("Map", "A Map remembers insertion order and allows keys of any type. Use `set`, `get`, `has`, `delete` and `size`.", 'const m = new Map();\nm.set("a", 1);\nm.get("a"); // 1'),
   ("Looping", "Both can be looped over with `for...of`.")],
  '''<script>
  const unique = new Set([1, 2, 2, 3, 3, 3]);
  console.log("unique size:", unique.size);
  console.log("as array:", [...unique]);
  console.log("has 2:", unique.has(2));

  const scores = new Map();
  scores.set("Asha", 90).set("Ravi", 75);
  console.log("Asha:", scores.get("Asha"), "| size:", scores.size);
  for (const [name, score] of scores) console.log(name + " scored " + score);
</script>''',
  "`[...new Set(array)]` is the classic one-line way to remove duplicates.",
  [("What does a Set do with duplicate values?", ["Keeps each value only once", "Keeps all of them", "Throws an error", "Sorts them"], 0),
   ("Which method reads a value from a Map?", ["get()", "read()", "fetch()", "at()"], 0)]),

L("js-json", "JavaScript JSON", "Arrays & Objects",
  "JSON is a text format for data. It looks like a JavaScript object but is just a string, used to send data between programs.",
  [("Object to text", "`JSON.stringify(value)` turns a value into a JSON string. Add a third argument such as `2` to indent it.", 'JSON.stringify({ a: 1 }); // \'{"a":1}\''),
   ("Text to object", "`JSON.parse(text)` turns a JSON string back into a value. It throws an error if the text is not valid JSON.", 'JSON.parse(\'{"a":1}\'); // { a: 1 }'),
   ("Rules", "JSON keys must be in double quotes. Functions and `undefined` are not part of JSON and are dropped by `stringify`.")],
  '''<script>
  const user = { name: "Asha", age: 21, tags: ["css", "js"] };
  const text = JSON.stringify(user);
  console.log(text);
  console.log(JSON.stringify(user, null, 2));

  const back = JSON.parse(text);
  console.log("parsed name:", back.name);

  try {
    JSON.parse("{ name: 'Asha' }");
  } catch (e) {
    console.log("Invalid JSON ->", e.name);
  }
</script>''',
  "Always wrap `JSON.parse` in `try...catch` when the text comes from outside your program.",
  [("Which method converts a JavaScript object into a JSON string?", ["JSON.stringify()", "JSON.parse()", "JSON.encode()", "JSON.toObject()"], 0),
   ("Which method converts a JSON string into a JavaScript value?", ["JSON.parse()", "JSON.stringify()", "JSON.decode()", "JSON.read()"], 0)]),

# ============================================================ The DOM
L("js-dom-intro", "JavaScript HTML DOM", "The DOM",
  "The DOM (Document Object Model) is the browser's live model of your page. JavaScript uses it to read and change the page.",
  [("A tree of nodes", "The browser turns your HTML into a tree. Every element, piece of text and attribute is a node you can reach from JavaScript."),
   ("The document object", "`document` is the entry point. `document.body` is the body element, and `document.title` is the page title."),
   ("Why it matters", "Changing the DOM changes what the user sees right away, without reloading the page.")],
  '''<h2 id="heading">Original heading</h2>
<p>A paragraph in the body.</p>
<script>
  console.log("Body children:", document.body.children.length);
  console.log("First element tag:", document.body.firstElementChild.tagName);
  document.getElementById("heading").textContent = "Changed by the DOM";
</script>''',
  "The DOM is not your HTML file. It is the live version in memory, and scripts can change it.",
  [("What does DOM stand for?", ["Document Object Model", "Data Object Mapping", "Digital Output Method", "Document Order Markup"], 0),
   ("Which object is the entry point to the DOM?", ["document", "window.page", "html", "body.root"], 0)]),

L("js-dom-selecting", "JavaScript Selecting Elements", "The DOM",
  "Before you can change an element you have to find it. Modern code mostly uses `querySelector`.",
  [("By id", "`document.getElementById(\"id\")` returns the single element with that id.", 'document.getElementById("title");'),
   ("By CSS selector", "`querySelector()` returns the first match and `querySelectorAll()` returns all matches, using the same selectors as CSS.", 'document.querySelector(".card");\ndocument.querySelectorAll("li");'),
   ("Null results", "If nothing matches, `querySelector` returns `null`. Using it without checking causes errors."),
   ("Looping over results", "`querySelectorAll()` returns a NodeList. You can use `forEach` on it, or spread it into an array.")],
  '''<ul id="list">
  <li class="item">One</li>
  <li class="item special">Two</li>
  <li class="item">Three</li>
</ul>
<script>
  const list = document.getElementById("list");
  const first = document.querySelector(".item");
  const all = document.querySelectorAll(".item");
  console.log("first:", first.textContent);
  console.log("count:", all.length);
  console.log("special:", document.querySelector(".special").textContent);
  console.log("missing:", document.querySelector(".nope"));
  all.forEach(li => (li.style.color = "#1d5bd8"));
</script>''',
  "Use `querySelector` and `querySelectorAll` for almost everything. The CSS skills you already have apply.",
  [("What does querySelector return when nothing matches?", ["null", "undefined", "An empty array", "An error"], 0),
   ("Which method returns all elements matching a CSS selector?", ["querySelectorAll()", "getElement()", "queryAll()", "selectAll()"], 0)]),

L("js-dom-content", "JavaScript Changing Content and Attributes", "The DOM",
  "Once you have an element you can change its text, its HTML and its attributes.",
  [("Text and HTML", "`textContent` sets plain text. `innerHTML` sets HTML markup, but never use it with untrusted text because it can run unwanted code.", 'el.textContent = "New text";\nel.innerHTML = "<b>Bold</b>";'),
   ("Attributes", "Use `getAttribute`, `setAttribute` and `removeAttribute`. Many attributes are also properties, such as `el.href` or `img.src`.", 'link.setAttribute("href", "https://example.com");'),
   ("Data attributes", "Attributes starting with `data-` store custom values. Read them with `el.dataset`.", '<div data-user-id="42"></div>\n// el.dataset.userId -> "42"')],
  '''<p id="msg">Old text</p>
<a id="link" href="#">A link</a>
<div id="card" data-user-id="42">User card</div>
<script>
  const msg = document.getElementById("msg");
  msg.textContent = "New text set by JavaScript";
  msg.innerHTML = "<strong>Bold</strong> text from innerHTML";

  const link = document.getElementById("link");
  link.setAttribute("title", "I was added with setAttribute");
  console.log("title attribute:", link.getAttribute("title"));

  const card = document.getElementById("card");
  console.log("data-user-id:", card.dataset.userId);
</script>''',
  "If the text comes from a user, use `textContent`. It cannot inject HTML.",
  [("Which property is the safest way to insert plain text into an element?", ["textContent", "innerHTML", "outerHTML", "insertAdjacentHTML"], 0),
   ("How do you read the value of data-user-id in JavaScript?", ["el.dataset.userId", "el.data.user-id", "el.getData(userId)", "el.userId"], 0)]),

L("js-dom-styles", "JavaScript Changing Styles", "The DOM",
  "JavaScript can change how elements look by setting inline styles or by switching CSS classes.",
  [("The style property", "`el.style.property` sets an inline style. Use camelCase for names with hyphens: `backgroundColor`, not `background-color`.", 'el.style.backgroundColor = "gold";'),
   ("classList", "A better approach is to define classes in CSS and toggle them. `classList` has `add`, `remove`, `toggle` and `contains`.", 'el.classList.add("active");\nel.classList.toggle("hidden");'),
   ("Why classes win", "Classes keep design in CSS and behaviour in JavaScript, which makes both easier to change.")],
  '''<style>
  .box { padding: 12px; border: 2px solid #1d5bd8; border-radius: 8px; margin-bottom: 8px; }
  .active { background: #1d5bd8; color: white; }
</style>
<div id="a" class="box">Styled with style.backgroundColor</div>
<div id="b" class="box">Styled with classList.add</div>
<script>
  document.getElementById("a").style.backgroundColor = "gold";
  const b = document.getElementById("b");
  b.classList.add("active");
  console.log("has active:", b.classList.contains("active"));
  b.classList.toggle("active");
  console.log("after toggle:", b.classList.contains("active"));
  b.classList.toggle("active");
</script>''',
  None,
  [("How do you write the CSS property background-color in JavaScript style?", ["backgroundColor", "background-color", "BackgroundColor", "background_color"], 0),
   ("Which classList method adds a class if missing and removes it if present?", ["toggle()", "flip()", "switch()", "swap()"], 0)]),

L("js-dom-elements", "JavaScript Creating and Removing Elements", "The DOM",
  "You can build new elements, add them to the page, move them and remove them.",
  [("Create and add", "`document.createElement()` makes an element. Set its content, then add it with `append()` or `prepend()`.", 'const li = document.createElement("li");\nli.textContent = "New item";\nlist.append(li);'),
   ("Insert and remove", "`before()` and `after()` insert next to an element. `remove()` takes an element out of the page.", 'item.remove();'),
   ("Cloning", "`el.cloneNode(true)` makes a copy of an element including its children.")],
  '''<ul id="list"><li>First</li><li>Second</li></ul>
<script>
  const list = document.getElementById("list");

  const li = document.createElement("li");
  li.textContent = "Added at the end";
  list.append(li);

  const first = document.createElement("li");
  first.textContent = "Added at the start";
  list.prepend(first);

  list.children[1].remove();     // removes "First"
  console.log("items now:", [...list.children].map(el => el.textContent));
</script>''',
  "Building many elements? Create them all first and add them once, which is faster than updating the page repeatedly.",
  [("Which method creates a new HTML element?", ["document.createElement()", "document.newElement()", "document.make()", "document.add()"], 0),
   ("Which method removes an element from the page?", ["remove()", "delete()", "destroy()", "clear()"], 0)]),

L("js-dom-forms", "JavaScript Forms and Input", "The DOM",
  "JavaScript can read what a visitor typed, check it and give feedback before anything is sent.",
  [("Reading values", "Every input has a `value` property, and it is always a string. Checkboxes use `checked`.", 'const age = Number(input.value);'),
   ("Validating", "Check the value and show a message. HTML attributes such as `required` and `type=\"email\"` help, but JavaScript lets you write custom rules."),
   ("The submit event", "Listen for `submit` on the form. Call `event.preventDefault()` to stop the page from reloading.", 'form.addEventListener("submit", e => {\n  e.preventDefault();\n});')],
  '''<form id="form">
  <input id="name" value="Asha" aria-label="Name">
  <input id="age" type="number" value="17" aria-label="Age">
  <button>Check</button>
</form>
<p id="result"></p>
<script>
  const form = document.getElementById("form");
  const result = document.getElementById("result");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    const name = document.getElementById("name").value.trim();
    const age = Number(document.getElementById("age").value);
    result.textContent = name === "" ? "Please enter a name"
      : age >= 18 ? name + " is an adult" : name + " is a minor";
    console.log("typeof age:", typeof age);
  });
  form.requestSubmit();   // run the handler once so you can see the result
</script>''',
  "Validate on the server too. Checks in the browser can be bypassed.",
  [("What type is the value property of a text input?", ["string", "number", "boolean", "object"], 0),
   ("Which method stops a form from reloading the page on submit?", ["event.preventDefault()", "event.stop()", "form.cancel()", "event.halt()"], 0)]),

# ============================================================ Events & Timers
L("js-events", "JavaScript Events", "Events & Timers",
  "Events are things that happen on the page: clicks, key presses, form changes and more. JavaScript can react to them.",
  [("Common events", "`click`, `dblclick`, `input`, `change`, `submit`, `keydown`, `mouseover`, `focus`, `load` and `DOMContentLoaded` cover most needs."),
   ("Handling an event", "Attach a function (a handler) to an element. The browser calls it each time the event happens.", 'button.addEventListener("click", () => {\n  console.log("Clicked");\n});'),
   ("Inline handlers", "You may see `onclick=\"...\"` written in HTML. It works, but it mixes code into markup, so use `addEventListener` instead.")],
  '''<button id="btn">Click me</button>
<p id="out">Not clicked yet</p>
<script>
  let count = 0;
  const btn = document.getElementById("btn");
  btn.addEventListener("click", function () {
    count++;
    document.getElementById("out").textContent = "Clicked " + count + " time(s)";
    console.log("click event handled, count =", count);
  });
  btn.click();   // simulate one click so you can see the result; now click it yourself
</script>''',
  "Think of a handler as an instruction: when this happens, run this function.",
  [("Which event fires when a user clicks an element?", ["click", "press", "tap", "select"], 0),
   ("Which approach is preferred for attaching event handlers?", ["addEventListener", "onclick attributes in HTML", "document.write", "setAttribute(\"onclick\")"], 0)]),

L("js-event-listener", "JavaScript addEventListener and the Event Object", "Events & Timers",
  "`addEventListener` is the modern way to handle events. The handler receives an event object with details about what happened.",
  [("Syntax", "`element.addEventListener(type, handler)`. You can add several handlers for the same event, and remove one with `removeEventListener`.", 'btn.addEventListener("click", handler);\nbtn.removeEventListener("click", handler);'),
   ("The event object", "`event.target` is the element that was clicked, `event.type` is the event name and `event.key` tells you which key was pressed. `event.preventDefault()` cancels the browser's default action."),
   ("Options", "A third argument such as `{ once: true }` makes the handler run only one time.", 'btn.addEventListener("click", fn, { once: true });')],
  '''<input id="field" placeholder="Type here" aria-label="Type here">
<button id="once">Only works once</button>
<p id="out"></p>
<script>
  const field = document.getElementById("field");
  field.addEventListener("input", function (event) {
    document.getElementById("out").textContent = "You typed: " + event.target.value;
  });
  field.value = "Hello";
  field.dispatchEvent(new Event("input"));   // simulate typing

  const once = document.getElementById("once");
  once.addEventListener("click", e => console.log("Handled once. type =", e.type), { once: true });
  once.click(); once.click();
</script>''',
  "Name your handlers (not anonymous functions) when you need to remove them later.",
  [("Which event property gives the element that triggered the event?", ["event.target", "event.source", "event.element", "event.node"], 0),
   ("What does the option { once: true } do?", ["Runs the handler only one time", "Runs it twice", "Blocks the event", "Runs it before the page loads"], 0)]),

L("js-event-delegation", "JavaScript Event Delegation", "Events & Timers",
  "Instead of adding a listener to every item, add one to the parent. Events bubble up, so the parent can handle them all.",
  [("Event bubbling", "When you click an element, the event runs on it, then on its parent, then on the parent's parent, and so on up the page."),
   ("Delegation", "Put one listener on a parent and check `event.target` to see which child was clicked. It works for items added later too.", 'list.addEventListener("click", e => {\n  if (e.target.matches("li")) {\n    // handle the item\n  }\n});'),
   ("Benefits", "Less memory, less code and no need to re-attach listeners when items are added or removed.")],
  '''<ul id="list">
  <li>Apple</li><li>Banana</li><li>Cherry</li>
</ul>
<p id="out">Click a fruit</p>
<script>
  const list = document.getElementById("list");
  list.addEventListener("click", function (e) {
    if (e.target.matches("li")) {
      document.getElementById("out").textContent = "You chose " + e.target.textContent;
      console.log("Chose:", e.target.textContent);
    }
  });
  const added = document.createElement("li");
  added.textContent = "Date (added later, still works)";
  list.append(added);
  added.click();
</script>''',
  None,
  [("What is event bubbling?", ["The event travels up from the target to its parents", "The event is cancelled", "The event runs twice", "The event travels down only"], 0),
   ("What is the main advantage of event delegation?", ["One listener can handle many child elements", "It makes events faster than the CPU", "It removes the need for event objects", "It works only for buttons"], 0)]),

L("js-timers", "JavaScript Timers", "Events & Timers",
  "Timers run code later or repeatedly. They are the simplest way to see asynchronous behaviour.",
  [("setTimeout", "Runs a function once after a delay in milliseconds. It returns an id you can pass to `clearTimeout` to cancel it.", 'setTimeout(() => console.log("later"), 1000);'),
   ("setInterval", "Runs a function again and again at an interval until you stop it with `clearInterval`.", 'const id = setInterval(tick, 1000);\nclearInterval(id);'),
   ("Not guaranteed", "The delay is a minimum. If the browser is busy the callback runs later.")],
  '''<p id="out">Waiting...</p>
<script>
  console.log("1. start");
  setTimeout(function () {
    console.log("3. after 500 ms");
    document.getElementById("out").textContent = "The timeout fired";
  }, 500);
  console.log("2. end of script (runs before the timeout)");

  let ticks = 0;
  const id = setInterval(function () {
    ticks++;
    console.log("tick " + ticks);
    if (ticks === 3) { clearInterval(id); console.log("interval stopped"); }
  }, 200);
</script>''',
  "Always keep the id from `setInterval` so you can stop it. A forgotten interval runs forever.",
  [("Which function runs code once after a delay?", ["setTimeout()", "setInterval()", "delay()", "wait()"], 0),
   ("How do you stop a repeating timer?", ["clearInterval(id)", "stopInterval()", "setInterval(false)", "id.stop()"], 0)]),

# ============================================================ Asynchronous JavaScript
L("js-event-loop", "JavaScript Event Loop", "Asynchronous JavaScript",
  "JavaScript runs one thing at a time. The event loop is how it still handles timers, clicks and network replies without freezing.",
  [("Single thread", "There is one call stack. Code runs to completion before anything else starts."),
   ("Queues", "Finished timers and events wait in a task queue. Promise callbacks wait in a microtask queue. When the stack is empty, the loop runs all microtasks first, then takes the next task."),
   ("What it means for you", "Even `setTimeout(fn, 0)` runs after the current code finishes. A long loop blocks the whole page.")],
  '''<script>
  console.log("1. script start");
  setTimeout(() => console.log("4. setTimeout (task queue)"), 0);
  Promise.resolve().then(() => console.log("3. promise (microtask queue)"));
  console.log("2. script end");
</script>''',
  "Order to remember: normal code first, then promises (microtasks), then timers (tasks).",
  [("Which runs first after the main script finishes?", ["Promise callbacks (microtasks)", "setTimeout callbacks", "setInterval callbacks", "Event listeners that are not triggered"], 0),
   ("Is JavaScript single-threaded or multi-threaded by default?", ["Single-threaded", "Multi-threaded", "Four threads", "One thread per function"], 0)]),

L("js-promises", "JavaScript Promises", "Asynchronous JavaScript",
  "A Promise stands for a value that will be available later. It is either pending, fulfilled with a value or rejected with an error.",
  [("Creating a promise", "The function you pass receives `resolve` and `reject`. Call one of them when the work finishes.", 'const p = new Promise((resolve, reject) => {\n  setTimeout(() => resolve("done"), 500);\n});'),
   ("then, catch, finally", "`then()` handles success, `catch()` handles failure and `finally()` runs either way. Each returns a new promise, so you can chain them.", 'p.then(v => console.log(v))\n .catch(err => console.log(err))\n .finally(() => console.log("end"));'),
   ("Combining", "`Promise.all()` waits for all promises. `Promise.race()` finishes with the first one that settles. `Promise.allSettled()` waits for every outcome.")],
  '''<script>
  function wait(ms, value, fail) {
    return new Promise(function (resolve, reject) {
      setTimeout(function () { fail ? reject(new Error(value)) : resolve(value); }, ms);
    });
  }
  wait(200, "first result")
    .then(v => { console.log("then:", v); return wait(100, "second result"); })
    .then(v => console.log("then:", v))
    .finally(() => console.log("finally runs either way"));

  wait(150, "something broke", true)
    .catch(err => console.log("catch:", err.message));

  Promise.all([wait(50, "A"), wait(80, "B")]).then(r => console.log("all:", r));
</script>''',
  "Always end a promise chain with `.catch()` so errors are not lost.",
  [("What are the three states of a Promise?", ["Pending, fulfilled, rejected", "Start, run, stop", "Open, closed, locked", "Ready, busy, done"], 0),
   ("Which method handles a rejected promise?", ["catch()", "then() only", "finally() only", "resolve()"], 0),
   ("What does Promise.all() do?", ["Waits for all the promises to fulfil", "Returns the first promise to finish", "Cancels all the promises", "Runs the promises one at a time"], 0)]),

L("js-async-await", "JavaScript Async and Await", "Asynchronous JavaScript",
  "`async` and `await` let you write promise code that reads like ordinary step-by-step code.",
  [("async functions", "A function marked `async` always returns a promise.", 'async function load() {\n  return 42;\n}'),
   ("await", "Inside an async function, `await` pauses until a promise settles and gives you its value. Other code keeps running while it waits.", 'const data = await getData();'),
   ("Errors", "Use `try...catch` around `await` to handle rejected promises.")],
  '''<p id="out">Loading...</p>
<script>
  function getUser(id) {
    return new Promise(function (resolve, reject) {
      setTimeout(function () {
        id === 0 ? reject(new Error("User not found")) : resolve({ id: id, name: "User " + id });
      }, 200);
    });
  }
  async function main() {
    try {
      const user = await getUser(1);
      console.log("loaded:", user);
      document.getElementById("out").textContent = "Hello, " + user.name;
      await getUser(0);
    } catch (err) {
      console.log("caught:", err.message);
    } finally {
      console.log("done");
    }
  }
  main();
</script>''',
  "`await` only works inside an `async` function (or at the top level of a module).",
  [("What does an async function always return?", ["A promise", "A string", "undefined", "A callback"], 0),
   ("Where can the await keyword be used in regular scripts?", ["Inside async functions", "Anywhere in a script", "Only in loops", "Only inside classes"], 0)]),

L("js-fetch", "JavaScript Fetch API", "Asynchronous JavaScript",
  "`fetch()` requests data from a server. It returns a promise, so it works naturally with `async` and `await`.",
  [("Basic request", "`fetch(url)` resolves to a Response. Call `response.json()` to read the body as JSON (this is also a promise).",
    'async function loadUser() {\n  const response = await fetch("https://api.example.com/users/1");\n  if (!response.ok) throw new Error("HTTP " + response.status);\n  return await response.json();\n}'),
   ("Check response.ok", "`fetch` only rejects on network failure. A 404 or 500 still resolves, so always check `response.ok`."),
   ("Sending data", "Pass an options object with the method, headers and body.", 'fetch("/api/save", {\n  method: "POST",\n  headers: { "Content-Type": "application/json" },\n  body: JSON.stringify({ name: "Asha" })\n});'),
   ("In this lesson", "The live example below fakes the network with a timer, because the tutorial preview does not make real requests.")],
  '''<p id="out">Loading...</p>
<script>
  // A fake fetch that returns a Response-like object after a short delay.
  function fakeFetch(url) {
    return new Promise(function (resolve) {
      setTimeout(function () {
        resolve({
          ok: url.indexOf("missing") === -1,
          status: url.indexOf("missing") === -1 ? 200 : 404,
          json: function () { return Promise.resolve({ id: 1, name: "Asha" }); }
        });
      }, 200);
    });
  }
  async function loadUser(url) {
    const response = await fakeFetch(url);
    if (!response.ok) throw new Error("HTTP " + response.status);
    return await response.json();
  }
  loadUser("/users/1").then(function (u) {
    console.log("user:", u);
    document.getElementById("out").textContent = "Loaded " + u.name;
  });
  loadUser("/users/missing").catch(e => console.log("error:", e.message));
</script>''',
  "Wrap `fetch` calls in `try...catch` so network failures do not break your page.",
  [("What does fetch() return?", ["A promise", "The data directly", "An XML document", "A DOM element"], 0),
   ("Which property tells you whether an HTTP response was successful?", ["response.ok", "response.success", "response.done", "response.valid"], 0)]),

# ============================================================ Modern JavaScript
L("js-error-handling", "JavaScript Error Handling", "Modern JavaScript",
  "Errors will happen. `try...catch` lets your program recover instead of stopping.",
  [("try, catch, finally", "Code in `try` runs normally. If it throws, `catch` runs with the error. `finally` always runs afterwards.", 'try {\n  riskyWork();\n} catch (error) {\n  console.log(error.message);\n} finally {\n  cleanUp();\n}'),
   ("throw", "Use `throw new Error(\"message\")` to raise your own error when something is wrong."),
   ("Error types", "Common built-in types are `TypeError`, `ReferenceError`, `SyntaxError` and `RangeError`. Every error has a `name` and a `message`.")],
  '''<script>
  function divide(a, b) {
    if (b === 0) throw new Error("Cannot divide by zero");
    return a / b;
  }
  try {
    console.log(divide(10, 2));
    console.log(divide(1, 0));
    console.log("this line is skipped");
  } catch (error) {
    console.log("Caught:", error.name, "-", error.message);
  } finally {
    console.log("finally always runs");
  }
  try { undefinedFunction(); } catch (e) { console.log(e.name); }
  try { null.length; } catch (e) { console.log(e.name); }
</script>''',
  "Catch errors where you can do something useful about them, not everywhere.",
  [("Which block always runs, whether or not an error occurred?", ["finally", "catch", "try", "else"], 0),
   ("Which keyword raises your own error?", ["throw", "raise", "error", "fail"], 0)]),

L("js-classes", "JavaScript Classes", "Modern JavaScript",
  "A class is a template for creating objects that share the same structure and behaviour.",
  [("Defining a class", "The `constructor` sets up each new object. Methods are written inside the class body. Create objects with `new`.", 'class Dog {\n  constructor(name) {\n    this.name = name;\n  }\n  speak() {\n    return this.name + " says woof";\n  }\n}\nconst d = new Dog("Rex");'),
   ("Static members", "`static` methods belong to the class itself, not to each object.", 'class MathUtil {\n  static double(n) { return n * 2; }\n}\nMathUtil.double(4);'),
   ("Private fields", "A name starting with `#` is private and can only be used inside the class.")],
  '''<script>
  class Dog {
    #secret = "private data";
    constructor(name) { this.name = name; }
    speak() { return this.name + " says woof"; }
    reveal() { return this.#secret; }
    static species() { return "Canis familiaris"; }
  }
  const rex = new Dog("Rex");
  console.log(rex.speak());
  console.log(rex.reveal());
  console.log(Dog.species());
  console.log("rex instanceof Dog:", rex instanceof Dog);
</script>''',
  "Classes are tidy syntax over JavaScript's prototype system. They do the same job with less clutter.",
  [("Which method runs automatically when you create an object with new?", ["constructor", "init", "create", "start"], 0),
   ("What does a field name starting with # mean inside a class?", ["It is private to the class", "It is a comment", "It is static", "It is a getter"], 0)]),

L("js-inheritance", "JavaScript Class Inheritance", "Modern JavaScript",
  "A class can extend another class to reuse its code and add or change behaviour.",
  [("extends and super", "`extends` makes the new class a child. Inside its constructor, call `super()` before using `this` to run the parent's constructor.", 'class Puppy extends Dog {\n  constructor(name) {\n    super(name);\n  }\n}'),
   ("Overriding", "A child can define a method with the same name to replace the parent's version. `super.method()` still reaches the parent's."),
   ("Prototype chain", "Under the hood the child's prototype links to the parent's prototype. If a property is not found on the object, JavaScript looks up the chain.")],
  '''<script>
  class Animal {
    constructor(name) { this.name = name; }
    speak() { return this.name + " makes a sound"; }
  }
  class Dog extends Animal {
    constructor(name) { super(name); this.tricks = []; }
    speak() { return super.speak() + ": woof!"; }
  }
  const d = new Dog("Rex");
  console.log(d.speak());
  console.log("is Dog:", d instanceof Dog, "| is Animal:", d instanceof Animal);
  console.log("tricks:", d.tricks);
</script>''',
  "Use inheritance only for true is-a relationships. Otherwise combine objects instead.",
  [("Which keyword makes one class a child of another?", ["extends", "inherits", "implements", "derives"], 0),
   ("What must a child constructor call before using this?", ["super()", "parent()", "base()", "init()"], 0)]),

L("js-getters-setters", "JavaScript Getters and Setters", "Modern JavaScript",
  "Getters and setters look like properties but run code when you read or write them.",
  [("get and set", "A getter computes a value when it is read. A setter runs when a value is assigned, which is a good place to validate.", 'class Circle {\n  constructor(r) { this._r = r; }\n  get area() { return Math.PI * this._r ** 2; }\n  set radius(v) { this._r = v; }\n}'),
   ("Computed properties", "Getters are great for values that depend on other fields, such as a full name from first and last name."),
   ("In object literals", "Getters and setters also work in plain objects.")],
  '''<script>
  class Person {
    constructor(first, last) { this.first = first; this.last = last; }
    get fullName() { return this.first + " " + this.last; }
    set fullName(value) {
      const parts = value.split(" ");
      this.first = parts[0];
      this.last = parts[1];
    }
  }
  const p = new Person("Asha", "Kumar");
  console.log(p.fullName);          // no parentheses: it is a getter
  p.fullName = "Ravi Shah";         // runs the setter
  console.log(p.first, "|", p.last);
</script>''',
  None,
  [("How do you read a getter named fullName?", ["obj.fullName", "obj.fullName()", "obj.get(fullName)", "obj->fullName"], 0),
   ("What is a good use for a setter?", ["Validating a value before storing it", "Looping over an array", "Declaring a class", "Importing a module"], 0)]),

L("js-iterators-generators", "JavaScript Iterators and Generators", "Modern JavaScript",
  "Iterators define how a value is looped over. Generators are functions that can pause and resume, producing values one at a time.",
  [("Iterables", "Arrays, strings, Sets and Maps are iterable. That is why `for...of` and spread work on them."),
   ("Generators", "A generator is declared with `function*`. Each `yield` pauses it and hands back a value. Calling `next()` resumes it.", 'function* count() {\n  yield 1;\n  yield 2;\n}'),
   ("Lazy values", "Generators produce values only when asked, so they can describe long or even endless sequences without storing them.")],
  '''<script>
  function* range(start, end) {
    for (let i = start; i <= end; i++) yield i;
  }
  console.log([...range(1, 5)]);
  for (const n of range(10, 12)) console.log("n =", n);

  const gen = range(1, 2);
  console.log(gen.next());
  console.log(gen.next());
  console.log(gen.next());

  function* ids() { let id = 1; while (true) yield id++; }
  const it = ids();
  console.log("endless generator:", it.next().value, it.next().value, it.next().value);
</script>''',
  None,
  [("Which keyword pauses a generator and returns a value?", ["yield", "pause", "return only", "await"], 0),
   ("How do you declare a generator function?", ["function* name() {}", "function name*() {}", "generator name() {}", "function! name() {}"], 0)]),

L("js-modules", "JavaScript Modules", "Modern JavaScript",
  "Modules let you split code into separate files and share only what you choose.",
  [("export", "Mark what a file shares with `export`. A file can have many named exports and one default export.", '// math.js\nexport function add(a, b) { return a + b; }\nexport const PI = 3.14159;\nexport default function square(n) { return n * n; }'),
   ("import", "Bring exports into another file with `import`.", '// main.js\nimport square, { add, PI } from "./math.js";'),
   ("Loading modules", "In a page, load a module file with `type=\"module\"`. Modules are always in strict mode, have their own scope and are deferred automatically.", '<script type="module" src="main.js"></script>'),
   ("In this lesson", "The preview here cannot import files, so the example uses an object to show the same idea of a private scope with a public interface.")],
  '''<script>
  // The "module pattern": private variables plus a public interface,
  // similar to what export gives you in a real module file.
  const counterModule = (function () {
    let count = 0;                       // private
    function increment() { count++; }    // private
    return {
      next() { increment(); return count; },
      reset() { count = 0; }
    };
  })();
  console.log(counterModule.next(), counterModule.next());
  console.log("count is private:", counterModule.count);
</script>''',
  "Modules avoid global variables and make dependencies obvious.",
  [("Which keyword makes a function available to other files?", ["export", "share", "public", "module"], 0),
   ("Which script attribute loads a file as a module?", ["type=\"module\"", "module", "import=\"true\"", "mode=\"es\""], 0)]),

L("js-web-storage", "JavaScript Web Storage", "Modern JavaScript",
  "Web storage saves small amounts of data in the visitor's browser. `localStorage` stays after the browser closes, and `sessionStorage` lasts for one tab session.",
  [("Using localStorage", "Store and read text values by key. Values are always strings, so use JSON for objects.", 'localStorage.setItem("theme", "dark");\nlocalStorage.getItem("theme"); // "dark"\nlocalStorage.removeItem("theme");'),
   ("Objects", "Convert with `JSON.stringify` when saving and `JSON.parse` when reading.", 'localStorage.setItem("user", JSON.stringify({ name: "Asha" }));\nconst user = JSON.parse(localStorage.getItem("user"));'),
   ("Limits and safety", "Storage holds about 5 MB per site. Never store passwords or secrets in it, because any script on the page can read it."),
   ("In this lesson", "This tutorial's preview is sandboxed, so real storage is blocked. The example uses a small in-memory object with the same methods, and a try/catch shows what happens when storage is unavailable.")],
  '''<script>
  // Same API as localStorage, but kept in memory
  const store = {
    data: {},
    setItem(k, v) { this.data[k] = String(v); },
    getItem(k) { return k in this.data ? this.data[k] : null; },
    removeItem(k) { delete this.data[k]; }
  };
  store.setItem("theme", "dark");
  store.setItem("user", JSON.stringify({ name: "Asha" }));
  console.log("theme:", store.getItem("theme"));
  console.log("user.name:", JSON.parse(store.getItem("user")).name);
  console.log("missing:", store.getItem("nothing"));

  try {
    window.localStorage.setItem("x", "1");
    console.log("real localStorage works here");
  } catch (e) {
    console.log("Real storage is blocked in this preview:", e.name);
  }
</script>''',
  "Always wrap storage calls in `try...catch`. Storage can be disabled or full.",
  [("What type are values stored in localStorage?", ["Strings", "Numbers", "Objects", "Any type"], 0),
   ("How do you save an object in localStorage?", ["JSON.stringify it first", "Store it directly", "Use object.save()", "Convert it to a number"], 0)]),

L("js-optional-chaining", "JavaScript Optional Chaining and Nullish Coalescing", "Modern JavaScript",
  "Two small operators that make working with missing data much safer.",
  [("Optional chaining ?.", "`a?.b` returns `undefined` instead of throwing an error when `a` is `null` or `undefined`. It also works for calls and arrays.", 'user?.address?.city;\nuser.greet?.();\nlist?.[0];'),
   ("Nullish coalescing ??", "`a ?? b` gives `b` only when `a` is `null` or `undefined`. Unlike `||`, it keeps `0`, `false` and empty strings.", 'const count = input ?? 10;'),
   ("Together", "Combine them to read deeply nested data with a safe default: `user?.profile?.name ?? \"Guest\"`.")],
  '''<script>
  const user = { name: "Asha", address: null };
  console.log("city:", user.address?.city);
  console.log("missing method:", user.greet?.());
  console.log("name or Guest:", user.nickname ?? "Guest");

  const quantity = 0;
  console.log("|| treats 0 as missing:", quantity || 10);
  console.log("?? keeps 0:", quantity ?? 10);
</script>''',
  None,
  [("What does user?.address?.city return if user.address is null?", ["undefined", "An error", "null", "\"city\""], 0),
   ("How does the ?? operator differ from ||?", ["It only replaces null and undefined", "It replaces every falsy value", "It compares types", "It joins two strings"], 0)]),

L("js-es6", "JavaScript ES6 and Beyond", "Modern JavaScript",
  "ES6 (ECMAScript 2015) was a major update. Since then JavaScript gets new features every year.",
  [("Features from ES6", "`let` and `const`, arrow functions, template literals, destructuring, spread and rest, classes, Promises, modules, `Map` and `Set`, default parameters and `for...of`."),
   ("Later additions", "Examples include `async`/`await`, `**`, `Object.entries`, optional chaining `?.`, nullish coalescing `??`, `Array.prototype.at()`, `replaceAll()` and private class fields `#x`."),
   ("Browser support", "All modern browsers support these features. Tools such as Babel can translate new syntax for very old browsers if you need them.")],
  '''<script>
  // A tour of modern syntax in a few lines
  const user = { name: "Asha", langs: ["css", "js"] };
  const { name, langs: [first, ...more] } = user;
  const greet = (who = "friend") => `Hi ${who}, you know ${first}`;
  console.log(greet(name));
  console.log([...langs()].at(-1), more);
  function* langs() { yield* ["html", "css", "js"]; }
  console.log(Object.entries(user).length, "entries");
  console.log(user.nickname ?? "no nickname");
</script>''',
  None,
  [("In which year was ECMAScript 2015 (ES6) released?", ["2015", "2009", "2020", "2005"], 0),
   ("Which of these is an ES6 feature?", ["Arrow functions", "Server-side rendering", "CSS Grid", "Cookies"], 0)]),

# ============================================================ Best Practices
L("js-debugging", "JavaScript Debugging", "Best Practices",
  "Debugging is finding and fixing mistakes. A calm, step-by-step approach finds most bugs quickly.",
  [("console methods", "`console.log()` shows values, `console.table()` shows arrays and objects as a table, `console.error()` flags problems and `console.assert()` logs only when a condition is false."),
   ("Browser developer tools", "Press F12 (or right-click and choose Inspect) to open the tools. The Console shows errors with file and line number. The Sources panel lets you set breakpoints and step through code line by line."),
   ("The debugger statement", "Writing `debugger;` pauses execution at that line when developer tools are open."),
   ("A method", "Read the error message, find the line, check the values just before it, change one thing at a time, and test again.")],
  '''<script>
  const cart = [
    { item: "Book", price: 12 },
    { item: "Pen", price: 3 }
  ];
  console.table(cart);
  const total = cart.reduce((sum, i) => sum + i.price, 0);
  console.log("total =", total);
  console.assert(total === 15, "total should be 15");
  console.assert(total === 20, "this assertion fails, so it is logged");
  console.error("console.error shows problems in red");
</script>''',
  "Most bugs are simple: a typo, the wrong variable or an unexpected value. Print the values and look.",
  [("What does the debugger statement do when developer tools are open?", ["Pauses execution at that line", "Fixes the error", "Clears the console", "Reloads the page"], 0),
   ("Which key usually opens browser developer tools?", ["F12", "F5", "Esc", "Tab"], 0)]),

L("js-best-practices", "JavaScript Best Practices", "Best Practices",
  "Good habits make your code shorter, safer and easier for others (and your future self) to read.",
  [("Declare and name well", "Use `const` by default, `let` when you must reassign, and never `var`. Choose clear names such as `totalPrice`, not `x`."),
   ("Keep functions small", "A function should do one job. Short functions are easier to test, reuse and understand."),
   ("Be strict", "Use `===` instead of `==`, and use `\"use strict\"` (or modules, which are strict automatically) to catch mistakes early."),
   ("Avoid globals and handle errors", "Keep variables inside functions or modules, check for `null` and `undefined`, and use `try...catch` around risky code."),
   ("Format consistently", "Pick a style, use a formatter such as Prettier and a linter such as ESLint, and comment the reason behind tricky code.")],
  '''<script>
  "use strict";

  const TAX_RATE = 0.18;

  function priceWithTax(price) {
    return Math.round(price * (1 + TAX_RATE) * 100) / 100;
  }

  function formatCurrency(amount) {
    return "Rs. " + amount.toFixed(2);
  }

  const prices = [100, 250, 40];
  prices.forEach(function (price) {
    console.log(formatCurrency(price) + " becomes " + formatCurrency(priceWithTax(price)));
  });
</script>''',
  "Code is read far more often than it is written. Write it for the reader.",
  [("Which equality operator is recommended in most JavaScript code?", ["===", "==", "=", "!=="], 0),
   ("What is a good guideline for the size of a function?", ["It should do one job", "It should contain the whole program", "It should never take parameters", "It should use only global variables"], 0),
   ("Which keyword should be your default for declaring variables?", ["const", "var", "global", "static"], 0)]),

L("js-security", "JavaScript Security Basics", "Best Practices",
  "Anything that runs in the browser can be seen and changed by the visitor. A few rules keep your pages and users safe.",
  [("Never trust user input", "Treat everything typed by a user, or loaded from a URL, as untrusted. Validate it on the server as well as in the browser."),
   ("Avoid injecting HTML", "Inserting user text with `innerHTML` can let an attacker run scripts (cross-site scripting, or XSS). Use `textContent`, or clean the text first.",
    'el.textContent = userText; // safe\nel.innerHTML = userText;   // risky'),
   ("Avoid eval", "`eval()` runs a string as code. It is slow and dangerous, and almost always unnecessary."),
   ("Secrets", "Never put passwords, API keys or tokens in front-end code or in `localStorage`. Keep them on the server.")],
  '''<div id="safe"></div>
<div id="unsafe"></div>
<script>
  const userText = '<img src=x onerror="alert(1)">Hello';

  // textContent shows the characters as plain text: safe
  document.getElementById("safe").textContent = "textContent: " + userText;

  // A simple escape function if you must build HTML strings
  function escapeHtml(text) {
    return text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  document.getElementById("unsafe").innerHTML = "escaped first: " + escapeHtml(userText);
  console.log(escapeHtml("<b>bold</b>"));
</script>''',
  "Escape on output, validate on input, and keep secrets on the server.",
  [("What is cross-site scripting (XSS)?", ["An attacker getting their script to run on your page", "Loading two stylesheets", "Copying a site's design", "Using two scripts in one file"], 0),
   ("Which property is safer than innerHTML for inserting user text?", ["textContent", "outerHTML", "insertAdjacentHTML", "document.write"], 0)]),

L("js-performance", "JavaScript Performance", "Best Practices",
  "Fast pages feel better and rank better. A few habits avoid most slowdowns.",
  [("Do less work", "Avoid repeating the same calculation. Store the result in a variable, and stop loops early with `break` when you have your answer."),
   ("Touch the DOM sparingly", "Changing the page is slower than running plain JavaScript. Build elements first and add them in one go, or use a `DocumentFragment`."),
   ("Throttle and debounce", "Events like `scroll` and `input` can fire dozens of times a second. Debouncing waits until the user pauses, and throttling limits how often the handler runs."),
   ("Load smartly", "Use `defer` on scripts, load only what the page needs and keep files small.")],
  '''<ul id="list"></ul>
<script>
  const list = document.getElementById("list");
  const fragment = document.createDocumentFragment();
  for (let i = 1; i <= 5; i++) {
    const li = document.createElement("li");
    li.textContent = "Item " + i;
    fragment.append(li);          // built off-screen
  }
  list.append(fragment);          // one DOM update

  function debounce(fn, wait) {
    let id;
    return function (...args) {
      clearTimeout(id);
      id = setTimeout(() => fn.apply(this, args), wait);
    };
  }
  const log = debounce(v => console.log("debounced call with", v), 100);
  log(1); log(2); log(3);         // only the last call runs
</script>''',
  "Measure before you optimise. `console.time()` and `console.timeEnd()` are an easy start.",
  [("What does debouncing a function do?", ["Waits until calls stop before running it", "Runs it faster", "Runs it twice", "Removes it from memory"], 0),
   ("Why is a DocumentFragment useful?", ["It lets you add many elements with one DOM update", "It styles elements", "It fetches data", "It stores cookies"], 0)]),
]

# ------------------------------------------------------------------------------------
# Shuffle each question's options once (fixed seed) so the right answer is not always first.
import random as _random

for _lesson in LESSONS:
    for _q in _lesson["exercise"]:
        _right = _q["options"][_q["answer"]]
        _rng = _random.Random(_lesson["slug"] + _q["q"])
        _rng.shuffle(_q["options"])
        _q["answer"] = _q["options"].index(_right)

BY_SLUG = {l["slug"]: l for l in LESSONS}
