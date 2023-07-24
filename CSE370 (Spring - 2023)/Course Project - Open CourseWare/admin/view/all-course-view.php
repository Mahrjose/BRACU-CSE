<?php 

$c = new Courses();

$courses = $c->getAllCourses();

?>


<section>

    <h4>All couress</h4>
    <table class="table container bg-warning-subtle shadow my-3 rounded" id="dataTable">
        <thead>
            <tr>
                <th>Course Code</th>
                <th>Course Title</th>
                <th>Category</th>
                <th>Course Type</th>
                <th>Price</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach($courses as $course){ ?>

            <tr>
                <td><?php echo htmlspecialchars($course['course_code']); ?></td>
                <td><?php echo htmlspecialchars($course['course_title']); ?></td>
                <td><?php echo htmlspecialchars($course['course_type']); ?></td>
                <td><?php echo htmlspecialchars($course['price_type']); ?></td>
                <td><?php echo htmlspecialchars($course['course_price']); ?></td>

                <td>
                    <a class="btn btn-info" href="edit-course.php?course_code=<?= $course['course_code']?>">Edit</a>
                    <a class="btn btn-danger" href="delete-course.php?course_code=<?= $course['course_code']?>">Delete</a>
                </td>
            </tr>

            <?php } ?>

        </tbody>
    </table>

</section>
