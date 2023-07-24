<?php 
if(isset($_GET['status'])){
    if($_GET['status']=='editpost'){
        $id=$_GET['id'];
        // echo $id;
        $previous_post_data=$obj->change_single_post($id);
    }
}

if (isset($_POST['update_post'])){
    $msg=$obj->update_post($_POST);
    echo $msg;
}


?>

<div class="shadow m-5 p-5">
    
    <form action="" method="POST"  class="form" enctype="multipart/form-data">

    <div class="form-group">
        <input type="hidden" name="edit_post_id" value="<?php  echo $id ?>">
        <label class="mb-1" for="change_title">Change Title</label></br>
        <input value="<?php echo $previous_post_data["post_title"] ?>" class="form-control py-4" name="change_title" id="change_title" type="text" />
    </div>
    <div class="form-group">
        <label class="mb-1" for="change_content">Change Content</label></br>
        <textarea  class="form-control py-4" name="change_content" id="change_content" cols="30" rows="8"><?php echo $previous_post_data["post_content"] ?></textarea>
    </div>

    <div class="form-group">
        <label class="mb-1" for="change_img">Change Image</label></br>
        <input class="py-4" name="change_img" id="change_img" type="file" />
        <span>Current Image: <?php echo $previous_post_data["post_img"]; ?></span>
    </div>

    <div class="form-group">
        <label class="mb-1" for="change_post_status">Post Status</label>
        <select  class="form-control" name="change_post_status" id="change_post_status">
            <option value="Publish">Publish Now</option>
            <option value="Draft">Save as Draft</option>
        </select>
    </div>

    <input type="submit" class="form-control btn-block btn-primary" name="update_post" value="Update Your Post" >
     </form>


</div>