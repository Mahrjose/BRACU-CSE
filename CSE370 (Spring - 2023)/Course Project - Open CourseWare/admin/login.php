<?php 

    session_start();
    if(isset($_SESSION["admin"])){
        header("location: index.php");
    }
    require "../config/dbconnect.php";
    require_once "../config/classes/Users.php";
    require_once "../config/classes/Update.php";

    $obj=new User();
    
    if(isset($_POST["login"])){
        if($obj->adminLogin($_POST)){
            header("Location: index.php");
        }
        else{
            echo "Invalid username or password";
        }
    }



?>




<?php include_once("include/head.php") ?>

    <body class="bg-primary">
        <div id="layoutAuthentication">
            <div id="layoutAuthentication_content">
                <main>
                    <div class="container">
                        <div class="row justify-content-center">
                            <div class="col-lg-5">
                                <div class="card shadow-lg border-0 rounded-lg mt-5">
                                    <div class="card-header"><h3 class="text-center font-weight-light my-4">Login</h3></div>
                                    <div class="card-body">
                                        <form action="login.php" method="POST">
                                            <div class="form-group">
                                                <label class="small mb-1"  for="inputEmailAddress">Admin username</label>
                                                <input class="form-control py-4" name="username" id="inputEmailAddress" type="text" placeholder="i.e david" />
                                            </div>
                                            <div class="form-group">
                                                <label class="small mb-1"  for="inputPassword">Admin password</label>
                                                <input class="form-control py-4" id="inputPassword" name="password" type="password" placeholder="Enter password" />
                                            </div>
                                            <div class="form-group">
                                                <div class="custom-control custom-checkbox">
                                                    <input class="custom-control-input" id="rememberPasswordCheck" type="checkbox" />
                                                    <label class="custom-control-label" for="rememberPasswordCheck">Remember password</label>
                                                </div>
                                            </div>
                                            <div class="form-group d-flex align-items-center justify-content-between mt-4 mb-0">
                                                <a class="small" href="password.html">Forgot Password?</a>
                                                <input type="submit" class="btn btn-primary" name="login" value="Login" >
                                            </div>
                                        </form>
                                    </div>
                                    <div class="card-footer text-center">
                                        <div class="small"><a href="../sign-up.php">Need an account? Sign up!</a></div>
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
        <?php include_once("include/script.php") ?>
        
    </body>
</html>
