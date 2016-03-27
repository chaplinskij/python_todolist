$(document).ready(function() {
	//Add a project
	$('#addProject').click( function(){
		var query = {};
		query.name = prompt("Please enter the name of new project");
		if (query.name != null) {
			$.ajax({
				type: "POST",
				url: "/project/add_project/",
				dataType:"text",
				data: query,
				success:function(response){
					$('#projectList').append(response);
				}
			});
		}
	});


	//Rename projects/task
	$('.glyphicon-pencil').on('click', function () {
		if($(this).hasClass('project-pencil')){
			var project_id = this.id.replace('project-pencil-', '');
			var elem = $("#project-name-" + project_id);
			elem.removeAttr('readonly').focus().select();


			elem.focusout(function(){
				$(this).prop('readonly', true);
				var query = {};
				query.id = project_id;
				query.name = $("#project-name-" + project_id).val();

				console.log(query);
				$.ajax({
					type: "POST",
					url: "/project/change_project/",
					dataType:"text",
					data: query
				});
			});
		}
		else if($(this).hasClass('task-pencil')){
			var task_id = this.id.replace('task-pencil-', '');
			var elem = $("#task-name-" + task_id);
		    elem.prop('contenteditable', true).focus();

			elem.focusout(function(){
				$(this).prop('contenteditable', false);
				var query = {};
				query.id = task_id;
				query.name = $("#task-name-" + task_id).text();
				$.ajax({
					type: "POST",
					url: "/project/change_task/",
					dataType:"text",
					data: query
				});
			});
		}
	});

	//Delete projects/task
	$('.glyphicon-trash').on('click', function () {
		if($(this).hasClass('trash-task')){
			var query = {};
			query.id = $(this).closest('tr')[0].id.replace('task-', '');
			$.ajax({
				type: "POST",
				url: "/project/delete_task/",
				dataType:"text",
				data: query,
				success:function(){
					$('#task-'+query.id).remove();
				}
			});
		}
		else if($(this).hasClass('trash-project')){
// СЮДА ДОБАВИТЬ КОД ДЛЯ УДАЛЕНИЯ ПРОЕКТА
		}

	});

	//Add new task
	$('.add-task').on('click', function(){
		var query = {};
		query.project = $(this).parent().parent().children('.form-control')[0].id.replace('new-task-name-', '');
		query.name = $(this).parent().parent().children('.form-control')[0].value;
		$(this).parent().parent().children('.form-control')[0].value = null;
		if (query.name != null) {
			$.ajax({
				type: "POST",
				url: "/project/add_task/",
				dataType:"text",
				data: query,
				success:function(response) {
					$('#list_tasks-'+query.project).append(response);

				}
			});

		}
	});

});


