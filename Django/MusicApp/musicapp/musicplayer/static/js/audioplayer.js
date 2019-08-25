var x = document.getElementById("myAudio");
var y = document.getElementById("current_song");
var z = document.getElementById("myAudioSource");
var startTime=0;
var stopTime=0;

// x.addEventListener('timeupdate',function(){
//     var currentTimeMs = x.currentTime*1000;
//     console.log(currentTimeMs);
// },false);


//var full_list = full_song_list;
//var cur_list = 0;
//var length_list = full_list.length;
//var current_song = full_list[0];

function setPosition() {
  document.getElementById("myAudio").currentTime = 5;
  document.getElementById("myAudio").play();
};

function playAudio() {
  startTime=getAudioCurrentTime();
  x.play();
  console.log(startTime);
};

function pauseAudio() {
  x.pause();
  stopTime=getAudioCurrentTime();
  console.log(stopTime);
};

function playNext() {
  // cur_list = cur_list + 1;
  // if (cur_list === length_list){
  //   cur_list = 0;
  // }
  // current_song = full_list[cur_list];
  // y.textContent=current_song;
  // z.src = "/static/musicapp/audiofiles/"+current_song;
  x.load();
  playAudio();
};

function playPrevious() {
  // cur_list = cur_list - 1;
  // if (cur_list === -1){
  //   cur_list = length_list-1;
  // }
  // current_song = full_list[cur_list];
  // y.textContent=current_song;
  // z.src = "/static/musicapp/audiofiles/"+current_song;
  x.load();
  playAudio();
};

function getAudioCurrentTime(){
  var m = document.getElementById("myAudio").currentTime;
  return m
}

// Submit post on submit
$('#record-event-form').on('submit', function(event){
  event.preventDefault();
  var m = getAudioCurrentTime();
  console.log("form 2 submitted!");  // sanity check
  console.log(m);
  //alert(m);
});

$("#button-play").click(function(event) {
    var form = $(this).closest("form");
    event.preventDefault();
    var m = getAudioCurrentTime();
    console.log("Start Time");
    $.ajax({
        type: "POST",
        // url: "/new/event/",
        url: "/createevent/",
        data: {
            user_id: "admin",
            track_id: "Numb",
            track: form.attr("track-info"),
            track_start_time: "2019-08-25 03:40:26.260524",
            track_end_time: "2019-08-25 03:45:26.260524",
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        },
        success: function(result) {
            console.log(startTime);
        },
        error: function(result) {
            console.log('error');
        }
    });
    return false; //<---- move it here
});
