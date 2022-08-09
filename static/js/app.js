$('document').ready(function() {
   $('#fullpage').fullpage({
             scrollingSpeed:1000,
							navigation:true,
							slidesNavigation:true,
							controlArrows:false,
							scrollbars:true,
							scrollOverflow:true,
							overflow: auto,
							anchors: ['first_page', 'second_page', 'third_page'],
     					sectionsColor : ['#BD97CB', '#495C83', '#4D4C60'],

         });
   $(document).on('click', '#view-tools-button', function(){
  fullpage_api.moveTo('anchor-second_page', 1);
});
   setTimeout(function(){
    $.fn.fullpage.reBuild();
}, 100);
$(".tool-list-button").click(function(){
  $(".tool-list").slideToggle(300);
  $("#view-tools-svg" ).toggleClass("view-tools-svg_active");
  $(".tool-list-button" ).toggleClass("tool-list-button_active");
});

var windowsize = $(window).width();

$(window).resize(function() {
  var windowsize = $(window).width();
});

$(window).resize(function() {
  if ($(window).width() > 1000) {
      $(".tool-list").show();
  }
 else {
 
 }
});
});

