

<?php 

error_reporting(E_ALL);
ini_set('display_errors', 1);



// Include the database connection class
require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/dbconnect.php';


require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/classes/Users.php';

require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/classes/Courses.php';



// Create an instance of the User class and pass the database connection
$user = new User();


// Fetch all the users
$users = $user->getAllUsers();
// print_r($users);


$course= new Courses();
$courses = $course->getAllCourses();
// print_r($courses);

$singleCourse = $course->getCoursesBy('CSE-101');
$enrolled = $user->enrolledCourses('gleen222');



include $_SERVER['DOCUMENT_ROOT'] . '/OCW/public/templates/header.php';

?>


    <title>My Courses</title>
</head>
<body>

    <?php include 'public/templates/navigation.php'; ?>

    <h1>Courses Enrolled</h1>

    <table>
        <thead>
            <tr>
                <th>Code</th>
                <th>Title</th>
                <th>Enrolled At</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach($enrolled as $e): ?>
            <tr>
                <td><?= $e['course_code']; ?></td>
                <td><?= $e['course_title']; ?></td>
                <td><?= strtotime($e['created_at']); ?></td>
            </tr>
            <?php endforeach; ?>
        </tbody>
    </table>


    <?php include $_SERVER['DOCUMENT_ROOT'] . '/OCW/public/templates/footer.php'; ?>

</body>
</html>
