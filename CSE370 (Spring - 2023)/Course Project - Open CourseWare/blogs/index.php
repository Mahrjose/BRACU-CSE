<?php 
    include("dashboard/class/function.php");
    $obj= new admin_blog();

    $get_cat=$obj->display_category();

?>



<?php include_once("head.php") ?>
<body>
    <?php include_once("preloader.php") ?>
    <?php include_once("header.php") ?>
    
    <!-- Page Content -->
    <?php include_once("banner.php") ?>
    <section class="blog-posts">
        <div class="container">
            <div class="row">
                <?php include_once("blog_post.php") ?>
                <?php include_once("sidebar.php") ?>
            </div>
        </div>
    </section>

    <?php include_once("footer.php") ?>
    <?php include_once("script.php") ?>