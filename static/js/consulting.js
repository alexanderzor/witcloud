$(document).ready(function() {
	function findAndToggle(height) {
		$(this).find('.pop-up-consult').stop().animate({'height' : height}, 300);
	}

	$('.pic-consult').hover(function() {
		findAndToggle.call(this, '100%');
	}, function() {
		findAndToggle.call(this, 0);
	}); // end hover

	var socialBut = $('.pop-up-consult').find('.social-but');
	var styles = {
		display : 'none',
		height: '100%',
		width: '100%',
		background: 'rgba(255,255,255,0.3)',
		position: 'absolute',
		left: 0,
		top: 0
	};
	$(socialBut).click(function() {
		$('.appended').fadeOut(200, function() {
			$(this).remove();
		}); //to clear hover effect before next adding.
		var appendIt = document.createElement('div');
		$(appendIt).css({
			'display' : styles.display,
			'height' : styles.height,
			'width' : styles.width,
			'background-color' : styles.background,
			'position' : styles.position,
			'left' : styles.left,
			'top' : styles.top
		});
		$(appendIt).appendTo(this).fadeIn(300).addClass('appended');

		var thisLinks = $(this).parent().find('.social-link');
		var thisButs = $(this).parent().find('.social-but');
		for (var i=0; i<thisButs.length; i+=1) {
			thisButs[i].number = i;
		}
		thisLinks.css({'width' : 0});
		$(thisLinks[this.number]).animate({'width' : '100%'}, 300);
	}); //end click

	/* $('.pop-up-consult').mouseover(function() {
		$(this).find('.appended').fadeOut(300);
	}); //end mouseover

	$(socialBut).mouseover(function(e) {
		e.stopPropagation();
		//$(socialBut).find('.appended').css({'display' : 'none'});
	}); //end mouseover */


}); //end ready