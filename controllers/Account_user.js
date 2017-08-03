'use strict';

var url = require('url');

var Account_user = require('./Account_userService');

module.exports.getUserForAccountID = function getUserForAccountID (req, res, next) {
  Account_user.getUserForAccountID(req.swagger.params, res, next);
};
