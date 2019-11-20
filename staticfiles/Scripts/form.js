window.onload = function(){
    // Return back to home page after adding a new course functionality
    const submitBtn=document.querySelector('#submit-btn');
    if(document.querySelector("#video-link").value && document.querySelector("#video-time").value && document.querySelector("#video-descp").value){
        submitBtn.addEventListener('click',function(){
            window.location.href="/home.html";
        });
    }

    // validating time
    const courseChatTime=document.querySelector('#video-time');
    courseChatTime.addEventListener('focusout',function(e){
        
        // user time
        var inputTime = e.target.value.split(":");
        var inputHour=inputTime[0];
        if(inputHour == '00'){inputHour = 24;}
        var inputMin=inputTime[1];
        inputTime=inputHour+"."+inputMin;

        // current time
        var currentTime = new Date();
        var currentHour=currentTime.getHours();
        var currentMin=currentTime.getMinutes();
        if(currentHour == '00'){currentHour = 24;}
        currentTime=currentHour+"."+currentMin;

        if((inputTime - currentTime) > 0)
        {
        } else{
            alert("invalid time");
        }
    });
}