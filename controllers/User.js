'use strict';

var url = require('url');

var User = require('./UserService');

module.exports.createUser = function createUser (req, res, next) {
  User.createUser(req.swagger.params, res, next);
};

module.exports.deleteUser = function deleteUser (req, res, next) {
  User.deleteUser(req.swagger.params, res, next);
};

module.exports.getUserByQuery = function getUserByQuery (req, res, next) {
  User.getUserByQuery(req.swagger.params, res, next);
};

module.exports.getUserByUUID = function getUserByUUID (req, res, next) {
  User.getUserByUUID(req.swagger.params, res, next);
};

module.exports.updateUser = function updateUser (req, res, next) {
  User.updateUser(req.swagger.params, res, next);
};
