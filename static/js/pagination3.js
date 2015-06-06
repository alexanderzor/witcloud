$(document).ready(function() {
	//had no time to refactor pagination.js code - so created new one :( if someone is going to work with it - sorry.
	var posts = $('.notes').find('.vidli');
	for (var i=9; i<posts.length; i+=1) { // making posts from 5 invisble.
		$(posts[i]).css({'display' : 'none'});
	}

	var paginumber = $('.pagination-2').find('.page-numb-2');
	for (var u=0; u<paginumber.length; u++) {
		paginumber[u].number = u;
	}
	paginumber.click(function() {
		paginumber.removeClass('active-page');
		$(this).addClass('active-page');

		var pageNumber = +$(this).text();
		posts.css({'display' : 'none'});
		for (var j = (9 * pageNumber) - 9; j < 9 * pageNumber; j+=1) {
			$(posts[j]).css({'display' : 'inline-block'});
		}

	}); //end click

	var rightArrow = $('.pagination-2').find('.page-ar-2')[1];
	$(rightArrow).click(function() {
		var lastNumber = +$(paginumber[paginumber.length - 1]).text();
		console.log(paginumber);
		for (var j=0; j<paginumber.length; j+=1) {
			if (posts[(9 * lastNumber) - 9]) { //checking if there are some posts on requested page. 
				$(paginumber[j]).text(lastNumber);
				lastNumber +=1;
			}
		}
		if (+$(paginumber[paginumber.length - 1]).text() < +$(paginumber[paginumber.length - 2]).text()) {
			+$(paginumber[paginumber.length - 1]).text(+$(paginumber[paginumber.length - 2]).text() + 1);
		} else if (+$(paginumber[0]).text() > +$(paginumber[1]).text()) {
			+$(paginumber[0]).text(+$(paginumber[1]).text() -1);
		}
		paginumber.removeClass('active-page');
	}); //end click

	var leftArrow = $('.pagination-2').find('.page-ar-2')[0];
	$(leftArrow).click(function() {
		var firstNumber = +$(paginumber[0]).text();
		for (var j=paginumber.length - 1; j>=0; j-=1) {
			if (firstNumber !== 1) {
				$(paginumber[j]).text(firstNumber);
				--firstNumber;
			} else {
				$(paginumber[0]).text(1);
			}
		}
		paginumber.removeClass('active-page');
	}); //end click
}); // end ready	