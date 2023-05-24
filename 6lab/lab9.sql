CREATE FUNCTION c_test(integer) RETURNS integer AS $$
    SELECT $1 * $1;
$$ LANGUAGE SQL;

-- \i c:/vvit/6lab/lab9.sql

-- CREATE FUNCTION c_test() RETURNS VARCHAR
--     AS 'c:/vvit/function.c', 'c_test'
--     LANGUAGE C STRICT;