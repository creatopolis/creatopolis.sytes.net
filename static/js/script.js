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
    .add("<span class='fa fa-spinner fa-spin fa-2x'></span>")
    .addClass("loading");
  $.getJSON("/check_upstate", function(data) {
    console.log(data);
    if (data.online) {
      $("#server-state")
        .empty()
        .add($("<span>Server online!</span>").css("color", "green"));
    } else {
      $("#server-state")
        .empty()
        .text($("<span>Server offline!</span>").css("color", "red"));
    }
  });
}

$(document).ready(function() {
  check_upstate();

  $("#check_upstate").click(check_upstate);
});
