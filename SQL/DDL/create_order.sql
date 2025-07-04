CREATE TABLE order_details (
  order_id VARCHAR(10) PRIMARY KEY,
  state VARCHAR(50),
  amount DECIMAL(10, 2),
  pincode VARCHAR(10),
  delivery_date DATE
);
