<?php 
    session_start();

    require_once "./config/dbconnect.php";
    require_once "./config/classes/Insert.php";

    $obj = new Insert();
    
    if(isset($_POST["signup"])){

        if ($_POST["password"] == $_POST["confirm_password"]){
            $data = ['username' => $_POST['username'], 'first_name' => $_POST['first_name'] ,'last_name' => $_POST['last_name'] , 'email' => $_POST['email'], 'password' => md5($_POST['password']), 'authority_level' => 'USER'];

            // print_r($data);
            if ($obj->insertIntoUsers($data)) {
                $_SESSION["username"] = $data["username"];
                header("Location: user.php");
            } else {
                echo "Error";
            }

            // print_r($_POST);
        }
        
    }


    if(isset($_SESSION["username"])){
        $logged_user=$_SESSION["username"];
        header("Location: user.php");
    }


?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>OCW | Sign Up</title>
        <link rel="stylesheet" href="./assets/css/bootstrap2.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/js/all.min.js" crossorigin="anonymous"></script>
    </head>




    <body class="bg-primary">
        <div id="layoutAuthentication">
            <div id="layoutAuthentication_content">
                <main>
                    <div class="container">
                        <div class="row justify-content-center">
                            <div class="col-lg-6 my-3">
                                <div class="card shadow-lg border-0 rounded-lg mt-5">
                                    <div class="card-header"><h3 class="text-center font-weight-light my-4">Create Account</h3></div>
                                    <div class="card-body">

                                        <form action="sign-up.php" method="POST">

                                            
                                            <input class="form-control py-2 my-2" name="username"  type="text" placeholder="@username" />
                                    
                                            <input class="form-control py-2 my-2" name="first_name"  type="text" placeholder="First Name" />

                                            <input class="form-control py-2 my-2" name="last_name"  type="text" placeholder="Last Name" />

                                            <input class="form-control py-2 my-2" name="email"  type="email" placeholder="example@company.com" />

                                            <input class="form-control py-2 my-2" name="password"  type="password" placeholder="New Password" />

                                            <input class="form-control py-2 my-2" name="confirm_password"  type="password" placeholder="Retype password" />

                                            <div class="custom-control custom-checkbox">
                                                <input class="custom-control-input" id="rememberPasswordCheck" type="checkbox" />
                                                <label class="custom-control-label" for="rememberPasswordCheck">Remember password</label>
                                            </div>

                                            <div class="form-group d-flex align-items-center justify-content-between mt-4 mb-0">
                                                <a class="small" href="#">Forgot Password?</a>
                                                <input type="submit" class="btn btn-primary" name="signup" value="Sign Up" >
                                            </div>
                                        </form>

                                    </div>
                                    <div class="card-footer text-center">
                                        <div class="small">Already have an account? <a href="login.php">Log in!</a></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
            <div id="layoutAuthentication_footer">
                <footer class="py-4 bg-light mt-auto">
                    <div class="container-fluid">
                        <div class="d-flex align-items-center justify-content-between small">
                            <div class="text-muted">Copyright &copy; Your Website 2020</div>
                            <div>
                                <a href="#">Privacy Policy</a>
                                &middot;
                                <a href="#">Terms &amp; Conditions</a>
                            </div>
                        </div>
                    </div>
                </footer>
            </div>
        </div>
        <?php include_once("./blogs/admin/include/script.php") ?>
        
    </body>
</html>
