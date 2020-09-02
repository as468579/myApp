const express = require('express');
const app = express;

app.listen(3000, () => {
    console.log('server running on port 3000')
})
  
app.get('/call/python', pythonProcess)

function pythonProcess(req, res) {

    console.log(`name: ${req.query.name}, from: ${req.query.from}`)

    let spawn = require("child_process").spawn

    let process = spawn('python', [
        "./process.py",
        req.query.name,
        req.query.from
])

process.stdout.on('data', (data) => {
    const parsedString = JSON.parse(data)
    res.json(parsedString)
})

} 