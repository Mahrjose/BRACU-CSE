<div class="col-lg-12">
    <div class="sidebar-item categories">
        <div class="sidebar-heading">
            <h2>Categories</h2>
        </div>
        <div class="content">
            <ul>
                <?php while ($category=mysqli_fetch_assoc($get_cat)){ ?>
                
                <li><a href="#">- <?php echo $category['ctg'];  ?>
                </a></li>

                <?php } ?>
                
            </ul>
        </div>
    </div>
</div>
