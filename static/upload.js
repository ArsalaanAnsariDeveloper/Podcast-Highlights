
function sendPost() {
    var data = {"title": "Startup Highlight 4", "url": "Bye"}
    console.log(data)
    $.ajax({
        type: "POST",
        url: 'http://localhost:5000/upload_podcast',
        data: {json: JSON.stringify(data)},
        success: function(data){
            console.log(JSON.stringify(data));
            $("#content").append("<div class = 'row center secondary' >Podcast Highlight Uploaded!</div>");
        }
    });
}



$(document).ready(function () {

    console.log("Ready")
    $("#submit_podcast").click(function () {
        $("#content").append('<div class = "row center secondary"><div><audio controls><source src = "https://www2.cs.uic.edu/~i101/SoundFiles/PinkPanther60.wav" type = "audio/wav" ></audio ><div>Startup Episode 2</div> <div><input type="text" name="stime"><input type="text" name="etime"> </div><button class ="secondary" id = "upload"> Upload</button></div>');              
        console.log("Audio Appended");
        
        $("#content").on('click', '#upload', function(){
            console.log("Upload Clicked")
            sendPost();
        });
    
    });

    

})

