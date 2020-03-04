/*
  Slidemenu
*/
(function() {
	let $body = document.body;
	let $menu_trigger = $body.getElementsByClassName('menu-trigger')[0];

	if ( typeof $menu_trigger !== 'undefined' ) {
		$menu_trigger.addEventListener('click', function() {
			$body.className = ( $body.className === 'menu-active' )? '' : 'menu-active';
		});
	}

	let $red_tools_button = $body.getElementsByClassName('red-tools')[0];
	$red_tools_button.addEventListener('click', function(){
		window.location.href ='/red-tools';
	});

	let $blue_tools_button = $body.getElementsByClassName('blue-tools')[0];
	$blue_tools_button.addEventListener('click', function(){
		window.location.href ='/blue-tools';
	});

	let $myaccount_button = $body.getElementsByClassName('my-account')[0];
	$myaccount_button.addEventListener('click', function(){
		window.location.href ='/';
	});

	let $changepass_button = $body.getElementsByClassName('change-pass')[0];
	$changepass_button.addEventListener('click', function(){
		window.location.href ='/accounts/password_change';
	});
}).call(this);

