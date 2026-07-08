create table if not exists job(
        id integer primary key autoincrement,
        name text,
            description text
                    );
create table if not exists places(
        id integer primary key autoincrement,
        name text,
            lat text,
            lon text,
             text
                    );
create table if not exists user(
        id integer primary key autoincrement,
        username text,
            email text,
            password text,
            phone text,
            country_id text,
            job_id text
                    );
create table if not exists fakecommunication(
        id integer primary key autoincrement,
        com_type text,
            content text,
            description text
                    );
