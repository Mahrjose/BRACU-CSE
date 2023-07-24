

<!-- content starts -->
<section>
    <div class="container justify-content-center bg-success-subtle shadow rounded my-3">
        <h4>User Profile</h4>
        <p>Name:<?php echo htmlspecialchars($user_info['first_name']); ?>
        </p>
        <p>Username: <?php echo htmlspecialchars($user_info['username']); ?>
        </p>
        <p>Email: <?= $user_info['email']?></p>


    </div>
</section>