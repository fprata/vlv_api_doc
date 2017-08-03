'use strict';

exports.deleteUserRole = function(args, res, next) {
  /**
   * Delete user role assignment
   * This can only be done by the logged in user.
   *
   * uuid String The name that needs to be deleted
   * no response value expected for this operation
   **/
  res.end();
}

exports.getUserRoles = function(args, res, next) {
  /**
   * manage user role assignments
   *
   * uuid Integer get role applicable by application
   * returns List
   **/
  var examples = {};
  examples['application/json'] = [ {
  "rolename" : "aeiou",
  "id" : 0
} ];
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.updateUserRole = function(args, res, next) {
  /**
   * Updated user role assigment
   * This can only be done by the logged in user.
   *
   * uuid String uuid that need to be updated
   * body List Updated user object
   * no response value expected for this operation
   **/
  res.end();
}

