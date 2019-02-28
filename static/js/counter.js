$(document).ready(function(){
	var counter = document.getElementById("counter"),
		seconds = 0, minutes = 0, hours = 0;
					
	document.getElementById("init_printer").addEventListener("click", start_count);	
				
	function start_count(){
		setInterval(stopwatch, 1000);
	}
				
	function stopwatch(){
		seconds++;
		if(seconds >= 60){
			seconds = 0;
			minutes++;
			if(minutes >= 60){
				minutes = 0;
				hours++;
			}
		}
					
		counter.innerHTML = (hours ? (hours > 9 ? hours : "0" + hours) : "00") + ":" + 
							(minutes ? (minutes > 9 ? minutes : "0" + minutes) : "00") + ":" +
							(seconds > 9 ? seconds : "0" + seconds);
	}
	
	//requst
	$('form').on('submit', function(){
		
		$.ajax({
		
			url: '/getData',
			type: 'POST',
			
			data: $('form').serialize();
			
		})
		.done(function(received){
			$("#contenedor").html(received);
		})
		.fail(function(){
			$("#contenedor").html("Request failed");
		});
		
	});
});











