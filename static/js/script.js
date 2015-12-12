/**
 * Client side script.
 * @author Alvin Lin (alvin.lin.dev@gmail.com)
 */


function check_upstate() {
  $.getJSON("/check_upstate", function(data) {
    console.log(data);
    if (data.online) {
      $("#upstate").text("Server online!").css("color", "green");
    } else {
      $("#upstate").text("Server offline!").css("color", "red");
    }
  });
}

$(document).ready(function() {
  check_upstate();

  $("#check_upstate").click(check_upstate);
});
