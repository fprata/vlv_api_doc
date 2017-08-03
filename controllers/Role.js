'use strict';

var url = require('url');

var Role = require('./RoleService');

module.exports.getRoles = function getRoles (req, res, next) {
  Role.getRoles(req.swagger.params, res, next);
};

module.exports.getRolesbyID = function getRolesbyID (req, res, next) {
  Role.getRolesbyID(req.swagger.params, res, next);
};

module.exports.updateRole = function updateRole (req, res, next) {
  Role.updateRole(req.swagger.params, res, next);
};
