$(document).ready(function() {
	function createUnderline() {
		var underline = document.createElement('div'); // the underline element.
		$(underline).css({ 
			'position' : 'absolute',
			'bottom' : '-20px',
			'left' : 0,
			'background-image' : 'url(images/html7/1.png)',
			'width' : '0',
			'height' : '10px',
			'display' : 'inline-block',
			'left' : '50%',
			'margin-left' : '-59.5px'
		}).addClass('under-line');

		 return function() { //closure to Append underline
		 	 $(this).append(underline);
			 $(underline).animate({'width' : '119px'}, 200);
		 };
	}

	function removeAllUnderlines(className, addBut) {
		li.find('.under-line').remove();
        if (!addButton) {
            li.find(className).text('');
        } else {
            addButton.find(className).text('');
        }
	}

	function createHoverText(className, whatElseDelete) {
		var hoverText = document.createElement('div');
		$(hoverText).css({
			'width' : '100%',
			'height' : '100%',
			'position' : 'absolute',
			'top' : 0,
			'right' : 0,
			'text-align' : 'right',
			'display' : 'none',
			'color' : '#0083C5'
		}).addClass(className); //here puts the argument.
		$(hoverText).html( '<p>' + $(this).text() + '</p>' );
		li.find('.'+ className).remove();
		if (whatElseDelete) $('.nav-hw').find('li').find('.'+ whatElseDelete).remove();
		$(this).append(hoverText);
		$(hoverText).fadeIn(550);
	}

	var li = $('.nav-hw').find('.ok-li');
	li.click(function() {
		var appendUnderline = createUnderline.call(this); //closure
		removeAllUnderlines('.hover-text');
		appendUnderline.call(this);
		createHoverText.call(this, 'hover-text', 'hover-text-add');
	}); // end click

	var addButton = $('.nav-hw').find('li');
	$(addButton[addButton.length - 1]).click(function() {
		removeAllUnderlines('.hover-text-add', true);
		createHoverText.call(this, 'hover-text-add', 'hover-text');
		$('html, body').animate({scrollTop : $('.s-2').offset().top}, 1000);;
	}); //end click

}); //end ready