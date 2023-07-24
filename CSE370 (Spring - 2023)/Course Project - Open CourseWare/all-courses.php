
<?php 

// include "./config/dbconnect.php" ;

require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/dbconnect.php';
require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/classes/Courses.php';


$course = new Courses();
$courses = $course->getAllCourses();



include "./templates/header.php";

?>


<title>Explore Courses</title>

</head>

<body>

    <?php include "./templates/navigation.php" ?>


    <!-- courses section -->
    <section class="section body-bg-tertiary container py-3">
        <h3 class="text-center">Explore Courses</h3>

        <div class="row gy-5 p-3 my-3" id="dataTable">
            <?php foreach($courses as $course){ ?>
            
                <div class="col-sm-12 col-md-6 col-lg-4 mb-3 mb-sm-0 d-flex justify-content-center" >
                    <div class="card shadow rounded" style="width: 18rem;">
                        <img src="./blogs/upload/<?=$course['thumbnail']?>" class="card-img-top" alt="...">
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
            <?php } ?>


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
    <script src="assets/js/datatables-demo.js"></script>
    
</body>

</html>