<?php 
    include("class/function.php");
    $obj= new admin_blog();
    session_start();

    if (!isset($_SESSION['username'])){
        header("location: /OCW/login.php");
    }

    if(isset($_GET["adminlogout"])){
        if ($_GET["adminlogout"]=="logout"){
            $obj->admin_logout();
        }

    }
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
                    <?php if(isset($view)){
                        if ($view=="dashboard"){
                            include("view/dashboard_view.php");
                        }elseif($view=="add_catagory"){
                            include("view/add_c_view.php");
                        }elseif($view=="add_post"){
                            include("view/add_p_view.php");
                        }elseif($view=="manage_catagory"){
                            include("view/manage_c_view.php");
                        }elseif($view=="manage_post"){
                            include("view/manage_p_view.php");
                        }elseif($view=="edit_image"){
                            include("view/edit_image_view.php");
                        }elseif($view=="edit_post"){
                            include("view/edit_post_view.php");
                    }}
                    
                    
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
