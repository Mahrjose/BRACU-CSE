<?php $posts = $obj->display_post_public() ?>
  
  <!-- Banner Starts Here -->
  <div class="main-banner header-text">
    <div class="container-fluid">
      <div class="owl-banner owl-carousel">
      <?php foreach($posts as $postdata) { ?>
        <div class="item">
        <img height="400px"  weight="400px" src="<?php echo './upload/'.$postdata['post_img']; ?>">
          <div class="item-content">
            <div class="main-content">
              <div class="meta-category">
                <span><?php echo $postdata["category"] ?></span>
              </div>
              <a href="post.php?id=<?php echo $postdata['post_id']?>"> <h4><?php echo $postdata["post_title"] ?></h4></a>
              <ul class="post-info">
                <li><a href="#"><?php echo $postdata["author"] ?></a></li>
                <li><a href="#"><?php echo $postdata["publish"] ?></a></li>
                
              </ul>
            </div>
          </div>
        </div>
      <?php } ?>
      
      </div>
    </div>
  </div>
  <!-- Banner Ends Here -->
