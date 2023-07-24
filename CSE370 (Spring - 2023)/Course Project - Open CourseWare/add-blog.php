

<?php 



include "./templates/header.php";

?>



<body>
    <?php include "./templates/navigation.php" ?>



    <section class="section container">


        <!-- Button trigger for write blog modal -->
        <button type="button" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#blogModal">
        Write a blog
        </button>






        <!--Write Blog Modal -->
        <div class="modal fade" id="blogModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="blogModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-scrollable">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="#">Add new Blog</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div>
                        <form action="">
                            <input type="text" name="title" id="">
                            <input type="text" name= "">
                            <input type="submit" value="Post">
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

    <?php include "./templates/footer.php" ?>
</body>
</html>