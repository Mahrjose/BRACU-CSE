<?php 
    session_start();

    if(isset($_SESSION['username'])){
        header("Location: index.php");
    }


    include "./config/dbconnect.php";
    include "./config/classes/Users.php";
    $user = new User();

    

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
                                    <div class="card-header"><h3 class="text-center font-weight-light my-4">Login to your account</h3></div>
                                    <div class="card-body">


                                    <?php 
                                    
                                            // Check if the login form has been submitted
                                            if (isset($_POST['login'])) {
                                                // print_r($_POST);
                                                
                                                // Retrieve the username and password submitted by the user
                                                $error_message = '';
                                                
                                                if ($user->login($_POST)) {

                                                    // print_r($user);
                                                    echo($_SESSION['username']);

                                                    header('Location: index.php');
                                                    exit;
                                                } else {
                                                    $error_message = 'Invalid email or password';
                                                }

                                            }
                                    ?>
                                    

                                        <form action="login.php" method="POST">

                                            <?php echo $error_message; ?>
                                            
                                            
                                            <input class="form-control py-4 my-2" name="username"  type="text" placeholder="your username" />

                                            <!-- <input class="form-control py-4 my-2" name="email"  type="email" placeholder="example@company.com" /> -->

                                            <input class="form-control py-4 my-2" name="password"  type="password" placeholder="Password" />


                                            <div class="custom-control custom-checkbox">
                                                <input class="custom-control-input" id="rememberPasswordCheck" type="checkbox" />
                                                <label class="custom-control-label" for="rememberPasswordCheck">Remember password</label>
                                            </div>

                                            <div class="form-group d-flex align-items-center justify-content-between mt-4 mb-0">
                                                <a class="small" href="password.html">Forgot Password?</a>
                                                <input type="submit" class="btn btn-primary" name="login" value="Login" >
                                            </div>
                                        </form>

                                    </div>
                                    <div class="card-footer text-center">
                                        <div class="small">Don't have an account? <a href="sign-up.php">Sign Up</a></div>
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

        
    </body>
</html>
