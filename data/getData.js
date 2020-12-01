var fs = require("fs");
console.log("Going to write into existing file");
// Open a new file with name input.txt and write Simply Easy Learning! to it.
fs.writeFile('videos.json', 'Simply Easy Learning!', function(err) {
   if (err) {
      return console.error(err);
   }
   console.log("Data written successfully!");
   console.log("Let's read newly written data");
});