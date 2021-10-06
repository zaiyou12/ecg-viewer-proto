CREATE TABLE `user` (
  `id`           INTEGER        not null,
  `email`        varchar(30)    not null,
  `created_time` datetime       DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id` AUTOINCREMENT)
);

CREATE TABLE `ecg_test` (
  `id`           INTEGER        not null,
  `region`       varchar(5)     not null,
  `start_time`   datetime       NULL,
  `end_time`     datetime       NULL,
  `duration`     INTEGER        DEFAULT '0',
  `updated_time` datetime       DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id` AUTOINCREMENT)
);

INSERT INTO user (email) VALUES ('test@test.com');
