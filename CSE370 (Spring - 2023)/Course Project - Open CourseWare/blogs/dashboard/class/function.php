<?php
class admin_blog
{
    private $conn;

    public function __construct()
    {
        $dbhost = 'localhost';
        $dbuser = 'root';
        $dbpass = "";
        $dbname = 'ocw';
        $this->conn = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);
        if (!$this->conn) {
            die("Database Connection Error!!");
        }
    }

    public function admin_login($data)
    {
        $email = $data["email"];
        $pass = md5($data["password"]);
        echo $email;
        $sql = " SELECT * FROM users WHERE email='$email' && password='$pass'";


        if (mysqli_query($this->conn, $sql)) {
            $users = mysqli_query($this->conn, $sql);

            if ($users) {
                header("Location: dashboard.php");
                $user_data = mysqli_fetch_assoc($users);
                session_start();
                $_SESSION["username"] = $user_data["username"];


            }
        }
    }

    public function admin_logout()
    {
        unset($_SESSION["username"]);
        header("location: index.php");

    }

    public function add_category($data)
    {
        $cat_name = $data["cat_name"];

        $sql = "INSERT INTO  category(ctg) VALUE('$cat_name')";

        if (mysqli_query($this->conn, $sql)) {
            return "Categopry Added Sucessfully";

        }

    }

    public function display_category()
    {
        $sql = "SELECT * FROM category";
        if (mysqli_query($this->conn, $sql)) {
            $cat_data = mysqli_query($this->conn, $sql);
            return $cat_data;
        }
    }

    public function delete_category($ctg)
    {
        $sql = "DELETE FROM category WHERE ctg='$ctg'";
        if (mysqli_query($this->conn, $sql)) {
            return "Delete Sucessful";
        }
    }

    public function add_post($data)
    {

        $post_title = $data['post_title'];
        $post_content = $data['post_content'];
        $post_img = $_FILES['post_img']['name'];
        $post_img_tmp = $_FILES['post_img']['tmp_name'];
        $post_category = $data['category'];
        $author = $data['author'];
        $post_status = $data['post_status'];

        $query = "INSERT INTO blogs (post_title, post_content, post_img, category, author, status) VALUES ('$post_title', '$post_content', '$post_img', '$post_category', '$author',  '$post_status')";

        
        if (mysqli_query($this->conn, $query)){ 
            move_uploaded_file($post_img_tmp, '../../blogs/upload/'.$post_img); 
            echo "Post Added Successfully!";
        }
        else{
            echo "Error";
        }
    }
    
    public function display_post(){
        $sql= "SELECT * FROM blogs";
        if(mysqli_query($this->conn,$sql)){
            $result = mysqli_query($this->conn,$sql);
            return $result;
        }
    }

    public function displayPostByUser($username){
        $sql= "SELECT * FROM blogs WHERE author='$username'";
        if(mysqli_query($this->conn,$sql)){
            $result = mysqli_query($this->conn,$sql);
            return $result;
        }
    }

    
    public function display_post_public($id = Null){
        if($id!= Null){
            $sql= "SELECT * FROM blogs WHERE status='Publish' AND post_id ='$id'";
        }
        else{
            $sql= "SELECT * FROM blogs WHERE status='Publish'" ;
        }
        
        if(mysqli_query($this->conn,$sql)){
            $result = mysqli_query($this->conn,$sql);
            return $result;
        }
    }


    public function delete_post($id)
    {
        $sql = "DELETE FROM blogs WHERE post_id='$id'";
        if (mysqli_query($this->conn, $sql)) {
            return "Delete Sucessful";
        }
    }

    public function edit_image($data){
        $id=$data['editimg_id'];
        $img_name=$_FILES['change_img']['name'];
        $tmp_name=$_FILES['change_img']['tmp_name'];
        // echo $id, $img_name;
        $sql= "UPDATE blogs SET post_img='$img_name' WHERE post_id='$id'";

        if (mysqli_query($this->conn, $sql)){ 
            move_uploaded_file($tmp_name, '../../blogs/upload/'.$img_name); 
            echo "Image Changed Successfully!";
    }

    }

    public function change_single_post($id){
        $sql= "SELECT * FROM blogs WHERE post_id='$id'"; 
        if(mysqli_query($this->conn,$sql)){
            $result = mysqli_query($this->conn,$sql);
            $post=mysqli_fetch_assoc($result);
            return $post;
        }
    }

    public function update_post($data){
        $id=$data['edit_post_id'];
        $title=$data['change_title'];
        $content=$data['change_content'];
        $status=$data['change_post_status'];

        $sql="UPDATE blogs SET post_title='$title', post_content='$content', status='$status' WHERE post_id='$id'  ";
        // echo "NAIM";        
        if(mysqli_query($this->conn,$sql)){
            return "Update Post Sucessful";
        }
    
    }


    public function GetComments($post_id){

        $sql = "SELECT * FROM comments WHERE post_id = '$post_id'";
        if(mysqli_query($this->conn,$sql)){
            $result = mysqli_query($this->conn,$sql);
            $comments=mysqli_fetch_assoc($result);
            return $result;
        }

    }

    public function AddComment($data){
        $post_id =$data['post_id'];
        $author = $data['author'];
        
        $comment_text = $data['comment_text'];

        $sql="INSERT INTO comments (post_id, author, comment_text) VALUES ($post_id, '$author', '$comment_text')";   

        if(mysqli_query($this->conn,$sql)){
            return "Sucessful";
        }
    
    }








}
?>