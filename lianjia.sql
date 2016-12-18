/*
Navicat MySQL Data Transfer

Source Server         : 192.168.33.11
Source Server Version : 50628
Source Host           : 192.168.33.11:3306
Source Database       : lianjia

Target Server Type    : MYSQL
Target Server Version : 50628
File Encoding         : 65001

Date: 2016-12-18 21:38:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for room
-- ----------------------------
DROP TABLE IF EXISTS `room`;
CREATE TABLE `room` (
  `id` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '',
  `sub_title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '',
  `follow` int(11) unsigned DEFAULT '0',
  `looked` int(11) unsigned DEFAULT '0',
  `price` varchar(8) DEFAULT NULL,
  `unit_price` int(10) unsigned DEFAULT NULL,
  `room_num` tinyint(2) unsigned DEFAULT NULL,
  `drawing_num` tinyint(2) unsigned DEFAULT NULL,
  `acreage` smallint(6) unsigned DEFAULT NULL,
  `district` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '',
  `area` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '',
  `year` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '',
  `prefix` varchar(10) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9535 DEFAULT CHARSET=utf8mb4;
SET FOREIGN_KEY_CHECKS=1;
