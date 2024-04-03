const $ = window.$;
window.onload = function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + languageCode, function (data) {
      $('#hello').text(data.hello);
    });
  });
};
