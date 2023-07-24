<?php 
session_start();


// ini_set('display_errors', 1);
// ini_set('display_startup_errors', 1);
// error_reporting(E_ALL);

if(!isset($_SESSION['username'])){
    header('Location: login.php');
}

include "./config/dbconnect.php" ;
include "./config/classes/Courses.php";
include "./config/classes/Insert.php";
include "./config/classes/Users.php";

$i = new Insert();
$c = new Courses();

$courses = $c->getAllCourses();


$msg = '';
if(isset($_POST['submit']) && isset($_POST['title']) && isset($_POST['course']) && isset($_FILES['file'])){

    $_POST['material_type'] = 'Resource';
    $_POST['uploader'] = $_SESSION['username'];
    

    $fileName = $_FILES['file']['name'];
    $_POST['resource_path'] = $fileName;
    
    $fileTmpName = $_FILES['file']['tmp_name'];
    $dir = "/uploads/resources/";


    print_r($_POST);
    if($i->insertIntoMaterials($_POST)){
        $msg =  '<div class="alert alert-success alert-dismissible fade show container" role="alert">
    <strong>Thank You!</strong> Resources uploaded Successfully.
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';
    }
    else{
        $msg =  '<div class="alert alert-danger alert-dismissible fade show container" role="alert"><strong>Sorry!</strong> Something went wrong.</div>';
    }
    move_uploaded_file($fileTmpName, $dir.$filename);

}

include "./templates/header.php"
?>

<title>Upload Resource</title>
</head>

<body>
    <?php include "./templates/navigation.php" ;?>

    <section>
        <?php echo $msg; ?>
        <div class="container col-lg-5 shadow rounded bg-warning-subtle my-3 p-3">
            <h3>Upload Resource</h3>
            
            
            <form action="add-resource.php" method="POST" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="title">Resource Title</label>
                    <input type="text" class="form-control"  name="material_title" placeholder="i.e Question paper from spring 23" required>
                </div>
                <div class="form-group">
                    <label for="course">Course</label>
                    <select class="form-control" id="course" name="course_code" required>

                        <?php foreach($courses as $course){
                            echo "<option value='" . $course['course_code'] . "'>" . $course['course_code'] . "</option>";
                        }?>
                    </select>
                </div>
                <div class="form-group my-2">
                    
                    <input type="file" class="form-control-file"  name="file" required>
                </div>
                <input type="submit" class="btn btn-primary" name='submit'  value="Upload"/>


            </form>
        </div>
    </section>
    <?php include "./templates/footer.php" ?>
</body>

