/**
 * Client side script.
 * @author Alvin Lin (alvin.lin.dev@gmail.com)
 */

/**
 * This function sends an AJAX request to the server that queries the server
 * and returns data on the server's state, player count, etc.
 */
function checkUpstate() {
  $("#server-status-spinner").show();
  $("#server-status").hide();
  $.getJSON("/check_upstate", function(data) {
    if (data.online) {
      $("#server-status").text("Server online").css("color", "#35a720").show();
      $("#server-players").empty();
      $("#server-players").append($("<li></li>").text("Players Online:"));
      data.players_online.forEach(function(player) {
        $("#server-players").append($("<li></li>").text(player));
      });
    } else {
      $("#server-status").text("Server offline").css("color", "#ff3535").show();
    }
    $("#server-status-spinner").hide();
  });
}

$(document).ready(function() {
  checkUpstate();

  $("#check_upstate").click(checkUpstate);
});
