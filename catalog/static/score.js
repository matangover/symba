var vrvToolkit = new verovio.toolkit();

$(function() {
  $.get(transcriptionUrl, function(data) {
      var svg = vrvToolkit.renderData(data, {});
      $("#transcription").html(svg);
      $("#transcription svg").width("100%").height("100%");
  }, "text");
});
