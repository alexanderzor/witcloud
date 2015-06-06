$(document).ready(function() {
	function getError(condition) {
			if ( condition ) {
				$(this).css({'border' : '1px solid red'}).addClass('error-class');
			} else {
				$(this).css({'border' : 'none'}).removeClass('error-class');
			}
		}

	var inputs = $('.inputs').find('input');
	inputs.keyup(function() {
		if ( !$(this).hasClass('nns') ) {
			getError.call(this, !$(this).val() );
			if ( $(this).hasClass('jmail') ) {
				getError.call(this, $(this).val().indexOf('@') === -1 || $(this).val().indexOf('.') === -1);
			}
		}// end if
         if ( $('.inputs').find('.error-class').length === 0 ) {
            $('.error').css({'display' : 'none'});
         } else {
            $('.error').css({'display' : 'block'});
         }
	}); //end keyup
    
    $('#submit-main').click(function(e) {
        inputs.each(function() {
            if ( !$(this).hasClass('nns') ) {
                getError.call(this, !$(this).val() );
                if ( $(this).hasClass('jmail') ) {
                    getError.call(this, $(this).val().indexOf('@') === -1 || $(this).val().indexOf('.') === -1);
                } 
            }
        }); //end each
         if ( $('.inputs').find('.error-class').length === 0 ) {
            $('.error').css({'display' : 'none'});
         } else {
            $('.error').css({'display' : 'block'});
             return false;
         }
    }); //end click.
});