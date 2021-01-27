//7-1 11654
const readline = require("readline");
const rl = readline.createInterface({
    input : process.stdin,
    output: process.stdout,
});

let inputValue;
const onInput = (value) => (inputValue = value);

const onClose = () => {
    console.log(inputValue.charCodeAt());
    process.exit();
};

rl.on("line", onInput).on("close", onClose);
