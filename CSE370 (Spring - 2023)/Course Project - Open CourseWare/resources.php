<?php 


include "./config/dbconnect.php" ;
include "./config/classes/Courses.php" ;
$c = new Courses();

    if (isset($_GET['course_code'])){
        $course_code = $_GET['course_code'];

        $resources = $c->getMaterialsBy($course_code, 'Resource');
    }
    else{
        $resources = $c->getAllResources();
    }

include "./templates/header.php" 

?>



<title>OCW | Resources</title>
</head>

<body>

    <?php include "./templates/navigation.php" ?>


    <section class="container">
        <h3 class="text-center">Resources (PDF, Docs, Images, Previous content)</h3>

        <table class="table container bg-warning-subtle shadow my-3 rounded" id="dataTable">
            <thead>
                <tr>
                    <th scope="col">File Title</th>
                    <th scope="col">Course</th>
                    <th scope="col">Uploaded By</th>
                    <th scope="col">Download</th>
                </tr>
            </thead>
            <tbody class="table-hover">
                <?php foreach($resources as $resource){ ?>

                <tr>
                    <td><?php echo htmlspecialchars($resource['material_title']); ?></td>
                    <td><?php echo htmlspecialchars($resource['course_code']); ?></td>
                    <td>@<?php echo htmlspecialchars($resource['uploader']); ?></td>
                    <td><a class="btn btn-info" href="">Download</a></td>
                </tr>

                <?php } ?>

            </tbody>
        </table>
    </section>


<?php 
    include "./templates/footer.php";
    include "./templates/scripts.php"; 
?>
    
    

</body>

</html>