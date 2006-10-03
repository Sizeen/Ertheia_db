DROP TABLE IF EXISTS `random_spawn`;
CREATE TABLE `random_spawn` (
  groupId INT NOT NULL default 0,
  npcId INT NOT NULL default 0,
  count INT NOT NULL default 0,
  initialDelay BIGINT NOT NULL default -1,
  respawnDelay BIGINT NOT NULL default -1,
  despawnDelay BIGINT NOT NULL default -1,
  broadcastSpawn VARCHAR(5) NOT NULL default 'false',
  randomSpawn VARCHAR(5) NOT NULL default 'true',
  PRIMARY KEY  (groupId)
);

INSERT INTO `random_spawn` VALUES (1, 7556, 1, -1, 1800000, 1800000, 'false', 'true');