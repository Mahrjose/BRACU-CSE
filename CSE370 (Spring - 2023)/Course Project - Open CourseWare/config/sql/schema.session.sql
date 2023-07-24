-- Create users Relation (without adding foreign keys yet)
CREATE TABLE users (
    username VARCHAR(50),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    autority_level ENUM('ADMIN', 'USER'),

    PRIMARY KEY(username),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Course Relation (acode,skillcode)
CREATE TABLE courses (
    course_code VARCHAR(10),
    course_title VARCHAR(100) NOT NULL,
    course_description TEXT,
    price_type ENUM('FREE','PAID'),
    course_price DECIMAL(10, 2) NOT NULL,
    course_type ENUM('Academic', 'Skill') NOT NULL,
    difficulty_level ENUM('Beginner', 'Intermediate', 'Advance'),
    added_by VARCHAR(50),

    PRIMARY KEY(course_code),
    FOREIGN KEY(added_by) REFERENCES users(username) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create paymentInfo Relation
CREATE TABLE paymentInfo (
    trx_id VARCHAR(100),
    username VARCHAR(50),
    course_code VARCHAR(10),
    approval ENUM('Approved', 'Rejected', 'Not Reviewed') DEFAULT 'Not Reviewed',
    approved_by VARCHAR(50),


    PRIMARY KEY(trx_id),
    FOREIGN KEY(username) REFERENCES users(username) ON DELETE SET NULL,
    FOREIGN KEY(approved_by) REFERENCES users(username) ON DELETE SET NULL,
    FOREIGN KEY(course_code) REFERENCES courses(course_code) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


-- Create Materials Relation
CREATE TABLE materials (
    material_id INT NOT NULL AUTO_INCREMENT,
    material_title VARCHAR(100) NOT NULL,
    course_code VARCHAR(10) NOT NULL,
    material_type ENUM('Tutorial', 'Resource'),
    
    tutorial_url VARCHAR(100),
    instructor VARCHAR(50) DEFAULT 'Guest',

    resource_path VARCHAR(100),
    uploader VARCHAR(50) DEFAULT 'Guest',

    PRIMARY KEY(material_id),
    FOREIGN KEY(course_code) REFERENCES courses(course_code) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(uploader) REFERENCES users(username) ON DELETE SET NULL ON UPDATE CASCADE,
    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Enroll Relation
CREATE TABLE enrollment (
    enroll_id INT NOT NULL AUTO_INCREMENT,
    trx_id VARCHAR(10),
    username VARCHAR(50),
    course_code VARCHAR(10),
    approval ENUM('Approved', 'Rejected', 'Not Reviewed') DEFAULT 'Not Reviewed',
    approved_by VARCHAR(50),


    PRIMARY KEY(trx_id),
    FOREIGN KEY(username) REFERENCES users(username) ON DELETE SET NULL,
    FOREIGN KEY(approved_by) REFERENCES users(username) ON DELETE SET NULL,
    FOREIGN KEY(course_code) REFERENCES courses(course_code) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- Create Blog Relation 

CREATE TABLE blogs (
    post_id INT NOT NULL AUTO_INCREMENT,
    post_title VARCHAR(100) NOT NULL,
    post_content LONGTEXT NOT NULL,
    post_img VARCHAR(100),
    
    category VARCHAR(100),
    author VARCHAR(50),
    status ENUM('Draft', 'Published'),

    publish TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY(post_id),
    FOREIGN KEY(author) REFERENCES users(username) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(category) REFERENCES category(ctg) ON DELETE SET NULL ON UPDATE CASCADE
);


-- tags
CREATE TABLE category (
    ctg VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY(ctg)

);

-- Create Blog Comments Relation

CREATE TABLE comments (
    comment_id INT NOT NULL AUTO_INCREMENT,
    post_id INT NOT NULL,
    author VARCHAR(50) NOT NULL,
    comment_text TEXT NOT NULL,

    PRIMARY KEY(comment_id),
    FOREIGN KEY(author) REFERENCES users(username) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(post_id) REFERENCES blogs(post_id) ON DELETE CASCADE ON UPDATE CASCADE,
    comment_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);




--------- Forum Section --------
CREATE TABLE questions (
    question_id INT NOT NULL AUTO_INCREMENT,
    course_code VARCHAR(10),
    username VARCHAR(50),
    question_title VARCHAR(255) NOT NULL,
    question_body TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    PRIMARY KEY (question_id),
    FOREIGN KEY (course_code) REFERENCES courses(course_code) ON DELETE SET NULL ON UPDATE CASCADE ,
    FOREIGN KEY (username) REFERENCES users(username) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE answers (
    answer_id INT AUTO_INCREMENT,
    course_code  VARCHAR(10) ,
    question_id INT NOT NULL,
    username VARCHAR(50),
    answer_text TEXT NOT NULL,
    
    PRIMARY KEY (answer_id),
    FOREIGN KEY (course_code) REFERENCES courses(course_code) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (question_id) REFERENCES questions(question_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE ON UPDATE CASCADE,
    post_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);




DROP TABLE users;
DROP TABLE courses;
DROP TABLE paymentInfo;
DROP TABLE materials;

-- enroll statements

-- check if price is free or paid
SELECT courses.price_type FROM courses;

-- if it's free
-- enroll

-- else 
SELECT paymentInfo.approval 
FROM paymentInfo
WHERE paymentInfo.course_id = courses.course_id

DELETE from users where autority_level = 'ADMIN';

SELECT * FROM users;