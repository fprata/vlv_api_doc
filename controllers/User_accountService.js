'use strict';

exports.deleteUserAccount = function(args, res, next) {
  /**
   * Delete user account assignment
   * This can only be done by the logged in user.
   *
   * uuid String The name that needs to be deleted
   * body List Updated account object
   * no response value expected for this operation
   **/
  res.end();
}

exports.getUserAccounts = function(args, res, next) {
  /**
   * manage user account assignments
   *
   * uuid Integer get accounts for user
   * returns List
   **/
  var examples = {};
  examples['application/json'] = [ {
  "division" : "aeiou",
  "accounttype" : "aeiou",
  "id" : "aeiou",
  "distchannel" : "aeiou",
  "salesorg" : "aeiou",
  "accoountnumber" : "aeiou"
} ];
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.updateUserAccounts = function(args, res, next) {
  /**
   * Updated user / account assignment
   * This can only be done by the logged in user.
   *
   * uuid String uuid that need to be updated
   * body List Updated account object
   * no response value expected for this operation
   **/
  res.end();
}

