# ************************************************************
# Sequel Pro SQL dump
# Version 4135
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.1.63)
# Database: python
# Generation Time: 2016-03-23 04:37:40 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

# Dump of table video
# ------------------------------------------------------------
#id，av，title，videotime, uploadtime, viewcount, commentcount, coincount, favourcount, danmucount, authorid, keywords, description
CREATE TABLE `video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `av` int(11) DEFAULT NULL,
  `title` varchar(256) DEFAULT NULL,
  `videotype` varchar(64) DEFAULT NULL,
  `uploadtime` datetime DEFAULT NULL,
  `description` varchar(2048) DEFAULT NULL,
  `authorid` int(12) DEFAULT NULL,
  `authorname` varchar(128) DEFAULT NULL,
  `duration` int(12) DEFAULT NULL,
  `viewcount` int(11) DEFAULT NULL,
  `danmaku` int(11) DEFAULT NULL,
  `comment` int(11) DEFAULT NULL,
  `favorite` int(11) DEFAULT NULL,
  `coin` int(11) DEFAULT NULL,
  `share` int(11) DEFAULT NULL,
  `likes` int(11) DEFAULT NULL,
  `keywords` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE `video_simple` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `av` int(11) DEFAULT NULL,
  `viewcount` int(11) DEFAULT NULL,
  `danmaku` int(11) DEFAULT NULL,
  `comment` int(11) DEFAULT NULL,
  `favorite` int(11) DEFAULT NULL,
  `coin` int(11) DEFAULT NULL,
  `share` int(11) DEFAULT NULL,
  `likes` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
