/*
Navicat MySQL Data Transfer

Source Server         : 123456789
Source Server Version : 50096
Source Host           : localhost:3306
Source Database       : hhmm

Target Server Type    : MYSQL
Target Server Version : 50096
File Encoding         : 65001

Date: 2013-04-19 16:43:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `ftppassword2`
-- ----------------------------
DROP TABLE IF EXISTS `ftppassword2`;
CREATE TABLE `ftppassword2` (
  `IP` varchar(100) NOT NULL,
  `user` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `root` varchar(100) NOT NULL,
  `html` varchar(100) default NULL,
  `baiduQZ` varchar(100) default NULL,
  `PR` varchar(100) default NULL,
  `time` varchar(100) NOT NULL,
  PRIMARY KEY  (`IP`,`user`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of ftppassword2
-- ----------------------------
INSERT INTO `ftppassword2` VALUES ('www.byecity.com', 'byecity', 'byecity', '2', 'html', null, null, '2012.04.15-23.51.31');
INSERT INTO `ftppassword2` VALUES ('www.jiandan8.com', 'ftp', 'mnbvcxz', '2', 'html', null, null, '2012.04.15-23.51.55');
INSERT INTO `ftppassword2` VALUES ('jws.gdga.gov.cn', 'access', '', 'NO', 'html', null, null, '2012.04.15-23.52.31');
INSERT INTO `ftppassword2` VALUES ('jws.gdga.gov.cn', 'account', '', 'NO', 'html', null, null, '2012.04.15-23.52.31');
INSERT INTO `ftppassword2` VALUES ('jws.gdga.gov.cn', 'administrator', '', 'NO', 'html', null, null, '2012.04.15-23.52.31');
INSERT INTO `ftppassword2` VALUES ('jws.gdga.gov.cn', 'backup', '', 'NO', 'html', null, null, '2012.04.15-23.52.31');
INSERT INTO `ftppassword2` VALUES ('jws.gdga.gov.cn', 'data', '', 'NO', 'html', null, null, '2012.04.15-23.52.31');
INSERT INTO `ftppassword2` VALUES ('jws.gdga.gov.cn', 'ftp', '', 'NO', 'html', null, null, '2012.04.15-23.52.31');
INSERT INTO `ftppassword2` VALUES ('jws.gdga.gov.cn', 'ftp@gdga.gov.cn', '', 'NO', 'html', null, null, '2012.04.15-23.52.31');
INSERT INTO `ftppassword2` VALUES ('jws.gdga.gov.cn', 'gdga', '', 'NO', 'html', null, null, '2012.04.15-23.52.31');
INSERT INTO `ftppassword2` VALUES ('jws.gdga.gov.cn', 'gdga.gov.cn', '', 'NO', 'html', null, null, '2012.04.15-23.52.31');
INSERT INTO `ftppassword2` VALUES ('jws.gdga.gov.cn', 'guest', '', 'NO', 'html', null, null, '2012.04.15-23.52.31');
INSERT INTO `ftppassword2` VALUES ('www.hssyj.com', 'hssyj', '123', '2', 'html', null, null, '2012.04.15-23.52.42');
INSERT INTO `ftppassword2` VALUES ('www.zjzuche.com', 'backup', 'backup', '2', 'html', null, null, '2012.04.15-23.52.51');
INSERT INTO `ftppassword2` VALUES ('down.ddvip.com', 'ftp', '147258369', '2', 'html', null, null, '2012.04.15-23.52.57');

-- ----------------------------
-- Table structure for `ftppassword3`
-- ----------------------------
DROP TABLE IF EXISTS `ftppassword3`;
CREATE TABLE `ftppassword3` (
  `IP` varchar(100) NOT NULL,
  `user` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `root` varchar(100) NOT NULL,
  `html` varchar(100) default NULL,
  `baiduQZ` varchar(100) default NULL,
  `PR` varchar(100) default NULL,
  `time` varchar(100) NOT NULL,
  PRIMARY KEY  (`IP`,`user`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of ftppassword3
-- ----------------------------
INSERT INTO `ftppassword3` VALUES ('www.qingdaochina.org', 'mysql', 'mnbvcxz', '2', 'html', '2', '5', '2012.04.15-23.41.44');
INSERT INTO `ftppassword3` VALUES ('www.kfxhbook.com', 'kfxhbook', 'www.kfxhbook.com', '3', 'html', '1', '3', '2012.04.15-23.41.55');
INSERT INTO `ftppassword3` VALUES ('www.51testing.net', 'www.51testing.net', '51testing12345', 'NO', 'html', '2', '5', '2012.04.15-23.42.10');
INSERT INTO `ftppassword3` VALUES ('www.tq121.com.cn', 'oracle', '123456', '3', 'html', '1', '7', '2012.04.15-23.42.17');
INSERT INTO `ftppassword3` VALUES ('www.zhjunshi.com', 'www', 'www', '3', 'html', '1', '6', '2012.04.15-23.42.25');
INSERT INTO `ftppassword3` VALUES ('www.zhjunshi.com', 'test', 'test', '3', 'html', '1', '6', '2012.04.15-23.42.37');
INSERT INTO `ftppassword3` VALUES ('www.cxylmr.com', 'ftp', 'mnbvcxz', '3', 'html', 'NO', '2', '2012.04.15-23.42.48');
INSERT INTO `ftppassword3` VALUES ('www.zsfan.com', 'zsfan.com', 'zsfan.com', '3', 'html', '1', '1', '2012.04.15-23.42.57');
INSERT INTO `ftppassword3` VALUES ('www.aviationnow.com.cn', 'ftp', 'mnbvcxz', '3', 'html', '1', '6', '2012.04.15-23.43.02');
INSERT INTO `ftppassword3` VALUES ('app.lifeweek.com.cn', 'test', 'test', '3', 'html', '1', '2', '2012.04.15-23.43.07');
INSERT INTO `ftppassword3` VALUES ('www.gyfyy.com', 'gyfyy', '123qwe', '3', 'html', '3', 'NO3', '2012.04.15-23.43.12');
INSERT INTO `ftppassword3` VALUES ('www.yhcare.com.cn', 'test', '123', '3', 'html', 'NO', '2', '2012.04.15-23.43.18');
INSERT INTO `ftppassword3` VALUES ('yeshir.com', 'yeshir', 'yeshir123', '3', 'html', '1', '4', '2012.04.15-23.43.23');
INSERT INTO `ftppassword3` VALUES ('www.9ic.cn', 'ftp', 'mnbvcxz', '3', 'html', '2', '6', '2012.04.15-23.43.30');
INSERT INTO `ftppassword3` VALUES ('www.bame.org.cn', 'ftp@bame.org.cn', '123456', '3', 'html', '1', '4', '2012.04.15-23.43.35');
INSERT INTO `ftppassword3` VALUES ('www.zsfan.com', 'ftp', 'mnbvcxz', '3', 'html', '1', '1', '2012.04.15-23.43.41');
INSERT INTO `ftppassword3` VALUES ('space.lifeweek.com.cn', 'test', 'test', '3', 'html', '1', '2', '2012.04.15-23.43.46');
INSERT INTO `ftppassword3` VALUES ('shop.lifeweek.com.cn', 'test', 'test', '3', 'html', '1', '5', '2012.04.15-23.43.51');
INSERT INTO `ftppassword3` VALUES ('yoti.cn', 'ftp', 'mnbvcxz', '3', 'html', '1', '5', '2012.04.15-23.43.56');
INSERT INTO `ftppassword3` VALUES ('rtdchina.net', 'webmaster@rtdchina.net', 'rtdchina.net', '3', 'html', 'NO', '3', '2012.04.15-23.44.02');
INSERT INTO `ftppassword3` VALUES ('www.tlgzjlb.com', 'ftp', 'mnbvcxz', '3', 'html', '2', '3', '2012.04.15-23.44.07');
INSERT INTO `ftppassword3` VALUES ('www.flp.com.cn', 'ftp', 'mnbvcxz', '3', 'html', '1', '6', '2012.04.15-23.44.12');
INSERT INTO `ftppassword3` VALUES ('www.blossompress.com.cn', 'ftp', 'mnbvcxz', '3', 'html', 'NO', '6', '2012.04.15-23.44.17');
INSERT INTO `ftppassword3` VALUES ('www.nwp.com.cn', 'ftp', 'mnbvcxz', '3', 'html', '1', '5', '2012.04.15-23.44.22');
INSERT INTO `ftppassword3` VALUES ('www.dolphin-books.com.cn', 'ftp', '2012', '3', 'html', '1', '6', '2012.04.15-23.44.31');
INSERT INTO `ftppassword3` VALUES ('www.zghbcbs.com', 'ftp', 'mnbvcxz', '3', 'html', '1', '6', '2012.04.15-23.44.36');
INSERT INTO `ftppassword3` VALUES ('www.lifeweek.com.cn', 'test', 'test', '3', 'html', '4', '7', '2012.04.15-23.44.41');
INSERT INTO `ftppassword3` VALUES ('www.yoti.cn', 'ftp', '2011', '3', 'html', '1', '5', '2012.04.15-23.44.46');
INSERT INTO `ftppassword3` VALUES ('www.ruocheng.com', 'test', '111111', '3', 'html', 'NO', '4', '2012.04.15-23.44.52');
INSERT INTO `ftppassword3` VALUES ('www.iconinfrastructure.com', 'sarah', 'sarah', '3', 'html', 'NO', '1', '2012.04.15-23.45.03');
INSERT INTO `ftppassword3` VALUES ('www.themanage.cn', 'admin', 'admin', '3', 'html', '4', '2', '2012.04.15-23.45.08');
INSERT INTO `ftppassword3` VALUES ('www.chinaqingsuan.com', 'ftp', 'mnbvcxz', '3', 'html', '1', '4', '2012.04.15-23.45.13');
INSERT INTO `ftppassword3` VALUES ('www.mankindhealth.com', 'mankindhealth', 'mankindhealth888', '3', 'html', '1', '2', '2012.04.15-23.45.18');
INSERT INTO `ftppassword3` VALUES ('bbs.offroader.com.cn', 'ftp', '111111111', '3', 'html', '1', '2', '2012.04.15-23.45.23');
INSERT INTO `ftppassword3` VALUES ('edu.3c3t.com', 'account', 'account', '3', 'html', '1', '2', '2012.04.15-23.45.29');
INSERT INTO `ftppassword3` VALUES ('edu.3c3t.com', 'guest', 'guest', '3', 'html', '1', '2', '2012.04.15-23.45.34');
INSERT INTO `ftppassword3` VALUES ('edu.3c3t.com', 'user', 'user', '3', 'html', '1', '2', '2012.04.15-23.45.39');
INSERT INTO `ftppassword3` VALUES ('bbs.atedu.net', 'guest', 'guest', '3', 'html', '1', '0', '2012.04.15-23.45.44');
INSERT INTO `ftppassword3` VALUES ('www.tzxctz.com', 'mysql', 'mnbvcxz', 'NO', 'html', '2', '4', '2012.04.15-23.45.50');
INSERT INTO `ftppassword3` VALUES ('www.tzxctz.com', 'www', 'mnbvcxz', '3', 'html', '2', '4', '2012.04.15-23.45.52');
INSERT INTO `ftppassword3` VALUES ('www.enbar.net', 'www', 'www', '3', 'html', 'NO', '4', '2012.04.15-23.45.58');
INSERT INTO `ftppassword3` VALUES ('www.enbar.net', 'test', 'test', '3', 'html', 'NO', '4', '2012.04.15-23.46.03');
INSERT INTO `ftppassword3` VALUES ('mag.morningpost.com.cn', 'test', 'test123', '3', 'html', '1', '5', '2012.04.15-23.46.08');
INSERT INTO `ftppassword3` VALUES ('www.wanglei.cc', 'wanglei', 'wanglei.cc', '3', 'html', '1', '4', '2012.04.15-23.46.15');
INSERT INTO `ftppassword3` VALUES ('www.sinolingua.com.cn', 'ftp', 'mnbvcxz', '3', 'html', 'NO', '5', '2012.04.15-23.46.20');
INSERT INTO `ftppassword3` VALUES ('dfkj.unicse.com', 'ftp', '111111111', '3', 'html', 'NO', '2', '2012.04.15-23.46.25');
INSERT INTO `ftppassword3` VALUES ('home.061300.net', 'ftp', '147258369', 'NO', 'html', 'NO', '3', '2012.04.15-23.46.39');
INSERT INTO `ftppassword3` VALUES ('www.chenanzhi.com.cn', 'chenanzhi', 'chenanzhi', '3', 'html', 'NO', '0', '2012.04.15-23.46.41');
INSERT INTO `ftppassword3` VALUES ('www.blogyz.net', 'web', 'web', '3', 'html', '1', '2', '2012.04.15-23.46.46');
INSERT INTO `ftppassword3` VALUES ('bbs.caihuanet.com', 'test', '123456', '3', 'html', 'NO', '2', '2012.04.15-23.46.51');
INSERT INTO `ftppassword3` VALUES ('www.8gp8.cn', 'admin', 'admin', '3', 'html', '3', '4', '2012.04.15-23.46.56');
INSERT INTO `ftppassword3` VALUES ('edu.cncost.net', 'cncost', 'cncost', '3', 'html', 'NO', '3', '2012.04.15-23.47.01');
INSERT INTO `ftppassword3` VALUES ('gk.cncost.net', 'cncost', 'cncost', '3', 'html', 'NO', '3', '2012.04.15-23.47.06');
INSERT INTO `ftppassword3` VALUES ('www.500zhaopin.com', 'webmaster@500zhaopin.com', '123456', '3', 'html', 'NO', '5', '2012.04.15-23.47.12');
INSERT INTO `ftppassword3` VALUES ('www.cdnat.com', 'ftp', '147258369', '3', 'html', 'NO', '2', '2012.04.15-23.47.20');
INSERT INTO `ftppassword3` VALUES ('www.chaohurx.com', 'chaohurx', 'chaohurx123', '3', 'html', '1', '2', '2012.04.15-23.47.26');
INSERT INTO `ftppassword3` VALUES ('love.433125.com', '433125', '433125.com', '3', 'html', 'NO', '1', '2012.04.15-23.47.31');
INSERT INTO `ftppassword3` VALUES ('vip.433125.com', '433125', '433125.com', '3', 'html', 'NO', '0', '2012.04.15-23.47.36');
INSERT INTO `ftppassword3` VALUES ('www.lelibang.com', 'ftp', '147258369', '3', 'html', '1', '1', '2012.04.15-23.47.43');
INSERT INTO `ftppassword3` VALUES ('www.mikrotik.com.cn', 'ftp', '147258369', '3', 'html', '2', '2', '2012.04.15-23.47.49');
INSERT INTO `ftppassword3` VALUES ('bbs.433125.com', '433125', '433125.com', '3', 'html', '1', '2', '2012.04.15-23.47.54');
INSERT INTO `ftppassword3` VALUES ('bbs.hysyg.com', 'ftp', '111111111', '3', 'html', 'NO', '2', '2012.04.15-23.48.01');
INSERT INTO `ftppassword3` VALUES ('bbs.hysyg.net', 'ftp', '111111111', 'NO', 'html', 'NO', '2', '2012.04.15-23.48.07');
INSERT INTO `ftppassword3` VALUES ('www.06xushi.cn', 'ftp', '147258369', '3', 'html', '1', '4', '2012.04.15-23.48.10');
INSERT INTO `ftppassword3` VALUES ('www.aswanmei.com', 'ftp', '147258369', '3', 'html', '1', '3', '2012.04.15-23.48.15');
INSERT INTO `ftppassword3` VALUES ('www.pnxrmyy.com', 'ftp', '111111111', '3', 'html', '1', '2', '2012.04.15-23.48.20');
INSERT INTO `ftppassword3` VALUES ('www.seo53.com', 'ftp', '111111111', '3', 'html', '1', '1', '2012.04.15-23.48.27');
INSERT INTO `ftppassword3` VALUES ('www.hysyg.com', 'ftp', '147258369', '3', 'html', '1', '2', '2012.04.15-23.48.34');
INSERT INTO `ftppassword3` VALUES ('www.ipk-club.com', 'test', '123456', '3', 'html', 'NO', '3', '2012.04.15-23.48.39');
INSERT INTO `ftppassword3` VALUES ('bbs.driverdevelop.com', 'backup', 'password', '3', 'html', '1', '3', '2012.04.15-23.48.45');
INSERT INTO `ftppassword3` VALUES ('www.higo.cc', 'higo', 'www.higo.cc', '3', 'html', '2', '3', '2012.04.15-23.48.51');
INSERT INTO `ftppassword3` VALUES ('www.kamiflorist.com.hk', 'guest', '12345', '3', 'html', 'NO', '2', '2012.04.15-23.48.57');
INSERT INTO `ftppassword3` VALUES ('www.lapsang.cn', 'ftp', '111111111', '3', 'html', '1', '3', '2012.04.15-23.49.02');
INSERT INTO `ftppassword3` VALUES ('www.mziii.com', 'mziii', 'mziii123', '3', 'html', 'NO', '4', '2012.04.15-23.49.07');
INSERT INTO `ftppassword3` VALUES ('www.sqnrsj.com', 'sqnrsj', 'sqnrsj.com', 'NO', 'html', '1', '1', '2012.04.15-23.49.14');
INSERT INTO `ftppassword3` VALUES ('www.ws8.org', 'ftp', '147258369', '3', 'html', '2', '1', '2012.04.15-23.49.16');
INSERT INTO `ftppassword3` VALUES ('www.xinwnet.com', 'xinwnet', '123456', '3', 'html', '1', '0', '2012.04.15-23.49.22');
INSERT INTO `ftppassword3` VALUES ('bbs.driverdevelop.com', 'oracle', '123456789', '1', 'html', '1', '3', '2012.04.15-23.49.37');
INSERT INTO `ftppassword3` VALUES ('www.xiuxingfu.com', 'ftp', '147258369', '3', 'html', 'NO', '2', '2012.04.15-23.49.39');
INSERT INTO `ftppassword3` VALUES ('www.yochu.com', 'test', '123123', '3', 'html', '1', '3', '2012.04.15-23.49.44');
INSERT INTO `ftppassword3` VALUES ('www.11gal.com', 'ftp', '111111111', '1', 'html', '1', '1', '2012.04.15-23.50.00');
INSERT INTO `ftppassword3` VALUES ('www.hack69.com', 'administrator', '123456', 'NO', 'html', '1', '3', '2012.04.15-23.50.05');
INSERT INTO `ftppassword3` VALUES ('bbs.driverdevelop.com', 'driverdevelop', 'password', '3', 'html', '1', '3', '2012.04.15-23.50.08');
INSERT INTO `ftppassword3` VALUES ('www.topnewinfo.com.cn', 'test', 'test', '3', 'html', 'NO', '1', '2012.04.15-23.50.13');
INSERT INTO `ftppassword3` VALUES ('www.yulehezi.com', 'test', 'test', 'NO', 'html', '1', '5', '2012.04.15-23.50.27');
