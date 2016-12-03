function update_department(major) {
  department = dept_by_major[major];
  $('#department').html(department); 
};

$('body').ready(function() {
  update_department($('#major').val());

  $('#major').change(function(e) {
    update_department(e.target.value);
  });
});
