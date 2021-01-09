// external js: flickity.pkgd.js
// fit text
$(".card.card-body h5, h6, #button").fitText(1, { minFontSize: '15px', maxFontSize: '25px' });
$(".card-text").fitText(.8);
$(".sperate").fitText(1, { minFontSize: '12px', maxFontSize: '30px' });

// header
$('.main-carousel').flickity({
  // options
    cellAlign: 'left',
    prevNextButtons: false,
    pageDots: false,
    autoPlay: true,
    draggable: false,
    contain: true,
});

var $carousel = $('.main-carousel').flickity({
  imagesLoaded: true,
  percentPosition: false,
});

var $imgs = $carousel.find('.carousel-cell img');
// get transform property
var docStyle = document.documentElement.style;
var transformProp = typeof docStyle.transform == 'string' ?
  'transform' : 'WebkitTransform';
// get Flickity instance
var flkty = $carousel.data('flickity');

$carousel.on( 'scroll.flickity', function() {
  flkty.slides.forEach( function( slide, i ) {
    var img = $imgs[i];
    var x = ( slide.target + flkty.x ) * -1/3;
    img.style[ transformProp ] = 'translateX(' + x  + 'px)';
  });
});
// end header

// content
$('.main-carousel-2').flickity({
  // options
    cellAlign: 'left',
    pageDots: false,
    draggable: false,
    contain: true,
});
// end content


//external js: owl.carousel.js
//content
$('#content').owlCarousel({
    nav:true,
    lazyLoad:true,
    loop:true,
    center:true,
    margin:10,
    navText:['<i class="fas fa-chevron-left fa-2x"></i>', '<i class="fas fa-chevron-right fa-2x"></i>'],
    responsive:{
        0:{
            items:2,
            margin:3,
            nav:false,
            center:false,
        },
        600:{
            items:3,
            center:false,
            nav:false,
        },
        1000:{
            items:5,
            mouseDrag:false,
            slideBy:3,
        }
    }
});

$('#special').owlCarousel({
    loop:false,
    margin:10,
    nav:true,
    center:true,
    navText:['<i class="fas fa-chevron-circle-right"></i>', '<i class="fas fa-chevron-circle-right"></i>'],
    responsive:{
        0:{
            items:2,
            margin:3,
            center:false,
            nav:false,
        },
        600:{
            items:3,
            center:false,
            nav:false,
        },
        1000:{
            items:5,
            mouseDrag:false,
            slideBy:3,
        }
    }
});

$('#image-content').owlCarousel({
    nav:false,
    lazyLoad:false,
    loop:true,
    center:false,
    item:1,
    mouseDrag:true,
});
//end content
//reveal

