<?php 
if(isset($_GET['status'])){
    if($_GET['status']=='editimg'){
        $id=$_GET['id'];
    }
}

if (isset($_POST['change_img_btn'])){
    $msg=$obj->edit_image($_POST);
}
?>





<div class="shadow m-5 p-5">
    <?php if(isset($msg)){
        echo $msg;
    } ?>
    
    <form action="" method="post" enctype="multipart/form-data" class="form">

    <div class="form-group">
        <input type="text" name="editimg_id" value="<?php  echo $id ?>">
        <label class="mb-1" for="change_img">Change Image</label></br>
        <input class="py-4" name="change_img" id="change_img" type="file" />
    </div>
    <input type="submit" value="Chnage Image"  name="change_img_btn" class="btn btn-primary">
    </form>

</div>