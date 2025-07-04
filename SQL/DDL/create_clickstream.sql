-- For My SQL
CREATE TABLE clickstream (
  click_id INT,
  user_id VARCHAR(10),
  event_timestamp DATETIME,  -- ✅ Use DATETIME to freely insert your own timestamps
  source_type VARCHAR(50),
  event_name VARCHAR(20),
  event_details VARCHAR(100)
);

-- For PostGres SQL 

CREATE TABLE clickstream (
  click_id INT,
  user_id VARCHAR(10),
  event_timestamp TIMESTAMP,  -- ✅ Use DATETIME to freely insert your own timestamps
  source_type VARCHAR(50),
  event_name VARCHAR(20),
  event_details VARCHAR(100)
);
