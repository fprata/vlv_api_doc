'use strict';

exports.getAccountID = function(args, res, next) {
  /**
   * get account info by id
   *
   * id String get accounts
   * returns Account
   **/
  var examples = {};
  examples['application/json'] = {
  "division" : "aeiou",
  "accounttype" : "aeiou",
  "id" : "aeiou",
  "distchannel" : "aeiou",
  "salesorg" : "aeiou",
  "accoountnumber" : "aeiou"
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

