var main = function(){
$('#animal').addClass('active');
}
$(function(){
  $('#reload').click(function(){
  	var inArr = [];
 	 $('.toggle.active').each(function() {
	inArr.push($(this).text().toLowerCase());	
  	});
	if(inArr.length == 0){
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
