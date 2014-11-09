$(function(){
	$('button').click(function(){
		var user = $('#txtUsername').val();
		var pass = $('#txtPassword').val();
		$.ajax({
			url: '/signUpUser',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				var data = JSON.parse(response);
				alert(data)
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
