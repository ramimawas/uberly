/* 
 * MIT Licensed
 * Copyright 2014 REM <rami.developer@gmail.com>.
 */

var in_clt = 'uber_vocab_1';
var out_clt = 'uber_vocab_2';

db[in_clt].aggregate([
    {
      $group: {
        _id: "$stem",
        count: {$sum: "$value"},
        words: {$addToSet: "$_id"}
      },
    },
    {$sort: {count: -1}},
    {$out: out_clt}
  ]);
  
  var count = 1;
  db[out_clt].find().sort({count: -1}).forEach(function(row){row.index=count++; db[out_clt].save(row);})
 
  //mongoexport --db uberly --collection uber_vocab_2 --csv --forceTableScan -q '{$query:{count: {$gt: 5}}, $orderby:{index: 1}}' --fields index,_id --out /Users/rami/github/uberly/octave/uber_vocab.txt