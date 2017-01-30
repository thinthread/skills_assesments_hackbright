-- Include your solutions to the More Practice problems in this file.



-- Insert a Brand

-- cars=# INSERT INTO brands (brand_id, name, founded, headquarters, discontinued)
-- cars-# VALUES ('sub', 'Subaru', 1953, 'Tokyo, Japan', NULL);
-- INSERT 0 1



-- Insert Models

-- cars=# INSERT INTO models(model_id, year, brand_id, name)
-- cars-# VALUES(48, 2015, 'sub', 'Outback');
-- INSERT 0 1



-- Create an Awards Table

-- cars=# CREATE TABLE awards(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50) NOT NULL,
--     year INTEGER NOT NULL,
--     winner_id INTEGER REFERENCES models(model_id) 
-- );



-- Insert Awards

-- cars=# SELECT model_id FROM models WHERE name Like'%Mal%';
--  model_id 
-- ----------
--        47

-- 1.
-- cars=# INSERT INTO awards(name, year, winner_id)
-- cars-#     VALUES('IIHS Safety Award', 2015, 47);


-- INSERT 0 1
-- cars=# \d awards
--                                   Table "public.awards"
--   Column   |         Type          |                      Modifiers                      
-- -----------+-----------------------+-----------------------------------------------------
--  id        | integer               | not null default nextval('awards_id_seq'::regclass)
--  name      | character varying(50) | not null
--  year      | integer               | not null
--  winner_id | integer               | not null
-- Indexes:
--     "awards_pkey" PRIMARY KEY, btree (id)
-- Foreign-key constraints:
--     "awards_winner_id_fkey" FOREIGN KEY (winner_id) REFERENCES models(model_id)



-- 2.cars=# SELECT model_id FROM models WHERE name Like '%Out%';
--  model_id 
-- ----------
--        48

-- cars=# INSERT INTO awards(name, year, winner_id)
-- cars-#     VALUES('IIHS Safety Award', 2015, 48);

-- INSERT 0 1
-- cars=# SELECT * FROM awards;
--  id |       name        | year | winner_id 
-- ----+-------------------+------+-----------
--   1 | IIHS Safety Award | 2015 |        47
--   2 | IIHS Safety Award | 2015 |        48
-- (2 rows)


-- 3.
-- cars=# INSERT INTO awards(name, year, winner_id)
-- cars-#     VALUES('Best in Class', 2015, NULL);


-- INSERT 0 1
-- cars=# SELECT * FROM awards;
--  id |       name        | year | winner_id 
-- ----+-------------------+------+-----------
--   1 | IIHS Safety Award | 2015 |        47
--   2 | IIHS Safety Award | 2015 |        48
--   3 | Best in Class     | 2015 |          
-- (3 rows)

