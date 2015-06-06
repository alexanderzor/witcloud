$(document).ready(function() {
	var chat_but = $('.chat-form-but');

	chat_but.click(function() {

		var months = [
				"Января", "Февраля", "Марта",
				"Апреля", "Мая", "Июня", "Июля",
				"Августа", "Сентября", "Октября",
				"Ноября", "Декабря"	
			];

		var texts = $('.chat').val();
		var dates = new Date();
		var date = dates.getDate() + " " + months[ dates.getMonth() ] + " " + dates.getFullYear() + " " +  dates.getHours() + ":" + dates.getMinutes() + ":" + dates.getSeconds();
		var post_it = "<div class=\"post-ch\"><div class=\"info-ch\"><span class=\"who-ch\">Oleksiy Ovdienko,</span><span class=\"when-ch\">" + " " + date + "</span></div><div class=\"mess-ch\">" + texts + "</div></div>";
		
		$('.messages-ch').append(post_it);
		clearTextarea();
	}); //end click

	$('.chat').keydown(function(e) {
		if (e.which == 13) {
			chat_but.click();
		}
	});

	function clearTextarea() {
		$('.chat').val('');
	}
	
});