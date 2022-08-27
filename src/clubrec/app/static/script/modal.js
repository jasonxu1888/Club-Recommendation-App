$(document).ready(function () {
    console.log("system ready called  ddd");
    // example: https://getbootstrap.com/docs/4.2/components/modal/

    let EditOrCreateStudent = null //true for edit, false for create
    let StudentId = null //save student id that needs to be edited
    let EditOrCreateClub = null //true for edit, false for create
    let ClubId = null //save club id that needs to be edited

    // modal for Student table
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes
        //true for edit, false for create
        
        const modal = $(this)
        if (taskID === 'New Student') {
            modal.find('.modal-title').text(taskID)
            modal.find('.modal-title').text(taskID)
            modal.find('.form-control-fname').val('');
            modal.find('.form-control-lname').val('');
            modal.find('.form-control-curyear').val('');
            modal.find('.form-control-degree').val('');
            modal.find('.form-control-gradyear').val('');
            modal.find('.form-control-deptid').val('');
            EditOrCreateStudent = false
        } else {
            modal.find('.modal-title').text('Edit Student ' + taskID)
            EditOrCreateStudent = true
            StudentId = taskID
        }

        if (content) {
            var space_separated_values = content.split(',,,')
            modal.find('.form-control-fname').val(space_separated_values[0]);
            modal.find('.form-control-lname').val(space_separated_values[1]);
            modal.find('.form-control-curyear').val(space_separated_values[2]);
            modal.find('.form-control-degree').val(space_separated_values[3]);
            modal.find('.form-control-gradyear').val(space_separated_values[4]);
            modal.find('.form-control-deptid').val(space_separated_values[5]);
        } else {
            modal.find('.form-control').val('');
        }
    })

    //modal for club table
    $('#club-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (taskID === 'New Club') {
            modal.find('.modal-title').text(taskID)
            modal.find('.form-control-clubname').val('');
            modal.find('.form-control-clubdesc').val('');
            modal.find('.form-control-clubage').val('');
            EditOrCreateClub = false
        } else {
            modal.find('.modal-title').text('Edit Club ' + taskID)
            $('#task-form-display').attr('taskID', taskID)
            EditOrCreateClub = true
            ClubId = taskID
        }

        if (content) {
            var space_separated_values = content.split(',,,')
            modal.find('.form-control-clubname').val(space_separated_values[0]);
            modal.find('.form-control-clubdesc').val(space_separated_values[1]);
            modal.find('.form-control-clubage').val(space_separated_values[2]);
        } else {
            modal.find('.form-control').val('');
        }
    })

    $('#dept-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (taskID === 'New Task') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Edit Task ' + taskID)
            $('#task-form-display').attr('taskID', taskID)
        }
    })
    
    $('#submit-query').click(function () {
        requrl = '/dept-activity/' +  $('#dept-modal').find('.form-control-deptlike').val();
        location.href=requrl;
        // may need to do a jquery set table data..
        // follow up with team on approach.
        /*
        $.ajax({
            type: 'GET',
            url: requrl,
            success: function (res) {
                console.log(res.response);
                //location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
        */
    });

    //search funcitonality for activity by description
    $('#submit-club-query').click(function(event) {
        var description = $('#club-description').val();
        requrl = '/clubs/' + description
        location.href=requrl;
    });

    //save change button for student table for creating and editing functionality for students
    $('#submit-student').click(function () {
        $.ajax({
            type: 'POST',
            url: EditOrCreateStudent ? '/edit-student/' + StudentId : '/create-student',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'fname': $('#task-modal').find('.form-control-fname').val(),
                'lname': $('#task-modal').find('.form-control-lname').val(),
                'curyear': $('#task-modal').find('.form-control-curyear').val(),
                'degree': $('#task-modal').find('.form-control-degree').val(),
                'gradyear': $('#task-modal').find('.form-control-gradyear').val(),
                'deptid': $('#task-modal').find('.form-control-deptid').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
 
    //save change button for club table for creating AND editing functionality for clubs
    $('#submit-club').click(function () {
        $.ajax({
            type: 'POST',
            url: EditOrCreateClub ? '/edit-club/' + ClubId : '/create-club',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'club_name': $('#club-modal').find('.form-control-clubname').val(),
                'club_desc': $('#club-modal').find('.form-control-clubdesc').val(),
                'club_age': $('#club-modal').find('.form-control-clubage').val(),
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    //remove button for student table to remove student
    $('.remove-student').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete-student/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });


    //TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO 
    //remove button for club table to remove club
    $('.remove-club').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete-club/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});