$(document).ready(function() {
	function resetIFrame() {
		var activeVideo = $(this).find('.playing');
		var src = activeVideo.attr('src');
		activeVideo.attr('src', '');
		activeVideo.attr('src', src);
	}

	function pasteText() {
		var title = $(this).find('.header-vid-1').text();
		var from = $(this).find('.header-vid-2').text();
		var vid_date = $(this).find('.date-vid').text();
		$('.wrp-video').find('.title-video').text(title);
		$('.wrp-video').find('.title-p-vids').text(title);
		$('.wrp-video').find('.author-p-vids').text(from);
		$('.wrp-video').find('.date-p-vids').text(vid_date);
	}

	var window_height = $(window).height();
	var document_height = $(document).height();

	$('.pop-up-videos').click(function() {
		$(this).css({'height' : 0});
		resetIFrame.call(this); //see the function in the top.
	}); // end click

	$('.wrp-video').click(function(e) {
		e.stopPropagation();
	}); //end click


	var links = $('.video-lesson').find('.vidli');
	for (var b=0; b<links.length; b+=1) {
		links[b].number = b;
	}
	links.click(function() {
			$('.pop-up-videos').css({'height' : document_height});
			var theVideos = $('.link-videos').find('.link-vid');
			$(theVideos).css({'display' : 'none'}).removeClass('playing');
			$(theVideos[this.number]).css({'display' : 'block'}).addClass('playing');
			//resetIFrame.call(this);
			var styles = {
				top: (window_height / 2),
				margin_left: $('.wrp-video').outerWidth() / 2,
				margin_top: $('.wrp-video').outerHeight() / 2
			};
		$('.wrp-video').css({'margin-left' : -styles.margin_left});
		if (styles.top - styles.margin_top > 0) { //checking if pop-up is ok with window size height.
			$('.wrp-video').css({'top' : styles.top, 'margin-top' : -styles.margin_top});
		} else {
			$('.wrp-video').css({'top' : '50px', 'margin-top' : 0});
		}
		pasteText.call(this);
		$('html, body').animate({scrollTop : 0}, 650);

		/*function resetIFrame() {
			var src = $(theVideos[this.number]).attr('src');
			$(theVideos[this.number]).attr('');
		}*/
	});// end click
}); //end click