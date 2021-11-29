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

INSERT INTO ecg_test (region, start_time, end_time)
    VALUES ('kr', '2021-09-21 15:28:14.000', '2021-09-21 16:04:03.500');
    INSERT INTO ecg_test (region, start_time, end_time)
    VALUES ('kr', '2021-09-08 12:10:56.000', '2021-09-08 15:48:50.000');
