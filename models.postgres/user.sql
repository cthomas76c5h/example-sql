create table if not exists api_user (
    id integer primary key generated always as identity,
    username text,
    email text,
    password text,
    bio text,
    image text
);
