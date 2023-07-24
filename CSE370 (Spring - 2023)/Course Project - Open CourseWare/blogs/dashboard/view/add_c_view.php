<?php 
    if(isset($_POST["add_cat"])){
        $return_msg=$obj->add_category($_POST);
    }    
    if(isset($return_msg)){
        echo $return_msg;
    }
?>




<form action="" method="POST">
<div class="form-group">
    <label class="mb-1" for="cat_name">Category Name</label>
    <input class="form-control py-4" name="cat_name" id="cat_name" type="text" placeholder="Enter Category Name" />
</div>
<input type="submit" class="form-control py-4 btn-block btn-primary" name="add_cat" value="Add Category" >
                                            

</form>
