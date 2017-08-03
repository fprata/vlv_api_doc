'use strict';

exports.getUserForAccountID = function(args, res, next) {
  /**
   * get users from account
   *
   * id String get user for account
   * returns List
   **/
  var examples = {};
  examples['application/json'] = [ {
  "firstName" : "aeiou",
  "lastName" : "aeiou",
  "userStatus" : 0,
  "manager" : "aeiou",
  "phone" : "aeiou",
  "uuid" : "aeiou",
  "email" : "aeiou",
  "username" : "aeiou"
} ];
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

