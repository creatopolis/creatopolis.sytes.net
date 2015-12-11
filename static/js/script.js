/**
 * Client side script.
 * @author Alvin Lin (alvin.lin.dev@gmail.com)
 */


$(document).ready(function() {
  $.get("/check_upstate", function(data) {
    console.log(data);
  });
});
