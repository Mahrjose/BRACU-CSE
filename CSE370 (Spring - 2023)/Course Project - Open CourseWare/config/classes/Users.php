<?php 

require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/dbconnect.php';


// require_once './config/dbconnect.php';

class User extends Dbconnect {
    private $conn;

    public function __construct() {
        $this->conn = $this->getConnection();
    }


    // login
    public function login($data){

        $username = $data['username'];
        $password = md5($data['password']);

        $stmt = $this->conn->prepare("SELECT * FROM users WHERE username = '$username' AND password = '$password'");

        $stmt->execute();
        $user = $stmt->fetch();
        
        if (!$user) {
            return false;
        }

        // if (!password_verify($password, $user['password'])) {
        //     return false;
        // }

        $_SESSION['username'] = $user['username'];
        $_SESSION['email'] = $user['email'];
        $_SESSION['authority_level']  = $user['authority_level'];

        return true;
    }



    // login
    public function adminLogin($data){

        $username = $data['username'];
        $password = md5($data['password']);

        $stmt = $this->conn->prepare("SELECT * FROM users WHERE username = '$username' AND password = '$password' AND authority_level = 'ADMIN'");

        $stmt->execute();
        $user = $stmt->fetch();
        
        if (!$user) {
            return false;
        }
        else{
            $_SESSION['username'] = $user['username'];
            $_SESSION['email'] = $user['email'];
            $_SESSION['admin']  = $user['username'];
            $_SESSION['authority_level']  = $user['authority_level'];
    
            return true;
        }

        // if (!password_verify($password, $user['password'])) {
        //     return false;
        // }
    }






    public function getAllUsers() {
        $stmt = $this->conn->prepare("SELECT * FROM users");

        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getUsersBy($param) {
        $stmt = $this->conn->prepare("SELECT * FROM users WHERE username = '$param'");

        $stmt->execute();
        return $stmt->fetch();
    }

    public function enrolledCourses($username, $course_code = null) {
        if($course_code!=null){
            $stmt = $this->conn->prepare("SELECT courses.*, paymentInfo.username, paymentInfo.trx_id FROM courses INNER JOIN paymentInfo ON courses.course_code = paymentInfo.course_code WHERE paymentInfo.username = '$username' AND paymentInfo.course_code = '$course_code'");
        }
        else{
            $stmt = $this->conn->prepare("SELECT courses.*, paymentInfo.username, paymentInfo.trx_id FROM courses INNER JOIN paymentInfo ON courses.course_code = paymentInfo.course_code WHERE paymentInfo.username = '$username'");
        }

        // $stmt = $this->conn->prepare("SELECT courses.*, paymentInfo.username, paymentInfo.trx_id FROM courses INNER JOIN paymentInfo ON courses.course_code = paymentInfo.course_code WHERE paymentInfo.username = '$username'");

        $stmt->execute();
        return $stmt->fetchAll();
    }



    public function updateUser($data){
        $username = $data['username'];
        $first_name = $data['first_name'];
        $last_name = $data['last_name'];
        $email = $data['email'];

        if(!isset($data['authority_level'])){
            $stmt = $this->conn->prepare("UPDATE users SET first_name = '$first_name', last_name = '$last_name', email = '$email' WHERE username = '$username'");
        }

        else{
            $authority_level = $data['authority_level'];
            $stmt = $this->conn->prepare("UPDATE users SET first_name = '$first_name', last_name = '$last_name', email = '$email', authority_level = '$authority_level' WHERE username = '$username'");
        }



        $stmt->execute();
        
        if($stmt->rowCount() > 0){
            return true;
        }
        else{
            return false;
        }
    }
    



    public function getAllBlogs(){
        $stmt = $this->conn->prepare("SELECT * FROM blogs");

        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getRecentBlogs(){
        $stmt = $this->conn->prepare("SELECT * FROM blogs ORDER BY publish DESC LIMIT 4");

        $stmt->execute();
        return $stmt->fetchAll();
    }


}



?>
