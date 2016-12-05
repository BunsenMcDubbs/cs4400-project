function reset_search() {
  $('#title').val(form_defaults['title']);
  $('select').each(function(index, select) {
    select.value = form_defaults[select.id];
  });
  $('#search_type-2')[0].checked = true;
}

$('body').ready(function() {
  $('#reset_search').click(reset_search);
});
