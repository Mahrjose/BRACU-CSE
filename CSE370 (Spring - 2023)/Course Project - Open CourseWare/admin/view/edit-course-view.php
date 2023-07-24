<?php 


$c = new Courses();
$course = $c->getCoursesBy($_GET['course_code']);
$course = $course[0];



if(isset($_POST['submit'])){

    if($c->updateCourse($_POST)){
        echo "Course Updated Successfully";
    }
    else{
        echo "Error: " . $error[2];
    }
}



?>

<div class="container col-lg-6 shadow rounded bg-warning-subtle my-3 p-4">


            <h4 class="text-center">Update Course</h4>

            <?php 
            
            
            ?>
            
            <form action="" method="POST" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="title">Course Code</label>
                    <input type="text" class="form-control"  name="course_code" placeholder="i.e CSE370" required value="<?= $course['course_code']?>">
                </div>
                <div class="form-group">
                    <label for="title">Course Title</label>
                    <input type="text" class="form-control"  name="course_title" placeholder="i.e Database Systems" required value="<?= $course['course_title']?>"> 
                </div>
                <div class="form-group">
                    <label for="floatingTextarea">Description</label>
                    <textarea class="form-control" style="height: 100px" placeholder="CSE370 is an amazing course ..." id="floatingTextarea" name="course_description" ><?= $course['course_description']?></textarea>
                    
                </div>
                <div class="form-group">
                    <label for="course">Price Type</label>
                    <select class="form-control"  name="price_type" required value="<?= $course['price_type']?>">

                        <option value='Free'>Free</option>
                        <option value='Paid'>Paid</option>

                    </select>
                </div>
                <div class="form-group">
                    <label for="title">Price</label>
                    <input type="text" class="form-control"  name="course_price" placeholder="0.0" required value="<?= $course['course_price']?>">
                </div>
                <div class="form-group">
                    <label for="course">Category</label>
                    <select class="form-control"  name="course_type" required value="<?= $course['course_type']?>">

                        <option value='Academic'>Academic</option>
                        <option value='Skill'>Skill</option>

                    </select>
                </div>
                <div class="form-group">
                    <label for="course">Difficulty Level</label>
                    <select class="form-control"  name="difficulty_level" required value="<?= $course['difficulty_level']?>">

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
                    <input type="file" class="form-control-file" id="file" name="thumbnail" value="<?= $course['thumbnail']?>">
                    <span>Current Image: <?php echo $course["thumbnail"]; ?></span>
                </div>
                <button type="submit" class="btn btn-primary" name='submit'>Update</button>


            </form>
        </div>