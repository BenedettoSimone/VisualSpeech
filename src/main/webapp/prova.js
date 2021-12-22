//https://www.youtube.com/watch?v=aoMzOgiE7rY


/*
const { spawn } = require('child_process');

const childPython = spawn('python', ['main.py']);

childPython.stdout.on('data', (data) => {
    console.log('stdout:' ${data})
});



childPython.stderr.on('data', (data) => {
    console.error('stderr:' ${data})
});


childPython.on('close', (code) => {
    console.log('childprocess exit code:' ${code})
})

 */

$.ajax({

    url: 'http://192.168.1.51:80/main',
    //data: null,
    type: 'GET',
    crossDomain: true,
   dataType: 'jsonp',
    success: function() { alert("Success"); },
    error: function() { alert('Failed!'); },
    //beforeSend: setHeader
});