var main = function(){
$('.default').addClass('active');
$('#allnone').removeClass('letter');
}
$(function(){
  $('#reload').click(function(){
  	var inArr = [];

 	 $('.noun.active').each(function() {
	inArr.push($(this).text().toLowerCase());
  	});
  var lntmp = inArr.length
  inArr.push(':catbrk:');
    $('.adj.active').each(function(){
      inArr.push($(this).text().toLowerCase());
    });
  inArr.push(':letbrk:');
  lntmplet = inArr.length
  $('.letter.toggle.active').each(function(){
    inArr.push($(this).text().toUpperCase());
  });
  if(inArr.length == lntmplet){
    	$('#namegen').html('<p>select<br>letters');
  }
	if((inArr.length - lntmp - 1) == 0 || lntmp == 0 ){
	$('#namegen').html('<p>select<br>categories');
	} else{
	$.ajax({
       	type: "GET",
	url: "scripts",
	data: {
		types: inArr
	},
	success: function(msg){
	$('#namegen').html(msg);
	}
	})
	}
    });


})

$(function() {
	$('.toggle').click(function() {
		var div = $(this);
		if(div.hasClass('active')) {
			div.removeClass('active');
		} else {
			div.addClass('active');
		}
	});
})

  $(function() {
  	$('#allnone').click(function() {
  		var div = $(this);
  		if(div.hasClass('active')) {
        $('.letter').each(function(){
          $(this).addClass('active');
        });
  			div.removeClass('active');
        div.text(' NONE');

  		} else {
  			div.addClass('active');
        div.text(' ALL');
        $('.letter').each(function(){
          $(this).removeClass('active');
        });
  		}
  	});
})

$(document).ready(main)
