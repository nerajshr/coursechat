window.onload = function(){
    // Click functionality for add course button
    const addCourseBtn=document.querySelector('.add_course');
    if(addCourseBtn){
        addCourseBtn.addEventListener('click',function(e){
            window.location.href="/form.html";
        });
    }
    // menu opening functionality
    const menuIcon=document.querySelector(".menu-icon");
    const userProfile=document.querySelector('.user-profile');
    menuIcon.addEventListener('click',function(){
        userProfile.classList.toggle('open');
    });

    // menu closing functionality
    const closeBtn=document.querySelector('.menu-close-btn');
    closeBtn.addEventListener('click',function(){
        userProfile.classList.toggle('open');
    });
}