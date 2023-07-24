<?php 


    $posts = $obj->display_post();

    if (isset($_GET["status"])){
        if ($_GET["status"]=="delete"){
            $del_id=$_GET["id"];
            $msg= $obj->delete_post($del_id);
        }
}

?>


<h2>Manage Post View</h2>
<div class="table-resposive">
    <table class="table">
        <thead>
            <tr>
                <th>Title</th>
                <th>Thumbnail</th>
                <th>Author</th>
                <th>Category</th>
                <th>Status</th>
                <th>Published at</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php while ($postdata = mysqli_fetch_assoc($posts)) { ?>
                <tr>

                    <td>
                        <?php echo $postdata["post_title"] ?>
                    </td>

                    <td><img height="100px" src="<?php echo '../../blogs/upload/'.$postdata['post_img']; ?>">
                    <br><a class="btn btn-warning btn-sm"  href="edit_image.php?status=editimg&&id=<?php echo $postdata["post_id"] ?>">Change</a>
                    </td>
                    
                    
                    <td>
                        <?php echo $postdata["author"] ?>
                    </td>
                    <td>
                        <?php echo $postdata["category"] ?>
                    </td>


                    <td>
                        <?php echo $postdata["status"] ?>
                    </td>
                    <td>
                        <?php echo $postdata["publish"] ?>
                    </td>
                    <td>
                        <a class="btn btn-primary" href="edit_post.php?status=editpost&&id=<?php echo $postdata["post_id"] ?>">Edit</a>
                        <a href="?status=delete&&id=<?php echo $postdata["post_id"]; ?>" class="btn btn-danger">Delete</a>
                    </td>
                </tr>
            </tbody>
        <?php } ?>

    </table>
</div>