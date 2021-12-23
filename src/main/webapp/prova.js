/*
var entry= {
    name: "Daniele",
    message: "Ciao Daniele"
}

*/ /*
str=JSON.stringify(entry)

fetch('http://192.168.1.51:80/main?str='+str, {
    method: "GET",
    credentials:"include",
    //body: ,
    cache:"no-cache",
    headers: new Headers({
        "content-type": "application/json",
        "Access-Control-Allow-Origin" : "*",
        "Access-Control-Allow-Methods" : "GET,PUT,POST,DELETE"
    })
})
    .then(function (response){

        console.log("ciao")
        response.json().then(function(data){
            console.log(data)
        })
})

*/




$.ajax({

    url: 'http://192.168.1.51:80/main',
    //data: null,
    type: 'GET',
    //crossDomain: true,
    //dataType: 'jsonp',
    success: function(data) {
        alert("Success");
        console.log(data)},

    error: function() { alert('Failed!'); },
    //beforeSend: setHeader
});


/*
var xml = new XMLHttpRequest();
xml.open("POST", "http://192.168.1.51:80/response", true);
xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
xml.onload = function (){
    var dataReply = JSON.parse(this.responseText)
    alert(dataReply)
};

xml.setRequestHeader('Access-Control-Allow-Origin', "*")
xml.setRequestHeader('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
xml.setRequestHeader('Access-Control-Allow-Headers', 'Content-Type')


dataSend = JSON.stringify( {
    'somedata':'data',
    'moredata':'moredata'
});

xml.send(dataSend);

*/
