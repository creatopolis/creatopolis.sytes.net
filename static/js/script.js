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
  $.getJSON("/check_upstate", function(data) {
    if (data.online) {
      $("#server-status").text("Server online!").css("color", "#35a720");
      // For each player, add them to the <ul>
      // $("#server-players")
    } else {
      $("#server-state").text("Server offline!").css("color", "#ff3535"));
    }
    $("#server-status-spinner").hide();
  });
}

$(document).ready(function() {
  checkUpstate();

  $("#check_upstate").click(checkUpstate);
});
