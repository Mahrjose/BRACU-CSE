<?php

session_start();

if (isset($_SESSION['username'])) {
    echo "Welcome, " . $_SESSION['username'];
} else {
    echo "You are not logged in";
}


?>
