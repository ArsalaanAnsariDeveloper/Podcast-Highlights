$(document).ready(function () {
    
        console.log("Ready")
        $.ajax({
            type: "GET",
            url: 'http://localhost:5000/get_podcast',
            success: function(data){
                console.log(JSON.stringify(data));
                if(data["data"] != ""){
                    $("#static").append('<div class="col-md-6 center"> <div> <audio controls> <source src="https://s3.amazonaws.com/ui-podcast-bucket/PinkPanther30.wav" type="audio/wav"> </audio> <div>Startup Highlight 5</div><div>0 Views</div> </div> </div>');
                }
            }
        });
    
        
    
    })
    