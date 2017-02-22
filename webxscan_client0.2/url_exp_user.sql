/*
Navicat MySQL Data Transfer

Source Server         : xiaoshu.gotoftp4.com 
Source Server Version : 50161
Source Host           : xiaoshu.gotoftp4.com:3306
Source Database       : xiaoshu

Target Server Type    : MYSQL
Target Server Version : 50161
File Encoding         : 65001

Date: 2013-08-02 15:46:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `url_exp_user`
-- ----------------------------
DROP TABLE IF EXISTS `url_exp_user`;
CREATE TABLE `url_exp_user` (
  `user` varchar(100) NOT NULL DEFAULT '',
  `root` varchar(100) DEFAULT NULL,
  `url` varchar(100) NOT NULL DEFAULT '',
  `exp` varchar(100) DEFAULT NULL,
  `expr` varchar(100) NOT NULL DEFAULT '',
  `urlexp` varchar(100) NOT NULL DEFAULT '',
  `Password` varchar(100) NOT NULL DEFAULT '',
  `bz` varchar(100) DEFAULT NULL,
  `post_server` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user`,`url`,`expr`,`urlexp`,`Password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of url_exp_user
-- ----------------------------
INSERT INTO `url_exp_user` VALUES ('1111', '222', '3333', '4444', '5555', '6666', '7777', '888', '127.0.0.1', '2013-07-17 17:48:02');
INSERT INTO `url_exp_user` VALUES ('admin', '1', '127.0.0.1', 'http_download', 'http://127.0.0.1', 'http://127.0.0.1www.rar---3085KB', '', 'http download', '118.123.16.120', '2013-07-26 02:27:50');
INSERT INTO `url_exp_user` VALUES ('admin', '0', 'http://163.com', 'exp', 'exp_cmseasy_IIS6_jx', 'http://163.com/celive/live/doajaxfileupload.php', '', '', '61.139.126.203', '2013-07-28 18:37:43');
INSERT INTO `url_exp_user` VALUES ('admin', '0', 'http://www.163.com', 'exp', 'exp_cmseasy_IIS6_jx', 'http://www.163.com/celive/live/doajaxfileupload.php', '', '', '118.123.16.120', '2013-07-29 13:21:12');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.163.com', 'url:port', 'socket_port', '2012open', '', '', '118.123.16.120', '2013-07-29 15:00:39');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.163.com', 'url:port', 'socket_port', '3000open', '', '', '118.123.16.120', '2013-07-29 15:01:10');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.163.com', 'url:port', 'socket_port', '3030open', '', '', '118.123.16.120', '2013-07-29 15:01:12');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.163.com', 'url:port', 'socket_port', '443open', '', '', '118.123.16.120', '2013-07-29 15:00:07');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.163.com', 'url:port', 'socket_port', '80open', '', '', '118.123.16.120', '2013-07-29 14:59:53');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.163.com', 'url:port', 'socket_port', '88open', '', '', '118.123.16.120', '2013-07-29 14:59:55');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.163.com', 'socket_port80', 'socket_port80', 'Server:CdnCacheServerV2.0', '', '', '118.123.16.120', '2013-07-29 13:23:04');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.a33.cn', 'http_download', 'http_download', 'http://www.a33.cn/data.bak---2427KB', '', 'http download', '118.123.16.120', '2013-07-29 02:12:54');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.a33.cn', 'http_download', 'http_download', 'http://www.a33.cn/Data/data.bak---2427KB', '', 'http download', '118.123.16.120', '2013-07-29 02:12:57');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.a33.cn', 'http_download', 'http_download', 'http://www.a33.cn/Data/db.bak---2427KB', '', 'http download', '118.123.16.120', '2013-07-29 02:12:59');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.a33.cn', 'http_download', 'http_download', 'http://www.a33.cn/data/sql2009car.config---1455KB', '', 'http download', '118.123.16.120', '2013-07-29 02:12:52');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.a33.cn', 'http_download', 'http_download', 'http://www.a33.cn/db.bak---2427KB', '', 'http download', '118.123.16.120', '2013-07-29 02:12:56');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.anzhuo.com', 'http_200', 'http://www.anzhuo.com', 'http://www.anzhuo.com/admin.php', '', 'http 200', '61.139.126.203', '2013-07-25 18:50:25');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.anzhuo.com', 'http_200', 'http://www.anzhuo.com', 'http://www.anzhuo.com/admin/admin.php', '', 'http 200', '61.139.126.203', '2013-07-25 18:50:23');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.anzhuo.com', 'http_200', 'http://www.anzhuo.com', 'http://www.anzhuo.com/include/dialoguser/select_soft.php', '', 'http 200', '61.139.126.203', '2013-07-25 18:50:26');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.ku6.com', 'url:port', 'socket_port', '443open', '', '', '61.139.126.203', '2013-08-01 19:40:49');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.ku6.com', 'url:port', 'socket_port', '80open', '', '', '61.139.126.203', '2013-08-01 19:40:45');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.ku6.com', 'url:port', 'socket_port', '88open', '', '', '61.139.126.203', '2013-08-01 19:40:47');
INSERT INTO `url_exp_user` VALUES ('admin', '1', 'www.wuyuan168.com', 'cms', 'www.wuyuan168.com', 'dedecms', '', '', '118.123.16.120', '2013-07-24 12:58:20');
