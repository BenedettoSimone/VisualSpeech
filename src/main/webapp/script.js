var sBrowser, sUsrAg = navigator.userAgent;

// The order matters here, and this may report false positives for unlisted browsers.

if (sUsrAg.indexOf("Firefox") > -1) {
    sBrowser = "Mozilla Firefox";
    // "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
} else if (sUsrAg.indexOf("SamsungBrowser") > -1) {
    sBrowser = "Samsung Internet";
    // "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G955F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36
} else if (sUsrAg.indexOf("Opera") > -1 || sUsrAg.indexOf("OPR") > -1) {
    sBrowser = "Opera";
    // "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 OPR/57.0.3098.106"
} else if (sUsrAg.indexOf("Trident") > -1) {
    sBrowser = "Microsoft Internet Explorer";
    // "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Zoom 3.6.0; wbx 1.0.0; rv:11.0) like Gecko"
} else if (sUsrAg.indexOf("Edge") > -1) {
    sBrowser = "Microsoft Edge (Legacy)";
    // "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
} else if (sUsrAg.indexOf("Edg") > -1) {
    sBrowser = "Microsoft Edge (Chromium)";
    // Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64
} else if (sUsrAg.indexOf("Chrome") > -1) {
    sBrowser = "Google Chrome or Chromium";
    // "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36"
} else if (sUsrAg.indexOf("Safari") > -1) {
    sBrowser = "Apple Safari";
    // "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1 980x1306"
} else {
    sBrowser = "unknown";
}



let camera_button = document.querySelector("#start-camera");
let video = document.querySelector("#video");
let start_button = document.querySelector("#start-record");
let stop_button = document.querySelector("#stop-record");
let download_link = document.querySelector("#download-video");
let div_recording =document.querySelector("#recording")

let camera_stream = null;
let media_recorder = null;
let blobs_recorded = [];
let video_local = null;


camera_button.addEventListener('click', async function() {
    try {
        camera_stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    }
    catch(error) {
        alert(error.message);
        return;
    }

    video.srcObject = camera_stream;
    camera_button.style.display = 'none';
    video.style.display = 'block';
    start_button.style.display = 'block';
});

start_button.addEventListener('click', function() {

    if(sBrowser==="Apple Safari"){
        media_recorder = new MediaRecorder(camera_stream, { mimeType: 'video/mp4' });
    }else {
        media_recorder = new MediaRecorder(camera_stream, { mimeType: 'video/webm' });
    }


    media_recorder.addEventListener('dataavailable', function(e) {
        blobs_recorded.push(e.data);
    });

    media_recorder.addEventListener('stop', function() {
        //var prova=new Blob(blobs_recorded, { type: 'video/mp4' })
        //video_local = URL.createObjectURL(new Blob(blobs_recorded, { type: 'video/mp4' }));
        video_local = new Blob(blobs_recorded,{ type: 'video/webm' });

        //video_local = new File(prova);
        //download_link.href = URL.createObjectURL(new Blob(blobs_recorded, { type: 'video/webm' }));

        stop_button.style.display = 'none';
        div_recording.style.display = 'none';
        download_link.style.display = 'block';

    });

    media_recorder.start(1000);

    start_button.style.display = 'none';
    stop_button.style.display = 'block';
    div_recording.style.display= 'block';
});

stop_button.addEventListener('click', function() {
    media_recorder.stop();
});

async function sendVideo() {
    let data = new FormData();
    data.append('file', video_local);


    const response = await fetch('http://192.168.1.31:80/main1', {
        method: "POST",
        body: data
    });

    var responseJson = response.json()
    responseJson.then(function(data){
        console.log(data.message)
    });

    /*
    $.ajax({

        url: 'http://192.168.1.51:80/main1',
        data: data,
        type: 'GET',
        crossDomain: true,
        //dataType: 'jsonp',
        success: function (data) {
            alert("Success");
            console.log(data)
        },

        error: function () {
            alert('Failed!');
        },
        //beforeSend: setHeader
    });


     */
}