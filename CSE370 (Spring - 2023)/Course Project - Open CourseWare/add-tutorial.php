<?php
    session_start();

    require_once "config/dbconnect.php";
    require_once "config/classes/Insert.php";
    require_once "config/classes/Courses.php";

    $i = new Insert();
    $c = new Courses();


    if(isset($_POST['submit'])){

        $_POST['material_type'] = 'Tutorial';    
        
        
        // call function to insert data into database
        if ($i->insertIntoMaterials($_POST)) {
            header("Location: index.php");
        } else {
            $erros['title'] = "Error: " . $error[2];
        }
    }

    // end post check



    include "./templates/header.php";

?>

<title>Add Tutorial</title>

<body>

<?php include "./templates/navigation.php" ?>

<section class="container grey-text">


    <div class="container col-lg-6 shadow rounded bg-warning-subtle my-3 p-4">
        <h4 class="center">Add a Tutorial</h4>
        <p class="center grey-text">(i.e Youtube Playlist)</p>

        <form action="add-tutorial.php" method="POST" class="white">
            <div class="form-group">
                <label for="course">Select Course</label>
                <select class="form-control"  name="course_code" required>

                <?php 

                    $courses = $c->getAllCourses();
                    foreach($courses as $course){
                        echo "<option value='" . $course['course_code'] . "'>" . $course['course_code'] . "</option>";
                    }?>
                </select>
            </div>
            <label for="">Title</label>
            <input class="form-control my-2" type="text" name="material_title" value="<?php echo htmlspecialchars($t_title); ?>">
            <div class="red-text"><?php echo $errors['t_title'] ?></div>
            <input type="hidden" name="material_type" value="Tutorial">

            <label for="">Tutorial URL</label>
            <input class="form-control my-2" type="url" name="tutorial_url" value="<?php echo $t_url;?>">
            <div class="red-text"><?php echo htmlspecialchars($errors['t_url']) ?></div>
            
            <label for="">Credit</label>
            <input class="form-control my-2" type="text" name="instructor" placeholder="i.e Shoaib Dipu" value="<?php echo $t_url;?>">
            
            <button type="submit" class="btn btn-primary" name='submit'>Add</button>
            
        </form>
    </div>

</section>


<?php include "templates/footer.php" ?>

</html>

