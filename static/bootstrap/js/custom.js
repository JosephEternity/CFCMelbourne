var helper = (function(){
	var authResult = undefined;
	return{
		/**
	     * Hides the sign-in button and connects the server-side app after
	     * the user successfully signs in.
	     *
	     * @param {Object} authResult An Object which contains the access token and
	     *   other authentication information.
	     */
		signinCallback: function(authResult){
			if (authResult['access_token']) {
				this.authResult = authResult;
				helper.connectServer();
			}
		},
		/**
	     * Calls the server endpoint to connect the app for the user. The client
	     * sends the one-time authorization code to the server and the server
	     * exchanges the code for its own tokens to use for offline API access.
	     * For more information, see:
	     *   https://developers.google.com/+/web/signin/server-side-flow
	     */
	     connectServer:function() {
	     	console.log(this.authResult.code);
	     	$.ajax({
	     		type:'POST',
	     		url: window.location.href + '/connect?state={{ STATE }}',
	     		contentType: 'application/octet-stream, charset=utf-8',
	     		success: function(result){
	     			console.log(result);
	     			helper.people();
	     		},
	     		processData: false,
	     		data: this.authResult.code
	     	});
	     },
	}
})