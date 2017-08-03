'use strict';

exports.createUser = function(args, res, next) {
  /**
   * Create user
   * Create a new user in the security API
   *
   * body User Created user object
   * no response value expected for this operation
   **/
  res.end();
}

exports.deleteUser = function(args, res, next) {
  /**
   * Delete user
   * This can only be done by the logged in user.
   *
   * uuid String The name that needs to be deleted
   * no response value expected for this operation
   **/
  res.end();
}

exports.getUserByQuery = function(args, res, next) {
  /**
   * get user info
   * get user by query
   *
   * name String get user object by user name (optional)
   * email String get user object by email (optional)
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

exports.getUserByUUID = function(args, res, next) {
  /**
   * Get user by user uuid
   * 
   *
   * uuid String The uuid that needs to be fetched. Use user1 for testing. 
   * returns User
   **/
  var examples = {};
  examples['application/json'] = {
  "firstName" : "aeiou",
  "lastName" : "aeiou",
  "userStatus" : 0,
  "manager" : "aeiou",
  "phone" : "aeiou",
  "uuid" : "aeiou",
  "email" : "aeiou",
  "username" : "aeiou"
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.updateUser = function(args, res, next) {
  /**
   * Updated user
   * This can only be done by the logged in user.
   *
   * uuid String uuid that need to be updated
   * body User Updated user object
   * no response value expected for this operation
   **/
  res.end();
}

