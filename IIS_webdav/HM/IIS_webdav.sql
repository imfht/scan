/*
Navicat MySQL Data Transfer

Source Server         : 123456789
Source Server Version : 50096
Source Host           : localhost:3306
Source Database       : data

Target Server Type    : MYSQL
Target Server Version : 50096
File Encoding         : 65001

Date: 2013-06-09 01:38:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `iis_webdav`
-- ----------------------------
DROP TABLE IF EXISTS `iis_webdav`;
CREATE TABLE `iis_webdav` (
  `url` varchar(100) NOT NULL default '',
  `postIP` varchar(100) default NULL,
  `time` varchar(100) default NULL,
  PRIMARY KEY  (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of iis_webdav
-- ----------------------------
