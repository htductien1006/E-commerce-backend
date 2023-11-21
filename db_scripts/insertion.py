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
        "International Men's Day Discount",
        "Chào mừng ngày quốc tế nam giới 19/11, hãy tận hưởng ngày lễ đặc biệt duy nhất giành cho phái mạnh đi nào!",
        "discount",
        99,
        TRUE,
        "2023-11-18 00:00:00",
        "2023-11-19 23:59:59"
    ),
    (
        "Christmas Discount",
        "Giáng sinh đến rồi, sắm đồ ấm thôi!",
        "discount",
        30,
        TRUE,
        "2023-12-18 00:00:00",
        "2023-12-25 23:59:59"
    );

-- Insert Product data
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
    ),

    (
    'Bút Khắc Tên',
    'Bút ký khắc tên là những chiếc bút hàng hiệu được khắc laser logo hoặc tên người được tặng. Là món quà hoàn hảo giúp đối tác luôn nhớ đến bạn đầu tiên.',
    floor(random() * (20000 - 5000 + 1) + 5000)::int, 
    'Cây', 
    1, 
    'https://caybutthan.vn/wp-content/uploads/2019/10/qua-tang-khac-ten-3.jpg', 
    1, 
    3, 
    ),

    (
    'Bút Bi Banner',
    'Quảng cáo được in trên dải banner trong thân bút với nội dung bắt mắt tạo cảm giác thích thú và mới lạ đối với người được tặng bút. Dải banner rộng là khoảng không gian dành cho bạn thể hiện nhiều nội dung quảng cáo của mình lên đó. Đầu dải banner gắn với một thanh kim loại giúp dải banner kéo ra thu vào một cách dễ dàng',
    floor(random() * (20000 - 5000 + 1) + 5000)::int, 
    'Cây', 
    1, 
    'https://butbi.vn/wp-content/uploads/2015/09/But-Banner-08-41.jpg', 
    1, 
    4, 
    2),

    (
    'Sổ Tay Ghi Chú',
    'Sổ tay ghi chú vuông nhỏ được sản xuất từ chất liệu giấy chuyên dụng cho sổ tay. Bìa sổ tay cứng in được mọi logo, hình ảnh trên cả 2 mặt.',
    floor(random() * (60000 - 15000 + 1) + 15000)::int, 
    'Quyển', 
    1, 
    'https://muadogiadung.vn/wp-content/uploads/2023/04/so-tay-ghi-chu-lo-xo-hinh-kute-8x10-5cm.jpg', 
    2, 
    5, 
    2),

    (
    'Sổ Tay Lò Xo',
    'Sổ tay lò xo có thiết kế chuyên nghiệp, khổ vừa phải, cung cấp diện tích ghi chép nhiều hơn nhưng vẫn gọn gàng và tiện dụng. Có nhiều kích thước A4, A5, A6',
    floor(random() * (60000 - 15000 + 1) + 15000)::int, 
    'Quyển', 
    1, 
    'https://inrenhat.vn/wp-content/uploads/2019/05/s%E1%BB%95-tay-l%C3%B2-xo-a4.jpg', 
    2, 
    6, 
    ),

    (
    'Sổ Tay A4',
    'Sổ tay A4 ruột trơn, bìa họa tiết phong cách và hiện đại, thích hợp với các bạn trẻ yêu cái đẹp và sự sáng tạo. Sổ tay A4 ruột ô vuông sử dụng loại giấy siêu mịn, siêu xịn phù hợp các bạn có nhu cầu sketchnote, vẽ, ghi chép hàng ngày, lên kế hoạch cá nhân',
    floor(random() * (60000 - 15000 + 1) + 15000)::int, 
    'Quyển', 
    1, 
    'https://bizweb.dktcdn.net/thumb/1024x1024/100/220/344/products/kem-so-a4-479-x-674-01.jpg?v=1564635191127', 
    2, 
    7, 
    1),

    (
    'Sổ Tay Bìa Da',
    'Sổ tay bìa còng bằng da là một sản phẩm tiện lợi, cần thiết mà ai cũng cần sử dụng. Từ những nhà lãnh đạo cấp cao, các doanh nhân, nhân viên văn phòng. Hay thậm chí cả những bạn học sinh, sinh viên. Đây là một món quà thiết thực, thể hiện sự quan tâm, trân trọng đến người nhận.',
    floor(random() * (60000 - 15000 + 1) + 15000)::int, 
    'Quyển', 
    1, 
    'https://bizweb.dktcdn.net/thumb/1024x1024/100/441/339/products/f5627ef3-4fcf-4e0f-937c-cb1c712ee1d7.jpg?v=1651732684420', 
    2, 
    8, 
    );

    
