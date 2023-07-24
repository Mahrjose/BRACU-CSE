<?php 

require_once $_SERVER['DOCUMENT_ROOT'] . '/OCW/config/dbconnect.php';

// require_once './config/dbconnect.php';

class Courses extends Dbconnect {
    private $conn;

    public function __construct() {
        $this->conn = $this->getConnection();
    }

    public function getAllCourses() {
        $stmt = $this->conn->prepare("SELECT * FROM courses");

        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getCoursesBy($course_code) {
        $stmt = $this->conn->prepare("SELECT * FROM courses WHERE course_code = :course_code");

        $stmt->execute(['course_code' => $course_code]);
        return $stmt->fetchAll();
    }

    public function getLatestCourses() {
        $stmt = $this->conn->prepare("SELECT * FROM courses ORDER BY created_at DESC LIMIT 5");

        $stmt->execute();
        return $stmt->fetchAll();
    }


    public function getMaterialsBy($course_code, $material_type) {
        $stmt = $this->conn->prepare("SELECT * FROM materials WHERE course_code = :course_code AND material_type = :material_type");

        $stmt->execute(['course_code' => $course_code, 'material_type' => $material_type]);
        return $stmt->fetchAll();
    }



    public function getQuestionsBy($course_code) {
        $stmt = $this->conn->prepare("SELECT * FROM questions WHERE course_code = :course_code");

        $stmt->execute(['course_code' => $course_code]);
        return $stmt->fetchAll();
    }

    public function getAllQuestions() {
        $stmt = $this->conn->prepare("SELECT * FROM questions");

        $stmt->execute();
        return $stmt->fetchAll();
    }


    public function getQuestion($question_id){
        $stmt = $this->conn->prepare("SELECT * FROM questions WHERE question_id = :question_id");

        $stmt->execute(['question_id' => $question_id]);
        return $stmt->fetch();
    }


    public function getAnswers($question_id = null) {
        if($question_id == null){
            $stmt = $this->conn->prepare("SELECT * FROM answers");
        }else{
            $stmt = $this->conn->prepare("SELECT * FROM answers WHERE question_id = '$question_id'");
        }

        $stmt->execute();
        return $stmt->fetchAll();
    }




    public function getAllResources() {
        $stmt = $this->conn->prepare("SELECT * FROM materials  WHERE material_type = 'Resource'");

        $stmt->execute();
        return $stmt->fetchAll();
    }


    public function getPaymentInfo(){
        $stmt = $this->conn->prepare("SELECT * FROM paymentInfo ORDER BY created_at DESC ");

        $stmt->execute();
        return $stmt->fetchAll();
    }




    public function updateCourse($data){
        $course_code = $data['course_code'];
        $course_title = $data['course_title'];
        $course_description = $data['course_description'];
        $price_type = $data['price_type'];
        $course_price = $data['course_price'];
        $course_type = $data['course_type'];
        $difficulty_level = $data['difficulty_level'];

        if(!isset($data['thumbnail'])){
            $stmt = $this->conn->prepare("UPDATE `courses` SET `course_code`='$course_code',`course_title`='$course_title',`course_description`='$course_description',`price_type`='$price_type',`course_price`='$course_price',`course_type`='$course_price',`difficulty_level`='$difficulty_level' WHERE course_code = '$course_code'");
        }

        else{
            $thumbnail = $data['thumbnail'];
            $stmt = $this->conn->prepare("UPDATE `courses` SET `course_code`='$course_code',`course_title`='$course_title',`course_description`='$course_description',`price_type`='$price_type',`course_price`='$course_price',`course_type`='$course_type',`difficulty_level`='$difficulty_level',`thumbnail`='$thumbnail' WHERE course_code = '$course_code'");
        }



        $stmt->execute();
        
        if($stmt->rowCount() > 0){
            return true;
        }
        else{
            return false;
        }
    }




}





?>