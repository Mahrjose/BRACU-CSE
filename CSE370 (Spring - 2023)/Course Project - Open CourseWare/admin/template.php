<?php 

    session_start();
    if(!isset($_SESSION["admin"])){
        header("location: login.php");
    }


    require_once "../config/dbconnect.php";
    require_once "../config/classes/Update.php";
    require_once "../config/classes/Users.php";
    require_once "../config/classes/Insert.php";
    require_once "../config/classes/Courses.php";
    



?>



<?php include_once("include/head.php") ?>
    <body class="sb-nav-fixed">
        
    <!-- This is for Top Navigation Bar -->
    <?php include_once("include/topnav.php") ?>
        <div id="layoutSidenav">

        <!-- This is for Side Navigation Bar -->
        <?php include_once("include/sidenav.php") ?>   
        
        
        <div id="layoutSidenav_content">
            <main>
                <div class="container-fluid">
                    <?php 
                    

                    if(isset($view)){
                        switch($view){


                            case "dashboard":
                                include("view/dashboard_view.php");
                                break;
                            
                            case "edit_course":
                                include("view/edit-course-view.php");
                                break;
                            case "add_course":
                                    include("view/add-course-view.php");
                                    break;
                            case "all_course":
                                include("view/all-course-view.php");
                                break;
                            case "enrollment":
                                include("view/manage-enrollment-view.php");
                                break;

                            case "manage_users":
                                include("view/manage-user-view.php");
                                break;

                            case "edit_user":
                                include("view/edit-user-view.php");
                                break;


                            case 'add_tutorial':
                                include("view/add-tutorial-view.php");
                                break;
                            default:
                                include("view/dashboard_view.php");
                        }
                    }
                    
                    
                    ?>
                </div>
            </main>

            <!-- This is for Side Navigation Bar -->
            <?php include_once("include/footer.php") ?>
        </div>
        </div>
        <?php include_once("include/script.php") ?>
        
    </body>
</html>
