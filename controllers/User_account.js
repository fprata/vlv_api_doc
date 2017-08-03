'use strict';

var url = require('url');

var User_account = require('./User_accountService');

module.exports.deleteUserAccount = function deleteUserAccount (req, res, next) {
  User_account.deleteUserAccount(req.swagger.params, res, next);
};

module.exports.getUserAccounts = function getUserAccounts (req, res, next) {
  User_account.getUserAccounts(req.swagger.params, res, next);
};

module.exports.updateUserAccounts = function updateUserAccounts (req, res, next) {
  User_account.updateUserAccounts(req.swagger.params, res, next);
};
