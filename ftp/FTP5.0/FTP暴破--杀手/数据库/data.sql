/*
Navicat MySQL Data Transfer

Source Server         : CS-FTP
Source Server Version : 50096
Source Host           : localhost:3306
Source Database       : data

Target Server Type    : MYSQL
Target Server Version : 50096
File Encoding         : 65001

Date: 2013-02-08 18:22:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `ftppassword0`
-- ----------------------------
DROP TABLE IF EXISTS `ftppassword0`;
CREATE TABLE `ftppassword0` (
  `IP` varchar(100) NOT NULL default '',
  `user` varchar(100) NOT NULL default '',
  `password` varchar(100) default NULL,
  `root` varchar(100) default NULL,
  `time` varchar(100) default NULL,
  PRIMARY KEY  (`IP`,`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ftppassword0
-- ----------------------------
INSERT INTO `ftppassword0` VALUES ('167ero.com', 'ftp@167ero.com', 'zxcvbnm', 'NO', '2013.02.07-14.43.15');
INSERT INTO `ftppassword0` VALUES ('18thstreet.org', 'oracle8', '00000000', 'NO', '2013.02.05-05.14.26');
INSERT INTO `ftppassword0` VALUES ('1deai.net', 'ftp@1deai.net', 'zxcvbnm', 'NO', '2013.02.07-10.11.11');
INSERT INTO `ftppassword0` VALUES ('2012.howtoweb.co', 'ftp@howtoweb.co', 'howtoweb', 'NO', '2013.02.06-22.17.30');
INSERT INTO `ftppassword0` VALUES ('21stcenturyfix.org.uk', 'ftp@21stcenturyfix.org.uk', 'super', 'NO', '2013.02.06-15.47.25');
INSERT INTO `ftppassword0` VALUES ('295douglass.org', 'ftp@295douglass.org', 'mnbvcxz', 'NO', '2013.02.07-07.42.02');
INSERT INTO `ftppassword0` VALUES ('2ch-tips.com', 'ftp@2ch-tips.com', 'mnbvcxz', 'NO', '2013.02.07-14.44.08');
INSERT INTO `ftppassword0` VALUES ('2ch-tips.com', 'webmaster@2ch-tips.com', '54321', 'NO', '2013.02.05-22.14.03');
INSERT INTO `ftppassword0` VALUES ('319heads.com', 'ftp@319heads.com', '2012', 'NO', '2013.02.07-11.06.44');
INSERT INTO `ftppassword0` VALUES ('39dreamnet.com', 'ftp@39dreamnet.com', 'mnbvcxz', 'NO', '2013.02.07-14.44.45');
INSERT INTO `ftppassword0` VALUES ('43folders.com', 'ftp@43folders.com', 'mnbvcxz', 'NO', '2013.02.07-08.02.12');
INSERT INTO `ftppassword0` VALUES ('49ers.pressdemocrat.com', 'ftp@pressdemocrat.com', 'mnbvcxz', 'NO', '2013.02.07-07.46.50');
INSERT INTO `ftppassword0` VALUES ('4d58e.xm.ylc78.com', 'ftp', 'mnbvcxz', 'NO', '2013.02.07-15.42.00');
INSERT INTO `ftppassword0` VALUES ('707.pressdemocrat.com', 'ftp@pressdemocrat.com', 'mnbvcxz', 'NO', '2013.02.07-07.46.54');
INSERT INTO `ftppassword0` VALUES ('7bc.cc', 'webmaster', 'root', 'NO', '2013.02.04-15.49.18');
INSERT INTO `ftppassword0` VALUES ('7memories.com', 'ftp@7memories.com', 'mnbvcxz', 'NO', '2013.02.06-16.38.12');
INSERT INTO `ftppassword0` VALUES ('8bitfunding.com', 'ftp@8bitfunding.com', 'mnbvcxz', 'NO', '2013.02.07-14.45.19');
INSERT INTO `ftppassword0` VALUES ('a2.43folders.com', 'ftp@43folders.com', 'mnbvcxz', 'NO', '2013.02.07-08.02.38');
INSERT INTO `ftppassword0` VALUES ('aaeblog.com', 'ftp@aaeblog.com', 'zxcvbnm', 'NO', '2013.02.07-16.06.21');
INSERT INTO `ftppassword0` VALUES ('aaronhockley.com', 'aaronhockley.com', '12345', 'NO', '2013.02.05-13.06.10');
INSERT INTO `ftppassword0` VALUES ('abeachcottage.com', 'ftp@abeachcottage.com', '2012', 'NO', '2013.02.06-15.31.23');
INSERT INTO `ftppassword0` VALUES ('aboutfoursquare.com', 'ftp@aboutfoursquare.com', 'alpha', 'NO', '2013.02.07-08.13.39');
INSERT INTO `ftppassword0` VALUES ('acetio.com', 'ftp@acetio.com', 'zxcvbnm', 'NO', '2013.02.07-09.47.44');
INSERT INTO `ftppassword0` VALUES ('acid.agsns.net', 'webmaster@agsns.net', '1234qwer', 'NO', '2013.02.05-22.12.39');
INSERT INTO `ftppassword0` VALUES ('adactio.com', 'network', 'alpha', 'NO', '2013.02.05-04.27.22');
INSERT INTO `ftppassword0` VALUES ('adashofbitters.com', 'adashofbitters.com', 'abc123', 'NO', '2013.02.05-12.58.40');
INSERT INTO `ftppassword0` VALUES ('adashofbitters.com', 'data', '654321', 'NO', '2013.02.05-13.16.23');
INSERT INTO `ftppassword0` VALUES ('adultsexdouga.com', 'ftp@adultsexdouga.com', 'zxcvbnm', 'NO', '2013.02.07-14.47.05');
INSERT INTO `ftppassword0` VALUES ('afia-forfaiting.org', 'ftp@afia-forfaiting.org', 'zxcvbnm', 'NO', '2013.02.06-08.59.29');
INSERT INTO `ftppassword0` VALUES ('afrojacks.com', 'wwwadmin', '2600', 'NO', '2013.02.05-13.41.54');
INSERT INTO `ftppassword0` VALUES ('afrolicofmyown.com', 'ftp@afrolicofmyown.com', 'mnbvcxz', 'NO', '2013.02.07-16.07.38');
INSERT INTO `ftppassword0` VALUES ('aintnobaddude.com', 'ftp@aintnobaddude.com', '2012', 'NO', '2013.02.07-16.08.41');
INSERT INTO `ftppassword0` VALUES ('air-jordan-release-dates.com', 'ftp@air-jordan-release-dates.com', '2011', 'NO', '2013.02.07-08.42.30');
INSERT INTO `ftppassword0` VALUES ('akasharabutphoto.com', 'ftp@akasharabutphoto.com', 'mnbvcxz', 'NO', '2013.02.07-10.49.38');
INSERT INTO `ftppassword0` VALUES ('akasharabutphoto.com', 'www', '000000', 'NO', '2013.02.07-11.22.17');
INSERT INTO `ftppassword0` VALUES ('akcees.com', 'ftp@akcees.com', 'mnbvcxz', 'NO', '2013.02.06-22.19.41');
INSERT INTO `ftppassword0` VALUES ('akcees.ro', 'ftp@akcees.ro', 'mnbvcxz', 'NO', '2013.02.06-22.20.14');
INSERT INTO `ftppassword0` VALUES ('alergotura.ro', 'alergotura.ro', '123123', 'NO', '2013.02.07-16.36.39');
INSERT INTO `ftppassword0` VALUES ('alergotura.ro', 'backup', '2011', 'NO', '2013.02.07-17.12.51');
INSERT INTO `ftppassword0` VALUES ('alergotura.ro', 'wwwadmin', '1234qwer', 'NO', '2013.02.07-17.05.47');
INSERT INTO `ftppassword0` VALUES ('alienblue.org', 'account', '111111', 'NO', '2013.02.07-11.10.02');
INSERT INTO `ftppassword0` VALUES ('alienblue.org', 'ftp@alienblue.org', 'mnbvcxz', 'NO', '2013.02.07-14.49.34');
INSERT INTO `ftppassword0` VALUES ('alienblue.org', 'guest', 'abcd', 'NO', '2013.02.07-11.20.56');
INSERT INTO `ftppassword0` VALUES ('alinearchimbaud.eelv.fr', 'eelv.fr', 'alinearchimbaud.eelv.fr', 'NO', '2013.02.06-22.18.22');
INSERT INTO `ftppassword0` VALUES ('allforwomen.com.au', 'ftp@allforwomen.com.au', '2012', 'NO', '2013.02.07-10.58.54');
INSERT INTO `ftppassword0` VALUES ('alsace.regions-europe-ecologie.fr', 'data', 'super', 'NO', '2013.02.06-22.21.19');
INSERT INTO `ftppassword0` VALUES ('alsace.regions-europe-ecologie.fr', 'web', '0', 'NO', '2013.02.06-22.19.06');
INSERT INTO `ftppassword0` VALUES ('alyamiah.com', 'ftp@alyamiah.com', '2012', null, '2013.02.07-16.52.41');
INSERT INTO `ftppassword0` VALUES ('americantroyalty.com', 'sybase', 'enable', 'NO', '2013.02.07-11.30.27');
INSERT INTO `ftppassword0` VALUES ('amscott.org', 'ftp@amscott.org', 'mnbvcxz', 'NO', '2013.02.07-10.51.39');
INSERT INTO `ftppassword0` VALUES ('anan-idol.info', 'ftp@anan-idol.info', 'zxcvbnm', 'NO', '2013.02.06-09.33.13');
INSERT INTO `ftppassword0` VALUES ('andregattolin.eelv.fr', 'eelv.fr', 'eelv', 'NO', '2013.02.06-22.18.23');
INSERT INTO `ftppassword0` VALUES ('andrewcarr.org', 'ftp@andrewcarr.org', 'mnbvcxz', 'NO', '2013.02.07-14.51.21');
INSERT INTO `ftppassword0` VALUES ('app-rising.com', 'ftp@app-rising.com', 'zxcvbnm', 'NO', '2013.02.07-14.52.08');
INSERT INTO `ftppassword0` VALUES ('arabiangazette.com', 'ftp@arabiangazette.com', 'mnbvcxz', 'NO', '2013.02.07-08.14.16');
INSERT INTO `ftppassword0` VALUES ('arashi-fan.jp', 'ftp@arashi-fan.jp', 'zxcvbnm', 'NO', '2013.02.06-09.41.19');
INSERT INTO `ftppassword0` VALUES ('archive.umwblogs.org', 'ftp@umwblogs.org', 'zxcvbnm', 'NO', '2013.02.06-09.41.36');
INSERT INTO `ftppassword0` VALUES ('artistastudio.liaison-pro.com', 'ftp@liaison-pro.com', 'zxcvbnm', 'NO', '2013.02.06-23.39.04');
INSERT INTO `ftppassword0` VALUES ('artistique-ilustra.net', 'network', '654321', 'NO', '2013.02.04-14.47.15');
INSERT INTO `ftppassword0` VALUES ('artistique-ilustra.net', 'webmaster@artistique-ilustra.net', 'enable', 'NO', '2013.02.04-14.31.26');
INSERT INTO `ftppassword0` VALUES ('artistsspace.org', 'webmaster@artistsspace.org', 'test', 'NO', '2013.02.07-11.12.27');
INSERT INTO `ftppassword0` VALUES ('ascdm.net', 'wwwadmin', '123asd', 'NO', '2013.02.04-15.49.21');
INSERT INTO `ftppassword0` VALUES ('asmack.freakempire.de', 'test', '123qwe', 'NO', '2013.02.04-15.13.01');
INSERT INTO `ftppassword0` VALUES ('asmack.freakempire.de', 'webmaster@freakempire.de', 'computer', 'NO', '2013.02.04-14.34.49');
INSERT INTO `ftppassword0` VALUES ('asmp.fr', 'web', '111111', 'NO', '2013.02.06-22.17.21');
INSERT INTO `ftppassword0` VALUES ('assignments.ds106.us', 'ftp@ds106.us', 'mnbvcxz', 'NO', '2013.02.06-09.46.51');
INSERT INTO `ftppassword0` VALUES ('ateliernord.no', 'ftp@ateliernord.no', '123abc', 'NO', '2013.02.06-16.41.59');
INSERT INTO `ftppassword0` VALUES ('atheistallianceamerica.org', 'ftp@atheistallianceamerica.org', 'zxcvbnm', 'NO', '2013.02.07-14.52.24');
INSERT INTO `ftppassword0` VALUES ('atheistcensus.com', 'ftp@atheistcensus.com', 'zxcvbnm', 'NO', '2013.02.07-08.54.58');
INSERT INTO `ftppassword0` VALUES ('athomecolorado.com', 'ftp@athomecolorado.com', 'zxcvbnm', 'NO', '2013.02.06-13.38.52');
INSERT INTO `ftppassword0` VALUES ('atlanticreview.org', 'atlanticreview', 'atlanticreview12345', 'NO', '2013.02.06-16.44.24');
INSERT INTO `ftppassword0` VALUES ('austin.eater.com', 'access', '!@#$%^&*()', 'NO', '2013.02.05-11.16.39');
INSERT INTO `ftppassword0` VALUES ('austin.eater.com', 'web', 'eater.com123', 'NO', '2013.02.05-11.06.58');
INSERT INTO `ftppassword0` VALUES ('austin.eater.com', 'webmaster', 'eater.com12345', 'NO', '2013.02.05-11.43.16');
INSERT INTO `ftppassword0` VALUES ('australianbatclinic.com.au', 'australianbatclinic', 'australianbatclinic', 'NO', '2013.02.06-16.15.35');
INSERT INTO `ftppassword0` VALUES ('australianbatclinic.com.au', 'data', '2011', 'NO', '2013.02.06-16.39.01');
INSERT INTO `ftppassword0` VALUES ('australianbatclinic.com.au', 'web', 'australianbatclinic12345', 'NO', '2013.02.06-16.35.52');
INSERT INTO `ftppassword0` VALUES ('australianclimatemadness.com', 'ftp@australianclimatemadness.com', 'zxcvbnm', 'NO', '2013.02.06-15.32.02');
INSERT INTO `ftppassword0` VALUES ('auto.gooniu.com', 'sybase', '2012', 'NO', '2013.02.04-14.41.36');
INSERT INTO `ftppassword0` VALUES ('av-tube.com', 'sybase', 'av-tube.comav-tube.com', 'NO', '2013.02.07-10.51.54');
INSERT INTO `ftppassword0` VALUES ('avoidaclaim.com', 'avoidaclaim.com', 'admin', 'NO', '2013.02.06-09.52.33');
INSERT INTO `ftppassword0` VALUES ('awe.mol.uj.edu.pl', 'uj.edu.pl', '2010', 'NO', '2013.02.07-07.53.52');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'access', 'mnbvcxz', 'NO', '2013.02.04-19.44.52');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'account', 'mnbvcxz', 'NO', '2013.02.04-19.43.37');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'admin', '2011', 'NO', '2013.02.04-20.02.18');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'administrator', 'mnbvcxz', 'NO', '2013.02.04-20.03.32');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'axinbao', '007', 'NO', '2013.02.04-19.36.54');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'axinbao.com', 'mnbvcxz', 'NO', '2013.02.04-19.38.01');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'backup', 'zxcvbnm', 'NO', '2013.02.04-19.49.53');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'data', 'mnbvcxz', 'NO', '2013.02.04-19.40.33');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'ftp', 'enable', 'NO', '2013.02.04-20.04.57');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'ftp@axinbao.com', '123123', 'NO', '2013.02.04-19.34.31');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'guest', 'mnbvcxz', 'NO', '2013.02.04-19.48.36');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'lizdy', '2012', 'NO', '2013.02.04-19.53.55');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'mysql', '2011', 'NO', '2013.02.04-19.56.35');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'network', '2011', 'NO', '2013.02.04-19.42.26');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'news', '2011', 'NO', '2013.02.04-19.41.49');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'oracle', 'zxcvbnm', 'NO', '2013.02.04-19.59.03');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'oracle8', 'zxcvbnm', 'NO', '2013.02.04-19.57.49');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'root', 'mnbvcxz', 'NO', '2013.02.04-20.01.37');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'sybase', 'zxcvbnm', 'NO', '2013.02.04-19.52.31');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'test', 'mnbvcxz', 'NO', '2013.02.04-19.55.10');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'user', 'mnbvcxz', 'NO', '2013.02.04-19.51.09');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'web', '123abc', 'NO', '2013.02.04-19.39.25');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'webmaster', '2012', 'NO', '2013.02.04-20.00.25');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'webmaster@axinbao.com', 'zxcvbnm', 'NO', '2013.02.04-19.35.34');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'www', '2010', 'NO', '2013.02.04-19.46.07');
INSERT INTO `ftppassword0` VALUES ('axinbao.com', 'wwwadmin', 'mnbvcxz', 'NO', '2013.02.04-19.47.17');
INSERT INTO `ftppassword0` VALUES ('balayoga.com', 'ftp@balayoga.com', 'mnbvcxz', 'NO', '2013.02.07-14.54.34');
INSERT INTO `ftppassword0` VALUES ('baohe.qqbaobao.com', 'administrator', 'administrator', 'NO', '2013.02.04-18.13.39');
INSERT INTO `ftppassword0` VALUES ('baohe.qqbaobao.com', 'webmaster', '123qwe', 'NO', '2013.02.04-17.48.42');
INSERT INTO `ftppassword0` VALUES ('Bassfamilyfarms.com', 'guest', 'Internet', 'NO', '2013.02.07-11.42.54');
INSERT INTO `ftppassword0` VALUES ('bbs.18wos.org', 'administrator', 'bbs.18wos.org12345', 'NO', '2013.02.04-17.37.09');
INSERT INTO `ftppassword0` VALUES ('bbs.18wos.org', 'user', 'abc123', 'NO', '2013.02.04-17.14.55');
INSERT INTO `ftppassword0` VALUES ('bbs.18wos.org', 'webmaster@18wos.org', 'enable', 'NO', '2013.02.04-16.45.04');
INSERT INTO `ftppassword0` VALUES ('bbs.18wos.org', 'www', '121212', 'NO', '2013.02.04-17.05.48');
INSERT INTO `ftppassword0` VALUES ('bbs.50hacker.com', 'ftp', 'mnbvcxz', 'NO', '2013.02.04-17.29.28');
INSERT INTO `ftppassword0` VALUES ('bbs.atmmama.com', 'webmaster@atmmama.com', 'atmmama.combbs.atmmama.com', 'NO', '2013.02.04-19.18.41');
INSERT INTO `ftppassword0` VALUES ('bbs.big-cd.com', 'big-cd.com', '007', 'NO', '2013.02.04-19.18.30');
INSERT INTO `ftppassword0` VALUES ('bbs.chinafishing.com', 'chinafishing.com', '111', 'NO', '2013.02.04-19.41.07');
INSERT INTO `ftppassword0` VALUES ('bbs.nmglabs.com', 'account', '2010', 'NO', '2013.02.05-06.51.35');
INSERT INTO `ftppassword0` VALUES ('bbs.nmglabs.com', 'user', 'zxcvbnm', 'NO', '2013.02.05-07.19.31');
INSERT INTO `ftppassword0` VALUES ('bbs.txtnovel.com', 'oracle', '2600', 'NO', '2013.02.05-10.06.33');
INSERT INTO `ftppassword0` VALUES ('bcfm.org.uk', 'ftp@bcfm.org.uk', '0', 'NO', '2013.02.06-15.38.02');
INSERT INTO `ftppassword0` VALUES ('bdconf.com', 'bdconf.com', '1234567', 'NO', '2013.02.05-10.53.24');
INSERT INTO `ftppassword0` VALUES ('beautifulpixels.com', 'ftp@beautifulpixels.com', '2012', 'NO', '2013.02.07-11.12.23');
INSERT INTO `ftppassword0` VALUES ('beautyisembarrassing.com', 'webmaster@beautyisembarrassing.com', '2600', 'NO', '2013.02.05-11.02.14');
INSERT INTO `ftppassword0` VALUES ('benzandabackpack.com', 'ftp@benzandabackpack.com', 'zxcvbnm', 'NO', '2013.02.07-14.57.02');
INSERT INTO `ftppassword0` VALUES ('bestespressomachinereviewshq.com', 'test', '111', 'NO', '2013.02.06-16.35.36');
INSERT INTO `ftppassword0` VALUES ('bestplacetoselltimeshare.com', 'admin', '0', 'NO', '2013.02.05-14.20.13');
INSERT INTO `ftppassword0` VALUES ('bicycledesign.net', 'ftp@bicycledesign.net', 'mnbvcxz', 'NO', '2013.02.07-14.58.16');
INSERT INTO `ftppassword0` VALUES ('bicycledesign.net', 'news', 'super', 'NO', '2013.02.06-16.42.53');
INSERT INTO `ftppassword0` VALUES ('biggreenboulder.com', 'ftp@biggreenboulder.com', 'mnbvcxz', 'NO', '2013.02.06-13.50.35');
INSERT INTO `ftppassword0` VALUES ('bikeportland.org', 'ftp@bikeportland.org', 'mnbvcxz', 'NO', '2013.02.06-16.23.21');
INSERT INTO `ftppassword0` VALUES ('bikeportland.org', 'network', 'mnbvcxz', 'NO', '2013.02.06-16.42.27');
INSERT INTO `ftppassword0` VALUES ('bizsugar.com', 'ftp@bizsugar.com', 'mnbvcxz', 'NO', '2013.02.07-14.59.06');
INSERT INTO `ftppassword0` VALUES ('blackswhitewash.com', 'ftp@blackswhitewash.com', '2010', 'NO', '2013.02.06-15.42.47');
INSERT INTO `ftppassword0` VALUES ('blairrobertson.com', 'ftp@blairrobertson.com', 'mnbvcxz', 'NO', '2013.02.06-15.42.49');
INSERT INTO `ftppassword0` VALUES ('blog.art21.org', 'wwwadmin', '1234', 'NO', '2013.02.05-13.49.54');
INSERT INTO `ftppassword0` VALUES ('blog.carringtontheme.com', 'ftp@carringtontheme.com', 'mnbvcxz', 'NO', '2013.02.07-15.00.33');
INSERT INTO `ftppassword0` VALUES ('blog.economedia.bg', 'webmaster@economedia.bg', 'oracle', 'NO', '2013.02.06-22.17.27');
INSERT INTO `ftppassword0` VALUES ('blog.giallozafferano.it', 'blog.giallozafferano.it', '123456', 'NO', '2013.02.05-13.15.44');
INSERT INTO `ftppassword0` VALUES ('blog.howtoweb.co', 'ftp@howtoweb.co', 'alpha', 'NO', '2013.02.06-22.26.48');
INSERT INTO `ftppassword0` VALUES ('blog.makemoneysir.com', 'account', 'mnbvcxz', 'NO', '2013.02.05-13.27.24');
INSERT INTO `ftppassword0` VALUES ('blog.massmoca.org', 'blog.massmoca.org', '111', 'NO', '2013.02.05-13.13.52');
INSERT INTO `ftppassword0` VALUES ('blog.netpolitique.net', 'netpolitique.net', '2011', 'NO', '2013.02.06-21.54.53');
INSERT INTO `ftppassword0` VALUES ('blog.proudphotography.com', 'ftp@proudphotography.com', 'zxcvbnm', 'NO', '2013.02.06-09.56.32');
INSERT INTO `ftppassword0` VALUES ('blog.rossannamarie.me', 'ftp@rossannamarie.me', 'zxcvbnm', 'NO', '2013.02.06-09.57.11');
INSERT INTO `ftppassword0` VALUES ('blog.smartadserver.com', 'smartadserver.com', '!@#$%^&*()', 'NO', '2013.02.06-23.22.40');
INSERT INTO `ftppassword0` VALUES ('blogosquare.com', 'backup', '88888888', 'NO', '2013.02.05-14.18.58');
INSERT INTO `ftppassword0` VALUES ('blogosquare.com', 'ftp@blogosquare.com', 'super', 'NO', '2013.02.05-13.39.21');
INSERT INTO `ftppassword0` VALUES ('blogosquare.com', 'guest', '0', 'NO', '2013.02.05-14.14.17');
INSERT INTO `ftppassword0` VALUES ('blogosquare.com', 'test', 'test', 'NO', '2013.02.05-14.34.15');
INSERT INTO `ftppassword0` VALUES ('blogosquare.com', 'wwwadmin', 'abc123', 'NO', '2013.02.05-14.11.46');
INSERT INTO `ftppassword0` VALUES ('blogs.adobe.com', 'adobe', 'abc123', 'NO', '2013.02.05-13.47.06');
INSERT INTO `ftppassword0` VALUES ('blogs.rcuk.ac.uk', 'ftp@rcuk.ac.uk', 'rcuk888', null, '2013.02.07-16.55.50');
INSERT INTO `ftppassword0` VALUES ('bobydimitrov.com', 'ftp@bobydimitrov.com', 'godblessyou', 'NO', '2013.02.06-22.28.13');
INSERT INTO `ftppassword0` VALUES ('boston.curbed.com', 'mysql', '00000000', 'NO', '2013.02.05-14.47.45');
INSERT INTO `ftppassword0` VALUES ('boston.curbed.com', 'sybase', 'database', 'NO', '2013.02.05-14.40.54');
INSERT INTO `ftppassword0` VALUES ('boston.eater.com', 'account', 'pass', 'NO', '2013.02.05-14.26.13');
INSERT INTO `ftppassword0` VALUES ('boston.eater.com', 'backup', '2012', 'NO', '2013.02.05-14.35.57');
INSERT INTO `ftppassword0` VALUES ('boston.racked.com', 'boston.racked.com', '111', 'NO', '2013.02.05-14.16.29');
INSERT INTO `ftppassword0` VALUES ('boston.racked.com', 'oracle8', '2012', 'NO', '2013.02.05-14.50.00');
INSERT INTO `ftppassword0` VALUES ('brillianter.com', 'ftp@brillianter.com', 'mnbvcxz', 'NO', '2013.02.07-09.00.37');
INSERT INTO `ftppassword0` VALUES ('browsehappy.com', 'browsehappy.com', '123qwe', 'NO', '2013.02.05-14.35.46');
INSERT INTO `ftppassword0` VALUES ('browsehappy.com', 'data', '000000', 'NO', '2013.02.05-14.47.30');
INSERT INTO `ftppassword0` VALUES ('brucerosenstein.com', 'news', 'brucerosenstein', 'NO', '2013.02.05-14.41.04');
INSERT INTO `ftppassword0` VALUES ('bt.gxbs.net', 'gxbs.net', 'gxbs888', 'NO', '2013.02.05-15.03.28');
INSERT INTO `ftppassword0` VALUES ('bumbumbum.me', 'ftp@bumbumbum.me', '0', 'NO', '2013.02.06-16.03.27');
INSERT INTO `ftppassword0` VALUES ('bumwine.com', 'guest', 'bumwine12345', 'NO', '2013.02.05-15.01.29');
INSERT INTO `ftppassword0` VALUES ('bumwine.com', 'webmaster@bumwine.com', 'pass', 'NO', '2013.02.05-14.38.27');
INSERT INTO `ftppassword0` VALUES ('burningtreeranch.com', 'ftp@burningtreeranch.com', 'mnbvcxz', 'NO', '2013.02.07-15.01.55');
INSERT INTO `ftppassword0` VALUES ('burnsidebrooklyn.com', 'ftp@burnsidebrooklyn.com', 'zxcvbnm', 'NO', '2013.02.07-09.04.51');
INSERT INTO `ftppassword0` VALUES ('cambridgelocalfirst.org', 'ftp@cambridgelocalfirst.org', '2012', 'NO', '2013.02.07-15.02.45');
INSERT INTO `ftppassword0` VALUES ('cancookmustcook.com', 'ftp@cancookmustcook.com', '123asd', 'NO', '2013.02.05-15.00.42');
INSERT INTO `ftppassword0` VALUES ('canon.ueuo.com', 'admin', '2600', 'NO', '2013.02.06-10.44.21');
INSERT INTO `ftppassword0` VALUES ('carelessnavigator.com', 'account', 'root', 'NO', '2013.02.05-19.44.34');
INSERT INTO `ftppassword0` VALUES ('carringtontheme.com', 'ftp@carringtontheme.com', 'zxcvbnm', 'NO', '2013.02.07-15.03.11');
INSERT INTO `ftppassword0` VALUES ('catalysttheme.com', 'ftp@catalysttheme.com', '2012', 'NO', '2013.02.06-10.05.14');
INSERT INTO `ftppassword0` VALUES ('causeequalstime.com', 'ftp@causeequalstime.com', 'mnbvcxz', 'NO', '2013.02.07-11.31.32');
INSERT INTO `ftppassword0` VALUES ('cboblog.cbo.gov', 'cbo', 'abc123', 'NO', '2013.02.05-19.10.58');
INSERT INTO `ftppassword0` VALUES ('centerforinquiry.net', 'ftp@centerforinquiry.net', 'zxcvbnm', 'NO', '2013.02.07-15.03.22');
INSERT INTO `ftppassword0` VALUES ('ceriscope.sciences-po.fr', 'ftp@sciences-po.fr', '0', 'NO', '2013.02.06-21.51.51');
INSERT INTO `ftppassword0` VALUES ('ceriscope.sciences-po.fr', 'sciences-po.fr', '2010', 'NO', '2013.02.06-21.59.50');
INSERT INTO `ftppassword0` VALUES ('ceriscope.sciences-po.fr', 'web', 'abc123', 'NO', '2013.02.06-22.07.07');
INSERT INTO `ftppassword0` VALUES ('challies.com', 'ftp@challies.com', 'mnbvcxz', 'NO', '2013.02.06-15.54.21');
INSERT INTO `ftppassword0` VALUES ('chasingdelicious.com', 'ftp@chasingdelicious.com', 'zxcvbnm', 'NO', '2013.02.06-22.55.08');
INSERT INTO `ftppassword0` VALUES ('chasingdelicious.com', 'root', 'abc', 'NO', '2013.02.07-00.15.12');
INSERT INTO `ftppassword0` VALUES ('chasingdelicious.com', 'webmaster@chasingdelicious.com', 'database', 'NO', '2013.02.06-22.57.20');
INSERT INTO `ftppassword0` VALUES ('chicago.curbed.com', 'backup', 'chicago.curbed.com123', 'NO', '2013.02.05-20.25.35');
INSERT INTO `ftppassword0` VALUES ('chicago.eater.com', 'webmaster', '2002', 'NO', '2013.02.05-20.41.37');
INSERT INTO `ftppassword0` VALUES ('chicago.racked.com', 'webmaster', 'abc123', 'NO', '2013.02.05-20.43.59');
INSERT INTO `ftppassword0` VALUES ('chickensintheroad.com', 'ftp@chickensintheroad.com', 'mnbvcxz', 'NO', '2013.02.07-13.39.43');
INSERT INTO `ftppassword0` VALUES ('chiiki-net.info', 'ftp@chiiki-net.info', 'mnbvcxz', 'NO', '2013.02.07-16.12.27');
INSERT INTO `ftppassword0` VALUES ('chistes.dechile.net', 'dechile.net', '1', null, '2013.02.07-17.12.38');
INSERT INTO `ftppassword0` VALUES ('chistes.dechile.net', 'ftp@dechile.net', 'mnbvcxz', null, '2013.02.07-17.00.10');
INSERT INTO `ftppassword0` VALUES ('churchm.ag', 'ftp@churchm.ag', 'mnbvcxz', 'NO', '2013.02.07-15.04.17');
INSERT INTO `ftppassword0` VALUES ('cialiscodex.com', 'ftp@cialiscodex.com', 'mnbvcxz', null, '2013.02.07-16.34.52');
INSERT INTO `ftppassword0` VALUES ('cialiscodex.com', 'user', '00000000', null, '2013.02.07-17.13.08');
INSERT INTO `ftppassword0` VALUES ('citysip.com', 'lizdy', 'zxcvbnm', 'NO', '2013.02.05-20.54.17');
INSERT INTO `ftppassword0` VALUES ('ciudades.dechile.net', 'ftp@dechile.net', 'mnbvcxz', null, '2013.02.07-17.01.08');
INSERT INTO `ftppassword0` VALUES ('clementine-goyard.fr', 'account', '2011', 'NO', '2013.02.05-20.53.22');
INSERT INTO `ftppassword0` VALUES ('club-alljapan.com', 'ftp@club-alljapan.com', 'mnbvcxz', 'NO', '2013.02.06-10.15.10');
INSERT INTO `ftppassword0` VALUES ('cn.winmount.com', 'winmount.com', '123asd', 'NO', '2013.02.05-21.31.33');
INSERT INTO `ftppassword0` VALUES ('cn.winmount.com', 'wwwadmin', 'server', 'NO', '2013.02.05-21.50.07');
INSERT INTO `ftppassword0` VALUES ('codeforces.com', 'admin', '12345', 'NO', '2013.02.07-13.40.18');
INSERT INTO `ftppassword0` VALUES ('codeforces.ru', 'admin', '12345', 'NO', '2013.02.07-13.40.54');
INSERT INTO `ftppassword0` VALUES ('codeforces.ru', 'codeforces.ru', '123123', 'NO', '2013.02.07-15.05.34');
INSERT INTO `ftppassword0` VALUES ('codex.wordthai.com', 'webmaster@wordthai.com', '111111', 'NO', '2013.02.05-21.27.19');
INSERT INTO `ftppassword0` VALUES ('codmagazine.com', 'network', 'abc', 'NO', '2013.02.05-22.21.24');
INSERT INTO `ftppassword0` VALUES ('colt-rane.com', 'web', '2011', 'NO', '2013.02.06-16.44.26');
INSERT INTO `ftppassword0` VALUES ('columnfivemedia.com', 'ftp@columnfivemedia.com', 'zxcvbnm', 'NO', '2013.02.07-08.03.26');
INSERT INTO `ftppassword0` VALUES ('community.dooce.com', 'ftp@dooce.com', '2012', 'NO', '2013.02.06-16.14.53');
INSERT INTO `ftppassword0` VALUES ('connorcourt.com', 'ftp@connorcourt.com', 'zxcvbnm', 'NO', '2013.02.06-16.10.20');
INSERT INTO `ftppassword0` VALUES ('cookingwithsin.com', 'oracle8', '123qwe', 'NO', '2013.02.05-22.22.13');
INSERT INTO `ftppassword0` VALUES ('corinnebouchoux.eelv.fr', 'corinnebouchoux.eelv.fr', '121212', 'NO', '2013.02.06-22.42.10');
INSERT INTO `ftppassword0` VALUES ('corinnebouchoux.eelv.fr', 'eelv', '123abc', 'NO', '2013.02.06-22.34.27');
INSERT INTO `ftppassword0` VALUES ('corinnebouchoux.eelv.fr', 'eelv.fr', '123', 'NO', '2013.02.06-22.40.59');
INSERT INTO `ftppassword0` VALUES ('corinnebouchoux.eelv.fr', 'ftp@eelv.fr', '1234qwer', 'NO', '2013.02.06-22.26.42');
INSERT INTO `ftppassword0` VALUES ('correntewire.com', 'ftp@correntewire.com', 'mnbvcxz', 'NO', '2013.02.06-13.09.04');
INSERT INTO `ftppassword0` VALUES ('cosmicrepairshop.com', 'web', 'web12', 'NO', '2013.02.05-22.09.03');
INSERT INTO `ftppassword0` VALUES ('cosplay.pclovers.net', 'cosplay.pclovers.net', '111', 'NO', '2013.02.07-11.50.53');
INSERT INTO `ftppassword0` VALUES ('cowboyjunkies.com', 'ftp@cowboyjunkies.com', 'mnbvcxz', 'NO', '2013.02.07-15.06.21');
INSERT INTO `ftppassword0` VALUES ('craftgossip.com', 'ftp', 'mnbvcxz', 'NO', '2013.02.07-15.07.14');
INSERT INTO `ftppassword0` VALUES ('dadushin.com', 'ftp', 'mnbvcxz', 'NO', '2013.02.07-15.08.06');
INSERT INTO `ftppassword0` VALUES ('dadushin.com', 'ftp@dadushin.com', 'zxcvbnm', 'NO', '2013.02.07-09.34.38');
INSERT INTO `ftppassword0` VALUES ('dailytimes.elpasotimes.net', 'ftp@elpasotimes.net', 'mnbvcxz', 'NO', '2013.02.06-12.07.44');
INSERT INTO `ftppassword0` VALUES ('danhughes.auditblogs.com', 'ftp@auditblogs.com', 'zxcvbnm', 'NO', '2013.02.07-15.08.19');
INSERT INTO `ftppassword0` VALUES ('daysofadomesticdad.com', 'ftp', 'mnbvcxz', 'NO', '2013.02.07-15.09.11');
INSERT INTO `ftppassword0` VALUES ('daysofadomesticdad.com', 'ftp@daysofadomesticdad.com', 'zxcvbnm', 'NO', '2013.02.07-15.09.56');
INSERT INTO `ftppassword0` VALUES ('deaeno.com', 'ftp@deaeno.com', 'zxcvbnm', 'NO', '2013.02.06-10.28.18');
INSERT INTO `ftppassword0` VALUES ('deai.navnavnav.com', 'deai.navnavnav.com', '123', 'NO', '2013.02.07-11.55.00');
INSERT INTO `ftppassword0` VALUES ('deai.navnavnav.com', 'lizdy', '123456', 'NO', '2013.02.07-12.22.25');
INSERT INTO `ftppassword0` VALUES ('deai.navnavnav.com', 'navnavnav', '!@#$%^&*()', 'NO', '2013.02.07-11.49.37');
INSERT INTO `ftppassword0` VALUES ('deai.navnavnav.com', 'www', 'navnavnav.comdeai.navnavnav.com', 'NO', '2013.02.07-12.10.14');
INSERT INTO `ftppassword0` VALUES ('deedeeparis.com', 'deedeeparis', 'xp', 'NO', '2013.02.06-22.33.52');
INSERT INTO `ftppassword0` VALUES ('deedeeparis.com', 'deedeeparis.com', 'password', 'NO', '2013.02.06-22.38.13');
INSERT INTO `ftppassword0` VALUES ('diet.nosbl.com', 'ftp@nosbl.com', 'mnbvcxz', null, '2013.02.07-16.51.01');
INSERT INTO `ftppassword0` VALUES ('digitalk.capital.bg', 'capital', '123123', 'NO', '2013.02.06-22.35.00');
INSERT INTO `ftppassword0` VALUES ('digitalk.capital.bg', 'webmaster@capital.bg', '123', 'NO', '2013.02.06-22.32.57');
INSERT INTO `ftppassword0` VALUES ('digitalnature.eu', 'ftp@digitalnature.eu', 'zxcvbnm', 'NO', '2013.02.07-15.10.42');
INSERT INTO `ftppassword0` VALUES ('diversitywoman.com', 'data', 'test', 'NO', '2013.02.06-12.24.11');
INSERT INTO `ftppassword0` VALUES ('dontloseyourdayjob.com', 'ftp@dontloseyourdayjob.com', 'zxcvbnm', 'NO', '2013.02.07-15.11.12');
INSERT INTO `ftppassword0` VALUES ('dreamupstudios.com', 'admin', 'zxcvbnm', 'NO', '2013.02.07-14.14.13');
INSERT INTO `ftppassword0` VALUES ('dubcnn.com', 'ftp@dubcnn.com', 'zxcvbnm', 'NO', '2013.02.07-13.44.18');
INSERT INTO `ftppassword0` VALUES ('ducksforum.net', 'ftp', 'mnbvcxz', 'NO', '2013.02.07-13.44.40');
INSERT INTO `ftppassword0` VALUES ('ducksforum.net', 'ftp@ducksforum.net', 'zxcvbnm', 'NO', '2013.02.07-09.34.55');
INSERT INTO `ftppassword0` VALUES ('ducksforum.net', 'guest', '2010', 'NO', '2013.02.07-10.29.55');
INSERT INTO `ftppassword0` VALUES ('dyspepsiageneration.com', 'backup', '111111', 'NO', '2013.02.07-11.08.55');
INSERT INTO `ftppassword0` VALUES ('echange-maison.net', 'echange-maison', 'xp', 'NO', '2013.02.06-22.37.20');
INSERT INTO `ftppassword0` VALUES ('ecologistes-senat.fr', 'data', 'server', 'NO', '2013.02.06-22.46.41');
INSERT INTO `ftppassword0` VALUES ('ecologistes-senat.fr', 'ecologistes-senat', 'godblessyou', 'NO', '2013.02.06-22.37.53');
INSERT INTO `ftppassword0` VALUES ('ecologistes-senat.fr', 'ecologistes-senat.fr', 'server', 'NO', '2013.02.06-22.41.33');
INSERT INTO `ftppassword0` VALUES ('ecoloinfo.com', 'webmaster@ecoloinfo.com', '1234qwer', 'NO', '2013.02.06-22.35.09');
INSERT INTO `ftppassword0` VALUES ('ecolosites.eelv.fr', 'ecolosites.eelv.fr', '123abc', 'NO', '2013.02.06-22.46.30');
INSERT INTO `ftppassword0` VALUES ('ecolosites.eelv.fr', 'eelv', 'zxcvbnm', 'NO', '2013.02.06-22.40.42');
INSERT INTO `ftppassword0` VALUES ('ecolosites.eelv.fr', 'webmaster@eelv.fr', 'godblessyou', 'NO', '2013.02.06-22.37.38');
INSERT INTO `ftppassword0` VALUES ('ecuablogs.com', 'ftp@ecuablogs.com', 'mnbvcxz', null, '2013.02.07-17.41.33');
INSERT INTO `ftppassword0` VALUES ('edcabellon.com', 'ftp@edcabellon.com', '2012', 'NO', '2013.02.07-13.44.51');
INSERT INTO `ftppassword0` VALUES ('eddriscoll.com', 'ftp@eddriscoll.com', '2012', 'NO', '2013.02.07-13.45.04');
INSERT INTO `ftppassword0` VALUES ('eelv.fr', 'eelv', 'computer', 'NO', '2013.02.06-22.42.09');
INSERT INTO `ftppassword0` VALUES ('eelv.fr', 'webmaster@eelv.fr', '000000', 'NO', '2013.02.06-22.39.33');
INSERT INTO `ftppassword0` VALUES ('eighthourday.com', 'oracle8', 'sybase', 'NO', '2013.02.07-10.30.11');
INSERT INTO `ftppassword0` VALUES ('electroniccigaretteboutique.com', 'ftp@electroniccigaretteboutique.com', 'mnbvcxz', null, '2013.02.07-17.41.59');
INSERT INTO `ftppassword0` VALUES ('elementsdesign.com', 'ftp@elementsdesign.com', 'zxcvbnm', 'NO', '2013.02.06-22.34.38');
INSERT INTO `ftppassword0` VALUES ('emobc.com', 'ftp@emobc.com', 'zxcvbnm', null, '2013.02.07-17.42.09');
INSERT INTO `ftppassword0` VALUES ('ericstoller.com', 'ftp@ericstoller.com', 'ericstoller123', 'NO', '2013.02.06-22.39.40');
INSERT INTO `ftppassword0` VALUES ('ero-frontier.com', 'ftp@ero-frontier.com', '2011', 'NO', '2013.02.06-08.40.55');
INSERT INTO `ftppassword0` VALUES ('ero.adultch.net', 'oracle', 'Internet', 'NO', '2013.02.07-12.47.26');
INSERT INTO `ftppassword0` VALUES ('erowan.net', 'erowan', 'pass', 'NO', '2013.02.06-11.01.07');
INSERT INTO `ftppassword0` VALUES ('essayswriter.net', 'ftp@essayswriter.net', '2012', 'NO', '2013.02.07-15.13.08');
INSERT INTO `ftppassword0` VALUES ('esthe-matsudo.com', 'ftp@esthe-matsudo.com', 'zxcvbnm', 'NO', '2013.02.06-10.58.43');
INSERT INTO `ftppassword0` VALUES ('ethancodes.com', 'ethancodes.com', '123', 'NO', '2013.02.07-12.08.06');
INSERT INTO `ftppassword0` VALUES ('etimologias.dechile.net', 'ftp@dechile.net', 'zxcvbnm', null, '2013.02.07-17.42.45');
INSERT INTO `ftppassword0` VALUES ('eventoblog.com', 'ftp@eventoblog.com', '1234qwer', null, '2013.02.07-17.43.19');
INSERT INTO `ftppassword0` VALUES ('eversolovely.com', 'ftp@eversolovely.com', 'mnbvcxz', 'NO', '2013.02.07-15.13.32');
INSERT INTO `ftppassword0` VALUES ('ezvideoguy.com', 'ftp@ezvideoguy.com', 'zxcvbnm', 'NO', '2013.02.07-13.46.40');
INSERT INTO `ftppassword0` VALUES ('facebook.stephendesroches.com', 'ftp@stephendesroches.com', 'mnbvcxz', 'NO', '2013.02.07-15.13.46');
INSERT INTO `ftppassword0` VALUES ('family.s11.x-beat.com', 'ftp@x-beat.com', '1234567', 'NO', '2013.02.06-23.48.24');
INSERT INTO `ftppassword0` VALUES ('family.s11.x-beat.com', 'webmaster@x-beat.com', 'abc', 'NO', '2013.02.06-23.50.23');
INSERT INTO `ftppassword0` VALUES ('family.s11.x-beat.com', 'x-beat', 'x-beat.com888', 'NO', '2013.02.07-00.11.25');
INSERT INTO `ftppassword0` VALUES ('farmhopping.com', 'ftp@farmhopping.com', '1', 'NO', '2013.02.06-22.50.04');
INSERT INTO `ftppassword0` VALUES ('fiberevolution.com', 'fiberevolution', 'Internet', 'NO', '2013.02.07-09.53.59');
INSERT INTO `ftppassword0` VALUES ('fifth-chome.com', 'ftp@fifth-chome.com', 'zxcvbnm', 'NO', '2013.02.07-15.15.19');
INSERT INTO `ftppassword0` VALUES ('fightingforliberty.com', 'ftp@fightingforliberty.com', 'mnbvcxz', 'NO', '2013.02.07-09.52.00');
INSERT INTO `ftppassword0` VALUES ('filmjourney.weblogger.com', 'oracle', 'enable', 'NO', '2013.02.07-11.55.35');
INSERT INTO `ftppassword0` VALUES ('finshops.com', 'ftp@finshops.com', 'mnbvcxz', 'NO', '2013.02.07-13.47.53');
INSERT INTO `ftppassword0` VALUES ('fireemblemwiki.org', 'ftp@fireemblemwiki.org', 'zxcvbnm', 'NO', '2013.02.06-22.49.46');
INSERT INTO `ftppassword0` VALUES ('floydwebb.com', 'ftp@floydwebb.com', 'zxcvbnm', 'NO', '2013.02.07-15.16.06');
INSERT INTO `ftppassword0` VALUES ('focusedonlight.com', 'ftp@focusedonlight.com', 'mnbvcxz', 'NO', '2013.02.07-15.16.31');
INSERT INTO `ftppassword0` VALUES ('foodformyfamily.com', 'ftp@foodformyfamily.com', 'mnbvcxz', 'NO', '2013.02.07-12.13.28');
INSERT INTO `ftppassword0` VALUES ('foodformyfamily.com', 'web', '000000', 'NO', '2013.02.07-12.21.44');
INSERT INTO `ftppassword0` VALUES ('forum.2001jeux.com', 'ftp@2001jeux.com', 'mnbvcxz', 'NO', '2013.02.07-09.55.02');
INSERT INTO `ftppassword0` VALUES ('freewpthemes.co', 'ftp@freewpthemes.co', 'zxcvbnm', 'NO', '2013.02.07-15.17.06');
INSERT INTO `ftppassword0` VALUES ('freewpthemesblog.com', 'ftp@freewpthemesblog.com', 'mnbvcxz', 'NO', '2013.02.07-13.49.27');
INSERT INTO `ftppassword0` VALUES ('freshpolitics.us', 'ftp@freshpolitics.us', 'mnbvcxz', 'NO', '2013.02.07-09.57.55');
INSERT INTO `ftppassword0` VALUES ('fube8f.com', 'access', 'fube8f', 'NO', '2013.02.06-12.01.42');
INSERT INTO `ftppassword0` VALUES ('fube8f.com', 'wwwadmin', 'server', 'NO', '2013.02.06-12.05.12');
INSERT INTO `ftppassword0` VALUES ('funkatrondigital.com', 'ftp@funkatrondigital.com', 'mnbvcxz', 'NO', '2013.02.07-12.29.44');
INSERT INTO `ftppassword0` VALUES ('fuzoku-s.net', 'ftp@fuzoku-s.net', 'mnbvcxz', 'NO', '2013.02.06-11.39.36');
INSERT INTO `ftppassword0` VALUES ('fuzoku-shibu.net', 'ftp@fuzoku-shibu.net', 'mnbvcxz', 'NO', '2013.02.06-11.39.39');
INSERT INTO `ftppassword0` VALUES ('fuzoku-shin.net', 'ftp@fuzoku-shin.net', 'mnbvcxz', 'NO', '2013.02.06-11.39.41');
INSERT INTO `ftppassword0` VALUES ('fuzoku-sm.net', 'ftp@fuzoku-sm.net', 'mnbvcxz', 'NO', '2013.02.06-11.39.39');
INSERT INTO `ftppassword0` VALUES ('fx2.nosbl.com', 'ftp@nosbl.com', 'mnbvcxz', null, '2013.02.07-18.10.45');
INSERT INTO `ftppassword0` VALUES ('garancedore.fr', 'backup', 'backup12', 'NO', '2013.02.06-23.27.04');
INSERT INTO `ftppassword0` VALUES ('garancedore.fr', 'ftp@garancedore.fr', '0', 'NO', '2013.02.06-22.52.46');
INSERT INTO `ftppassword0` VALUES ('garancedore.fr', 'webmaster@garancedore.fr', 'alpha', 'NO', '2013.02.06-22.55.29');
INSERT INTO `ftppassword0` VALUES ('garancedore.fr', 'wwwadmin', 'garancedore.fr888', 'NO', '2013.02.06-23.22.13');
INSERT INTO `ftppassword0` VALUES ('gardnercampbell.net', 'web', 'test', 'NO', '2013.02.06-12.04.42');
INSERT INTO `ftppassword0` VALUES ('gbearn-forex.com', 'ftp@gbearn-forex.com', 'zxcvbnm', null, '2013.02.07-18.10.59');
INSERT INTO `ftppassword0` VALUES ('gceleb.com', 'ftp@gceleb.com', 'mnbvcxz', 'NO', '2013.02.07-12.41.48');
INSERT INTO `ftppassword0` VALUES ('geekblog.oneandoneis2.org', 'oneandoneis2.org', 'administrator', 'NO', '2013.02.07-12.46.12');
INSERT INTO `ftppassword0` VALUES ('geezersisters.com', 'ftp@geezersisters.com', 'mnbvcxz', 'NO', '2013.02.07-15.18.13');
INSERT INTO `ftppassword0` VALUES ('geezersisters.com', 'network', 'mnbvcxz', 'NO', '2013.02.06-23.21.35');
INSERT INTO `ftppassword0` VALUES ('geotarget-iplookup.info', 'ftp@geotarget-iplookup.info', 'mnbvcxz', 'NO', '2013.02.07-12.43.06');
INSERT INTO `ftppassword0` VALUES ('geotarget-iplookup.info', 'geotarget-iplookup', '123asd', 'NO', '2013.02.07-12.46.02');
INSERT INTO `ftppassword0` VALUES ('geotarget-iplookup.info', 'root', '1234qwer', 'NO', '2013.02.07-13.44.57');
INSERT INTO `ftppassword0` VALUES ('gey.adultlesson1.com', 'ftp@adultlesson1.com', '2010', null, '2013.02.07-18.11.19');
INSERT INTO `ftppassword0` VALUES ('gilles.wittezaele.fr', 'ftp@wittezaele.fr', 'zxcvbnm', 'NO', '2013.02.06-22.52.43');
INSERT INTO `ftppassword0` VALUES ('glimpsescience.net', 'ftp@glimpsescience.net', 'mnbvcxz', 'NO', '2013.02.07-15.19.02');
INSERT INTO `ftppassword0` VALUES ('gobernantes.dechile.net', 'ftp@dechile.net', '2012', null, '2013.02.07-18.13.40');
INSERT INTO `ftppassword0` VALUES ('godonnybrook.com', 'guest', 'guest123', 'NO', '2013.02.07-13.37.37');
INSERT INTO `ftppassword0` VALUES ('gplus.stephendesroches.com', 'access', 'gplus.stephendesroches.com888', 'NO', '2013.02.07-00.01.14');
INSERT INTO `ftppassword0` VALUES ('gplus.stephendesroches.com', 'ftp@stephendesroches.com', 'zxcvbnm', 'NO', '2013.02.07-15.19.58');
INSERT INTO `ftppassword0` VALUES ('hackingthehumanities.org', 'hackingthehumanities.org', '1', 'NO', '2013.02.06-12.13.50');
INSERT INTO `ftppassword0` VALUES ('halocoatings.com', 'account', '00000000', 'NO', '2013.02.06-23.13.43');
INSERT INTO `ftppassword0` VALUES ('halocoatings.com', 'data', 'data12', 'NO', '2013.02.06-23.06.47');
INSERT INTO `ftppassword0` VALUES ('halocoatings.com', 'ftp@halocoatings.com', 'mnbvcxz', 'NO', '2013.02.06-22.53.22');
INSERT INTO `ftppassword0` VALUES ('halocoatings.com', 'network', 'godblessyou', 'NO', '2013.02.06-23.10.12');
INSERT INTO `ftppassword0` VALUES ('halocoatings.com', 'root', 'server', 'NO', '2013.02.06-23.56.07');
INSERT INTO `ftppassword0` VALUES ('handheldconf.com', 'ftp@handheldconf.com', 'mnbvcxz', 'NO', '2013.02.07-12.58.02');
INSERT INTO `ftppassword0` VALUES ('hardknock.tv', 'ftp@hardknock.tv', 'hardknock123', 'NO', '2013.02.07-13.00.47');
INSERT INTO `ftppassword0` VALUES ('hatemongers.mu.nu', 'ftp@hatemongers.mu.nu', 'zxcvbnm', 'NO', '2013.02.07-13.00.11');
INSERT INTO `ftppassword0` VALUES ('healthy-delicious.com', 'ftp@healthy-delicious.com', 'zxcvbnm', 'NO', '2013.02.07-13.03.03');
INSERT INTO `ftppassword0` VALUES ('heatherbrooke.org', 'ftp@heatherbrooke.org', 'mnbvcxz', 'NO', '2013.02.07-15.21.41');
INSERT INTO `ftppassword0` VALUES ('heathereatsalmondbutter.com', 'account', '2011', 'NO', '2013.02.06-13.48.48');
INSERT INTO `ftppassword0` VALUES ('heavylightrecords.com', 'ftp@heavylightrecords.com', 'mnbvcxz', 'NO', '2013.02.07-13.04.43');
INSERT INTO `ftppassword0` VALUES ('hege123.com', 'ftp@hege123.com', '2012', 'NO', '2013.02.06-22.53.23');
INSERT INTO `ftppassword0` VALUES ('helenaseodesign.com', 'mysql', 'oracle', 'NO', '2013.02.06-13.57.51');
INSERT INTO `ftppassword0` VALUES ('hghdefinition.com', 'ftp@hghdefinition.com', '2012', null, '2013.02.07-18.21.44');
INSERT INTO `ftppassword0` VALUES ('hiphop-n-more.com', 'ftp@hiphop-n-more.com', 'mnbvcxz', 'NO', '2013.02.07-13.08.09');
INSERT INTO `ftppassword0` VALUES ('hitchhikingtoheaven.com', 'ftp@hitchhikingtoheaven.com', 'mnbvcxz', 'NO', '2013.02.07-15.22.54');
INSERT INTO `ftppassword0` VALUES ('hitoduma.navnavnav.com', 'mysql', '!@#$%^&*()', 'NO', '2013.02.07-13.51.23');
INSERT INTO `ftppassword0` VALUES ('hitozumania.info', 'ftp@hitozumania.info', '2012', 'NO', '2013.02.07-15.23.04');
INSERT INTO `ftppassword0` VALUES ('homes.gruh.org', 'backup', 'abcd', 'NO', '2013.02.06-23.54.10');
INSERT INTO `ftppassword0` VALUES ('honeymedvd.com', 'ftp@honeymedvd.com', 'zxcvbnm', 'NO', '2013.02.06-12.39.39');
INSERT INTO `ftppassword0` VALUES ('hotateweb.com', 'account', 'hotateweb.com12345', 'NO', '2013.02.06-13.02.35');
INSERT INTO `ftppassword0` VALUES ('hotateweb.com', 'guest', 'guest123', 'NO', '2013.02.06-13.12.08');
INSERT INTO `ftppassword0` VALUES ('hotel-eliri.eu', 'ftp@hotel-eliri.eu', 'zxcvbnm', 'NO', '2013.02.06-23.15.41');
INSERT INTO `ftppassword0` VALUES ('hotel-eliri.eu', 'hotel-eliri', 'hotel-elirihotel-eliri.eu', 'NO', '2013.02.06-23.21.58');
INSERT INTO `ftppassword0` VALUES ('hotel-eliri.eu', 'lizdy', '88888888', 'NO', '2013.02.06-23.59.03');
INSERT INTO `ftppassword0` VALUES ('hotel-eliri.eu', 'oracle8', 'hotel-eliri', 'NO', '2013.02.07-00.06.38');
INSERT INTO `ftppassword0` VALUES ('hotel-eliri.eu', 'web', 'pass', 'NO', '2013.02.06-23.26.15');
INSERT INTO `ftppassword0` VALUES ('howtogetpaidforsurveys.com', 'www', 'super', 'NO', '2013.02.06-13.13.46');
INSERT INTO `ftppassword0` VALUES ('howtoweb.co', 'ftp@howtoweb.co', 'passwd', 'NO', '2013.02.06-23.21.19');
INSERT INTO `ftppassword0` VALUES ('html5weekly.com', 'ftp@html5weekly.com', 'zxcvbnm', 'NO', '2013.02.07-13.19.40');
INSERT INTO `ftppassword0` VALUES ('i-erect.com', 'guest', '0', 'NO', '2013.02.06-13.30.01');
INSERT INTO `ftppassword0` VALUES ('iamphildodd.com', 'iamphildodd.com', 'iamphildodd12345', 'NO', '2013.02.06-13.13.25');
INSERT INTO `ftppassword0` VALUES ('iamphildodd.com', 'web', '2600', 'NO', '2013.02.06-13.14.25');
INSERT INTO `ftppassword0` VALUES ('ianhin.es', 'ftp@ianhin.es', 'zxcvbnm', 'NO', '2013.02.07-13.22.32');
INSERT INTO `ftppassword0` VALUES ('icecap.us', 'news', '000000', 'NO', '2013.02.06-23.43.52');
INSERT INTO `ftppassword0` VALUES ('icecap.us', 'webmaster@icecap.us', 'mnbvcxz', 'NO', '2013.02.06-23.25.07');
INSERT INTO `ftppassword0` VALUES ('idf.eelv.fr', 'data', 'test', 'NO', '2013.02.07-00.11.26');
INSERT INTO `ftppassword0` VALUES ('idf.eelv.fr', 'eelv', 'Internet', 'NO', '2013.02.07-00.01.27');
INSERT INTO `ftppassword0` VALUES ('idf.eelv.fr', 'news', '123', 'NO', '2013.02.07-00.14.46');
INSERT INTO `ftppassword0` VALUES ('idf.eelv.fr', 'webmaster@eelv.fr', '1234qwer', 'NO', '2013.02.06-23.58.00');
INSERT INTO `ftppassword0` VALUES ('ignacioricci.com', 'ftp@ignacioricci.com', 'mnbvcxz', 'NO', '2013.02.07-13.27.03');
INSERT INTO `ftppassword0` VALUES ('iissonline.net', 'ftp@iissonline.net', 'zxcvbnm', 'NO', '2013.02.07-13.27.49');
INSERT INTO `ftppassword0` VALUES ('ilovethatphoto.net', 'ftp@ilovethatphoto.net', 'zxcvbnm', 'NO', '2013.02.07-15.25.19');
INSERT INTO `ftppassword0` VALUES ('impact.7973.com', '7973.com', 'passwd', 'NO', '2013.02.06-13.31.36');
INSERT INTO `ftppassword0` VALUES ('inkbarreltv.com', 'ftp@inkbarreltv.com', 'zxcvbnm', 'NO', '2013.02.06-13.23.36');
INSERT INTO `ftppassword0` VALUES ('ironchefshellie.com', 'user', 'ironchefshellie12345', 'NO', '2013.02.07-14.23.42');
INSERT INTO `ftppassword0` VALUES ('isuda.org', 'ftp@isuda.org', 'mnbvcxz', 'NO', '2013.02.07-07.32.08');
INSERT INTO `ftppassword0` VALUES ('it.playbonuscasino.net', 'ftp', 'mnbvcxz', 'NO', '2013.02.07-15.26.56');
INSERT INTO `ftppassword0` VALUES ('it.playbonuscasino.net', 'ftp@playbonuscasino.net', 'mnbvcxz', 'NO', '2013.02.07-15.27.17');
INSERT INTO `ftppassword0` VALUES ('ivoprokopiev.com', 'wwwadmin', '123456', 'NO', '2013.02.07-07.58.49');
INSERT INTO `ftppassword0` VALUES ('jasminewanders.com', 'ftp@jasminewanders.com', 'mnbvcxz', 'NO', '2013.02.07-15.32.34');
INSERT INTO `ftppassword0` VALUES ('jasonmcc.com', 'ftp@jasonmcc.com', 'mnbvcxz', 'NO', '2013.02.07-15.32.51');
INSERT INTO `ftppassword0` VALUES ('jasonmorrissey.org', 'ftp@jasonmorrissey.org', 'mnbvcxz', 'NO', '2013.02.07-15.33.22');
INSERT INTO `ftppassword0` VALUES ('jasonmorrissey.org', 'jasonmorrissey.org', '123asd', 'NO', '2013.02.07-13.45.43');
INSERT INTO `ftppassword0` VALUES ('joecraven.com', 'ftp@joecraven.com', 'mnbvcxz', 'NO', '2013.02.07-13.46.48');
INSERT INTO `ftppassword0` VALUES ('judykang.com', 'ftp@judykang.com', 'mnbvcxz', 'NO', '2013.02.07-15.33.42');
INSERT INTO `ftppassword0` VALUES ('justbarkingmad.com', 'ftp@justbarkingmad.com', '2012', 'NO', '2013.02.07-13.48.41');
INSERT INTO `ftppassword0` VALUES ('justsomethingimade.com', 'ftp@justsomethingimade.com', '2012', 'NO', '2013.02.07-07.33.02');
INSERT INTO `ftppassword0` VALUES ('kaka-cuuka.com', 'ftp@kaka-cuuka.com', '2011', 'NO', '2013.02.07-15.34.01');
INSERT INTO `ftppassword0` VALUES ('kanagawa-hitsearch.tk', 'kanagawa-hitsearch', '1', 'NO', '2013.02.06-14.03.42');
INSERT INTO `ftppassword0` VALUES ('kanagawa-hitsearch.tk', 'kanagawa-hitsearch.tk', 'kanagawa-hitsearch.tkkanagawa-hitsearch.tk', 'NO', '2013.02.06-14.07.20');
INSERT INTO `ftppassword0` VALUES ('kanagawa-hitsearch.tk', 'web', 'abc123', 'NO', '2013.02.06-14.09.11');
INSERT INTO `ftppassword0` VALUES ('katemiss.com', 'ftp@katemiss.com', 'zxcvbnm', 'NO', '2013.02.07-15.34.36');
INSERT INTO `ftppassword0` VALUES ('kevinandamanda.com', 'ftp@kevinandamanda.com', 'zxcvbnm', 'NO', '2013.02.07-07.36.01');
INSERT INTO `ftppassword0` VALUES ('killedbyradio.com', 'ftp@killedbyradio.com', 'zxcvbnm', 'NO', '2013.02.07-13.55.00');
INSERT INTO `ftppassword0` VALUES ('kingfortwodays.com', 'ftp@kingfortwodays.com', '2012', 'NO', '2013.02.07-13.55.37');
INSERT INTO `ftppassword0` VALUES ('kingfortwodays.com', 'kingfortwodays', '!@#$%^&*()', 'NO', '2013.02.07-13.59.48');
INSERT INTO `ftppassword0` VALUES ('knuttz.net', 'ftp@knuttz.net', 'zxcvbnm', 'NO', '2013.02.07-13.59.22');
INSERT INTO `ftppassword0` VALUES ('lamusicblog.com', 'lamusicblog.com', 'abc123', 'NO', '2013.02.07-14.19.11');
INSERT INTO `ftppassword0` VALUES ('landshape.org', 'access', 'zxcvbnm', 'NO', '2013.02.07-14.29.51');
INSERT INTO `ftppassword0` VALUES ('landshape.org', 'ftp@landshape.org', 'landshape.org888', 'NO', '2013.02.07-14.12.43');
INSERT INTO `ftppassword0` VALUES ('legalnomads.com', 'ftp@legalnomads.com', 'mnbvcxz', 'NO', '2013.02.07-14.21.01');
INSERT INTO `ftppassword0` VALUES ('likecer.com', 'ftp@likecer.com', 'mnbvcxz', 'NO', '2013.02.07-14.24.27');
INSERT INTO `ftppassword0` VALUES ('liliroby.com', 'ftp@liliroby.com', 'zxcvbnm', 'NO', '2013.02.07-14.24.39');
INSERT INTO `ftppassword0` VALUES ('link.moonx.net', 'ftp@moonx.net', '2012', 'NO', '2013.02.07-14.29.33');
INSERT INTO `ftppassword0` VALUES ('links.masklife.com', 'sybase', 'links.masklife.com888', 'NO', '2013.02.07-15.17.48');
INSERT INTO `ftppassword0` VALUES ('littled.dentonrc.com', 'guest', 'guest12', 'NO', '2013.02.07-15.13.49');
INSERT INTO `ftppassword0` VALUES ('livingwithoutreligion.org', 'data', 'data12', 'NO', '2013.02.07-14.52.19');
INSERT INTO `ftppassword0` VALUES ('livingwithoutreligion.org', 'ftp@livingwithoutreligion.org', 'zxcvbnm', 'NO', '2013.02.07-14.33.41');
INSERT INTO `ftppassword0` VALUES ('lizosaurus.com', 'lizosaurus.com', 'lizosaurus.com12', 'NO', '2013.02.07-15.16.01');
INSERT INTO `ftppassword0` VALUES ('local-artists.org', 'user', 'abc123', 'NO', '2013.02.07-15.21.30');
INSERT INTO `ftppassword0` VALUES ('lomovera.com', 'ftp@lomovera.com', 'password', 'NO', '2013.02.07-14.35.26');
INSERT INTO `ftppassword0` VALUES ('lomovera.com', 'lomovera', 'pass', 'NO', '2013.02.07-14.44.53');
INSERT INTO `ftppassword0` VALUES ('lomovera.com', 'webmaster@lomovera.com', '12345678', 'NO', '2013.02.07-14.38.16');
INSERT INTO `ftppassword0` VALUES ('lostincheeseland.com', 'data', 'root', 'NO', '2013.02.07-14.43.59');
INSERT INTO `ftppassword0` VALUES ('love-is-all-around.com', 'backup', 'backup123', 'NO', '2013.02.07-15.02.55');
INSERT INTO `ftppassword0` VALUES ('loveeverybody.com', 'lizdy', 'database', 'NO', '2013.02.07-15.19.33');
INSERT INTO `ftppassword0` VALUES ('loveeverybody.com', 'webmaster@loveeverybody.com', 'administrator', 'NO', '2013.02.07-14.39.17');
INSERT INTO `ftppassword0` VALUES ('shemale.zzzubi.com', 'ftp@zzzubi.com', '2012', 'NO', '2013.02.07-15.35.05');

-- ----------------------------
-- Table structure for `ftppassword1`
-- ----------------------------
DROP TABLE IF EXISTS `ftppassword1`;
CREATE TABLE `ftppassword1` (
  `IP` varchar(100) NOT NULL default '',
  `user` varchar(100) NOT NULL default '',
  `password` varchar(100) default NULL,
  `root` varchar(100) default NULL,
  `time` varchar(100) default NULL,
  PRIMARY KEY  (`IP`,`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ftppassword1
-- ----------------------------
INSERT INTO `ftppassword1` VALUES ('aaj.mobi', 'ftp@aaj.mobi', 'mnbvcxz', '1', '2013.02.07-16.45.20');
INSERT INTO `ftppassword1` VALUES ('account.unmatchedstyle.com', 'ftp@unmatchedstyle.com', 'zxcvbnm', '1', '2013.02.07-16.45.33');
INSERT INTO `ftppassword1` VALUES ('adjg.org', 'ftp@adjg.org', 'mnbvcxz', '1', '2013.02.07-16.45.43');
INSERT INTO `ftppassword1` VALUES ('adulteropicture.com', 'ftp@adulteropicture.com', 'zxcvbnm', '1', '2013.02.07-16.45.55');
INSERT INTO `ftppassword1` VALUES ('altmetrics.org', 'ftp@altmetrics.org', '2010', '1', '2013.02.07-17.57.13');
INSERT INTO `ftppassword1` VALUES ('americandigest.org', 'ftp@americandigest.org', '2012', '1', '2013.02.07-16.46.06');
INSERT INTO `ftppassword1` VALUES ('americanthinker.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.46.49');
INSERT INTO `ftppassword1` VALUES ('andstillipersist.com', 'ftp@andstillipersist.com', '2011', '1', '2013.02.07-16.47.08');
INSERT INTO `ftppassword1` VALUES ('asobo-saga.jp', 'ftp', 'zxcvbnm', '1', '2013.02.07-16.47.34');
INSERT INTO `ftppassword1` VALUES ('au.foundationbeyondbelief.org', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.47.56');
INSERT INTO `ftppassword1` VALUES ('auditblogs.com', 'ftp@auditblogs.com', 'mnbvcxz', '1', '2013.02.07-16.48.05');
INSERT INTO `ftppassword1` VALUES ('az-moga.com', 'ftp@az-moga.com', 'zxcvbnm', '1', '2013.02.07-16.48.13');
INSERT INTO `ftppassword1` VALUES ('bakerella.com', 'ftp@bakerella.com', 'zxcvbnm', '1', '2013.02.07-16.48.29');
INSERT INTO `ftppassword1` VALUES ('baoxian.dghjw.com', 'ftp@dghjw.com', 'zxcvbnm', '1', '2013.02.07-16.48.50');
INSERT INTO `ftppassword1` VALUES ('bbs.5icbd.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.49.01');
INSERT INTO `ftppassword1` VALUES ('bbs.dghjw.com', 'ftp@dghjw.com', 'mnbvcxz', '1', '2013.02.07-16.49.08');
INSERT INTO `ftppassword1` VALUES ('bbs.iazhuo.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.49.15');
INSERT INTO `ftppassword1` VALUES ('bbs.zhangzi.tv', 'test', 'test', '1', '2013.02.07-16.49.41');
INSERT INTO `ftppassword1` VALUES ('bcbookstore.collegestoreonline.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.50.04');
INSERT INTO `ftppassword1` VALUES ('bestofbothoffices.com', 'ftp@bestofbothoffices.com', 'mnbvcxz', '1', '2013.02.07-16.50.15');
INSERT INTO `ftppassword1` VALUES ('bettermess.com', 'ftp@bettermess.com', 'mnbvcxz', '1', '2013.02.07-16.50.19');
INSERT INTO `ftppassword1` VALUES ('bfwa.com', 'ftp@bfwa.com', 'mnbvcxz', '1', '2013.02.07-16.50.32');
INSERT INTO `ftppassword1` VALUES ('bike.nosbl.com', 'ftp@nosbl.com', 'mnbvcxz', '1', '2013.02.07-16.50.44');
INSERT INTO `ftppassword1` VALUES ('bitcoinmagazine.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.51.01');
INSERT INTO `ftppassword1` VALUES ('bjmama.5721.net', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.51.10');
INSERT INTO `ftppassword1` VALUES ('blog.5721.net', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.51.16');
INSERT INTO `ftppassword1` VALUES ('bombonem.com', 'ftp@bombonem.com', '2011', '1', '2013.02.07-16.51.36');
INSERT INTO `ftppassword1` VALUES ('bp.autooo.net', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.51.59');
INSERT INTO `ftppassword1` VALUES ('businessword.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.52.27');
INSERT INTO `ftppassword1` VALUES ('bz.gz1w.com', 'mysql', 'mysql', '1', '2013.02.07-16.52.38');
INSERT INTO `ftppassword1` VALUES ('c-rank.lady-dir.jp', 'ftp@lady-dir.jp', 'mnbvcxz', '1', '2013.02.07-16.52.43');
INSERT INTO `ftppassword1` VALUES ('cdps.chicagofedblogs.org', 'ftp@chicagofedblogs.org', 'zxcvbnm', '1', '2013.02.07-16.52.54');
INSERT INTO `ftppassword1` VALUES ('chaigyaru.com', 'ftp@chaigyaru.com', 'zxcvbnm', '1', '2013.02.07-16.53.03');
INSERT INTO `ftppassword1` VALUES ('chuzhong.kt5u.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.53.16');
INSERT INTO `ftppassword1` VALUES ('citizenjournal.net', 'ftp@citizenjournal.net', '2011', '1', '2013.02.07-16.53.29');
INSERT INTO `ftppassword1` VALUES ('convergefl.com', 'ftp@convergefl.com', 'zxcvbnm', '1', '2013.02.07-16.53.38');
INSERT INTO `ftppassword1` VALUES ('cran.r-project.org', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.53.54');
INSERT INTO `ftppassword1` VALUES ('cs.iazhuo.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.54.01');
INSERT INTO `ftppassword1` VALUES ('csicop.org', 'ftp@csicop.org', 'mnbvcxz', '1', '2013.02.07-16.54.17');
INSERT INTO `ftppassword1` VALUES ('curiosityintheclassroom.com', 'ftp', 'zxcvbnm', '1', '2013.02.07-16.54.39');
INSERT INTO `ftppassword1` VALUES ('d-rank.lady-dir.jp', 'ftp@lady-dir.jp', 'zxcvbnm', '1', '2013.02.07-16.54.46');
INSERT INTO `ftppassword1` VALUES ('d1kt.cn', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.54.55');
INSERT INTO `ftppassword1` VALUES ('dh-virgin.com', 'ftp', '2012', '1', '2013.02.07-16.55.03');
INSERT INTO `ftppassword1` VALUES ('diamentyforbesa.pl', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.55.10');
INSERT INTO `ftppassword1` VALUES ('ejectejecteject.com', 'ftp@ejectejecteject.com', '2011', '1', '2013.02.07-16.55.16');
INSERT INTO `ftppassword1` VALUES ('eroi-douga.info', 'ftp@eroi-douga.info', '2012', '1', '2013.02.07-16.55.33');
INSERT INTO `ftppassword1` VALUES ('ffii.org', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.55.55');
INSERT INTO `ftppassword1` VALUES ('filmjourney.weblogger.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.56.37');
INSERT INTO `ftppassword1` VALUES ('filmjourney.weblogger.com', 'ftp@weblogger.com', 'mnbvcxz', '1', '2013.02.07-16.56.37');
INSERT INTO `ftppassword1` VALUES ('forbes.ro', 'ftp@forbes.ro', '2012', '1', '2013.02.07-16.57.01');
INSERT INTO `ftppassword1` VALUES ('furfly.net', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.57.32');
INSERT INTO `ftppassword1` VALUES ('fvza.org', 'ftp@fvza.org', '2012', '1', '2013.02.07-16.57.49');
INSERT INTO `ftppassword1` VALUES ('gamingbolt.com', 'ftp@gamingbolt.com', 'mnbvcxz', '1', '2013.02.07-16.58.05');
INSERT INTO `ftppassword1` VALUES ('gaozhong.kt5u.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.58.20');
INSERT INTO `ftppassword1` VALUES ('getoutandgo.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.58.49');
INSERT INTO `ftppassword1` VALUES ('glowhost.com', 'ftp@glowhost.com', 'mnbvcxz', '1', '2013.02.07-16.59.04');
INSERT INTO `ftppassword1` VALUES ('gourmetreport.net', 'ftp@gourmetreport.net', 'zxcvbnm', '1', '2013.02.07-16.59.13');
INSERT INTO `ftppassword1` VALUES ('hamesen-gigarank.net', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.59.31');
INSERT INTO `ftppassword1` VALUES ('hchamp.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.59.39');
INSERT INTO `ftppassword1` VALUES ('hnst.org', 'ftp', 'mnbvcxz', '1', '2013.02.07-16.59.52');
INSERT INTO `ftppassword1` VALUES ('homes.gruh.org', 'ftp@gruh.org', 'mnbvcxz', '1', '2013.02.07-16.59.59');
INSERT INTO `ftppassword1` VALUES ('hopisen.com', 'ftp@hopisen.com', 'zxcvbnm', '1', '2013.02.07-17.00.05');
INSERT INTO `ftppassword1` VALUES ('iddy.jp', 'ftp', 'mnbvcxz', '1', '2013.02.07-17.00.09');
INSERT INTO `ftppassword1` VALUES ('insidetheusa.net', 'ftp@insidetheusa.net', '2012', '1', '2013.02.07-17.00.30');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'access', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'account', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'admin', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'administrator', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'backup', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'data', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'ftp', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'ftp@seng.sg', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'guest', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'james.seng.sg', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'lizdy', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'mysql', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'network', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'news', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'oracle', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'oracle8', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'root', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'seng', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'seng.sg', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'sybase', 'zxcvbnm', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'test', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'user', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'web', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'webmaster', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'webmaster@seng.sg', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'www', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('james.seng.sg', 'wwwadmin', 'mnbvcxz', '1', '2013.02.07-17.09.15');
INSERT INTO `ftppassword1` VALUES ('jjsg.yaowan.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-17.09.34');
INSERT INTO `ftppassword1` VALUES ('kaoyan.wanxue.cn', 'ftp', 'mnbvcxz', '1', '2013.02.07-17.09.57');
INSERT INTO `ftppassword1` VALUES ('kia-buzz.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-17.10.05');
INSERT INTO `ftppassword1` VALUES ('kirtsybook.com', 'ftp@kirtsybook.com', 'mnbvcxz', '1', '2013.02.07-17.10.23');
INSERT INTO `ftppassword1` VALUES ('kkld.net', 'ftp', 'mnbvcxz', '1', '2013.02.07-17.10.44');
INSERT INTO `ftppassword1` VALUES ('lambertsaustin.com', 'ftp@lambertsaustin.com', 'mnbvcxz', '1', '2013.02.07-17.10.57');
INSERT INTO `ftppassword1` VALUES ('latenightcocoa.com', 'ftp@latenightcocoa.com', '2011', '1', '2013.02.07-17.11.09');
INSERT INTO `ftppassword1` VALUES ('laurajul.dk', 'ftp', 'mnbvcxz', '1', '2013.02.07-17.11.27');
INSERT INTO `ftppassword1` VALUES ('lc.goghsun.net', 'ftp@goghsun.net', 'mnbvcxz', '1', '2013.02.07-17.11.54');
INSERT INTO `ftppassword1` VALUES ('lescambridge.com', 'ftp@lescambridge.com', 'mnbvcxz', '1', '2013.02.07-17.12.17');
INSERT INTO `ftppassword1` VALUES ('lifeasrose.ca', 'ftp@lifeasrose.ca', 'mnbvcxz', '1', '2013.02.07-17.12.50');
INSERT INTO `ftppassword1` VALUES ('linkedin.rbarnes.com', 'ftp@rbarnes.com', 'zxcvbnm', '1', '2013.02.07-17.13.05');
INSERT INTO `ftppassword1` VALUES ('lisathiessen.ca', 'ftp@lisathiessen.ca', '2012', '1', '2013.02.07-17.13.13');
INSERT INTO `ftppassword1` VALUES ('live.momo-club.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-17.13.17');
INSERT INTO `ftppassword1` VALUES ('loveamovie.net', 'ftp@loveamovie.net', 'mnbvcxz', '1', '2013.02.07-17.13.24');
INSERT INTO `ftppassword1` VALUES ('shequ.edufww.com', 'ftp', 'mnbvcxz', '1', '2013.02.07-17.13.29');

-- ----------------------------
-- Table structure for `ftppassword2`
-- ----------------------------
DROP TABLE IF EXISTS `ftppassword2`;
CREATE TABLE `ftppassword2` (
  `IP` varchar(100) NOT NULL default '',
  `user` varchar(100) NOT NULL default '',
  `password` varchar(100) default NULL,
  `root` varchar(100) default NULL,
  `title` varchar(100) default NULL,
  `time` varchar(100) default NULL,
  PRIMARY KEY  (`IP`,`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ftppassword2
-- ----------------------------

-- ----------------------------
-- Table structure for `ftppassword3`
-- ----------------------------
DROP TABLE IF EXISTS `ftppassword3`;
CREATE TABLE `ftppassword3` (
  `IP` varchar(100) NOT NULL default '',
  `user` varchar(100) NOT NULL default '',
  `password` varchar(100) default NULL,
  `root` varchar(100) default NULL,
  `title` varchar(100) default NULL,
  `time` varchar(100) default NULL,
  PRIMARY KEY  (`IP`,`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ftppassword3
-- ----------------------------

-- ----------------------------
-- Table structure for `openftp`
-- ----------------------------
DROP TABLE IF EXISTS `openftp`;
CREATE TABLE `openftp` (
  `url` varchar(100) NOT NULL default '',
  `linkftp` varchar(10) default NULL,
  `time` varchar(30) default NULL,
  PRIMARY KEY  (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of openftp
-- ----------------------------

-- ----------------------------
-- Table structure for `openurl`
-- ----------------------------
DROP TABLE IF EXISTS `openurl`;
CREATE TABLE `openurl` (
  `url` varchar(100) NOT NULL default '',
  `openurl` varchar(10) default NULL,
  `openftp` varchar(10) default NULL,
  `time` varchar(30) default NULL,
  PRIMARY KEY  (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of openurl
-- ----------------------------
