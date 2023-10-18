function evenOrOdd(number) {
    if (number % 2 === 0) {
        return "Even";
    } else {
        return "Odd";
    }
}

// Example usage
const number1 = 10;
const number2 = 7;

console.log(`${number1} is ${evenOrOdd(number1)}`);
console.log(`${number2} is ${evenOrOdd(number2)}`);
