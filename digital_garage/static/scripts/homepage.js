
//scroll to top
if ($(window).scrollTop() === 0) {
    //Garage door slide up 
    setTimeout(function(){
        $("#garage-door-loader").animate({top: '-100%'}, 'slow');
    }, 300);
    setTimeout(function(){
        $("#garage-door-loader").addClass('gone')
    }, 1000)
} else{
    $("#garage-door-loader").addClass('gone')
}

// Detect request animation frame
var scroll = window.requestAnimationFrame ||
             // IE Fallback
             function(callback){ window.setTimeout(callback, 1000/60)};
var elementsToShow = document.querySelectorAll('.show-on-scroll'); 
var shown = false; 

function loop() {

    Array.prototype.forEach.call(elementsToShow, function(element){
      if (isElementInViewport(element)) {
        element.classList.add('is-visible');
        shown = true;
      } else {
        //element.classList.remove('is-visible');
      }
    });

    if (shown == false){
        scroll(loop);
    }
}

// Call the loop for the first time
loop();

// Helper function from: http://stackoverflow.com/a/7557433/274826
function isElementInViewport(el) {
  // special bonus for those using jQuery
  if (typeof jQuery === "function" && el instanceof jQuery) {
    el = el[0];
  }
  var rect = el.getBoundingClientRect();
  return (
    (rect.top <= 0
      && rect.bottom >= 0)
    ||
    (rect.bottom >= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.top <= (window.innerHeight || document.documentElement.clientHeight))
    ||
    (rect.top >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight))
  );
}

$('window').ready(function(){
    $('.card').removeClass('is-loading')
})

//load on interaction
/*
const body = document.body;
let loaded = false;

const onInteraction = () => {
    if (loaded === true) {
        return;
    }
    loaded = true;

    const modelViewer = document.createElement('script'); 
    modelViewer.type = 'module';
    modelViewer.src = 'https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js'; 
    body.appendChild(modelViewer);

    const focusVisible = document.createElement('script');
    focusVisible.src = 'https://unpkg.com/focus-visible/dist/focus-visible.js'; 
    body.appendChild(focusVisible);
};

body.addEventListener('mouseover', onInteraction, {once:true});
body.addEventListener('touchmove', onInteraction, {once:true});
body.addEventListener('scroll', onInteraction, {once:true});
body.addEventListener('keydown', onInteraction, {once:true});
*/

const onProgress = (event) => {
const progressBar = event.target.querySelector('.progress-bar');
const updatingBar = event.target.querySelector('.update-bar');
updatingBar.style.width = `${event.detail.totalProgress*100}%`;
if (event.detail.totalProgress == 1) {
    progressBar.classList.add('hide');
}
};



document.querySelector('#first').addEventListener('progress', onProgress);
document.querySelector('#second').addEventListener('progress', onProgress);


$('.card').on('click', function () {  
    $(this).toggleClass('flipped');
});
$('.user-direct-btn').click(function(e){
    e.stopPropagation();
})


//LOADING SCREEN ANIMATION UNUSED
/*
$(window).load(function() {
    setTimeout(function(){
        $("#loading-txt").fadeOut(complete=txtChangeFadeIn);
    }, 1500);
    function txtChangeFadeIn(){
        document.getElementById("loading-txt").textContent="welcome";
        $("#loading-txt").removeClass("loading")
        setTimeout(function() {
            $("#loading-txt").fadeIn(complete=garageDoorSlideUp);
        }, 500)    
    };
    function garageDoorSlideUp(){
        setTimeout(function(){
            $("#garage-door-loader").animate({top: '-900px'}, 'slow');
            document.getElementsByTagName("html")[0].style = 'overflow-y: visible';
        }, 2500)

        setTimeout(function(){
            $("#garage-door-loader").addClass('gone')
        }, 8000)
    }
})
*/
