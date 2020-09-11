USE test;

CREATE TABLE test_table(
    test_id varchar(20) primary key,
    test_column varchar(30)
);
INSERT INTO test_table
VALUES
    ("test_key1", "test_value1"),
    ("test_key2", "test_value2"),
    ("test_key3", "test_value3");
