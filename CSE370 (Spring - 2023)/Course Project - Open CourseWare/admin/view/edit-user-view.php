
<?php 


$u = new User();
if(isset($_GET['username'])){
    $user_info = $u->getUsersBy($_GET['username']);
}
// else{
//     header('Location: user.php');
// }

?>



<div class="container">
    <div class="my-3">

        <h4 class="text-center">Update User</h4>
        <?php 
        // edit user (from logged user)
        if(isset($_POST['submit'])){
            if($u->updateUser($_POST)){
                echo "User updated successfully";
                header('Location: manage-user.php');
            }
            else{
                echo "User not updated";
                // header('Location: user.php');
            }
        }
        ?>
        

        <form action="" method="POST">

            <input type="hidden" name="username" value="<?=$user_info['username']?>">
            <label for="">First Name</label>
            <input class="form-control py-2 my-2" type="text" name="first_name" id="" value="<?= $user_info['first_name'] ?>">
            <label for="">Last Name</label>
            <input class="form-control py-2 my-2" type="text" name="last_name" value="<?= $user_info['last_name'] ?>">
            <label for="">Email</label>
            <input class="form-control py-2 my-2" type="email" name= "email" value="<?= $user_info['email'] ?>">
            <label for="">Authority Level</label>
            <input class="form-control py-2 my-2" type="text" name= "authority_level" value="<?= $user_info['authority_level'] ?>">
            <button class="form-control btn btn-secondary" type="submit" name="submit">Save</button> 
        </form>
    </div>
</div>