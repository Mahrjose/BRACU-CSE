
<?php 



    include "./config/dbconnect.php";
    include "./config/classes/Courses.php";

    $c = new Courses();

    if (isset($_GET['course_code'])) {
        $course_code = $_GET['course_code'];

        // fetch tutorials
        $tutorials = $c->getMaterialsBy($course_code, 'tutorial'); 



        echo ($tutorials);
    }


    include "./templates/header.php"

?>


<title>Tutorials</title>
<link rel="stylesheet" href="./assets/css/watch.css">

</head>
<body>
    
<?php include 'templates/navigation.php' ?>
    
    <section class="container">

        <div class="course-container">
            <div class="main-video">
                <iframe id="video-player"
                    src="<?php echo $tutorials[0]['tutorial_url']; ?>"
                    title="Course" frameborder="8" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen></iframe>
            </div>

            <!-- tutorial list -->
            <div class="courses">
                <div class="playlist">
                    <div>
                        <h2>Tutorials</h2>
                        <ul>
                            <?php foreach($tutorials as $tut){ ?>                   
                                <li><button class="btn" onclick="document.getElementById('video-player').src='<?php echo htmlspecialchars($tut['tutorial_url']);?>'"><?php echo htmlspecialchars($tut['material_title']); ?>
                                </button>
                                </li>
                            <?php } ?>
                        </ul>
                    </div>
                </div>
            </div>


            <!-- Button trigger modal -->
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#tutorialModal">
            All Tutorials
            </button>

            <!-- Modal -->
            <div class="modal fade" id="tutorialModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="tutorialModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-scrollable">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="staticBackdropLabel">Tutorials</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div>
                            <ul class="unstyled">
                                <?php foreach($tutorials as $tut){ ?>                   
                                    <li><button class="btn" onclick="document.getElementById('video-player').src='<?php echo htmlspecialchars($tut['tutorial_url']);?>'" data-bs-dismiss="modal"><?php echo htmlspecialchars($tut['material_title']); ?>
                                    </button>
                                    </li>
                                    
                                <?php } ?>
                                
                            </ul>
                        </div>
                    </div>

                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary">Understood</button>
                    </div>
                    </div>
                </div>
            </div>

        </div>
    </section>


    <?php include "./templates/footer.php" ?>
    
</body>

</html>