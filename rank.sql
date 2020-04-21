/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 22/04/2020 00:01:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for rank
-- ----------------------------
DROP TABLE IF EXISTS `rank`;
CREATE TABLE `rank`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `score` int(10) NULL DEFAULT NULL,
  `addtime` datetime(0) NULL DEFAULT NULL,
  `updatetime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rank
-- ----------------------------
INSERT INTO `rank` VALUES (1, '1', 2, NULL, '2020-04-21 22:49:10');
INSERT INTO `rank` VALUES (7, '5', 5, NULL, NULL);
INSERT INTO `rank` VALUES (6, '4', 4, NULL, NULL);
INSERT INTO `rank` VALUES (4, '2', 3, NULL, NULL);
INSERT INTO `rank` VALUES (5, '3', 3, NULL, NULL);
INSERT INTO `rank` VALUES (8, '6', 6, NULL, NULL);
INSERT INTO `rank` VALUES (9, '7', 7, NULL, NULL);
INSERT INTO `rank` VALUES (10, '8', 8, NULL, NULL);
INSERT INTO `rank` VALUES (11, '9', 9, NULL, NULL);
INSERT INTO `rank` VALUES (12, '10', 10, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
