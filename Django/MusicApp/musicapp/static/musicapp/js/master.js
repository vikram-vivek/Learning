  var x = document.getElementById("myAudio");
  var y = document.getElementById("current_song");
  var z = document.getElementById("myAudioSource");
  var full_list = full_song_list;
  var cur_list = 0;
  var length_list = full_list.length;
  var current_song = full_list[0];

  function playAudio() {
    x.play();
  }

  function pauseAudio() {
    x.pause();
  }

  function playNext() {
    cur_list = cur_list + 1;
    if (cur_list === length_list){
      cur_list = 0;
    }
    current_song = full_list[cur_list];
    y.textContent=current_song;
    z.src = "/static/musicapp/audiofiles/"+current_song;
    x.load();
    playAudio();
  }

  function playPrevious() {
    cur_list = cur_list - 1;
    if (cur_list === -1){
      cur_list = length_list-1;
    }
    current_song = full_list[cur_list];
    y.textContent=current_song;
    z.src = "/static/musicapp/audiofiles/"+current_song;
    x.load();
    playAudio();
  }
