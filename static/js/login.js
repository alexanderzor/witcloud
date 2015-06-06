$(document).ready(function() {
	var styles = {
		width: $(window).width(),
		height: $('html').height()
	};
	$('.log-pop-up').css({
		'width' : styles.width,
		'height' : styles.height
	});


	$('.log-in').click(function() {
		$('.log-pop-up').fadeIn(150);
	}); //end click.

	$('.log-pop-up, .close').click(function() {
		$('.log-pop-up').css({'display' : 'none'});
	}); // end click. 

	$('.log-window').click(function(e) {
		e.stopPropagation();
	}); //end click.
}); //end ready.