<?php




    $insert = new Insert();

    // using post method & check post request
    if (isset($_POST['add_course'])) {

        $_POST['added_by'] = $_SESSION['username'];

        if(!isset($_POST['thumbnail'])){
            $_POST['thumbnail'] = "default.jpg";
        }

        // call function to insert data into database
        if ($insert->insertIntoCourses($_POST)) {
            // header("Location: all-courses.php");
            echo "Success";
        } else {
            // $erros['title'] = "Error: " . $error[2];
            echo "Error";
        }
    }
    

    // end post check


?>



<title>Add Course</title>


<?php include "templates/navigation.php" ?>

<section class="">


    <div class="container col-lg-6 shadow rounded bg-warning-subtle my-3 p-4">
            <h4 class="text-center">Add new Course</h4>
            <form action="add-course.php" method="POST" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="title">Course Code</label>
                    <input type="text" class="form-control"  name="course_code" placeholder="i.e CSE370" required>
                </div>
                <div class="form-group">
                    <label for="title">Course Title</label>
                    <input type="text" class="form-control"  name="course_title" placeholder="i.e Database Systems" required>
                </div>
                <div class="form-group">
                    <label for="floatingTextarea">Description</label>
                    <textarea class="form-control" style="height: 100px" placeholder="CSE370 is an amazing course ..." id="floatingTextarea" name="course_description"></textarea>
                    
                </div>
                <div class="form-group">
                    <label for="course">Price Type</label>
                    <select class="form-control"  name="price_type" required>

                        <option value='Free'>Free</option>
                        <option value='Paid'>Paid</option>

                    </select>
                </div>
                <div class="form-group">
                    <label for="title">Price</label>
                    <input type="text" class="form-control"  name="course_price" placeholder="0.0" required>
                </div>
                <div class="form-group">
                    <label for="course">Category</label>
                    <select class="form-control"  name="course_type" required>

                        <option value='Academic'>Academic</option>
                        <option value='Skill'>Skill</option>

                    </select>
                </div>
                <div class="form-group">
                    <label for="course">Difficulty Level</label>
                    <select class="form-control"  name="difficulty_level" required>

                        <option value='Beginner'>Beginner</option>
                        <option value='Intermediate'>Intermediate</option>
                        <option value='Advance'>Advance</option>

                    </select>
                </div>
                <!-- <div class="form-group">
                    <label for="course">Course Category</label>
                    <select class="form-control" id="course" name="course" required>

                        <?php /*foreach($courses as $course){
                            echo "<option value='" . $course['course_code'] . "'>" . $course['course_code'] . "</option>";
                        }*/?>
                    </select>
                </div> -->
                <div class="form-group my-2">
                    <label for="">Course Thumbnail: </label>
                    <input type="file" class="form-control-file" id="file" name="thumbnail">
                </div>
                <button type="submit" class="btn btn-primary" name='add_course'>Add Course</button>


            </form>
        </div>


</section>

