/**
 * Client side script.
 * @author Alvin Lin (alvin.lin.dev@gmail.com)
 */

/**
 * This function sends an AJAX request to the server that queries the server
 * and returns data on the server's state, player count, etc.
 */
function checkUpstate() {
  $("#server-state")
    .empty()
    .append($("<span></span>").addClass("fa fa-spinner fa-spin fa-2x"));
  $.getJSON("/check_upstate", function(data) {
    if (data.online) {
      $("#server-state")
        .empty()
        .append(
          $("<span></span>").text("Server online!").css("color", "green"));
    } else {
      $("#server-state")
        .empty()
        .append($("<span></span>").text("Server offline!").css("color", "red"));
    }
  });
}

$(document).ready(function() {
  checkUpstate();

  $("#check_upstate").click(checkUpstate);
});
