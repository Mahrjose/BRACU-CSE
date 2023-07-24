<?php $posts = $obj->display_post_public() ?>





<div class="col-lg-8">
  <div class="all-blog-posts">
    <div class="row">

      <?php foreach($posts as $postdata) { ?>


        <div class="col-lg-12">
          <div class="blog-post">
            <div class="blog-thumb">
            <img src="<?php echo './upload/'.$postdata['post_img']; ?>">
            </div>
            <div class="down-content">
              <span>
              <a href="post-details.php?id=<?php echo $postdata['post_id']?>"><?php echo $postdata["post_title"] ?></a>
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

      <?php } ?>

    </div>
  </div>
</div>