var vrvToolkit = new verovio.toolkit();

$.get("music/Chopin_Etude_op.10_no.9.mei", function(data) {
    var svg = vrvToolkit.renderData(data, {});
    $("#transcription").html(svg);
    $("#transcription svg").width("100%").height("100%");
}, "text");
