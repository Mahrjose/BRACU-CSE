

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
$users = $user->getUsersBy('syedfaysel');
// print_r($users);


$course= new Courses();
$courses = $course->getAllCourses();
// print_r($courses);



// Include the header file 
require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/public/templates/header.php';

// start adding from 'title' tag

?>

    <title>User</title>
</head>
<body>

    <?php include $_SERVER['DOCUMENT_ROOT'] . '/OCW/public/templates/navigation.php'; ?>
    

    <h1>Welcome to Profile</h1>

    <p><?= $users[0]['username'] ;?></p>

    <h1>My Courses</h1>

    <table>
        <thead>
            <tr>
                <th>Code</th>
                <th>Title</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach($courses as $c): ?>
            <tr>
                <td><?= $c['course_code']; ?></td>
                <td><?= $c['course_title']; ?></td>
            </tr>
            <?php endforeach; ?>
        </tbody>
    </table>


    <?php include $_SERVER['DOCUMENT_ROOT'] . '/OCW/public/templates/footer.php'; ?>

</body>
</html>
