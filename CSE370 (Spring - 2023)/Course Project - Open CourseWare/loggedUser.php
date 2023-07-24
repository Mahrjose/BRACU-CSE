


<!-- content starts -->
<section class="my-3">
    <div class="container justify-content-center bg-success-subtle shadow rounded p-3">
        <h4>User Profile <span style="font-size:small"><a href="#edit" data-bs-toggle="modal" data-bs-target="#editProfile"><i class="fas fa-user-pen fa-fw"></i>Edit</a></span></h4>
        <p>Name: <?php echo htmlspecialchars($user_info['first_name']); ?>
        </p>
        <p>username: <?php echo htmlspecialchars($user_info['username']); ?>
        </p>
        <p>Email: <?= $user_info['email']?></p>

    </div>


    <!--Edit Modal -->
    <div class="modal fade" id="editProfile" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="editProfileLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="#">Update Information</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div>
                        <?php 
                        // edit user (from logged user)
                        if(isset($_POST['submit'])){
                            $_POST['username'] = $_SESSION['username'];
                            if($u->updateUser($_POST)){
                                echo "User updated successfully";
                                header('Location: user.php');
                            }
                            else{
                                echo "User not updated";
                                header('Location: user.php');
                            }
                        }
                        ?>
                        

                        <form action="user.php" method="POST">
                            <label for="">First Name</label>
                            <input class="form-control py-2 my-2" type="text" name="first_name" id="" value="<?= $user_info['first_name'] ?>">
                            <label for="">Last Name</label>
                            <input class="form-control py-2 my-2" type="text" name="last_name" value="<?= $user_info['last_name'] ?>">
                            <label for="">Email</label>
                            <input class="form-control py-2 my-2" type="email" name= "email" value="<?= $user_info['email'] ?>">
                            <button class="form-control btn btn-secondary" type="submit" name="submit">Save</button> 
                        </form>
                    </div>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    
                </div>
            </div>
        </div>
    </div>

</section>