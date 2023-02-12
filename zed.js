const express = require('express');
const { exec } = require('child_process');
const app = express();

app.get('/run/:website', (req, res) => {
  const website = req.params.website;
  console.log(`https://${website}`)
  exec(
    `python dos.py https://${website}`,
    (error, stdout, stderr) => {
      if (error) {
        res.status(500).send(error);
      } else {
        res.send(stdout);
      }
    }
  );
});

app.listen(3002, () => {
  console.log('API server running on port 3001');
});
