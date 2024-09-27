create table if not exists api_user (
    id integer primary key AUTOINCREMENT,
    username text,
    email text,
    password text,
    bio text,
    image text
);
