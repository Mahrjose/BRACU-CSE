


<?php 
session_start();


require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/dbconnect.php';
require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/classes/Courses.php';
require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/classes/Users.php';
require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/classes/Insert.php';


$c= new Courses();
$u = new User();
$i = new Insert();


    // check GET request id param
    if(isset($_GET['course_code'])){
        $course_code = $_GET['course_code'];

        // retrieve data
        $course = $c->getCoursesBy($course_code);
    }


    include "./templates/header.php";
?>
<title><?php echo htmlspecialchars($course['course_title'])  ?></title>
</head>

<body>
<?php include "./templates/navigation.php" ?>


    <section class="container">
        <div class="container-fluid text-center shadow m-3 p-3 bg-warning-subtle rounded">
            <?php if($course){ ?>
            
                <h4>Course Code: <?php echo htmlspecialchars($course[0]['course_code']) ?>
                </h4>
                <h3>Course Title: <?php echo htmlspecialchars($course[0]['course_title']) ?>
                </h3>
                <p>Course Type: <?php echo htmlspecialchars($course[0]['course_type']); ?>
                </p>
                <p>Difficulty Level: <?php echo htmlspecialchars($course[0]['difficulty_level']); ?>
                </p>
                <p>Course Description: <?php echo htmlspecialchars($course[0]['course_description']); ?>
                </p>
                <div>
                    <?php if($u->enrolledCourses($_SESSION['username'], $course[0]['course_code'])){ ?>
                    
                        <a class="btn btn-primary" href="watch.php?course_code=<?php echo htmlspecialchars($course[0]['course_code']) ?>">Tutorials</a>
                        <a class="btn btn-primary" href="resources.php?course_code=<?php echo htmlspecialchars($course[0]['course_code']) ?>">Resources</a>
                        <a class="btn btn-primary" href="discussion.php?course_code=<?php echo htmlspecialchars($course[0]['course_code']) ?>">Discussion</a>

                    <?php } else { ?>
                        <p>Price:<?=$course[0]['course_price']?></p>
                        <a class="btn btn-primary" href=""  data-bs-toggle="modal" data-bs-target="#enroll">Enroll Now</a>

                    <?php } 
                        
                        // edit user (from logged user)
                        if(isset($_POST['submit'])){
                            $_POST['username'] = $_SESSION['username'];

                            if($i->enrollCourse($_POST)){
                                echo "Enrollment Pending";
                                // header('Location: enrolled.php');
                            }
                            else{
                                echo "Enrollment Failed! TrxId is not valid";
                            }
                        }
                    
                    ?>
                </div>
            <?php } else { ?>
                <h3>No such course found</h3>
            <?php } ?>
        </div>
    </section>


    <!--Edit Modal -->
    <div class="modal fade" id="enroll" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="enrollLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="#">Enroll Course</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div>

                    <?php 
                        if(!isset($_SESSION['username'])){
                            echo "<p>You need to login first</p><br><a class='btn btn-primary' href='login.php'>Login</a>";

                        }
                        else{?>

                        <form action="" method="POST">
                            <label for="">Enrolling the following course</label>
                            <input class="form-control py-2 my-2" type="text" name="course_code" id="" value="<?= $course[0]['course_code'] ?>" readonly>

                            <label for="">TrxId</label>
                            <input class="form-control py-2 my-2" type="text" name="trx_id" required>
                            
                            
                            <button class="form-control btn btn-secondary" type="submit" name="submit">Confirm</button> 
                        </form>
                        <?php } ?>
                    

                    </div>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    
                </div>
            </div>
        </div>
    </div>


<?php include "./templates/footer.php" ?>

</body>
</html>