--create join table
CREATE TABLE `meetings_topic_presentors` (
  `topic_id` int(11) DEFAULT NULL,
  `presentor_id` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1

--get data...this doesn't parse multiple presentors who are currently one record
--production data (from chipy.org) that has multiple presentors
--Optimizing Django Templates - Chris Detmer and John Yang
--Python for Scientific and High Performance Computing: Part 2 - William Scullin and James P. Snyder
--Python for Scientific and High Performance Computing: Part 1 - William Scullin and James P. Snyder
INSERT INTO meetings_topic_presentors (topic_id, presentor_id) 
  SELECT id, by_id FROM meetings_topic

--optional--
--Drop fk...don't think key name will be the same??
--Drop column
--ALTER TABLE meetings_topic DROP KEY meetings_topic_3acff7b7;
--ALTER TABLE meetings_topic DROP by_id;
