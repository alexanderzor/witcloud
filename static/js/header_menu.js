$(document).ready(function() {
    var a = $('.nav-h').find('a'); //checking what link in header we shoul to mark as active.
    a.each(function() {
        if ( (window.location.href).indexOf($(this).attr('href')) >=0 ) $(this).find('li').addClass('active-click');
    }); //end each.
	//$('a[href="'+ window.location.href +'"]').find('li').addClass('active-click');

	function setActiveClassToThis() {
		li.removeClass('active-click');
		$(this).addClass('active-click');
	}

	$('.user-h').click(function() {
		$(this).find('.drop-menu').stop().toggle(300);
	}); //end click

	$('.drop-menu, header').on('mouseover', function(e) {
		e.stopPropagation();
	});

	$('html').on('mouseover', function(e) {
		$('.drop-menu').fadeOut('fast');
	});
	
	var li = $('.nav-h').find('li');
	li.click(function () {
		setActiveClassToThis.call(this);
	}); //end click
}); //end ready