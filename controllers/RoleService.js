'use strict';

exports.getRoles = function(args, res, next) {
  /**
   * manage roles
   *
   * application String get role applicable by application (optional)
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

exports.getRolesbyID = function(args, res, next) {
  /**
   * manage roles
   *
   * id Integer get role object by id
   * returns Role
   **/
  var examples = {};
  examples['application/json'] = {
  "rolename" : "aeiou",
  "id" : 0
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.updateRole = function(args, res, next) {
  /**
   * Updated role
   * Update role info.
   *
   * id Integer id that need to be updated
   * body Role Updated role object
   * no response value expected for this operation
   **/
  res.end();
}

