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