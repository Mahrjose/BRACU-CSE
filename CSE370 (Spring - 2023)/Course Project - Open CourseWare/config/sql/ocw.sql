-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 17, 2023 at 01:40 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ocw`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE `answers` (
  `answer_id` int(11) NOT NULL,
  `course_code` varchar(10) DEFAULT NULL,
  `question_id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `answer_text` text NOT NULL,
  `post_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`answer_id`, `course_code`, `question_id`, `username`, `answer_text`, `post_time`) VALUES
(1, 'CSE-101', 1, 'gleen222', 'You should search more. You can go to bracu lost & found', '2023-04-05 21:33:56');

-- --------------------------------------------------------

--
-- Table structure for table `blogs`
--

CREATE TABLE `blogs` (
  `post_id` int(11) NOT NULL,
  `post_title` varchar(100) NOT NULL,
  `post_content` longtext NOT NULL,
  `post_img` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `status` enum('Draft','Publish') DEFAULT NULL,
  `publish` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blogs`
--

INSERT INTO `blogs` (`post_id`, `post_title`, `post_content`, `post_img`, `category`, `author`, `status`, `publish`) VALUES
(2, 'Is python worth Learning!', 'Programming is very crucial to computer science.', 'blog-thumb-02.jpg', 'Programming', 'syedfaysel', 'Publish', '2023-04-09 13:00:57'),
(4, 'How to start Competitive Programming', 'You need to practice more', 'blog-thumb-01.jpg', 'Programming', 'syedfaysel', 'Publish', '2023-04-15 22:45:15'),
(5, 'Another Post test', 'test test test', 'python-1110x550.jpg', 'Programming', 'syedfaysel', 'Publish', '2023-04-15 22:49:13');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `ctg` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`ctg`) VALUES
('Programming');

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `comment_id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  `author` varchar(50) NOT NULL,
  `comment_text` text NOT NULL,
  `comment_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`comment_id`, `post_id`, `author`, `comment_text`, `comment_at`) VALUES
(1, 2, 'rajo', 'Bhai, Chobi koi', '2023-04-15 22:46:15'),
(2, 2, 'rajo', 'WOw', '2023-04-16 18:35:13');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `course_code` varchar(10) NOT NULL,
  `course_title` varchar(100) NOT NULL,
  `course_description` text DEFAULT NULL,
  `price_type` enum('FREE','PAID') DEFAULT NULL,
  `course_price` decimal(10,2) NOT NULL,
  `course_type` enum('Academic','Skill') NOT NULL,
  `difficulty_level` enum('Beginner','Intermediate','Advance') DEFAULT NULL,
  `thumbnail` varchar(50) DEFAULT NULL,
  `added_by` varchar(50) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`course_code`, `course_title`, `course_description`, `price_type`, `course_price`, `course_type`, `difficulty_level`, `thumbnail`, `added_by`, `created_at`) VALUES
('CSE-101', 'Introduction to Computer Science', 'This course is designed to introduce students to the field of computer science. The course will cover the basic concepts of computer science, including the history of computing, the hardware and software components of a computer, and the basic concepts of programming.', 'FREE', '0.00', 'Academic', 'Beginner', 'php-tutorials.png', 'mahrjose', '2023-04-05 21:24:41'),
('CSE110', 'Programming Language I', 'This course is designed to introduce students to the field of computer science & Programming Language ', 'FREE', '0.00', 'Academic', 'Beginner', 'python-1110x550.jpg', 'syedfaysel', '2023-04-05 22:36:04'),
('CSE220', 'Data Structures', 'This course is designed to introduce students to the field of computer science & Programming Language ', 'FREE', '0.00', 'Academic', 'Intermediate', 'php-tutorials.png', 'syedfaysel', '2023-04-14 23:17:32'),
('CSE221', 'Algorithm Design & Analysis', 'Amazing Course', 'FREE', '0.00', 'Academic', 'Intermediate', 'python-1110x550.jpg', 'syedfaysel', '2023-04-15 18:18:21'),
('CSE331', 'Automata', 'triala', 'FREE', '0.00', 'Academic', 'Advance', 'python-1110x550.jpg', 'rajo', '2023-04-15 18:32:44'),
('CSE370', 'Database Systems', 'CSE370 is amazing', 'FREE', '0.00', 'Academic', 'Intermediate', 'php-tutorials.png', 'admin', '2023-04-16 18:38:29'),
('web101', 'Website Design', 'Very simple course', 'FREE', '0.00', 'Skill', 'Beginner', 'python-1110x550.jpg', 'afra', '2023-04-15 20:19:10');

-- --------------------------------------------------------

--
-- Table structure for table `materials`
--

CREATE TABLE `materials` (
  `material_id` int(11) NOT NULL,
  `material_title` varchar(100) NOT NULL,
  `course_code` varchar(10) NOT NULL,
  `material_type` enum('Tutorial','Resource') NOT NULL,
  `tutorial_url` varchar(100) DEFAULT NULL,
  `instructor` varchar(50) DEFAULT 'Guest',
  `resource_path` varchar(100) DEFAULT NULL,
  `uploader` varchar(50) DEFAULT 'Guest',
  `last_modified` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `materials`
--

INSERT INTO `materials` (`material_id`, `material_title`, `course_code`, `material_type`, `tutorial_url`, `instructor`, `resource_path`, `uploader`, `last_modified`) VALUES
(3, 'Introduction to Programming', 'CSE110', 'Tutorial', 'https://www.youtube.com/embed?v=cb5coX1jAYE&list=PLvr0Ht-XkB_0V-mjAYlfgk-3VRmFarlzC', 'Tawhid Anwar', NULL, NULL, '2023-04-06 00:52:07'),
(4, 'Python Tutorial', 'CSE110', 'Tutorial', 'https://www.youtube-nocookie.com/embed/videoseries?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU', 'Corey Schafer', NULL, NULL, '2023-04-06 01:15:12'),
(5, 'Introduction to Programming Book', 'CSE110', 'Resource', NULL, 'Guest', 'Opencourseware-v2/uploads/resources/programming_book.pdf', 'syedfaysel', '2023-04-06 01:27:58'),
(8, 'dummy', 'CSE-101', 'Resource', NULL, 'Guest', 'Gravatar.png', 'rajo', '2023-04-10 00:55:50'),
(9, 'dummy 2', 'CSE-101', 'Resource', NULL, 'Guest', 'learn_tuple.py', 'rajo', '2023-04-10 00:57:31'),
(10, 'another resource', 'CSE110', 'Resource', NULL, 'Guest', 'learn_tuple.py', 'rajo', '2023-04-10 01:00:23'),
(14, 'test 1', 'CSE-101', 'Resource', NULL, 'Guest', 'A.cpp', 'rajo', '2023-04-10 07:19:13'),
(15, 'python code', 'CSE110', 'Resource', NULL, 'Guest', 'learn_tuple.py', 'rajo', '2023-04-10 07:43:31'),
(16, 'Dummy Resource', 'CSE110', 'Resource', NULL, 'Guest', 'C.cpp', 'rajo', '2023-04-10 09:37:14'),
(17, 'Full Playlist', 'CSE221', 'Tutorial', 'https://www.youtube.com/embed/videoseries?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O', 'Abdul Bari', NULL, NULL, '2023-04-15 20:59:59');

-- --------------------------------------------------------

--
-- Table structure for table `paymentInfo`
--

CREATE TABLE `paymentInfo` (
  `trx_id` varchar(100) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `course_code` varchar(10) DEFAULT NULL,
  `approval` enum('Approved','Rejected','Not Reviewed') DEFAULT 'Not Reviewed',
  `approved_by` varchar(50) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `paymentInfo`
--

INSERT INTO `paymentInfo` (`trx_id`, `username`, `course_code`, `approval`, `approved_by`, `created_at`) VALUES
('abc12xyzUmno', 'gleen222', 'CSE110', 'Approved', 'rajo', '2023-04-14 22:45:28'),
('freecourseXYZ', 'admin', 'CSE110', 'Not Reviewed', NULL, '2023-04-16 22:37:27'),
('randomTrxId', 'afra', 'CSE110', 'Approved', NULL, '2023-04-16 00:42:52');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `question_id` int(11) NOT NULL,
  `course_code` varchar(10) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `question_title` varchar(255) NOT NULL,
  `question_body` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`question_id`, `course_code`, `username`, `question_title`, `question_body`, `created_at`, `updated_at`) VALUES
(1, 'CSE-101', 'mahrjose', 'Ki ache Jibone?', 'Onek khuje dekhlam, kintu Painai', '2023-04-05 21:30:42', '2023-04-05 21:30:42'),
(2, 'CSE-101', 'gleen222', 'What is the prerq?', 'Onek kasdfldsaflkjsa', '2023-04-05 21:44:02', '2023-04-05 21:44:02'),
(3, 'CSE110', 'syedfaysel', 'Is dictionary better than list?', 'I am confused about which one is better for me. I am a beginner. Please help me.', '2023-04-05 23:15:13', '2023-04-05 23:15:13');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `authority_level` enum('ADMIN','USER') DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `first_name`, `last_name`, `email`, `password`, `authority_level`, `created_at`) VALUES
('admin', 'Syed Faysel', 'Ahammad Rajo', 'admin@ocw.com', '827ccb0eea8a706c4c34a16891f84e7b', 'ADMIN', '2023-04-16 16:18:04'),
('afra', 'Jannatul Mawa', 'Afra', 'afra@gmail.com', '827ccb0eea8a706c4c34a16891f84e7b', 'USER', '2023-04-15 17:12:21'),
('gleen222', 'Gleen', 'Stan', 'gleen222@gmail.com', '12345', 'USER', '2023-04-05 21:32:18'),
('kaysel', 'Syed Kaysel', 'Ahmed', 'dr.kaysel@gmail.com', '323f73960fa6c2d99007e7efc449b5a9', 'USER', '2023-04-16 10:06:17'),
('mahrjose', 'Mahrab', 'Hossain', 'mirzamahrabhossain@gmail.com', 'bracu222!', 'ADMIN', '2023-04-05 21:24:24'),
('nazim', 'Nazim', 'Parves', 'kichu@gmail.com', '2faa44bc6856eb04f361d2cf833ac4a8', 'USER', '2023-04-15 18:42:47'),
('rajo', 'Syed Faysel', 'Ahammad Rajo', 'sfa.rajo20@gmail.com', '827ccb0eea8a706c4c34a16891f84e7b', 'USER', '2023-04-09 13:46:42'),
('syedfaysel', 'Syed Faysel', 'Ahammad Rajo', 'syedfaysel@gmail.com', '12345', 'ADMIN', '2023-04-05 22:35:35');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`answer_id`),
  ADD KEY `course_code` (`course_code`),
  ADD KEY `question_id` (`question_id`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `blogs`
--
ALTER TABLE `blogs`
  ADD PRIMARY KEY (`post_id`),
  ADD KEY `author` (`author`),
  ADD KEY `category` (`category`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`ctg`),
  ADD UNIQUE KEY `ctg` (`ctg`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`comment_id`),
  ADD KEY `author` (`author`),
  ADD KEY `post_id` (`post_id`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`course_code`),
  ADD KEY `added_by` (`added_by`);

--
-- Indexes for table `materials`
--
ALTER TABLE `materials`
  ADD PRIMARY KEY (`material_id`),
  ADD KEY `course_code` (`course_code`),
  ADD KEY `uploader` (`uploader`);

--
-- Indexes for table `paymentInfo`
--
ALTER TABLE `paymentInfo`
  ADD PRIMARY KEY (`trx_id`),
  ADD KEY `username` (`username`),
  ADD KEY `approved_by` (`approved_by`),
  ADD KEY `course_code` (`course_code`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`question_id`),
  ADD KEY `course_code` (`course_code`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `answers`
--
ALTER TABLE `answers`
  MODIFY `answer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `blogs`
--
ALTER TABLE `blogs`
  MODIFY `post_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `comment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `materials`
--
ALTER TABLE `materials`
  MODIFY `material_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `question_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `answers`
--
ALTER TABLE `answers`
  ADD CONSTRAINT `answers_ibfk_1` FOREIGN KEY (`course_code`) REFERENCES `courses` (`course_code`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `answers_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `answers_ibfk_3` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `blogs`
--
ALTER TABLE `blogs`
  ADD CONSTRAINT `blogs_ibfk_1` FOREIGN KEY (`author`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `blogs_ibfk_2` FOREIGN KEY (`category`) REFERENCES `category` (`ctg`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`author`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `blogs` (`post_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `courses`
--
ALTER TABLE `courses`
  ADD CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`added_by`) REFERENCES `users` (`username`) ON DELETE SET NULL;

--
-- Constraints for table `materials`
--
ALTER TABLE `materials`
  ADD CONSTRAINT `materials_ibfk_1` FOREIGN KEY (`course_code`) REFERENCES `courses` (`course_code`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `materials_ibfk_2` FOREIGN KEY (`uploader`) REFERENCES `users` (`username`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `paymentInfo`
--
ALTER TABLE `paymentInfo`
  ADD CONSTRAINT `paymentInfo_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE SET NULL,
  ADD CONSTRAINT `paymentInfo_ibfk_2` FOREIGN KEY (`approved_by`) REFERENCES `users` (`username`) ON DELETE SET NULL,
  ADD CONSTRAINT `paymentInfo_ibfk_3` FOREIGN KEY (`course_code`) REFERENCES `courses` (`course_code`) ON DELETE SET NULL;

--
-- Constraints for table `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`course_code`) REFERENCES `courses` (`course_code`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `questions_ibfk_2` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
