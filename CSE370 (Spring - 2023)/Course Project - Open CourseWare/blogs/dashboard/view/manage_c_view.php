<?php 
    $cat_data=$obj->display_category();
    
    if (isset($_GET["status"])){
        if ($_GET["status"]=="delete"){
            $del_id=$_GET["id"];
            $msg= $obj->delete_category($del_id);
        }
    }
?>



<h2>Manage  Catagory View</h2>
<table class="table">
    <thead>
        <tr>
            <th>ID</th>
            <th>Category Title</th>
            <th>Category Description</th>
            <th>Acrion</th>
        </tr>
    </thead>
    <tbody>  
        <?php while($cat=mysqli_fetch_assoc($cat_data)){ ?>
        <tr>
        <td><?php echo $cat["cat_id"]; ?>       </td>
        <td><?php echo $cat["cat_name"]; ?></td>
        <td> <?php echo $cat["cat_des"]; ?></td>
        <td><a href="?status=delete&&id=<?php echo $cat["cat_id"]; ?>" class="btn btn-danger">Delete</a></td>
        </tr>
        <?php } ?>
        
    </tbody>
</table>