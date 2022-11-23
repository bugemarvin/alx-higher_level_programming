/*a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header */
const $ = window.$;
$('#red_header').click(function red() {
  $("#red_header").css("color", "#FF0000");
});
