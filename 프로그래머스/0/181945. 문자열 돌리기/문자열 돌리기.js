const fs = require('fs')
const input = fs.readFileSync(0).toString().trim();

for (let i = 0; i < input.length; i++){
    console.log(input[i]);
}
