<?php 

error_reporting(E_ALL);
ini_set('display_errors', 1);



// Include the database connection class
require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/dbconnect.php';


require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/classes/Insert.php';

require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/classes/Courses.php';



// Create an instance of the User class and pass the database connection
$insert = new Insert();


// Insert into all the users
$addCourse = $insert->insertIntoCourses();
// print_r($users);


?>


