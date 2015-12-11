/**
 * Client side script.
 * @author Alvin Lin (alvin.lin.dev@gmail.com)
 */


$(document).ready(function() {
  $.get("/check_upstate", function(data) {
    var stat = data.scan.tcp;
    if (stat && stat["25565"]["product"] == "Minecraft") {
      $("#upstate").text("Server online!").css("color", "green");
    } else {
      $("#upstate").text("Server offline!").css("color", "red");
    }
  });
});
