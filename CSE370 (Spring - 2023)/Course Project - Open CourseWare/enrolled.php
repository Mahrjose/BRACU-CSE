
<?php 
session_start();

// include "./config/dbconnect.php" ;

require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/dbconnect.php';
require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/classes/Users.php';

$user = new User();
$courses = $user->enrolledCourses($_SESSION['username']);



include "./templates/header.php";

?>





<title>Enrolled Courses</title>

</head>

<body>

    <?php include "./templates/navigation.php" ?>


    <!-- courses section -->
    <section class="section body-bg-tertiary container py-3">
        <h3 class="text-center">Continue Learning</h3>

        <div class="row gy-5 p-3 my-3">

            <?php if(!$courses){
                echo "<h3 class='text-center'>You are not enrolled in any course</h3>";
            }
            else{
                foreach($courses as $course){

            ?>
            
                <div class="col-sm-12 col-md-6 col-lg-4 mb-3 mb-sm-0 d-flex justify-content-center" >
                    <div class="card shadow rounded bg-warning-subtle" style="width: 18rem;">
                        <img src="..." class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title"><?php echo htmlspecialchars($course['course_code']); ?>
                            </h5>
                            <h4><?php echo htmlspecialchars($course['course_title']); ?>
                            </h4>
                            <p class="card-text"><?php echo htmlspecialchars($course['course_description']); ?>
                            </p>
                            <a href="course.php?course_code=<?php echo $course['course_code'] ?>" class="btn btn-primary">Details</a>
                        </div>
                    </div>
                </div>
            <?php  }
        } ?>


        </div>

        <!-- Pagination -->
        <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">
                <li class="page-item">
                    <a class="page-link">Previous</a>
                </li>
                <li class="page-item active"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item">
                    <a class="page-link" href="#">Next</a>
                </li>
            </ul>
        </nav>

    </section>



    <?php include "./templates/footer.php" ?>
    
</body>

</html>