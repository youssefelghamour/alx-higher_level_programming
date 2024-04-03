const $ = window.$;

$(document).ready(() => {
  const fetchTranslation = () => {
    const languageCode = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + languageCode, (data) => {
      $('#hello').text(data.hello);
    });
  };

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress((e) => {
    if (e.which === 13) fetchTranslation();
  });
});
