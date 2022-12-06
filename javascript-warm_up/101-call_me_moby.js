#!/usr/bin/node
function callMeMoby (number, theFunction) {
  for (let i = 0; i < number; i++) {
    theFunction();
  }
}
module.exports = { callMeMoby };
