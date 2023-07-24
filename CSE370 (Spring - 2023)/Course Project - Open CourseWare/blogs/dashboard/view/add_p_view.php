<?php 
    $cat_name = $obj->display_category();
    if(isset($_POST['add_post'])){

        $post_data = $_POST;
        $msg = $obj-> add_post($post_data);
    }

?>

<h2>Add Your Post</h2>
<?php if (isset($msg)){echo $msg;} ?>

<form action="" method="POST" enctype="multipart/form-data">
    <div class="form-group">
        <label class="mb-1" for="post_title">Title</label>
        <input class="form-control py-4" name="post_title" id="post_title" type="text" />
    </div>
    <div class="form-group">
        <label class="mb-1" for="post_content">Post Content</label>
        <textarea class="form-control py-4" name="post_content" id="post_content" cols="30" rows="10"></textarea>
        
    </div>
    <div class="form-group">
        <label class="mb-1" for="post_img">Thumbnail</label></br>
        <input class="py-4" name="post_img" id="post_img" type="file" />
    </div>
    <div class="form-group">
        <label class="mb-1" for="post_category">Select Post Category</label>
        <select class="form-control" name="category" id="post_category">
        <?php while($cat=mysqli_fetch_assoc($cat_name)){ ?>
            
            <option value="<?php echo $cat["ctg"]; ?>"><?php echo $cat["ctg"]; ?></option>
    <?php } ?>

        </select>
    </div>

    <div class="form-group">
        <label class="mb-1" for="post_status">Post Status</label>
        <select  class="form-control" name="post_status" id="post_status">
            <option value="Publish">Publish Now</option>
            <option value="Draft">Save as Draft</option>
        </select>
    </div>

    <input type="submit" class="form-control btn-block btn-primary" name="add_post" value="Add Post" >
                                            

</form>