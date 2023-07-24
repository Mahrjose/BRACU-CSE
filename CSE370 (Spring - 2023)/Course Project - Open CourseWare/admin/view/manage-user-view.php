<?php 

$c = new User();

$users = $c->getAllUsers();

?>


<section>

    <h4>All Users</h4>
    <table class="table container bg-warning-subtle shadow my-3 rounded" id="dataTable">
        <thead>
            <tr>
                <th>username</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Email</th>
                <th>Type</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach($users as $user){ ?>

            <tr>
                <td><?php echo htmlspecialchars($user['username']); ?></td>
                <td><?php echo htmlspecialchars($user['first_name']); ?></td>
                <td><?php echo htmlspecialchars($user['last_name']); ?></td>
                <td><?php echo htmlspecialchars($user['email']); ?></td>
                <td><?php echo htmlspecialchars($user['authority_level']); ?></td>

                <td>
                    <a class="btn btn-info" href="edit-user.php?username=<?= $user['username']?>">Edit</a>
                    <a class="btn btn-danger" href="delete-user.php?username=<?= $user['username']?>">Delete</a>
                </td>
            </tr>

            <?php } ?>

        </tbody>
    </table>

</section>
