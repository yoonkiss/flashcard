drop table if exists cards;
create table cards (
  id integer primary key autoincrement,
   /* 1 for interview, 2 for code, 3 for english, 4 for ielts */
  type tinyint not null,
  front text not null,
  back text not null,
  sort int default 0,
  known boolean default 0
);
