/* 
 * MIT Licensed
 * Copyright 2014 REM <rami.developer@gmail.com>.
 */

//load('/Users/rami/github/uberly/twitter/db/map_reduce.js')

// @author ryanve http://jsperf.com/tok
function strtok (s, delims, rtl) {
  var n, i = delims.length;
  rtl = true === rtl;
  while (i--) {
      n = s.indexOf(delims[i]);
      s = n < 0 ? s : rtl 
          ? s.substr(++n)
          : s.substr(0, n);
  }
  return s;
}

var map_v2 = function() {
  var tweet = this.text;
  //print(tweet);
  if (tweet) {
    tweet = tweet
      .toLowerCase()
      .replace(/[0-9]+/, 'number')
      .replace(/(http|https):\/\/[^\s]*/, 'httpaddr')
      .replace(/[^\s]+@[^\s]+/, 'emailaddr');
    var words = tweet.match(/[^\s@\$\/\#\.-:&\*\+=\[\]\?!\(\)\{\},'\\">_<;%\^]+/g);
    var clean_words = [];
    for (var i = 0; words !== null && i<words.length; i++) {
      if (words[i]) {
        var word = words[i].replace(/[^a-zA-Z0-9]+/, '');
        //for(var j=0; j<word.length; j++) print('['+j+']: ' + word.charAt(j) + ', ' + word.charCodeAt(j));
        if (word.length>1) {
          if(word === 'http')
            print(tweet)
          clean_words.push(word);
          emit(word, 1);
        }
      }
    }
    //print(clean_words.toString());
    //print('\n');
  }
};

var map_v1 = function() {
  var tweet = this.text;
  if (tweet) {
    words = tweet.toLowerCase().split(' ');
    for (var i = words.length - 1; i >= 0; i--) {
      if (words[i]) {
        emit(words[i], 1);
      }
    }
  }
};

//var map = map_v1;
var map = map_v2;

var reduce = function(key, values) {
  var count = 0;
  values.forEach(function(v) {
    count +=v;
  });
  return count;
}

var dictionary = 'uber_vocab_1'
db.tweets.mapReduce(map, reduce, {out: dictionary});
//db.tweets.mapReduce(map, reduce, {query: {id:501142004751810560}, out: dictionary});
//db[dictionary].find().sort({value:-1}).pretty();

//db.uber_dictionary.aggregate([{$group: {_id: {word: "$stem"}, count: {$sum: "$value"}}}, {$sort: {count: -1}}])

/*
 * 
 * dump the list into a file
 * run it through porter stemmer
 * build the final corpus list
 * 
 */