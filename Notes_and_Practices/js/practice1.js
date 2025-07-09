console.log("Hello, World!")

let a = 5;
const b = 10; // unchangeable constant
a = 20; // This is fine, 'a' can be reassigned

// let b = 15; // This will cause an error because 'b' is a constant

let number = 42; // This is a number
let text = "This is a string"; // This is a string
let isTrue = true; // This is a boolean
let nothing = null; // This is null
let notDefined; // This is undefined
let bigIntNumber = 1234567890123456789012345678901234567890n; // This is a BigInt

let symbolValue = Symbol("This is a symbol"); // This is a symbol
let object = { key: "value" }; // This is an object
let array = [1, 2, 3, 4, 5]; // This is an array

function greet(name = "World") {
    return `Hello, ${name}!`;
}

console.log(greet("Alice")); // Outputs: Hello, Alice!
console.log(greet()); // Outputs: Hello, World!

function add(x, y) {
    return x + y;
}

function add2(...nums) {
    return nums.reduce((acc, num) => acc + num, 0);
}

console.log(add(5, 10)); // Outputs: 15
console.log(add2(1, 2, 3, 4, 5)); // Outputs: 15


let number1 = 7;
let number2 = 3;

if (number1 > number2) {
    console.log(`${number1} is greater than ${number2}`);
} else if (number1 < number2) {
    console.log(`${number1} is less than ${number2}`);
} else {
    console.log(`${number1} is equal to ${number2}`);
}

// NaN is a special value in JavaScript that represents "Not-a-Number"
// Null is a special value that represents the intentional absence of any object value
// Undefined is a special value that indicates a variable has been declared but not assigned a value

//false and 0 and emptry and null and undefined and NaN are all considered falsy values in JavaScript.

let falsyValue = null; // This is a falsy value
if (falsyValue) {
    console.log(`This will not be printed because ${falsyValue} is truthy`);
} else {
    console.log(`This will be printed because ${falsyValue} is falsy`);
}

//msg = "Even" if x % 2 == 0 else "Odd"
let msg = (x) => x % 2 === 0 ? "Even" : "Odd";


for (let i = 0; i < 5; i++) {
    console.log(`Iteration ${i}`);
}

fruits = ["apple", "banana", "cherry"];

for (let fruit of fruits) {
    console.log(`Fruit: ${fruit}`);
}

person = {
    name: "John",
    age: 30,
    city: "New York"
};

for (let key in person) {
    console.log(`${key}: ${person[key]}`);
}

let num3 = 10;

while (num3 > 0) {
    console.log(`Countdown: ${num3}`);
    num3--;
}

let num4 = 10;
do {
    console.log(`Countdown with do: ${num4}`);
    num4--;
} while (num4 > 50);

let num5 = 10;

switch (num5) {
    case 1:
        console.log("Number is 1");
        break;
    case 2:
        console.log("Number is 2");
        break;
    case 3:
        console.log("Number is 3");
        break;
    default:
        console.log("Number is something else");
}

num6 = 10;

while (num6 > 0) {
    if (num6 === 8) {
        num6--;
        continue; // Skip the rest of the loop iteration when num6 is 8
    }
    if (num6 === 5) {
        console.log("Skipping 5");
        num6--;
        break; // Exit the loop when num6 is 5
    }
    console.log(`Countdown: ${num6}`);
    num6--;
}