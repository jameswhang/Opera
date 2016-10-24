$(document).ready(function() {
    $('.btn').on('click', function() {
        var githubID = $(this).attr('id');
        $.get('http://localhost:3000/count_push/' + githubID, function(data) {
            console.log(data);
        });
    });
});
