var vrvToolkit = new verovio.toolkit();

$(function() {
  let searchParams = new URLSearchParams(window.location.search);
  var score = searchParams.get("score");
  $("#scan embed").attr("src", "music/" + score + ".pdf");

  $.get("music/" + score + ".mei", function(data) {
      var svg = vrvToolkit.renderData(data, {});
      $("#transcription").html(svg);
      $("#transcription svg").width("100%").height("100%");
  }, "text");
});
