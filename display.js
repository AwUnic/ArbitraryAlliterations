var main = function(){
  alert('hola')
$('.default').addClass('active');
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

$(document).ready(main)
