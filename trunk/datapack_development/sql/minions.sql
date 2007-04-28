--
-- Table structure for table `minions`
--

DROP TABLE IF EXISTS `minions`;
CREATE TABLE `minions` (
  `boss_id` int(11) NOT NULL default '0',
  `minion_id` int(11) NOT NULL default '0',
  `amount_min` int(4) NOT NULL default '0',
  `amount_max` int(4) NOT NULL default '0',
  PRIMARY KEY  (`boss_id`,`minion_id`)
) TYPE=MyISAM;

--
-- Dumping data for table `minions`
--

-- c1 mobs
INSERT INTO `minions` VALUES
(20117,20118,1,3),
(20376,20377,1,2),
(20398,20399,1,2),
(20520,20445,3,5),
(20522,20524,2,4),
(20738,20739,3,5),
(20745,20746,1,2), 
(20747,20748,1,2), 
(20749,20750,1,2), 
(20751,20752,3,3), 
(20753,21040,4,4), 
(20758,20759,1,1), 
(20758,20760,1,1), 
(20761,20762,2,3), 
(20763,20764,1,1),
(20763,20765,1,1),
(20763,20766,1,1),
(20767,20768,1,1), 
(20767,20769,1,1), 
(20767,20770,1,1), 
(20771,20772,1,3), 
(20773,20774,2,4),
(20779,20750,1,3),
(20930,20928,1,1), 
(20930,20929,1,1), 
(20933,20931,1,1), 
(20933,20932,1,1), 
(20935,20934,1,3), 
(20936,20937,1,1),
(20936,20938,1,1),
(20936,20939,1,1),
(20941,20940,3,3),
(20944,20942,1,1),
(20944,20943,2,2),
(20947,20945,1,2), 
(20947,20946,1,2), 
(20950,20948,1,2), 
(20950,20949,1,2), 
(20953,20951,1,2), 
(20953,20952,1,2), 
(20956,20954,1,2), 
(20956,20955,1,2), 
(20959,20957,1,2), 
(20959,20958,1,2), 
(20963,20960,1,1), 
(20963,20961,1,1), 
(20963,20962,1,1), 
(20966,20964,1,2), 
(20966,20965,1,2), 
(20969,20967,1,2), 
(20969,20968,1,2), 
(20973,20970,1,1), 
(20973,20971,1,1), 
(20973,20972,1,1), 
(20974,20975,1,2), 
(20974,20976,1,2), 
(20977,20978,1,1), 
(20977,20979,1,1), 
(20980,20981,1,1), 
(20980,20982,1,1), 
(20986,20987,1,2), 
(20986,20988,1,2), 
(20989,20990,1,1), 
(20991,20992,1,2), 
(20991,20993,1,2), 
(20994,20995,3,4);

INSERT INTO `minions` VALUES 
(21058,21059,1,2), 
(21058,21060,1,2), 
(21075,21076,1,1),
(21075,21077,1,2), 
(21078,21079,1,1), 
(21078,21080,1,2), 
(21081,21082,1,1), 
(21081,21083,1,3),
(21090,21091,1,1),
(21090,21092,1,1),
(21312,21313,2,2);

-- 
-- work in progress C5 minions - 22xxx mobs
-- 
INSERT INTO `minions` VALUES 
(22028,22027,3,4),
(22080,22079,3,3),
(22082,22081,3,3),
(22084,22083,3,3),
(22086,22085,3,3),
(22088,22087,3,3),
(22092,22091,3,3),
(22094,22093,3,3),
(22096,22095,3,3),
(22098,22097,3,3),
(22123,22122,2,3),
(22135,22130,1,1),
(22135,22131,1,1);

INSERT INTO `minions` VALUES 
(27021,20492,6,8),
(27022,20367,1,3),
(27036,27037,2,3),
(27110,27111,3,5),
(27113,27111,3,6);

-- raid bosses
INSERT INTO `minions` VALUES 
(25001,25002,1,2),
(25001,25003,1,2),
(25004,25005,2,3),
(25004,25006,1,1),
(25007,25008,1,1),
(25007,25009,1,2),
(25010,25011,2,3),
(25010,25012,1,1),
(25013,25014,1,2),
(25013,25015,1,2),
(25016,25017,1,2),
(25016,25018,1,2),
(25217,25218,2,3),
(25217,25219,2,4),
(25020,25021,1,1),
(25020,25022,1,1),
(25023,25024,3,5),
(25023,25025,4,5),
(25026,25027,1,2),
(25026,25028,2,4),
(25029,25030,1,2),
(25029,25031,1,3),
(25032,25033,1,2),
(25032,25034,4,6),
(25035,25036,1,2),
(25035,25037,2,3),
(25038,25039,1,1),
(25038,25040,2,4),
(25041,25042,2,3),
(25041,25043,1,1),
(25044,25045,2,4),
(25044,25046,1,1),
(25047,25048,1,2),
(25047,25049,1,2),
(25051,25052,1,1),
(25051,25053,1,1),
(25054,25055,1,1),
(25054,25056,1,1),
(25057,25058,1,2),
(25057,25059,2,3),
(25060,25061,1,2),
(25060,25062,1,2),
(25064,25065,1,2),
(25064,25066,1,2),
(25067,25068,1,2),
(25067,25069,1,2),
(25070,25071,1,2),
(25073,25074,1,2),
(25076,25077,1,2),
(25079,25080,1,2),
(25070,25072,1,2),
(25073,25075,1,2),
(25076,25078,1,2),
(25079,25081,1,2),
(25082,25083,1,2),
(25082,25084,1,2),
(25085,25086,1,2),
(25085,25087,1,2),
(25089,25091,1,2),
(25089,25090,1,2),
(25092,25093,1,2),
(25092,25094,1,2),
(25095,25096,1,2),
(25095,25097,1,2),
(25099,25100,1,2),
(25099,25101,1,2),
(25103,25104,1,2),
(25103,25105,1,2),
(25106,25107,1,2),
(25106,25108,1,2),
(25109,25110,1,2),
(25109,25111,1,2),
(25112,25113,1,2),
(25112,25114,1,2),
(25115,25116,1,2),
(25115,25117,1,2),
(25119,25120,1,2),
(25119,25121,1,2),
(25122,25123,1,2),
(25122,25124,1,2),
(25128,25129,1,2),
(25128,25130,1,2),
(25131,25132,1,2),
(25131,25133,1,2),
(25134,25135,1,2),
(25134,25136,1,2),
(25137,25138,1,2),
(25137,25139,1,2),
(25140,25141,1,2),
(25140,25142,1,2),
(25143,25144,1,2),
(25143,25145,1,2),
(25146,25147,1,2),
(25146,25148,1,2),
(25149,25150,1,2),
(25149,25151,1,2),
(25152,25153,1,2),
(25152,25154,1,2),
(25155,25156,1,2),
(25155,25157,1,2),
(25159,25160,1,2),
(25159,25161,1,2),
-- (25163,25164,1,3), -- minion npcID removed in interlude
-- (25163,25165,1,2), -- minion npcID removed in interlude
(25166,25167,1,2),
(25166,25168,1,2),
(25170,25171,1,2),
(25170,25172,1,2),
(25173,25174,1,2),
(25173,25175,1,2),
(25176,25177,1,2),
(25176,25178,1,2),
(25179,25180,1,2),
(25179,25181,1,2),
(25182,25183,1,2),
(25182,25184,1,2),
(25185,25186,1,2),
(25185,25187,1,2),
(25189,25190,1,2),
(25189,25191,1,2),
(25192,25193,1,2),
(25192,25194,1,2),
(25199,25200,1,2),
(25199,25201,1,2),
(25202,25203,1,2),
(25202,25204,1,2),
(25205,25206,1,2),
(25205,25207,1,2),
(25208,25209,1,2),
(25208,25210,1,2),
(25211,25212,1,2),
(25211,25213,1,2),
(25214,25215,1,2),
(25214,25216,1,2),
(25220,25221,1,2),
(25220,25222,1,2),
(25223,25224,2,3),
(25223,25225,1,1),
(25226,25227,1,2),
(25226,25228,1,2),
(25230,25231,1,1),
(25230,25232,2,4),
(25235,25236,1,2),
(25235,25237,1,2),
(25238,25239,1,2),
(25238,25240,1,2),
(25241,25242,1,1),
(25241,25243,1,3),
(25245,25246,1,1),
(25245,25247,1,4),
(25249,25250,2,3),
(25249,25251,1,1),
(25252,25253,1,3),
(25252,25254,1,1),
(25256,25257,2,3),
(25256,25258,1,2),
(25260,25261,1,2),
(25260,25262,1,3),
(25263,25264,1,1),
(25263,25265,1,3),
(25266,25267,1,1),
(25266,25268,2,4),
(25269,25270,1,3),
(25269,25271,1,2),
(25283,25284,1,3),
(25283,25285,1,3),
(25286,25287,1,2),
(25286,25288,1,2),
(25286,25289,1,2),
(25290,25291,1,2),
(25290,25292,2,4),
(25293,25294,1,2),
(25293,25295,2,3),
(25296,25297,2,4),
(25296,25298,1,3),
(25299,25300,1,2),
(25299,25301,2,4),
(25302,25303,1,3),
(25302,25304,1,3),
(25306,25307,1,2),
(25306,25308,2,4),
(25309,25310,1,3),
(25309,25311,1,3),
(25312,25313,1,2),
(25312,25314,2,4),
(25316,25317,1,2),
(25316,25318,2,4),
(25319,25320,2,3),
(25319,25321,1,2),
(25322,25323,2,3),
(25322,25324,1,3),
(25325,25326,1,2),
(25325,25327,2,3),
(25328,25329,1,1),
(25328,25330,1,1),
(25328,25331,1,1),
(25328,25332,1,1),
(25339,25340,1,1),
(25339,25341,1,1),
(25342,25343,1,1),
(25342,25344,1,1),
(25342,25345,1,1),
(25346,25347,1,1),
(25346,25348,1,1),
(25349,25350,1,1),
(25349,25351,1,1),
(25352,25353,3,6),
(25354,25355,2,4),
(25354,25356,2,4),
(25357,25358,1,3),
(25357,25359,1,3),
(25360,25361,4,6),
(25362,25363,2,4),
(25362,25364,1,3),
(25366,25367,2,4),
(25366,25368,1,2),
(25369,25370,1,3),
(25369,25371,1,3),
(25373,25374,2,4),
(25375,25376,2,4),
(25375,25377,1,3),
(25378,25379,1,4),
(25380,25381,1,3),
(25380,25382,1,3),
(25383,25384,3,5),
(25385,25386,1,3),
(25385,25387,1,3),
(25388,25389,1,3),
(25388,25390,2,5),
(25392,25393,4,7),
(25395,25396,1,1),
(25395,25397,2,2),
(25398,25399,1,4),
(25398,25400,1,2),
(25401,25402,2,3),
(25401,25403,3,5),
(25404,25405,2,4),
(25404,25406,2,4),
(25407,25408,2,3),
(25407,25409,2,4),
(25410,25411,4,8),
(25412,25413,1,2),
(25412,25414,1,4),
(25415,25416,1,3),
(25415,25417,1,3),
(25418,25419,2,5),
(25420,25421,2,5),
(25420,25422,2,3),
(25423,25424,6,8),
(25423,25425,3,4),
(25426,25427,2,3),
(25426,25428,2,4),
(25429,25430,6,9),
(25431,25432,3,4),
(25431,25433,3,4),
(25434,25435,3,4),
(25434,25436,2,3),
(25438,25439,3,5),
(25438,25440,2,4),
(25441,25442,2,5),
(25441,25443,2,4),
(25444,25445,3,5),
(25444,25446,2,4),
(25447,25448,2,4),
(25447,25449,3,5),
(25450,25451,2,3),
(25450,25452,2,5),
(25453,25454,3,5),
(25453,25455,2,4),
(25456,25457,3,4),
(25456,25458,3,4),
(25456,25459,3,4),
(25460,25461,3,5),
(25460,25462,3,5),
(25463,25464,2,4),
(25463,25465,2,3),
(25463,25466,3,5),
(25467,25468,3,5),
(25467,25469,2,4),
(25470,25471,3,4),
(25470,25472,3,5),
(25473,25474,6,8),
(25475,25476,3,4),
(25475,25477,2,3),
(25478,25479,3,5),
(25478,25480,2,4),
(25481,25482,2,4),
(25481,25483,2,4),
(25484,25485,3,5),
(25484,25486,2,4),
(25487,25488,2,3),
(25487,25489,1,4),
(25490,25491,2,3),
(25490,25492,1,4),
(25493,25494,3,4),
(25493,25495,3,4),
(25496,25497,5,9),
(25498,25499,2,4),
(25498,25500,1,5),
(25501,25502,3,3),
(25501,25503,2,2),
(25504,25505,3,3),
(25506,25507,1,1),
(25506,25508,3,3),
(25509,25510,1,1),
(25509,25511,3,3);

-- grand bosses
INSERT INTO `minions` VALUES 
(29001,29003,5,8),
(29001,29004,6,9),
(29006,29007,10,10),
(29006,29008,3,3),
(29006,29011,4,4),
(29014,29015,6,8),
(29014,29016,4,7),
(29014,29017,6,8),
(29014,29018,4,7);

-- ToI - Binder group
INSERT INTO `minions` VALUES 
(20983,20984,1,1),
(20983,20985,1,1),
(20983,21074,1,1);