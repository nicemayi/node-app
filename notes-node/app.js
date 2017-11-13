console.log("Starting app.js");

const fs = require("fs");
const os = require("os");
const notes = require("./notes");

console.log(`Result: ${notes.add(9, -2)}`);

// const { username } = os.userInfo();

// fs.appendFile("greetings.txt", `Hello ${username}!`, function(err) {
//   if (err) {
//     console.log("Unable to write to file");
//   }
// });
