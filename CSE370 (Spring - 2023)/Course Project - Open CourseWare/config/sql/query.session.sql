-- users INSERT

-- ADMINs
INSERT INTO users (
    username,
    first_name,
    last_name,
    email,
    password,
    autority_level
  )
VALUES (
    'mahrjose',
    'Mahrab',
    'Hossain',
    'mirzamahrabhossain@gmail.com',
    'bracu222!',
    'ADMIN'
  );

INSERT INTO users (
    username,
    first_name,
    last_name,
    email,
    password,
    autority_level  
  )
VALUES (
    'syedfaysel',
    'Syed Faysel',
    'Ahammad Rajo',
    'syedfaysel@gmail.com',
    '12345',
    'ADMIN'
  );

INSERT INTO users (
    username,
    first_name,
    last_name,
    email,
    password,
    autority_level  
  )
VALUES (
    'naimparves',
    'Naim',
    'Parves',
    'naimparves@gmail.com',
    '12345',
    'ADMIN'
  );

-- Normal Users

INSERT INTO users (
    username,
    first_name,
    last_name,
    email,
    password,
    autority_level  
  )
VALUES (
    'gleen222',
    'Gleen',
    'Stan',
    'gleen222@gmail.com',
    '12345',
    'USER'
  );

INSERT INTO users (
    username,
    first_name,
    last_name,
    email,
    password,
    autority_level  
  )
VALUES (
    'anjuro',
    'Amit',
    'Saha',
    'amita@gmail.com',
    '12345',
    'USER'
  );

-- courses

INSERT INTO courses (
    course_code,
    course_title,
    course_description,
    price_type,
    course_price,
    course_type,
    difficulty_level,
    added_by
  ) VALUES (
    'CSE110',
    'Programming Language I',
    'This course is designed to introduce students to the field of computer science & Programming Language ',
    'FREE',
    0.00,
    'Academic',
    'Beginner',
    'syedfaysel'
  );

-- Materials ---

-- Tutorial
INSERT INTO materials (
    material_title,
    course_code,
    material_type,
    tutorial_url,
    instructor,
    uploader
) VALUES (
    'Python Tutorial',
    'CSE110',
    'Tutorial',
    'https://www.youtube-nocookie.com/embed/videoseries?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU',
    'Corey Schafer',
    NULL
);


-- Payment info
INSERT INTO `paymentInfo` (`trx_id`, `username`, `course_code`, `approval`, `approved_by`) VALUES ('abc12xyzUmno', 'gleen222', 'CSE110', 'Approved', 'rajo');



-- Resource
INSERT INTO materials (material_title, course_code, material_type, resource_path, uploader)
VALUES ('Introduction to Programming Book', 'CSE110', 'Resource', '/Resources/programming_book.pdf', 'syedfaysel');



-- QUESTION---

INSERT INTO questions (
    course_code,
    username,
    question_title,
    question_body
  )
VALUES (
    'CSE110',
    'syedfaysel',
    'Is dictionary better than list?',
    'I am confused about which one is better for me. I am a beginner. Please help me.'

  );



-- Answer ---
INSERT INTO answers (

    course_code,
    question_id,
    username,
    answer_text

  )
VALUES (
    
    'CSE-101',
    1,
    'gleen222',
    'You should search more. You can go to bracu lost & found'

  );



-- Blogs ---

INSERT INTO blogs (

    post_title,
    post_content,
    post_img,
    category,
    author,
    status
  )

VALUES(
        'How to learn programming',
        'Lorem ipsum dolor sit amet consectetur adipiscing elit. Donec auctor nisl eget ultricies tincidunt nunc nisl aliquam nisl',
        'post1.img',
        'Programming',
        'syedfaysel',
        'Published'
)


INSERT INTO `blogs` ( `post_title`, `post_content`, `post_img`, `category`, `author`, `status`) VALUES ( 'Is python worth Learning!', 'Programming is very crucial to computer science.', 'thubnail.jpg', 'Programming', 'syedfaysel', 'Publish');



INSERT INTO category (
    ctg
  )
VALUES (
    'Programming'
  );
