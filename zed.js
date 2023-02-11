const express = require('express');
const { exec } = require('child_process');
const app = express();

app.get('/run', (req, res) => {
  exec(
    'node httpfuzz.js https://www.iitb.ac.in/ proxy.txt 10000 POST',
    (error, stdout, stderr) => {
      if (error) {
        res.status(500).send(error);
      } else {
        res.send(stdout);
      }
    }
  );
});

app.listen(3001, () => {
  console.log('API server running on port 3001');
});
