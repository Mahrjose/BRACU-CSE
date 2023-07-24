
  


<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i&display=swap" rel="stylesheet">

    <title>OCW Post Details</title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Additional CSS Files -->
    <link rel="stylesheet" href="assets/css/fontawesome.css">
    <link rel="stylesheet" href="assets/css/templatemo-stand-blog.css">
    <link rel="stylesheet" href="assets/css/owl.css">
  </head>

  <body>

    <!-- ***** Preloader Start ***** -->
    <div id="preloader">
        <div class="jumper">
            <div></div>
            <div></div>
            <div></div>
        </div>
    </div>  
    <!-- ***** Preloader End ***** -->

    <!-- Header -->
    <?php include "./header.php" ?>
    

    <!-- Page Content -->
    <!-- Banner Starts Here -->
    <div class="heading-page header-text">
      <section class="page-heading">
        <div class="container">
          <div class="row">
            <div class="col-lg-12">
              <div class="text-content">
                <h4>Post Details</h4>
                <h2>Single blog post</h2>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
    

  
 <?php 

include "./dashboard/class/function.php";
$obj= new admin_blog();
if(isset($_GET['id'])){
    $post_id = $_GET['id'];
    $posts = $obj->display_post_public($post_id);
    $postdata = mysqli_fetch_assoc($posts);
}

// Fetch Comments
     
$comments = $obj->GetComments($post_id);

$commentCount = 0;

$get_cat=$obj->display_category();


// COMMENT  
if(isset($_POST['add_comment']) && isset($_POST['comment_text'])){
    
    $msg=$obj->AddComment($_POST);
}

?>

<section class="blog-posts grid-system">
      <div class="container">
        <div class="row">
          <div class="col-lg-8">
            <div class="all-blog-posts">
              <div class="row">
                <div class="col-lg-12">
                <div class="blog-post">
                  <div class="blog-thumb">
                  <img class="img-fluid" src="<?php echo './upload/'.$postdata['post_img']; ?>">
                  </div>
                  <div class="down-content">
                      <span>
                      <a href="post.php?id=<?php echo $postdata['post_id']?>"><?php echo $postdata["post_title"] ?></a>
                      </span>

                      <ul class="post-info">
                      <li><a href="#">
                          <?php echo $postdata["author"] ?>
                          </a></li>
                      <li><a href="#">
                          <?php echo $postdata["publish"] ?>
                          </a></li>
                      </ul>
                      <p><?php echo $postdata["post_content"] ?> </p>
                      <div class="post-options">
                      <div class="row">
                          <div class="col-6">
                          <ul class="post-share">
                              <li><i class="fa fa-share-alt"></i></li>
                              <li><a href="#">Facebook</a>,</li>
                              <li><a href="#"> Twitter</a></li>
                          </ul>
                          </div>
                      </div>
                      </div>
                  
                  </div>
              </div>
   
                </div>
                <div class="col-lg-12">
                  <div class="sidebar-item comments">
                    <div class="sidebar-heading">
                      <h2><?php echo $commentCount
                      ?> comments</h2>
                    </div>
                    <div class="content">
                      <ul>
                        
                        <?php foreach($comments as $comment){ $commentCount++; ?>
                            
                        <li>
                          <div class="author-thumb">
                            <img src="assets/images/comment-author-01.jpg" alt="">
                          </div>
                          <div class="right-content">
                            <h4><?php echo $comment['author']. "<span>".Date($comment['comment_at'])."</span>" ?>
                            </h4>
                            <p><?php echo $comment['comment_text'] ;?>
                            </p>
                          </div>
                        </li><br>
                       <?php } ?>
                       
                      </ul>
                    </div>
                  </div>
                    
              </div>
                <div class="col-lg-12">
                  <div class="sidebar-item submit-comment">
                    <div class="sidebar-heading">
                      <h2>Your comment</h2>
                    </div>

                    <div class="content">
                      <form id="comment" action="" method="POST">
                        <div class="row">
                          <!-- <div class="col-md-12 col-sm-12">
                            <fieldset>
                              <input name="subject" type="text" id="subject" placeholder="Subject">
                            </fieldset>
                          </div> -->
                          <div class="col-lg-12">
                            <input type="hidden" name="post_id" value="<?php echo $post_id?>">
                            <input type="hidden" name="author" value="<?php echo 'rajo' ?>">
                            <fieldset>
                              <textarea name="comment_text" rows="6" id="message" placeholder="Add your comment" required=""></textarea>
                            </fieldset>
                          </div>
                          <div class="col-lg-12">
                            <fieldset>
                              <button type="submit" id="form-submit" class="main-button" name="add_comment">Comment</button>
                            </fieldset>
                          </div>
                        </div>
                      </form>
                    </div>
                  
                  </div>
                </div>
              </div>
            </div>
          
          </div>
          <div class="col-lg-4">
            <div class="sidebar">
              <div class="row">
                
              <?php include_once("searchbar.php") ?>

              
            <?php include_once("recent_post.php") ?>

            
            <?php include_once("category.php") ?>
                
                
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>



    
    <footer>
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <ul class="social-icons">
              <li><a href="#">Facebook</a></li>
              <li><a href="#">Twitter</a></li>
              <li><a href="#">Behance</a></li>
              <li><a href="#">Linkedin</a></li>
              <li><a href="#">Dribbble</a></li>
            </ul>
          </div>
          <div class="col-lg-12">
            <div class="copyright-text">
              <p>Copyright 2020 Stand Blog Co.
                    
                 | Design: <a rel="nofollow" href="https://templatemo.com" target="_parent">TemplateMo</a></p>
            </div>
          </div>
        </div>
      </div>
    </footer>


    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>


    <!-- Additional Scripts -->
    <script src="assets/js/custom.js"></script>
    <script src="assets/js/owl.js"></script>
    <script src="assets/js/slick.js"></script>
    <script src="assets/js/isotope.js"></script>
    <script src="assets/js/accordions.js"></script>


    <script language = "text/Javascript"> 
      cleared[0] = cleared[1] = cleared[2] = 0; //set a cleared flag for each field
      function clearField(t){                   //declaring the array outside of the
      if(! cleared[t.id]){                      // function makes it static and global
          cleared[t.id] = 1;  // you could use true and false, but that's more typing
          t.value='';         // with more chance of typos
          t.style.color='#fff';
          }
      }
    </script>


  </body>

</html>
