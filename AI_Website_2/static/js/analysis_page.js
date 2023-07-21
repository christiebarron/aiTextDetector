function loadData() {
    var teacher = $('#teacher').val();

    // Fetch student names
    $.ajax({
        url: '/get_students',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ teacher: teacher }),
        success: function(response) {
            // Update student list
            var students = response.students;
            // ...
        }
    });

    // Fetch class data
    $.ajax({
        url: '/get_class_data',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ teacher: teacher }),
        success: function(response) {
            // Update class data visualization
            var classData = response.classData;
            // ...
        }
    });
}