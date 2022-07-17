var text = require('textbelt');

text.send('9196187361', 'A sample text message!', undefined, function(err) {
  if (err) {
    console.log(err);
  }
});