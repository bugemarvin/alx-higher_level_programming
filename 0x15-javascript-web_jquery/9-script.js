/* a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello */
const $ = window.$;
$('document').ready(() => {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', (data) => {
    $('#hello').text(data.hello);
  });
});
