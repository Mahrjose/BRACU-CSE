
<?php

session_start();
// require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/dbconnect.php';
include "./config/dbconnect.php";
include  "./config/classes/Insert.php";
include  "./config/classes/Courses.php";
include  "./config/classes/Users.php";

$u = new User();


// echo $_SESSION['username'];



include "./templates/header.php";

?>

<title>User</title>
</head>

<body>

    <!-- Navbar -->
    <?php 
        include "./templates/navigation.php" ;

        

        if(!isset($_SESSION['username'])){
            // header("Location: login.php");
            echo  "<div class='container'><h3>You are not logged in! Please login to view this page</h3> <br>";
            echo  "<a href='login.php'>Login</a></div>";
        }


        else{    
            if(isset($_GET['username'])){

                $username = $_GET['username'];
    
                $user_info = $u->getUsersBy($username);
                
                if($_SESSION['username'] == $username){
                    include  "loggedUser.php";
                }
                else{
                    include "otherUser.php";
                }
            }
            else{
                
                $user_info = $u->GetUsersBy($_SESSION['username']);
                include "loggedUser.php";
                
            }
        }




    
    
    ?>



    <!-- footer -->
    <?php include "./templates/footer.php" ?>
        
</body>
<html>

