'use strict';

var url = require('url');

var User_role = require('./User_roleService');

module.exports.deleteUserRole = function deleteUserRole (req, res, next) {
  User_role.deleteUserRole(req.swagger.params, res, next);
};

module.exports.getUserRoles = function getUserRoles (req, res, next) {
  User_role.getUserRoles(req.swagger.params, res, next);
};

module.exports.updateUserRole = function updateUserRole (req, res, next) {
  User_role.updateUserRole(req.swagger.params, res, next);
};
