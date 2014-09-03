/* 
 * MIT Licensed
 * Copyright 2014 REM <rami.developer@gmail.com>.
 */

$.MJAX.namespace( 'UBERLY', true );

$.MJAX.register( 'Classifier', {
  _debug: true,
  __self: function( params ) {
    this.$classifyBtn = $('#classify').first(),
    this.$classtLbl = $('#class'),
    this.$tweetTxt = $('#tweet');
    this.$classifyBtn
      .button()
      .click( function(event) {
        event.preventDefault();
        UBERLY.Classifier.classify(UBERLY.Classifier.$tweetTxt.val());
      });
  },
  _public: {
    classify: function(tweet) {
      var data = {};
      data.tweet = tweet;
      $.ajax({
          dataType: 'json',
          success: function(data, status) {
            console.log(UBERLY.Classifier.$classtLbl);
            UBERLY.Classifier.$classtLbl.text(data.class);
          },
          url: 'http://127.0.0.1:8000/live/uberly',
          data: data
        });
    }
  }
 });

$.MJAX.driver( 'MainDriver', function() {
  UBERLY.load( 'Classifier', {}, function() {});
});

$.MJAX.driver( 'MainDriver' );
