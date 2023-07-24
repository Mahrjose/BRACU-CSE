<?php $posts = $obj->display_post_public() ?>

        <div class="col-lg-12">
                <div class="sidebar-item recent-posts">
                    <div class="sidebar-heading">
                        <h2>Recent Posts</h2>
                    </div>
                    <div class="content">

                        <ul>
                            <?php foreach ($posts as $post) { ?>
                                    <li><a href="post-details.php?id=<?php echo $post['post_id']?>">
                                            <h5><?php echo $post["post_title"] ?></h5>
                                            <span><?php echo $post["publish"] ?></span>
                                        </a></li>
                                        
                            <?php } ?>
                        </ul>
                        
                    </div>
                </div>
            </div>

         