
//landing page gradient
import { Gradient } from "https://gist.githack.com/jordienr/64bcf75f8b08641f205bd6a1a0d4ce1d/raw/35a5c7c1ddc9f97ec84fe7e1ab388a3b726db85d/Gradient.js";

const gradient = new Gradient();
gradient.initGradient("#gradient-canvas");

var controller = new ScrollMagic.Controller();
var scene = new ScrollMagic.Scene({
  triggerElement: "#trigger-second",
  triggerHook: "onEnter"
})
  .setClassToggle(".change-position-on-scroll, nav", "is-relative")
  .addTo(controller);

var blackoutTweenFirst = TweenMax.to("#second .blackout", 1, {
  opacity: 0,
  ease: Linear.easeNone
});

var scene = new ScrollMagic.Scene({
  duration: "100%",
  triggerElement: "#blackout-first",
  triggerHook: "onEnter"
})
  .setClassToggle("#second .blackout", "is-visible")
  .setTween(blackoutTweenFirst)
  .addTo(controller);


$('.nft-prototype-card').click(function(){
  var clickedButton = $(this);
  this.remove();
  $('.nft-prototype-card-wrapper').prepend(clickedButton);
});
$(window).on('load', function(){
  function rotateCard(){
    if ($('.nft-prototype-card-wrapper').is(":hover") == false){
      $('.nft-prototype-card-wrapper').prepend($('.nft-prototype-card').last());
    };
    setTimeout(rotateCard,7000)
  }
  setTimeout(rotateCard,7000);
});

//Car company logo carousel
$(window).on('load', function(){
  // Please run it with window.onload, not with document.ready
  initSmoothScrolling('.block','smoothscroll');
});

function initSmoothScrolling(container,animation){
 /*
	* @param {String} container Class or ID of the animation container
	* @param {String} animation Name of the animation, e.g. smoothscroll
	*/
	var sliderWidth = 0;	
	var animationWidth = 0;	
	var sliderHeight = $('>div>div:first-of-type',container).outerHeight(false);

	$('>div>div', container).each(function(){				
		animationWidth += $(this).outerWidth(false);		
	});
	
	// detect number of visible slides
	var slidesVisible = $(container).width() / $('>div>div:first-of-type',container).outerWidth(false);	
	slidesVisible = Math.ceil(slidesVisible);

  // count slides to determine animation speed
	var slidesNumber = $('>div>div', container).length;
	var speed = slidesNumber*4;
	
// append the tail	
	$('>div>div',container).slice(0,slidesVisible).clone().appendTo($('>div',container));	

	// Detect the slider width with appended tail
	$('>div>div', container).each(function(){
		sliderWidth += $(this).outerWidth(false);
	});

	// set slider dimensions
	$('>div',container).css({'width':sliderWidth,'height':sliderHeight});
  
// Insert styles to html
	$("<style type='text/css'>@keyframes "+animation+" { 0% { margin-left: 0px; } 100% { margin-left: -"+animationWidth+"px; } } "+$('>div>div:first-of-type',container).selector+" { -webkit-animation: "+animation+" "+speed+"s linear infinite; -moz-animation: "+animation+" "+speed+"s linear infinite; -ms-animation: "+animation+" "+speed+"s linear infinite; -o-animation: "+animation+" "+speed+"s linear infinite; animation: "+animation+" "+speed+"s linear infinite; }</style>").appendTo("head");	

	// restart the animation (e.g. for safari & ie)	
	var cl = $(container).attr("class");
	$(container).removeClass(cl).animate({'nothing':null}, 1, function () {
		$(this).addClass(cl);
	});
}

$.fn.isInViewport = function() {
  var elementTop = $(this).offset().top;
  var elementBottom = elementTop + $(this).outerHeight();

  var viewportTop = $(window).scrollTop();
  var viewportBottom = viewportTop + $(window).height();

  return elementBottom > viewportTop && elementTop < viewportBottom;
};

$(window).on('resize scroll', function() {
  $('.show-on-scroll').each(function() {
    if ($(this).isInViewport()) {
      $(this).addClass('is-visible')
    } else {
    }
  });
});

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

//document.querySelector('#first').addEventListener('progress', onProgress);
document.querySelector('#car-model').addEventListener('progress', onProgress);

$(window).blur(function(){
    $('#car-model').hide();
  });
  $(window).focus(function(){
    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {

    } 
    else{
      if (window.innerWidth > 700){
        $('#car-model').show();
      }
    }
  });


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
