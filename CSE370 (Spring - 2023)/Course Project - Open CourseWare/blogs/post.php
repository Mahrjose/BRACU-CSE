<?php include_once("head.php") ?>
<?php include_once("preloader.php") ?>
<?php include_once("header.php") ?>

    <?php 

        include "./dashboard/class/function.php";
        $obj= new admin_blog();
        if(isset($_GET['id'])){
            $post_id = $_GET['id'];
            $posts = $obj->display_post_public($post_id);
            $postdata = mysqli_fetch_assoc($posts);
        }

        // COMMENT  
        if(isset($_POST['add_comment']) && isset($_POST['comment_text'])){
            
            $msg=$obj->AddComment($_POST);
        }
        
     ?>



    <div class="container blog-posts">
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




            <!-- Comments starts -->
            <?php 
            
            $comments = $obj->GetComments($post_id);

            $commentCount = 0;
            
            ?>
            

            <div class="col-sm-12">
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
                        </li>
                       <?php } ?>
                       
                      </ul>
                    </div>
                  </div>
                </div>

                <!-- add comment -->  


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

            <!-- Comments Ends -->
        
        
        </div>
        </div>
    </div>

</div>



<?php include_once("footer.php") ?>
<?php include_once("script.php") ?>