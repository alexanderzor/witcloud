$(document).ready(function() {
	function scrollToNeed() {
		$('html, body').animate({scrollTop : $('.s-2').offset().top}, 1000);
	}

	$('.right-ribbon').click(function() {
		scrollToNeed();
	}); // end click.
}); // end ready.