CREATE TABLE IF NOT EXISTS category
(
  _id SERIAL NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (_id)
);

CREATE TABLE IF NOT EXISTS inventory
(
  _id SERIAL NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (_id)
);

CREATE TABLE IF NOT EXISTS promotion
(
  _id SERIAL NOT NULL,
  name VARCHAR(50) NOT NULL,
  description VARCHAR(255),
  type_of_promotion VARCHAR(50) NOT NULL,
  discount_percent INT NOT NULL,
  active BOOLEAN NOT NULL,
  start_date TIMESTAMP NOT NULL,
  end_date TIMESTAMP NOT NULL,
  PRIMARY KEY (_id)
);

CREATE TABLE IF NOT EXISTS payment_details
(
  _id SERIAL NOT NULL,
  payment_type VARCHAR(50) NOT NULL,
  amount INT NOT NULL,
  status VARCHAR(10) NOT NULL,
  create_time DATE NOT NULL,
  PRIMARY KEY (_id)
);

-- CREATE TABLE IF NOT EXISTS user_account
-- (
--   _id SERIAL NOT NULL,
--   username VARCHAR(50) NOT NULL,
--   password VARCHAR(50) NOT NULL,
--   first_name VARCHAR(50) NOT NULL,
--   last_name VARCHAR(50) NOT NULL,
--   PRIMARY KEY (_id)
-- );

-- CREATE TABLE IF NOT EXISTS user_address
-- (
--   _id SERIAL NOT NULL,
--   address VARCHAR(100) NOT NULL,
--   postal_code VARCHAR(10) NOT NULL,
--   country VARCHAR(50) NOT NULL,
--   phone_number VARCHAR(20) NOT NULL,
--   email VARCHAR(100) NOT NULL,
--   user_id INTEGER NOT NULL,
--   PRIMARY KEY (_id),
--   FOREIGN KEY (user_id) REFERENCES user_account(_id)
-- );

CREATE TABLE IF NOT EXISTS user_credit
(
  _id SERIAL NOT NULL,
  credit_type VARCHAR(50) NOT NULL,
  bank_name VARCHAR(100) NOT NULL,
  bank_branch VARCHAR(255) NOT NULL,
  credit_number VARCHAR(20) NOT NULL,
  user_id INTEGER NOT NULL,
  PRIMARY KEY (_id),
  FOREIGN KEY (user_id) REFERENCES user_account(_id)
);

-- CREATE TABLE IF NOT EXISTS admin_account
-- (
--   _id SERIAL NOT NULL,
--   username VARCHAR(50) NOT NULL,
--   password VARCHAR(100) NOT NULL,
--   first_name VARCHAR(50) NOT NULL,
--   last_name VARCHAR(50) NOT NULL,
--   last_login TIMESTAMP NOT NULL,
--   PRIMARY KEY (_id)
-- );

CREATE TABLE IF NOT EXISTS product
(
  _id SERIAL NOT NULL,
  name VARCHAR(100) NOT NULL,
  description VARCHAR(1000),
  price INT NOT NULL,
  uom_name VARCHAR(20),
  uom_quantitative INT,
  image_url VARCHAR(255) NOT NULL,
  category_id INTEGER NOT NULL,
  inventory_id INTEGER NOT NULL,
  promotion_id INTEGER,
  PRIMARY KEY (_id),
  FOREIGN KEY (category_id) REFERENCES category(_id),
  FOREIGN KEY (inventory_id) REFERENCES inventory(_id),
  FOREIGN KEY (promotion_id) REFERENCES promotion(_id)
);

CREATE TABLE IF NOT EXISTS shopping_session
(
  _id SERIAL NOT NULL,
  total INT NOT NULL,
  user_id INTEGER NOT NULL,
  PRIMARY KEY (_id),
  FOREIGN KEY (user_id) REFERENCES user_account(_id)
);

CREATE TABLE IF NOT EXISTS order_details
(
  _id SERIAL NOT NULL,
  total INT NOT NULL,
  payment_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  PRIMARY KEY (_id),
  FOREIGN KEY (payment_id) REFERENCES payment_details(_id),
  FOREIGN KEY (user_id) REFERENCES user_account(_id)
);

CREATE TABLE IF NOT EXISTS order_items
(
  _id SERIAL NOT NULL,
  quantity INT NOT NULL,
  product_id INTEGER NOT NULL,
  order_id INTEGER NOT NULL,
  PRIMARY KEY (_id),
  FOREIGN KEY (product_id) REFERENCES product(_id),
  FOREIGN KEY (order_id) REFERENCES order_details(_id)
);

CREATE TABLE IF NOT EXISTS cart_items
(
  _id SERIAL NOT NULL,
  quantity INT NOT NULL,
  product_id INTEGER NOT NULL,
  session_id INTEGER NOT NULL,
  PRIMARY KEY (_id),
  FOREIGN KEY (product_id) REFERENCES product(_id),
  FOREIGN KEY (session_id) REFERENCES shopping_session(_id)
);





-- Insert Category data --
INSERT INTO category (name) VALUES
    ('Bút'),
    ('Sổ tay'),
    ('Kỷ niệm chương'),
    ('Ly'),
    ('Túi vải'),
    ('Huy Chương'),
    ('Móc khóa'),
    ('Bình giữ nhiệt');

-- Insert Inventory data --
INSERT INTO inventory (quantity) VALUES
  (floor(random() * (10000 - 50 + 1) + 50)::int),
  (floor(random() * (10000 - 50 + 1) + 50)::int),
  (floor(random() * (10000 - 50 + 1) + 50)::int),
  (floor(random() * (10000 - 50 + 1) + 50)::int),
  (floor(random() * (10000 - 50 + 1) + 50)::int),
  (floor(random() * (10000 - 50 + 1) + 50)::int),
  (floor(random() * (10000 - 50 + 1) + 50)::int),
  (floor(random() * (10000 - 50 + 1) + 50)::int),
  (floor(random() * (10000 - 50 + 1) + 50)::int),
  (floor(random() * (10000 - 50 + 1) + 50)::int);

-- Insert Promotion data --
INSERT INTO promotion (name, description, type, discount_percent, active, start_date, end_date)
    VALUES (
        'International Men Day Discount',
        'Chào mừng ngày quốc tế nam giới 19/11, hãy tận hưởng ngày lễ đặc biệt duy nhất giành cho phái mạnh đi nào!',
        'discount',
        99,
        TRUE,
        '2023-11-18 00:00:00',
        '2023-11-19 23:59:59'
    ),
    (
        'Christmas Discount',
        'Giáng sinh đến rồi, sắm đồ ấm thôi!',
        'discount',
        30,
        TRUE,
        '2023-12-18 00:00:00',
        '2023-12-25 23:59:59'
    );

-- Insert Product data --
INSERT INTO product (name, description, price, uom_name, uom_quantitative, image_url, category_id, inventory_id, promotion_id) VALUES
    (
    'Bút Bi Vỏ Gỗ',
    'Bút bi vỏ gỗ là dòng bút bi, toàn thân vỏ được làm bằng gỗ tự nhiên nên có màu sắc của các vân gỗ được mài nhẵn khá bắt mắt, tạo nên đặc trưng riêng cho dòng bút gỗ.',
    floor(random() * (20000 - 5000 + 1) + 5000)::int, 
    'Cây', 
    1, 
    'https://down-vn.img.susercontent.com/file/48eacf5e1e0e35d302597aa330a4b432', 
    1, 
    1, 
    1),
    (
    'Bút Bi Giấy',
    'Thân bút màu nâu, cán bút màu đen, thân thiện với môi trường. Mực đen, kích thước cao 14cm, đường kính 1cm. Logo, hình ảnh được in trên banner ngoài thân bút để tối ưu vùng in.',
    floor(random() * (20000 - 5000 + 1) + 5000)::int, 
    'Cây', 
    1, 
    'https://www.dtcworld.com.vn/storage/product-images/1034/EcoRange%20Pen%205a_20201122160212.jpg', 
    1, 
    2, 
    2),(
    'Bút Khắc Tên',
    'Bút ký khắc tên là những chiếc bút hàng hiệu được khắc laser logo hoặc tên người được tặng. Là món quà hoàn hảo giúp đối tác luôn nhớ đến bạn đầu tiên.',
    floor(random() * (20000 - 5000 + 1) + 5000)::int, 
    'Cây', 
    1, 
    'https://caybutthan.vn/wp-content/uploads/2019/10/qua-tang-khac-ten-3.jpg', 
    1, 
    3, 
    1),(
    'Bút Bi Banner',
    'Quảng cáo được in trên dải banner trong thân bút với nội dung bắt mắt tạo cảm giác thích thú và mới lạ đối với người được tặng bút. Dải banner rộng là khoảng không gian dành cho bạn thể hiện nhiều nội dung quảng cáo của mình lên đó. Đầu dải banner gắn với một thanh kim loại giúp dải banner kéo ra thu vào một cách dễ dàng',
    floor(random() * (20000 - 5000 + 1) + 5000)::int, 
    'Cây', 
    1, 
    'https://butbi.vn/wp-content/uploads/2015/09/But-Banner-08-41.jpg', 
    1, 
    4, 
    2),(
    'Sổ Tay Ghi Chú',
    'Sổ tay ghi chú vuông nhỏ được sản xuất từ chất liệu giấy chuyên dụng cho sổ tay. Bìa sổ tay cứng in được mọi logo, hình ảnh trên cả 2 mặt.',
    floor(random() * (60000 - 15000 + 1) + 15000)::int, 
    'Quyển', 
    1, 
    'https://muadogiadung.vn/wp-content/uploads/2023/04/so-tay-ghi-chu-lo-xo-hinh-kute-8x10-5cm.jpg', 
    2, 
    5, 
    2),(
    'Sổ Tay Lò Xo',
    'Sổ tay lò xo có thiết kế chuyên nghiệp, khổ vừa phải, cung cấp diện tích ghi chép nhiều hơn nhưng vẫn gọn gàng và tiện dụng. Có nhiều kích thước A4, A5, A6',
    floor(random() * (60000 - 15000 + 1) + 15000)::int, 
    'Quyển', 
    1, 
    'https://inrenhat.vn/wp-content/uploads/2019/05/s%E1%BB%95-tay-l%C3%B2-xo-a4.jpg', 
    2, 
    6, 
    2),(
    'Sổ Tay A4',
    'Sổ tay A4 ruột trơn, bìa họa tiết phong cách và hiện đại, thích hợp với các bạn trẻ yêu cái đẹp và sự sáng tạo. Sổ tay A4 ruột ô vuông sử dụng loại giấy siêu mịn, siêu xịn phù hợp các bạn có nhu cầu sketchnote, vẽ, ghi chép hàng ngày, lên kế hoạch cá nhân',
    floor(random() * (60000 - 15000 + 1) + 15000)::int, 
    'Quyển', 
    1, 
    'https://bizweb.dktcdn.net/thumb/1024x1024/100/220/344/products/kem-so-a4-479-x-674-01.jpg?v=1564635191127', 
    2, 
    7, 
    1),(
    'Sổ Tay Bìa Da',
    'Sổ tay bìa còng bằng da là một sản phẩm tiện lợi, cần thiết mà ai cũng cần sử dụng. Từ những nhà lãnh đạo cấp cao, các doanh nhân, nhân viên văn phòng. Hay thậm chí cả những bạn học sinh, sinh viên. Đây là một món quà thiết thực, thể hiện sự quan tâm, trân trọng đến người nhận.',
    floor(random() * (60000 - 15000 + 1) + 15000)::int, 
    'Quyển', 
    1, 
    'https://bizweb.dktcdn.net/thumb/1024x1024/100/441/339/products/f5627ef3-4fcf-4e0f-937c-cb1c712ee1d7.jpg?v=1651732684420', 
    2, 
    8, 
    1);

