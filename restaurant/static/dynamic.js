$(document).ready(function() {
	// credit http://stackoverflow.com/questions/14804941/how-to-add-smooth-scrolling-to-bootstraps-scroll-spy-function
	$(".navbar-nav li a[href^='#']").on("click", function(e) {
		// prevent default anchor click behavior
		e.preventDefault();
		var hash = e.hash;
		// animate
		$("html, body").animate({
			scrollTop: $(this.hash).offset().top
		}, 300, function() {
			// when done, add hash to url
			window.location.hash = hash;
		});
	});
});