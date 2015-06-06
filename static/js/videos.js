$(document).ready(function() {

  function setActiveClassToThis() {
    lists.removeClass('active-click-vids');
    $(this).addClass('active-click-vids');
    console.log(this);
  }

    var videos = $('.video-wrp').find('video');
    var lists = $('.body-as').find('.post-as');
 
  for (var i = 0; i < videos.length; i++) {
    lists[i].number = i;
  }
    var lastClicked = {
        count: 0,
    };
    
    lists.click(function() {
        $(videos[lastClicked.count])[0].pause();  //this is previous clicked video
        setActiveClassToThis.call(this);
        $(videos).css( {'display' : 'none'} );
        $( videos[this.number] ).css( {'display' : 'block'} );
        lastClicked.count = this.number;
    }); //end click


 /* var previous_video = [

  {
    count: 0,
    src_v: "https://www.youtube.com/embed/TsNmOdt5FgI"
  }

  ];

  lists.click(function() {
    setActiveClassToThis.call(this);

    $(videos).css( {'display' : 'none'} );
    $( videos[this.number] ).css( {'display' : 'block'} );

    previous_video.push(

    {
      count: this.number,
      src_v: $(videos[this.number]).attr("src")
    }

    );

    $( videos[ previous_video[previous_video.length - 2].count ] ).attr("src", "");
    $( videos[ previous_video[previous_video.length - 2].count ] ).attr("src", previous_video[previous_video.length - 2].src_v );
    




  }); */



});