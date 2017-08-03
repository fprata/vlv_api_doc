'use strict';

var url = require('url');

var Account = require('./AccountService');

module.exports.getAccountID = function getAccountID (req, res, next) {
  Account.getAccountID(req.swagger.params, res, next);
};
