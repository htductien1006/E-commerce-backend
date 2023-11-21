CREATE TABLE category
(
  _id SERIAL NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (_id)
);

CREATE TABLE inventory
(
  _id SERIAL NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (_id)
);

CREATE TABLE promotion
(
  _id SERIAL NOT NULL,
  name VARCHAR(50) NOT NULL,
  description VARCHAR(255),
  type VARCHAR(50) NOT NULL,
  discount_percent INT NOT NULL,
  active BOOLEAN NOT NULL,
  start_date TIMESTAMP NOT NULL,
  end_date TIMESTAMP NOT NULL,
  PRIMARY KEY (_id)
);

CREATE TABLE payment_details
(
  _id SERIAL NOT NULL,
  payment_type VARCHAR(50) NOT NULL,
  amont INT NOT NULL,
  status VARCHAR(10) NOT NULL,
  create_time DATE NOT NULL,
  PRIMARY KEY (_id)
);

CREATE TABLE user_account
(
  _id SERIAL NOT NULL,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (_id)
);

CREATE TABLE user_address
(
  _id SERIAL NOT NULL,
  address VARCHAR(100) NOT NULL,
  postal_code VARCHAR(10) NOT NULL,
  country VARCHAR(50) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  user_id INTEGER NOT NULL,
  PRIMARY KEY (_id),
  FOREIGN KEY (user_id) REFERENCES user(_id)
);

CREATE TABLE user_credit
(
  _id SERIAL NOT NULL,
  credit_type VARCHAR(50) NOT NULL,
  bank_name VARCHAR(100) NOT NULL,
  bank_branch VARCHAR(255) NOT NULL,
  credit_number VARCHAR(20) NOT NULL,
  user_id INTEGER NOT NULL,
  PRIMARY KEY (_id),
  FOREIGN KEY (user_id) REFERENCES user(_id)
);

CREATE TABLE admin_account
(
  _id SERIAL NOT NULL,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(100) NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  last_login TIMESTAMP NOT NULL,
  PRIMARY KEY (_id)
);

CREATE TABLE product
(
  _id SERIAL NOT NULL,
  name VARCHAR(100) NOT NULL,
  description VARCHAR(1000),
  price INT NOT NULL,
  uom_name VARCHAR(20),
  uom_quantitive INT,
  image_url VARCHAR(255) NOT NULL,
  category_id INTEGER NOT NULL,
  inventory_id INTEGER NOT NULL,
  promotion_id INTEGER,
  PRIMARY KEY (_id),
  FOREIGN KEY (category_id) REFERENCES category(_id),
  FOREIGN KEY (inventory_id) REFERENCES inventory(_id),
  FOREIGN KEY (promotion_id) REFERENCES promotion(_id)
);

CREATE TABLE shopping_session
(
  _id SERIAL NOT NULL,
  total INT NOT NULL,
  user_id INTEGER NOT NULL,
  PRIMARY KEY (_id),
  FOREIGN KEY (user_id) REFERENCES user(_id)
);

CREATE TABLE order_details
(
  _id SERIAL NOT NULL,
  total INT NOT NULL,
  payment_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  PRIMARY KEY (_id),
  FOREIGN KEY (payment_id) REFERENCES payment_details(_id),
  FOREIGN KEY (user_id) REFERENCES user(_id)
);

CREATE TABLE order_items
(
  _id SERIAL NOT NULL,
  quantity INT NOT NULL,
  product_id INTEGER NOT NULL,
  order_id INTEGER NOT NULL,
  PRIMARY KEY (_id),
  FOREIGN KEY (product_id) REFERENCES product(_id),
  FOREIGN KEY (order_id) REFERENCES order_details(_id)
);

CREATE TABLE cart_items
(
  _id SERIAL NOT NULL,
  quantity INT NOT NULL,
  product_id INTEGER NOT NULL,
  session_id INTEGER NOT NULL,
  PRIMARY KEY (_id),
  FOREIGN KEY (product_id) REFERENCES product(_id),
  FOREIGN KEY (session_id) REFERENCES shopping_session(_id)
);