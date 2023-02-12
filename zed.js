const express = require('express');
const { exec } = require('child_process');
const app = express();

app.get('/run?:website', (req, res) => {
  const website = req.params.website;
  exec(
    `python3 dos.py ${website}`,
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
